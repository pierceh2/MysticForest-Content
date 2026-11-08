"""Draws the 1x1 reskins for the Thanksgiving Feast pack (sprites/thanksgiving_feast/).

Run: python3 tools/make_thanksgiving_pack.py [sprites_dir]
Writes <sprites_dir>/thanksgiving_feast/<key>.png (default: this repo's sprites/ folder).
The look is warm and cosy: honey and burgundy leaves, string lights, ribbons, and baskets
and piles of harvest fruit at the foot of each item. Same canvas, foot and silhouette as the
default items. Reuses the other tools/make_*.py scripts. Pillow only.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import make_harvest as mh  # noqa: E402
import make_november as mn  # noqa: E402
import make_sprites as ms  # noqa: E402
import make_thanksgiving_items as mt  # noqa: E402
from make_sprites import SPRITES_DIR, ellipse, image_from_rows, noise, polygon, puff, tree_grid, trunk  # noqa: E402

HONEY_OAK = "EF678"      # honey gold to amber: warmer and yellower than the fall pack's orange oak
WINE_MAPLE = "_=+~0"     # deep crimson to wine: darker than the fall pack's scarlet maple
GOLD_APPLE = "EFIJK"     # golden leaves so the red apples stand out


def ring(g, cells):
    """Outline a small group of pixels in the dark outline colour."""
    for x, y in list(cells):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if (nx, ny) not in cells and 0 <= nx < g.w and 0 <= ny < g.h and g.c[ny][nx] in ".s":
                g.put(nx, ny, "k")


def basket(g, x0, y0, width=8):
    """A small woven basket of apples whose top-left corner is at (x0, y0)."""
    cells = set()
    for k in range(1, width - 2, 2):  # heaped apples
        for dx, dy, c in ((0, 0, "6"), (1, 0, "_"), (0, 1, "_"), (1, 1, "=")):
            g.put(x0 + k + dx, y0 - 2 + dy - (k % 4 == 3), c)
            cells.add((x0 + k + dx, y0 - 2 + dy - (k % 4 == 3)))
    for dy in range(4):  # the woven body, with a lighter rim
        for dx in range(width):
            g.put(x0 + dx, y0 + dy, "t" if dy == 0 else ("u" if (dx + dy) % 2 else "v"))
            cells.add((x0 + dx, y0 + dy))
    ring(g, cells)


def lights(g, points, crown):
    """Warm string lights: dark wire with a glowing bulb every third pixel, only where there is foliage."""
    for i, (x, y) in enumerate(points):
        if 0 <= x < g.w and 0 <= y < g.h and g.c[y][x] in crown:
            g.put(x, y, ("G" if (i // 2) % 2 == 0 else "Z") if i % 2 == 0 else "v")


def swag(x0, x1, y0, sag):
    """Points along a sagging curve from (x0, y0) to (x1, y0)."""
    mid = (x0 + x1) / 2
    half = (x1 - x0) / 2
    return [(x, int(round(y0 + sag * (1 - ((x - mid) / half) ** 2)))) for x in range(x0, x1 + 1)]


def make_oak():
    g = ms.make_oak(HONEY_OAK, ("E", "6", "7"))
    for pts in (swag(5, 26, 13, 6), swag(4, 27, 21, 6)):
        lights(g, pts, HONEY_OAK)
    basket(g, 4, 38)
    return g


def make_maple():
    g = mn.make_maple(WINE_MAPLE, ("_", "=", "E"), "F")  # wine red with a few gold flecks
    for x in range(13, 19):  # a cream ribbon round the trunk
        for y, c in ((32, "Z"), (33, "Z"), (34, "V")):
            if g.c[y][x] in "tuv":
                g.put(x, y, c)
    bow = {(19, 31): "Z", (20, 31): "Z", (19, 32): "Z", (20, 32): "V", (22, 31): "Z", (23, 31): "Z",
           (22, 32): "Z", (21, 32): "V", (20, 33): "V", (21, 33): "V", (20, 34): "V", (22, 34): "V"}
    for (x, y), c in bow.items():
        if g.c[y][x] in ".s":
            g.put(x, y, c)
    ring(g, set(bow))
    return g


def make_apple_tree():
    g = tree_grid()
    trunk(g, 16, 26, 40, 2.4, 3.6)
    for cx, cy, r in ((9.5, 19.5, 6.5), (22.5, 19.5, 6.5), (16, 14.5, 8.0), (16, 21.5, 8.5),
                      (11, 25.5, 4.5), (21, 25.5, 4.5)):
        puff(g, cx, cy, r, GOLD_APPLE)
    for x, y in ((8, 14), (15, 9), (21, 13), (12, 18), (19, 20), (25, 19), (6, 21), (14, 25), (22, 25),
                 (10, 11), (18, 15), (26, 14), (9, 24), (16, 20)):
        mt.apple(g, x, y)
    g.outline()
    basket(g, 20, 38, 9)
    return g


def pumpkin_pile():
    """Three pumpkins of different sizes and colours, with a curling vine."""
    g = tree_grid()

    def one(cx, cy, rx, ry, tones):
        base, light, dark = tones
        g.paint(ellipse(cx, cy, rx + 0.8, ry + 0.8), lambda x, y: dark)  # dark rim

        def pick(x, y):
            s = (-(x + 0.5 - cx) / rx - (y + 0.5 - cy) / ry) / 1.8
            if abs(x + 0.5 - cx) in (0.5, 1.5) and False:
                return dark
            rib = min(abs(x + 0.5 - (cx - rx * 0.45)), abs(x + 0.5 - (cx + rx * 0.45))) < 0.6
            if rib:
                return dark
            return light if s > 0.35 else base if s > -0.2 else dark if noise(x, y) % 3 == 0 else base
        g.paint(ellipse(cx, cy, rx, ry), pick)
        g.put(int(cx), int(cy - ry - 1), "v")
        g.put(int(cx), int(cy - ry - 2), "v")

    one(15.0, 33.5, 7.8, 5.6, ("7", "6", "8"))  # big orange, at the back
    one(8.5, 38.0, 5.0, 4.0, ("8", "7", "9"))   # deep red-orange, front left
    one(22.5, 38.0, 5.2, 4.0, ("Z", "Z", "V"))  # cream, front right
    for x, y in ((18, 27), (19, 26), (20, 26), (21, 27)):  # a curling vine and a leaf
        g.put(x, y, "3")
    g.paint(ellipse(23, 28, 2.6, 1.4), lambda x, y: "3" if y < 28 else "4")
    g.outline()
    return g


def make_scarecrow():
    g = mh.make_scarecrow()
    for x in range(12, 20):  # a warm scarf at the neck
        for y in (17, 18):
            if g.c[y][x] not in ".kv":
                g.put(x, y, "7" if (x + y) % 2 else "8")
    for i, x in enumerate(range(10, 21)):  # autumn leaves tucked in the hat band
        if g.c[8][x] == "9":
            g.put(x, 8, ("7", "8", "E")[i % 3])
    cells = set()  # a small pumpkin at the foot, in colours the scarecrow already uses
    inside = ellipse(24.5, 38.8, 3.6, 2.6)
    for y in range(34, 44):
        for x in range(18, 30):
            if inside(x + 0.5, y + 0.5) and g.c[y][x] in ".s":
                g.put(x, y, "8" if (x > 25 or y > 39) else "7")
                cells.add((x, y))
    for x, y in ((24, 36), (24, 35)):
        g.put(x, y, "v")
        cells.add((x, y))
    ring(g, cells)
    return g


SPRITES = {"oak": make_oak, "maple": make_maple, "apple_tree": make_apple_tree,
           "pumpkin": pumpkin_pile, "scarecrow": make_scarecrow}


def main(root=None):
    out_dir = os.path.join(root or SPRITES_DIR, "thanksgiving_feast")
    os.makedirs(out_dir, exist_ok=True)
    for key, make in SPRITES.items():
        image = image_from_rows(make().rows())
        colours = len({p for p in image.get_flattened_data() if p[3]})
        if colours > 16:
            sys.exit("%s uses %d colours (max 16)" % (key, colours))
        image.save(os.path.join(out_dir, key + ".png"))
        print("wrote thanksgiving_feast/%s.png (%dx%d, %d colours)" % (key, image.width, image.height, colours))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
