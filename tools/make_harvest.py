"""Draws the harvest items: pumpkin, jack_o_lantern, scarecrow, hay_bales.

Run: python3 tools/make_harvest.py [output_dir]
Writes <output_dir>/<key>.png (default: sprites/default8bit). Reuses the helpers
and palette from make_sprites.py. Pillow only.
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from make_sprites import (  # noqa: E402
    SPRITES_DIR, Grid, ellipse, image_from_rows, noise, polygon, scatter, tree_grid,
)


# ---------- pumpkins ----------

def pumpkin_body(g):
    """Three ribbed lobes in orange, lit from the top left, foot at row 40."""
    for cx, cy, rx, ry in ((10.5, 34.0, 5.6, 5.6), (21.5, 34.0, 5.6, 5.6), (16, 33.5, 6.4, 6.3)):
        g.paint(ellipse(cx, cy, rx + 0.9, ry + 0.9), lambda x, y: "9")  # dark rib line

        def pick(x, y, cx=cx, cy=cy, rx=rx, ry=ry):
            s = (-(x + 0.5 - cx) / rx - (y + 0.5 - cy) / ry) / 1.8
            n = noise(x, y)
            if s > 0.38:
                return "6" if n % 4 else "7"
            if s > -0.08:
                return "7"
            if s > -0.5:
                return "8" if n % 5 else "7"
            return "8" if n % 3 else "9"
        g.paint(ellipse(cx, cy, rx, ry), pick)


def pumpkin_stem(g, leaf):
    for x, y, c in ((15, 26, "u"), (16, 26, "v"), (15, 25, "u"), (16, 25, "v"),
                    (15, 24, "u"), (16, 24, "v"), (16, 23, "u"), (17, 23, "v")):
        g.put(x, y, c)
    if leaf:
        for x, y in ((17, 25), (18, 25), (19, 24), (20, 24), (21, 25), (21, 26)):
            g.put(x, y, "3")
        g.paint(ellipse(23.4, 27.2, 2.8, 1.5), lambda x, y: "3" if y < 27 else "4")


def make_pumpkin():
    g = tree_grid()
    pumpkin_body(g)
    pumpkin_stem(g, True)
    g.outline()
    return g


def make_jack_o_lantern():
    g = tree_grid()
    pumpkin_body(g)
    pumpkin_stem(g, False)
    eye = {(12, 30), (11, 31), (12, 31), (13, 31), (10, 32), (11, 32), (12, 32), (13, 32), (14, 32)}
    eyes = eye | {(x + 7, y) for x, y in eye}
    nose = {(15, 34), (16, 34), (14, 35), (15, 35), (16, 35), (17, 35)}
    mouth = {(x, 37) for x in (9, 10, 13, 14, 17, 18, 21, 22)} | {(x, 38) for x in range(10, 22)}
    carved = eyes | nose | mouth
    for x, y in carved:  # dark rim round each cut so the glow stands out
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, -1)):
            nx, ny = x + dx, y + dy
            if (nx, ny) not in carved and g.c[ny][nx] in "6789":
                g.put(nx, ny, "0")
    for x, y in carved:
        g.put(x, y, "G" if (x, y + 1) in carved else "H")
    g.outline()
    return g


# ---------- scarecrow ----------

def make_scarecrow():
    g = tree_grid()
    rng = random.Random(41)
    straw = ("E", "F", "I")
    # post and crossbar
    g.paint(lambda x, y: 15 <= x < 17 and 16 <= y <= 40, lambda x, y: "u" if x < 16 else "v")
    g.paint(lambda x, y: 3 <= x <= 29 and 19 <= y < 21, lambda x, y: "u" if y < 20 else "v")
    # trousers: two legs with ragged hems, a patch
    for x0, x1, dark in ((11, 15.4, False), (16.6, 21, True)):
        g.paint(lambda x, y, x0=x0, x1=x1: x0 <= x <= x1 and 30 <= y < 38 + (1 if int(x) % 2 else 0),
                lambda x, y, dark=dark: "T" if dark or (x + y) % 6 == 0 else "S")
    g.paint(lambda x, y: 12 <= x < 15 and 33 <= y < 36, lambda x, y: "7" if (x + y) % 2 else "8")
    # shirt: torso and sleeves, plaid
    def plaid(x, y):
        return "9" if (y % 4 == 0 or x % 5 == 0) else ("7" if x < 13 and (x + y) % 3 == 0 else "8")
    g.paint(lambda x, y: 11 <= x < 21 and 18 <= y < 31 + (1 if int(x) % 3 == 0 else 0), plaid)
    g.paint(polygon([(4, 20.5), (11, 18.5), (11, 24), (4, 23)]), plaid)
    g.paint(polygon([(21, 18.5), (28, 20.5), (28, 23), (21, 24)]), plaid)
    # sack head with stitched face
    def sack(x, y):
        s = (-(x + 0.5 - 15.5) - (y + 0.5 - 13.5)) / 6.6
        return "L" if s > 0.3 else "M" if s > -0.25 else "N"
    g.paint(ellipse(15.5, 13.5, 4.8, 4.9), sack)
    for x, y in ((13, 12), (13, 13), (18, 12), (18, 13), (12, 15), (13, 16), (14, 16), (15, 16),
                 (16, 16), (17, 16), (18, 16), (19, 15)):
        g.put(x, y, "v")
    g.put(15, 14, "N")
    g.put(16, 14, "N")
    # straw hat
    g.paint(ellipse(15.5, 9.2, 10, 2.3), lambda x, y: "F" if y < 10 else "I")
    g.paint(ellipse(15.5, 6.2, 5.6, 4.0), lambda x, y: "E" if x < 15 and y < 7 else "F")
    g.paint(lambda x, y: 10 <= x < 21 and 8 <= y < 9, lambda x, y: "9")
    # straw poking out at the cuffs, collar and trouser hems
    spots = ([(2 + rng.randint(0, 1), 19 + rng.randint(0, 5)) for _ in range(9)]
             + [(28 + rng.randint(0, 1), 19 + rng.randint(0, 5)) for _ in range(9)]
             + [(11 + rng.randint(0, 2), 17 + rng.randint(0, 1)) for _ in range(3)]
             + [(18 + rng.randint(0, 2), 17 + rng.randint(0, 1)) for _ in range(3)]
             + [(11 + rng.randint(0, 9), 38 + rng.randint(0, 2)) for _ in range(9)])
    for x, y in spots:
        if g.c[y][x] in (".", "s"):
            g.put(x, y, rng.choice(straw))
            if rng.random() < 0.5 and g.c[y + 1][x] in (".", "s"):
                g.put(x, y + 1, rng.choice(straw))
    g.outline()
    return g


# ---------- hay bales (2x2 landmark) ----------

def make_hay_bales():
    g = Grid(64, 96)

    def P(u, v, z):  # iso projection; ground diamond is (32,64) (64,80) (32,96) (0,80)
        return (32 + u - v, 64 + (u + v) / 2 - z)

    def box(u0, v0, z0, du, dv, h, axis):
        zt = z0 + h
        length, start = (du, u0) if axis == "u" else (dv, v0)

        def band(t):
            f = (t - start) / length
            return abs(f - 0.27) < 0.028 or abs(f - 0.73) < 0.028

        def top_pick(x, y):
            s, d = 2 * (y + 0.5 - 64 + zt), x + 0.5 - 32
            u, v = (s + d) / 2, (s - d) / 2
            if band(u if axis == "u" else v):
                return "u"
            return "F" if noise(x, y) % 7 == 0 else "E"

        def left_pick(x, y):  # face at v = v0 + dv, spans u
            if axis == "u" and band(x + 0.5 - 32 + v0 + dv):
                return "u"
            return "I" if (y % 3 == 0 and noise(x, y) % 2) else "F"

        def right_pick(x, y):  # face at u = u0 + du, spans v
            if axis == "v" and band(32 + u0 + du - (x + 0.5)):
                return "v"
            return "J" if (y % 3 == 0 and noise(x, y) % 2) else "I"

        faces = (polygon([P(u0, v0 + dv, z0), P(u0 + du, v0 + dv, z0), P(u0 + du, v0 + dv, zt), P(u0, v0 + dv, zt)]),
                 polygon([P(u0 + du, v0, z0), P(u0 + du, v0 + dv, z0), P(u0 + du, v0 + dv, zt), P(u0 + du, v0, zt)]),
                 polygon([P(u0, v0, zt), P(u0 + du, v0, zt), P(u0 + du, v0 + dv, zt), P(u0, v0 + dv, zt)]))
        g.paint(polygon([P(u0, v0 + dv, z0), P(u0 + du, v0 + dv, z0), P(u0 + du, v0 + dv, zt), P(u0, v0 + dv, zt)]), left_pick)
        g.paint(polygon([P(u0 + du, v0, z0), P(u0 + du, v0 + dv, z0), P(u0 + du, v0 + dv, zt), P(u0 + du, v0, zt)]), right_pick)
        g.paint(polygon([P(u0, v0, zt), P(u0 + du, v0, zt), P(u0 + du, v0 + dv, zt), P(u0, v0 + dv, zt)]), top_pick)
        # dark edge round this bale, and a light ridge where the top meets the front faces
        inside = lambda x, y: any(f(x, y) for f in faces)
        edge = [(x, y) for y in range(g.h) for x in range(g.w)
                if inside(x + 0.5, y + 0.5) and not all(inside(x + 0.5 + dx, y + 0.5 + dy)
                                                       for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))]
        for x, y in edge:
            g.put(x, y, "J")

    # layer 1: two bales; layer 2: two bales crosswise; layer 3: one bale on top
    for args in ((2, 2, 0, 28, 14, 11, "u"), (2, 16, 0, 28, 14, 11, "u"),
                 (2, 2, 11, 14, 28, 11, "v"), (16, 2, 11, 14, 28, 11, "v"),
                 (2, 9, 22, 28, 14, 11, "u")):
        box(*args)
    # ragged straw on the silhouette
    src = [row[:] for row in g.c]
    for y in range(g.h):
        for x in range(g.w):
            if src[y][x] != ".":
                continue
            near = [src[y + dy][x + dx] for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
                    if 0 <= x + dx < g.w and 0 <= y + dy < g.h]
            if any(c in "EFI" for c in near) and noise(x, y) % 9 == 0 and 3 <= x <= 60:
                g.put(x, y, "F")
    g.outline()
    diamond = polygon([(32, 64), (62, 79), (32, 94), (2, 79)])
    scatter(g, 51, 12, ("E", "F", "I"), lambda x, y, ch: ch == "." and diamond(x + 0.5, y + 0.5), (3, 66, 60, 94))
    return g


SPRITES = {
    "pumpkin": make_pumpkin,
    "jack_o_lantern": make_jack_o_lantern,
    "scarecrow": make_scarecrow,
    "hay_bales": make_hay_bales,
}


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
