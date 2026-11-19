"""List or swap the colours of an existing sprite: the quickest way to make a seasonal reskin
that keeps the exact same pixels, silhouette and foot.

  # list the colours a sprite uses, with how many pixels each covers
  python3 tools/recolour_sprite.py sprites/default8bit/oak.png --list

  # swap colours (old=new, as #RRGGBB) and write a new PNG
  python3 tools/recolour_sprite.py sprites/default8bit/oak.png out/oak_winter.png \\
      --map "#7aa63f=#e8eef0" "#58903a=#c9d6dc" "#40762f=#9fb2bb"

Colours not listed stay as they are. Transparent pixels are never touched, so the shape and
foot position cannot change. Pillow only.
"""
import argparse
import sys
from collections import Counter

from PIL import Image


def pixels(img):
    """All pixels in order (works on old and new Pillow)."""
    return img.get_flattened_data() if hasattr(img, "get_flattened_data") else img.getdata()


def hex_colour(text):
    text = text.strip().lstrip("#")
    if len(text) != 6:
        sys.exit("colours must be #RRGGBB, got %r" % text)
    return tuple(int(text[i:i + 2], 16) for i in (0, 2, 4))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input")
    ap.add_argument("output", nargs="?")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--map", nargs="+", default=[])
    args = ap.parse_args()

    img = Image.open(args.input).convert("RGBA")
    counts = Counter(c[:3] for c in pixels(img) if c[3] == 255)
    if args.list or not args.output:
        for c, n in counts.most_common():
            print("#%02x%02x%02x  %4d px" % (c + (n,)))
        print("%d colours" % len(counts))
        return
    mapping = {}
    for pair in args.map:
        old, _, new = pair.partition("=")
        mapping[hex_colour(old)] = hex_colour(new)
    missing = [k for k in mapping if k not in counts]
    if missing:
        print("note: not in this sprite: " + ", ".join("#%02x%02x%02x" % c for c in missing))
    img.putdata([(mapping.get(c[:3], c[:3]) + (255,)) if c[3] == 255 else c for c in pixels(img)])
    used = len({c for c in pixels(img) if c[3] == 255})
    if used > 16:
        sys.exit("result has %d colours; at most 16 allowed" % used)
    img.save(args.output)
    print("wrote %s (%d colours)" % (args.output, used))


if __name__ == "__main__":
    main()
