"""Draws the November trees: larch, maple and ginkgo, in the default pack and the fall pack.

Run: python3 tools/make_november.py [sprites_dir]
Writes <sprites_dir>/default8bit/<key>.png and <sprites_dir>/fall/<key>.png
(default: this repo's sprites/ folder). Reuses the helpers and palette from
make_sprites.py. Pillow only.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import make_sprites as ms  # noqa: E402
from make_sprites import (  # noqa: E402
    PALETTE, SPRITES_DIR, ellipse, image_from_rows, noise, polygon, scatter, tree_grid, trunk, rgb,
)

PALETTE.update({k: rgb(v) for k, v in {
    # larch: fresh spring green
    "!": "#a9c75f", "@": "#86ab4c", "#": "#678d3d", "$": "#4b7032", "%": "#365527",
    # maple: cool deep green, then autumn red
    "^": "#68a85a", "&": "#4c9150", "*": "#387648", "(": "#285c3e", ")": "#1b4331",
    "-": "#f2603a", "_": "#e0402f", "=": "#c42f2c", "+": "#9a2328", "~": "#6e1a22",
    # ginkgo: lime green, then lemon yellow
    "<": "#9ac85a", ">": "#78ac48", "?": "#5c9040", ":": "#447236", ";": "#2f5429",
    "[": "#f8e56a", "]": "#efcf4a", "{": "#d4a93a", "}": "#a98332", "|": "#7a5c2b",
}.items()})

LARCH = "!@#$%"
LARCH_FALL = "E6789"  # gold, amber, orange, rust
MAPLE = "^&*()"
MAPLE_FALL = "-_=+~"
GINKGO = "<>?:;"
GINKGO_FALL = "[]{}|"


def scatter_tree(g, colours, seed, count):
    """Fallen leaves on the ground around the foot, kept inside rows 35 to 44 and the one-tile diamond."""
    def allowed(x, y, ch):
        return ch in ".s" and abs(x + 0.5 - 16) / 12 + abs(y + 0.5 - 40) / 6 <= 1
    scatter(g, seed, count, colours, allowed, (4, 35, 27, 44))


def blob(g, cx, cy, rx, ry, ramp, under=False):
    """A lit ellipse of foliage: light from the top left, darker at the lower right."""
    def pick(x, y):
        s = (-(x + 0.5 - cx) / rx - (y + 0.5 - cy) / ry) / 1.8
        idx = 0 if s > 0.4 else 1 if s > 0.0 else 2 if s > -0.4 else 3 if s > -0.75 else 4
        n = noise(x, y)
        if n % 9 == 0 and idx > 0:
            idx -= 1
        elif n % 13 == 0 and idx < 4:
            idx += 1
        if under and (y + 0.5 - cy) / ry > 0.55:
            idx = max(idx, 3)  # shaded underside, so each tuft shows
        return ramp[idx]
    g.paint(ellipse(cx, cy, rx, ry), pick)


def make_larch(ramp=LARCH, leaves=None):
    """A feathery conifer: ragged tufts that droop, with a few gaps, unlike the solid pine."""
    g = tree_grid()
    trunk(g, 16, 5, 40, 1.0, 2.8)
    tiers = ((6.0, 0.0, 3.4), (9.0, 3.0, 3.4), (12.0, 4.5, 3.8), (15.0, 5.8, 4.0), (18.5, 7.0, 4.2),
             (22.0, 8.0, 4.3), (25.5, 8.8, 4.3), (29.0, 9.0, 4.2), (32.5, 9.2, 4.0))
    for i, (y, d, rx) in enumerate(tiers):
        j = abs(noise(i, 5) % 3 - 1) * 0.5
        centres = [(15.5, y)]
        if d:
            centres = [(15.5 - d + j, y + noise(i, 9) % 2), (15.5 + d - j, y + noise(i, 4) % 2),
                       (15.5, y - 0.5)]
            if i >= 3:  # fill the gap between the centre and the edge
                centres += [(15.5 - d / 2, y + 0.5), (15.5 + d / 2, y + 0.5)]
        for cx, cy in centres:
            blob(g, cx, cy, rx, 3.0, ramp, under=True)
            for k in range(int(-rx + 1), int(rx)):  # drooping tips
                x, yy = int(cx + k), int(cy + 3.6)
                if noise(x, yy) % 2 == 0 and g.c[yy][x] == ".":
                    g.put(x, yy, ramp[3])
    g.outline()
    if leaves:
        scatter_tree(g, leaves, 21, 6)
    return g


def make_maple(ramp=MAPLE, leaves=None, accent=None):
    """A crown shaped like a maple leaf: five pointed lobes."""
    g = tree_grid()
    trunk(g, 16, 27, 40, 2.0, 3.2)
    outline = [(16, 2.5), (18, 7), (20.5, 5.5), (20, 9.5), (27.5, 8.5), (23.5, 13.5), (27, 15.5), (22.5, 17.5),
               (23.5, 24.5), (17.5, 21), (16, 22.5), (14.5, 21), (8.5, 24.5), (9.5, 17.5), (5, 15.5),
               (8.5, 13.5), (4.5, 8.5), (12, 9.5), (11.5, 5.5), (14, 7)]
    leaf = polygon([(x, 4.5 + (y - 2.5) * 1.2) for x, y in outline])  # stretched to a fuller crown

    def pick(x, y):
        s = (-(x + 0.5 - 16) - (y + 0.5 - 15)) / 20
        idx = 0 if s > 0.35 else 1 if s > 0.0 else 2 if s > -0.3 else 3 if s > -0.55 else 4
        n = noise(x, y)
        if accent and idx <= 1 and n % 7 == 0:
            return accent  # a few orange flecks in the light
        if n % 9 == 0 and idx > 0:
            idx -= 1
        elif n % 13 == 0 and idx < 4:
            idx += 1
        return ramp[idx]
    g.paint(leaf, pick)
    g.outline()
    if leaves:
        scatter_tree(g, leaves, 22, 6)
    return g


def fan(g, cx, cy, r, ramp):
    """A ginkgo leaf cluster: a half disc with veins fanning out from its base."""
    def inside(x, y):
        return (x - cx) ** 2 + (y - cy) ** 2 <= r * r and y <= cy + 0.8

    def pick(x, y):
        s = (-(x + 0.5 - cx) - (y + 0.5 - cy)) / (r * 1.4)
        idx = 0 if s > 0.45 else 1 if s > 0.05 else 2
        angle = math.atan2(-(y + 0.5 - cy), x + 0.5 - cx)
        if int(angle / (math.pi / 7)) % 2 == 0:
            idx += 1
        return ramp[min(idx, 3)]
    g.paint(inside, pick)


def make_ginkgo(ramp=GINKGO, leaves=None):
    """A tiered crown of fan-shaped leaves on a straight trunk."""
    g = tree_grid()
    trunk(g, 16, 14, 40, 1.4, 3.0)
    for cx, cy, r in ((16, 9, 5.0),
                      (10.5, 14, 5.2), (21.5, 14, 5.2), (16, 16, 5.2),
                      (7, 20, 5.0), (16, 21.5, 5.2), (25, 20, 5.0),
                      (11.5, 25.5, 4.8), (20.5, 25.5, 4.8)):
        fan(g, cx, cy, r, ramp)
    g.outline()
    if leaves:
        scatter_tree(g, leaves, 23, 9 if ramp == GINKGO_FALL else 6)
    return g


DEFAULT = {"larch": make_larch, "maple": make_maple, "ginkgo": make_ginkgo}
FALL = {
    "larch": lambda: make_larch(LARCH_FALL, ("E", "6", "7")),
    "maple": lambda: make_maple(MAPLE_FALL, ("-", "_", "6"), "7"),
    "ginkgo": lambda: make_ginkgo(GINKGO_FALL, ("[", "]", "{")),
}
PACKS = {"default8bit": DEFAULT, "fall": FALL}


def main(root=None):
    root = root or SPRITES_DIR
    for pack, sprites in PACKS.items():
        os.makedirs(os.path.join(root, pack), exist_ok=True)
        for key, make in sprites.items():
            image = image_from_rows(make().rows())
            colours = len({p for p in image.get_flattened_data() if p[3]})
            if colours > 16:
                sys.exit("%s/%s uses %d colours (max 16)" % (pack, key, colours))
            image.save(os.path.join(root, pack, key + ".png"))
            print("wrote %s/%s.png (%dx%d, %d colours)" % (pack, key, image.width, image.height, colours))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
