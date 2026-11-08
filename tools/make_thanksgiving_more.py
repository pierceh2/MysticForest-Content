"""Draws the rest of the Thanksgiving Feast reskins: hay_bales, shrine, birch, pond.

Run: python3 tools/make_thanksgiving_more.py [sprites_dir]
Writes <sprites_dir>/thanksgiving_feast/<key>.png (default: this repo's sprites/ folder).
Same canvas, foot/base and silhouette as the default items, with warm string lights,
harvest fruit, a wreath and lanterns added. Reuses the other tools/make_*.py scripts. Pillow only.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import make_harvest as mh  # noqa: E402
import make_sprites as ms  # noqa: E402
import make_thanksgiving_pack as tp  # noqa: E402
from make_sprites import SPRITES_DIR, ellipse, image_from_rows, polygon  # noqa: E402


def ring(g, cells, over=".s"):
    """Outline a small group of pixels, over the given kinds of pixel."""
    for x, y in list(cells):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if (nx, ny) not in cells and 0 <= nx < g.w and 0 <= ny < g.h and g.c[ny][nx] in over:
                g.put(nx, ny, "k")


def small_pumpkin(g, cx, cy, rx, ry, tones=("7", "6", "8"), over=".s"):
    """A little ribbed pumpkin with a stem, outlined on its own, painted over the given kinds of pixel."""
    base, light, dark = tones
    cells = set()
    inside = ellipse(cx, cy, rx, ry)
    for y in range(int(cy - ry - 3), int(cy + ry + 2)):
        for x in range(int(cx - rx - 1), int(cx + rx + 2)):
            if 0 <= x < g.w and 0 <= y < g.h and inside(x + 0.5, y + 0.5) and g.c[y][x] in over:
                s = (-(x + 0.5 - cx) / rx - (y + 0.5 - cy) / ry) / 1.8
                rib = abs(x + 0.5 - cx) < 0.6
                g.put(x, y, dark if rib or s < -0.35 else light if s > 0.4 else base)
                cells.add((x, y))
    for dy in (1, 2):
        if g.c[int(cy - ry) - dy][int(cx)] in over:
            g.put(int(cx), int(cy - ry) - dy, "v")
            cells.add((int(cx), int(cy - ry) - dy))
    ring(g, cells, over)


# ---------- birch ----------

def make_birch():
    g = ms.make_birch(tp.HONEY_OAK, ("E", "6", "7"))
    for pts in (tp.swag(8, 24, 12, 4), tp.swag(7, 25, 19, 4)):
        tp.lights(g, pts, tp.HONEY_OAK)
    small_pumpkin(g, 8.5, 39.5, 3.2, 2.4)
    small_pumpkin(g, 23.5, 40.0, 2.8, 2.1, ("8", "7", "9"))
    return g


# ---------- hay bales ----------

def make_hay_bales():
    g = mh.make_hay_bales()

    def P(u, v, z):
        return (32 + u - v, 64 + (u + v) / 2 - z)

    # pumpkins resting on the top bale (its top face is at z = 33)
    for u, v, rx, ry, tones in ((7.0, 15.0, 4.6, 3.4, ("7", "6", "8")), (17.0, 15.0, 3.8, 2.9, ("Z", "Z", "V")),
                                (26.0, 21.0, 3.2, 2.5, ("8", "7", "9"))):
        x, y = P(u, v, 33)
        small_pumpkin(g, x, y - ry + 0.5, rx, ry, tones, over=".sEFIJ")
    # a swag of string lights along the front of the lower bales, only where there is hay
    for pts in (tp.swag(6, 30, 79, 4), tp.swag(34, 58, 80, 4)):
        tp.lights(g, pts, "EFIJ")
    return g


# ---------- shrine ----------

def make_shrine():
    g = ms.make_shrine(True)
    # a wreath of wheat and berries hung above the door
    cx, cy = 24.0, 63.5
    for y in range(int(cy - 6), int(cy + 7)):
        for x in range(int(cx - 6), int(cx + 7)):
            d = ((x + 0.5 - cx) ** 2 + ((y + 0.5 - cy) * 1.1) ** 2) ** 0.5
            if 2.6 <= d <= 5.0 and g.c[y][x] in "ABCD":
                g.put(x, y, "_" if (x * 3 + y) % 7 == 0 else ("6", "7", "8")[(x + y) % 3])
    # string lights along the roof eaves
    for (x0, y0), (x1, y1) in (((12, 54), (32, 64)), ((32, 64), (52, 54))):
        n = int(max(abs(x1 - x0), abs(y1 - y0)) * 2)
        for i in range(n + 1):
            x, y = int(round(x0 + (x1 - x0) * i / n)), int(round(y0 + (y1 - y0) * i / n))
            if i % 5 == 0 and g.c[y][x] in "RST":
                g.put(x, y, "G")
    # two lanterns on the slab corners
    for lx, ly in ((7, 77), (56, 77)):
        cells = set()
        for dy in range(5):
            g.put(lx, ly - dy, "D")
            cells.add((lx, ly - dy))
        for dx in (-1, 0, 1):
            for dy in (-7, -6, -5):
                g.put(lx + dx, ly + dy, "H" if dy == -5 else "G")
                cells.add((lx + dx, ly + dy))
        g.put(lx, ly - 8, "D")
        cells.add((lx, ly - 8))
        tp.ring(g, cells)
    return g


# ---------- pond ----------

def make_pond():
    g = ms.make_pond(True)
    for lx, ly in ((23, 80), (42, 82)):  # two floating paper lanterns, cream with a warm glow
        cells = set()
        for dy in (-2, -1, 0):
            for dx in (-2, -1, 0, 1):
                if g.c[ly + dy][lx + dx] in "WXYQ678":
                    g.put(lx + dx, ly + dy, "F" if (dx in (-1, 0) and dy == -1) else "Z")
                    cells.add((lx + dx, ly + dy))
        for dx in (-1, 0):
            if g.c[ly + 1][lx + dx] in "WXYQ":
                g.put(lx + dx, ly + 1, "v")
                cells.add((lx + dx, ly + 1))
        ring(g, cells, "WXYQ678")
    return g


SPRITES = {"hay_bales": make_hay_bales, "shrine": make_shrine, "birch": make_birch, "pond": make_pond}
KINDS = {"hay_bales": "landmark", "shrine": "landmark", "pond": "landmark", "birch": "tree"}


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
