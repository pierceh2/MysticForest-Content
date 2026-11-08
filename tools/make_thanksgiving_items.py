"""Draws the Thanksgiving-season default items: apple_tree, corn_stalks, harvest_table.

Run: python3 tools/make_thanksgiving_items.py [output_dir]
Writes <output_dir>/<key>.png (default: sprites/default8bit). Reuses the helpers
and palette from make_sprites.py. Pillow only.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import make_november  # noqa: E402,F401  (adds the red and green ramps to the shared palette)
from make_sprites import PALETTE as _PAL, rgb as _rgb  # noqa: E402

_PAL.update({"Z": _rgb("#e8dcc0"), "V": _rgb("#c4b594")})  # warm cream for the cloth and candles

from make_sprites import (  # noqa: E402
    OAK, PALETTE, SPRITES_DIR, Grid, ellipse, image_from_rows, noise, polygon, puff, scatter, tree_grid, trunk,
)


# ---------- apple tree ----------

def apple(g, x, y):
    """A 2x2 red apple with a highlight, top-left pixel at (x, y)."""
    for dx, dy, c in ((0, 0, "6"), (1, 0, "_"), (0, 1, "_"), (1, 1, "=")):
        g.put(x + dx, y + dy, c)


def make_apple():
    g = tree_grid()
    trunk(g, 16, 26, 40, 2.4, 3.6)
    for cx, cy, r in ((9.5, 19.5, 6.5), (22.5, 19.5, 6.5), (16, 14.5, 8.0), (16, 21.5, 8.5),
                      (11, 25.5, 4.5), (21, 25.5, 4.5)):
        puff(g, cx, cy, r, OAK)
    for x, y in ((8, 14), (15, 9), (21, 13), (12, 18), (19, 20), (25, 19), (6, 21), (14, 25), (22, 25)):
        apple(g, x, y)
    g.outline()
    for x, y in ((20, 41), (23, 42)):  # two windfalls by the trunk
        if g.c[y][x] in ".s" and g.c[y + 1][x] in ".s":
            apple(g, x, y)
    return g


# ---------- corn stalks ----------

def line(g, x0, y0, x1, y1, colour):
    steps = int(max(abs(x1 - x0), abs(y1 - y0))) * 2 + 1
    for i in range(steps + 1):
        t = i / steps
        g.put(int(round(x0 + (x1 - x0) * t)), int(round(y0 + (y1 - y0) * t)), colour)


def make_corn_stalks():
    g = tree_grid()
    # five dried stalks tied in a bundle: they meet at the twine and fan out above and below,
    # far enough apart that the outline does not fill the gaps
    bundle = ((-2, 12), (-1, 7), (0, 5), (1, 8), (2, 13))  # (position in the bundle, top row)
    for k, top in bundle:
        base_x, tie_x, top_x = 15.5 + k * 2.6, 15.5 + k * 0.7, 15.5 + k * 4.4
        line(g, base_x, 40, tie_x, 33, "F")
        line(g, tie_x, 33, top_x, top, "F")
    # a few long blades that arch out and droop, alternating sides
    for k, side, y in ((-2, -1, 19), (-1, -1, 25), (2, 1, 21), (1, 1, 27), (0, -1, 30), (0, 1, 31)):
        x0 = 15.5 + k * 3.2
        for i in range(10):
            x = x0 + side * i
            if not 3 <= x <= 28:  # keep clear of the canvas edges
                break
            yy = y - i * 0.45 + (i * i) / 11
            g.put(int(x), int(yy), "g" if i < 6 else "h")
            if i < 8:  # blades are two pixels wide, tapering to a point
                g.put(int(x), int(yy) + 1, "h" if i < 6 else "g")
    # three cobs in green husks with a golden tip
    for x, y in ((9, 17), (21, 15), (15, 22)):
        for dy in range(8):
            for dx in range(3):
                if dy < 3:
                    g.put(x + dx, y + dy, "E" if (dx + dy) % 2 == 0 else "6")  # exposed golden kernels
                else:
                    g.put(x + dx, y + dy, "g" if dx == 0 else "h")  # the green husk
        g.put(x + 1, y - 1, "6")
    # a small tassel at the top of each stalk
    for k, top in bundle:
        tx = int(round(15.5 + k * 4.4))
        for dx, dy in ((0, -2), (0, -1), (-1, -1), (1, -1)):
            g.put(tx + dx, top + dy, "I")
    # twine
    for x in range(13, 19):
        g.put(x, 33, "u")
        g.put(x, 34, "v")
    g.outline()
    return g


# ---------- harvest table (2x2 landmark) ----------

def make_harvest_table():
    g = Grid(64, 96)

    def P(u, v, z):  # iso projection over the ground diamond (32,64) (64,80) (32,96) (0,80)
        return (32 + u - v, 64 + (u + v) / 2 - z)

    def uv_top(x, y, z):
        s, d = 2 * (y + 0.5 - 64 + z), x + 0.5 - 32
        return (s + d) / 2, (s - d) / 2

    TOP, HEM = 14, 5
    u0, u1, v0, v1 = 2, 30, 3, 26

    def leg(lu, lv):
        g.paint(polygon([P(lu, lv + 2, 0), P(lu + 2, lv + 2, 0), P(lu + 2, lv + 2, HEM), P(lu, lv + 2, HEM)]), lambda x, y: "u")
        g.paint(polygon([P(lu + 2, lv, 0), P(lu + 2, lv + 2, 0), P(lu + 2, lv + 2, HEM), P(lu + 2, lv, HEM)]), lambda x, y: "v")
    for lu, lv in ((u1 - 3, v0 + 1), (u1 - 3, v1 - 3), (u0 + 1, v1 - 3)):
        leg(lu, lv)

    # cloth: front-left face, front-right face, top with a burgundy runner down the middle
    def left(x, y):
        u = x + 0.5 - 32 + v1
        if y > P(u, v1, HEM)[1] - 1.2 and int(u) % 2 == 0:  # scalloped hem
            return "x"
        return "x" if int(u) % 6 == 0 else "V"

    def runner(v):
        return "5" if (12.5 <= v < 13.5 or 16 <= v < 17) else "4"

    def right(x, y):
        v = 32 + u1 - (x + 0.5)
        if 11.5 <= v <= 17.5:
            return runner(v)  # the runner hangs over the end
        if y > P(u1, v, HEM)[1] - 1.2 and int(v) % 2 == 0:
            return "V"
        return "x"

    def top(x, y):
        u, v = uv_top(x, y, TOP)
        return runner(v) if 11.5 <= v <= 17.5 else "Z"
    g.paint(polygon([P(u0, v1, HEM), P(u1, v1, HEM), P(u1, v1, TOP), P(u0, v1, TOP)]), left)
    g.paint(polygon([P(u1, v0, HEM), P(u1, v1, HEM), P(u1, v1, TOP), P(u1, v0, TOP)]), right)
    g.paint(polygon([P(u0, v0, TOP), P(u1, v0, TOP), P(u1, v1, TOP), P(u0, v1, TOP)]), top)

    def at(u, v):
        x, y = P(u, v, TOP)
        return int(round(x)), int(round(y))

    def pie(u, v):
        x, y = at(u, v)
        g.paint(ellipse(x, y + 1.4, 5.0, 2.5), lambda a, b: "I")
        g.paint(ellipse(x, y, 5.0, 2.5), lambda a, b: "I" if (a + b) % 3 == 0 else "F")

    def bread(u, v):
        x, y = at(u, v)
        g.paint(ellipse(x, y, 4.6, 2.3), lambda a, b: "F" if b < y else "u")
        for dx in (-2, 0, 2):
            g.put(x + dx, y - 1, "v")

    def pumpkin(u, v):
        x, y = at(u, v)
        g.paint(ellipse(x, y - 2.4, 4.0, 3.0), lambda a, b: "8" if a > x + 1 else "7")
        g.put(x, y - 5, "v")
        g.put(x, y - 4, "v")

    def apples(u, v):
        x, y = at(u, v)
        g.paint(ellipse(x, y, 5.0, 2.4), lambda a, b: "u")  # a little bowl
        for dx, dy, c in ((-2, -2, "_"), (0, -3, "8"), (2, -2, "_"), (0, -1, "_"), (-3, -1, "8"), (3, -1, "8")):
            g.paint(ellipse(x + dx, y + dy, 1.8, 1.7), lambda a, b, c=c: c)

    def candle(u, v):
        x, y = at(u, v)
        for dy in range(6):
            g.put(x, y - dy, "Z")
            g.put(x + 1, y - dy, "V")
        g.put(x, y - 6, "H")
        g.put(x, y - 7, "G")
        g.put(x + 1, y - 7, "G")
        g.put(x, y - 8, "G")

    for fn, u, v in sorted(((candle, 4, 14.5), (pie, 10, 10.5), (bread, 10.5, 18.5), (apples, 17, 14.5),
                            (pumpkin, 23.5, 11), (pie, 24, 19), (candle, 27.5, 14.5)), key=lambda t: t[1] + t[2]):
        fn(u, v)

    g.outline()
    diamond = polygon([(32, 64), (62, 79), (32, 94), (2, 79)])
    scatter(g, 61, 10, ("7", "8", "F"), lambda x, y, ch: ch == "." and diamond(x + 0.5, y + 0.5), (3, 66, 60, 94))
    return g


SPRITES = {"apple_tree": make_apple, "corn_stalks": make_corn_stalks, "harvest_table": make_harvest_table}


def main(out_dir=None):
    out_dir = out_dir or os.path.join(SPRITES_DIR, "default8bit")
    os.makedirs(out_dir, exist_ok=True)
    for key, make in SPRITES.items():
        image = image_from_rows(make().rows())
        colours = len({p for p in image.get_flattened_data() if p[3]})
        if colours > 16:
            sys.exit("%s uses %d colours (max 16)" % (key, colours))
        image.save(os.path.join(out_dir, key + ".png"))
        print("wrote %s.png (%dx%d, %d colours)" % (key, image.width, image.height, colours))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
