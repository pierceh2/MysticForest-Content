"""Turn any picture (for example an AI-generated image) into a valid Mystic Forest sprite.

Image generators give large, smooth, anti-aliased pictures on a background. This script cuts out
the subject, shrinks it to the sprite canvas, limits it to at most 16 hard colours, adds the
1-pixel dark outline, puts the foot or base in the right place, and checks the result against
the sprite rules in CLAUDE.md.

Examples (run from the repo root):

  # a new tree, colours chosen automatically
  python3 tools/fit_sprite.py generated.png out/maple.png --kind tree

  # a redraw or reskin that must sit exactly where the existing sprite sits, using the
  # existing art's palette so it matches the set
  python3 tools/fit_sprite.py generated.png out/oak.png --kind tree \\
      --like sprites/default8bit/oak.png --palette sprites/default8bit/oak.png

  # a 2x2 landmark, with an 8x preview on dark green to look at
  python3 tools/fit_sprite.py generated.png out/well.png --kind landmark --preview out/well_8x.png

Options:
  --kind tree|landmark   Canvas 32x48 (tree) or 64x96 (2x2 landmark). Required.
  --like PNG             Match the drawn area (width, height, bottom-centre) of an existing sprite.
  --palette PNG [PNG..]  Map every colour to the nearest colour found in these PNGs. Without it,
                         up to --colours colours are chosen from the picture itself.
  --colours N            Most colours in the result, outline included (default 16, max 16).
  --key #RRGGBB          Background colour to remove (default: read from the picture's corners).
  --tolerance N          How close a pixel must be to the background colour to be removed (default 60).
  --box WxH              Largest drawn area, outline included (default 28x38 tree, 60x64 landmark).
  --defringe N           Trim N source pixels off the cut-out edge, to drop the soft halo where the
                         subject blends into the background (default: about 1% of the picture; 0 = off).
  --no-outline           Keep the picture's own edge instead of adding a 1-pixel outline.
  --preview PNG          Also write an 8x nearest-neighbour preview on dark green.

Pillow only. Exits with status 1 and a message if the result breaks a sprite rule.
"""
import argparse
import sys
from collections import deque

from PIL import Image, ImageFilter


def pixels(img):
    """All pixels in order (works on old and new Pillow)."""
    return img.get_flattened_data() if hasattr(img, "get_flattened_data") else img.getdata()

OUTLINE = (16, 27, 21, 255)  # the set's outline colour, #101b15
CANVAS = {"tree": (32, 48), "landmark": (64, 96)}
DEFAULT_BOX = {"tree": (28, 38), "landmark": (60, 64)}
PREVIEW_BG = (24, 48, 34, 255)


def hex_colour(text):
    text = text.lstrip("#")
    return tuple(int(text[i:i + 2], 16) for i in (0, 2, 4))


def distance(a, b):
    return sum((x - y) ** 2 for x, y in zip(a[:3], b[:3])) ** 0.5


def cut_out(img, key, tolerance):
    """Make the background transparent. Uses the picture's own alpha if it has any; otherwise
    flood-fills from the edges through pixels close to the background colour."""
    img = img.convert("RGBA")
    w, h = img.size
    px = img.load()
    if any(px[x, y][3] < 128 for x, y in ((0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1))):
        return img  # already has a transparent background
    if key is None:
        corners = [px[x, y] for x, y in ((0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1))]
        key = tuple(sorted(c[i] for c in corners)[1] for i in range(3))
    seen = bytearray(w * h)
    queue = deque()
    for x in range(w):
        queue.extend(((x, 0), (x, h - 1)))
    for y in range(h):
        queue.extend(((0, y), (w - 1, y)))
    while queue:
        x, y = queue.popleft()
        i = y * w + x
        if seen[i]:
            continue
        seen[i] = 1
        if distance(px[x, y], key) > tolerance:
            continue
        r, g, b, _ = px[x, y]
        px[x, y] = (r, g, b, 0)
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and not seen[ny * w + nx]:
                queue.append((nx, ny))
    return img


def defringe(img, n):
    """Shrink the opaque area by n pixels all round, removing background-tinted edge pixels."""
    if n <= 0:
        return img
    alpha = img.split()[3].point(lambda a: 255 if a >= 128 else 0)
    for _ in range(n):
        alpha = alpha.filter(ImageFilter.MinFilter(3))
    img = img.copy()
    img.putalpha(alpha)
    return img


def opaque_bbox(img):
    return img.split()[3].point(lambda a: 255 if a >= 128 else 0).getbbox()


def palette_from(paths):
    colours = set()
    for p in paths:
        for c in pixels(Image.open(p).convert("RGBA")):
            if c[3] == 255:
                colours.add(c[:3])
    return sorted(colours)


def shrink(img, size):
    """Shrink with area averaging (clean for painterly input), then make alpha hard."""
    small = img.resize(size, Image.BOX)
    a = small.split()[3].point(lambda v: 255 if v >= 128 else 0)
    small.putalpha(a)
    return small


def limit_colours(img, palette, count):
    px = img.load()
    w, h = img.size
    opaque = [(x, y) for y in range(h) for x in range(w) if px[x, y][3] == 255]
    if palette:
        cache = {}
        for x, y in opaque:
            c = px[x, y][:3]
            if c not in cache:
                cache[c] = min(palette, key=lambda p: distance(p, c))
            px[x, y] = cache[c] + (255,)
        return img
    if not opaque:
        return img
    strip = Image.new("RGB", (len(opaque), 1))
    strip.putdata([px[x, y][:3] for x, y in opaque])
    q = strip.quantize(colors=count, method=Image.Quantize.MEDIANCUT).convert("RGB")
    for (x, y), c in zip(opaque, pixels(q)):
        px[x, y] = c + (255,)
    return img


def add_outline(img):
    w, h = img.size
    grown = Image.new("RGBA", (w + 2, h + 2), (0, 0, 0, 0))
    grown.alpha_composite(img, (1, 1))
    src = grown.copy().load()
    px = grown.load()
    for y in range(h + 2):
        for x in range(w + 2):
            if src[x, y][3]:
                continue
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < w + 2 and 0 <= ny < h + 2 and src[nx, ny][3]:
                    px[x, y] = OUTLINE
                    break
    return grown


def check(img, kind):
    """The same checks as check_sprite.py and scripts/validate.py; returns a list of problems."""
    problems = []
    w, h = img.size
    if img.size != CANVAS[kind]:
        problems.append("size is %s, must be %s" % (img.size, CANVAS[kind]))
    px = img.load()
    alphas = {px[x, y][3] for x in range(w) for y in range(h)}
    if not alphas <= {0, 255}:
        problems.append("alpha values other than 0 and 255")
    if 255 not in alphas:
        return problems + ["the sprite is empty"]
    if any(px[0, y][3] or px[w - 1, y][3] for y in range(h)):
        problems.append("an opaque pixel touches the left or right edge")
    if any(px[x, 0][3] for x in range(w)):
        problems.append("an opaque pixel touches the top edge")
    low = max(y for y in range(h) if any(px[x, y][3] for x in range(w)))
    if kind == "tree" and not 36 <= low <= 44:
        problems.append("lowest opaque row is %d; a tree's foot should end around row 40" % low)
    if kind == "landmark" and low < h - 8:
        problems.append("lowest opaque row is %d; a landmark's base should reach row %d or lower" % (low, h - 8))
    colours = {px[x, y] for x in range(w) for y in range(h) if px[x, y][3]}
    if len(colours) > 16:
        problems.append("%d colours; at most 16 allowed" % len(colours))
    return problems


def fit(args):
    kind = args.kind
    cw, ch = CANVAS[kind]
    src = cut_out(Image.open(args.input), hex_colour(args.key) if args.key else None, args.tolerance)
    n = args.defringe if args.defringe is not None else max(1, round(min(src.size) / 100))
    src = defringe(src, n)
    bbox = opaque_bbox(src)
    if not bbox:
        sys.exit("nothing left after removing the background; try --key or a lower --tolerance")
    src = src.crop(bbox)

    outline = 0 if args.no_outline else 2
    if args.like:
        ref = Image.open(args.like).convert("RGBA")
        if ref.size != (cw, ch):
            sys.exit("--like sprite is %s, but a %s canvas is %s" % (ref.size, kind, (cw, ch)))
        rx0, ry0, rx1, ry1 = opaque_bbox(ref)
        box_w, box_h = rx1 - rx0, ry1 - ry0
        centre_x, bottom = (rx0 + rx1) / 2, ry1
    else:
        box_w, box_h = (int(v) for v in args.box.split("x")) if args.box else DEFAULT_BOX[kind]
        centre_x = cw / 2
        bottom = 41 if kind == "tree" else ch - 1  # a tree's foot on row 40; a landmark's base on the last row

    colours = min(16, args.colours) - (0 if args.no_outline else 1)
    palette = palette_from(args.palette) if args.palette else None
    if palette:
        palette = [c for c in palette if c != OUTLINE[:3]] or palette

    while True:
        scale = min((box_w - outline) / src.width, (box_h - outline) / src.height)
        size = (max(1, round(src.width * scale)), max(1, round(src.height * scale)))
        art = limit_colours(shrink(src, size), palette, colours)
        if not args.no_outline:
            art = add_outline(art)
        out = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
        left = int(round(centre_x - art.width / 2))
        top = int(bottom - art.height)
        out.alpha_composite(art, (max(0, left), max(0, top)))
        problems = check(out, kind)
        edge = [p for p in problems if "edge" in p]
        if edge and box_w > 6 and box_h > 6:
            box_w, box_h = box_w - 2, box_h - 2  # shrink a little and try again
            continue
        break

    out.save(args.output)
    if args.preview:
        prev = Image.new("RGBA", out.size, PREVIEW_BG)
        prev.alpha_composite(out)
        prev.resize((out.width * 8, out.height * 8), Image.NEAREST).save(args.preview)
    used = len({c for c in pixels(out) if c[3]})
    if problems:
        print("wrote %s, but it breaks the sprite rules:" % args.output)
        for p in problems:
            print("  - " + p)
        sys.exit(1)
    print("OK %s (%dx%d, drawn area %dx%d, %d colours)" % (args.output, cw, ch, art.width, art.height, used))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--kind", required=True, choices=sorted(CANVAS))
    ap.add_argument("--like")
    ap.add_argument("--palette", nargs="+")
    ap.add_argument("--colours", type=int, default=16)
    ap.add_argument("--key")
    ap.add_argument("--tolerance", type=float, default=60)
    ap.add_argument("--box")
    ap.add_argument("--defringe", type=int)
    ap.add_argument("--no-outline", action="store_true")
    ap.add_argument("--preview")
    fit(ap.parse_args())


if __name__ == "__main__":
    main()
