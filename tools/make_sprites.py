"""Draws the Mystic Forest sprites in code. Run: python3 tools/make_sprites.py

Each sprite is built on a character grid (one character per pixel, '.' is
transparent) mapped through PALETTE, outlined, and saved as an RGBA PNG.
Pillow only.
"""
import os
import sys

from PIL import Image

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sprites", "default8bit")


def rgb(hex_color):
    h = hex_color.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 255)


PALETTE = {k: rgb(v) for k, v in {
    "k": "#101b15",  # outline
    "s": "#1d2d22",  # ground shadow under a tree foot
    # trunk browns
    "t": "#80552f", "u": "#5d3d23", "v": "#3f2a1a",
    # oak greens, light to dark
    "1": "#7aa63f", "2": "#58903a", "3": "#40762f", "4": "#2d5c2b", "5": "#1f4426",
    # pine blue-greens
    "a": "#4f8f62", "b": "#377249", "c": "#27583b", "d": "#1a4030", "e": "#112c22",
    # birch yellow-greens, bark
    "f": "#b0c24f", "g": "#8cab40", "h": "#6c8f36", "i": "#527230", "j": "#3b5628",
    "w": "#dcd8c8", "x": "#aaa696", "y": "#2a2a28",
    # willow pale greens
    "l": "#a3c077", "m": "#80a262", "n": "#648550", "o": "#4b6a40", "p": "#37522f",
    # stone
    "A": "#8c9289", "B": "#6f7770", "C": "#565e58", "D": "#3c443f",
    # slate roof
    "R": "#5f8590", "S": "#486a75", "T": "#34515c",
    # warm glow
    "G": "#f4c85e", "H": "#c98a3a",
}.items()}

OAK = "12345"
PINE = "abcde"
BIRCH = "fghij"
WILLOW = "lmnop"


class Grid:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.c = [["."] * w for _ in range(h)]

    def put(self, x, y, ch):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.c[y][x] = ch

    def paint(self, inside, pick):
        """For every pixel whose centre is inside, set the char pick(x, y) returns."""
        for y in range(self.h):
            for x in range(self.w):
                if inside(x + 0.5, y + 0.5):
                    ch = pick(x, y)
                    if ch:
                        self.c[y][x] = ch

    def outline(self):
        src = [row[:] for row in self.c]
        for y in range(self.h):
            for x in range(self.w):
                if src[y][x] != ".":
                    continue
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.w and 0 <= ny < self.h and src[ny][nx] not in (".", "s"):
                        self.c[y][x] = "k"
                        break

    def rows(self):
        return ["".join(r) for r in self.c]


def noise(x, y):
    return ((x * 73856093) ^ (y * 19349663)) % 97


def circle(cx, cy, r):
    return lambda x, y: (x - cx) ** 2 + (y - cy) ** 2 <= r * r


def ellipse(cx, cy, rx, ry):
    return lambda x, y: ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1


def polygon(pts):
    def inside(x, y):
        hit = False
        j = len(pts) - 1
        for i in range(len(pts)):
            xi, yi = pts[i]
            xj, yj = pts[j]
            if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
                hit = not hit
            j = i
        return hit
    return inside


def puff(g, cx, cy, r, ramp):
    """A lit ball of leaves: light from the top left, darker rim at the lower right."""
    def pick(x, y):
        s = (-(x + 0.5 - cx) - (y + 0.5 - cy)) / (r * 1.414)
        idx = 0 if s > 0.5 else 1 if s > 0.15 else 2 if s > -0.25 else 3 if s > -0.6 else 4
        n = noise(x, y)
        if n % 9 == 0 and idx > 0:
            idx -= 1
        elif n % 13 == 0 and idx < 4:
            idx += 1
        return ramp[idx]
    g.paint(circle(cx, cy, r), pick)


def trunk(g, cx, top, bottom, half_top, half_bottom, lean=0.0):
    def half(y):
        t = (y - top) / (bottom - top)
        return half_top + (half_bottom - half_top) * t ** 2

    def mid(y):
        return cx + lean * (1 - (y - top) / (bottom - top))

    def inside(x, y):
        return top <= y <= bottom and abs(x - mid(y)) <= half(y)

    def pick(x, y):
        d = (x + 0.5 - mid(y + 0.5)) / half(y + 0.5)
        return "t" if d < -0.35 else "u" if d < 0.55 else "v"
    g.paint(inside, pick)


def tree_grid():
    g = Grid(32, 48)
    g.paint(ellipse(16, 40, 9, 2), lambda x, y: "s")  # shadow; only rows 40-41 stay visible
    return g


def make_oak():
    g = tree_grid()
    trunk(g, 16, 26, 40, 2.4, 3.6)
    for cx, cy, r in ((9.5, 21, 7.5), (22.5, 21, 7.5), (16, 22.5, 8.5), (7.5, 15, 5.5),
                      (24.5, 15, 5.5), (16, 11.5, 9)):
        puff(g, cx, cy, r, OAK)
    g.outline()
    return g


def make_pine():
    g = tree_grid()
    trunk(g, 16, 33, 40, 1.9, 2.6)
    for apex, base, hw in ((22, 37, 14.0), (16, 31, 12.0), (9, 24, 9.5), (3, 16, 6.5)):
        def inside(x, y, apex=apex, base=base, hw=hw):
            t = (y - apex) / (base - apex)
            row_hw = t * hw + (0.8 if int(y) % 3 == 0 else 0)
            bottom = base + (1 if int(x) % 4 in (1, 2) else 0)
            return apex <= y < bottom and abs(x - 16) <= row_hw

        def pick(x, y, apex=apex, base=base, hw=hw):
            t = (y - apex) / (base - apex)
            row_hw = t * hw + 0.8
            d = (x + 0.5 - 16) / row_hw
            if y >= base - 1:
                return PINE[4] if d > -0.2 else PINE[3]
            if y >= base - 3:
                return PINE[3] if d > -0.2 else PINE[2]
            idx = 0 if d < -0.55 else 1 if d < -0.05 else 2 if d < 0.5 else 3
            if noise(x, y) % 11 == 0 and idx > 0:
                idx -= 1
            return PINE[idx]
        g.paint(inside, pick)
    g.outline()
    return g


def make_birch():
    g = tree_grid()
    # white trunk with dark bark marks
    def pick_trunk(x, y):
        if (x, y) in ((15, 27), (16, 27), (14, 31), (15, 31), (16, 35), (17, 35), (14, 37), (15, 33)):
            return "y"
        return "w" if x <= 15 else "x"
    g.paint(lambda x, y: 20 <= y <= 40 and abs(x - 16) <= 1.5 + (0.9 if y > 37 else 0), pick_trunk)
    for cx, cy, r in ((16, 9.5, 6), (12, 14, 5.2), (20.5, 14, 5.2), (16, 18.5, 6),
                      (12.5, 23, 4.3), (19.5, 23.5, 4.3)):
        puff(g, cx, cy, r, BIRCH)
    g.outline()
    return g


def make_willow():
    g = tree_grid()
    trunk(g, 16, 22, 40, 2.8, 4.0, lean=-0.6)
    # dome
    for cx, cy, r in ((16, 13, 10.5), (8.5, 17, 6), (23.5, 17, 6), (16, 17, 9)):
        puff(g, cx, cy, r, WILLOW)
    # hanging strands, shorter in the middle so the trunk shows through
    for x in range(3, 29):
        if x % 3 == 2:
            continue
        mid = abs(x - 15.5)
        end = 30 + noise(x, 7) % 7 if mid > 5 else 27 + noise(x, 7) % 3
        for y in range(17, end):
            d = (x - 15.5) / 13.0
            idx = 0 if d < -0.5 else 1 if d < 0.0 else 2 if d < 0.5 else 3
            if (y + x) % 7 == 0 and idx > 0:
                idx -= 1
            if y > end - 3:
                idx = min(4, idx + 1)
            g.put(x, y, WILLOW[idx])
    g.outline()
    return g


def make_shrine():
    g = Grid(64, 96)
    stone = "ABCD"

    def face_pick(x, y, light, step):
        base = {"L": 1, "R": 2, "T": 0}[light]
        n = noise(x, y)
        if step and (y // step + (x // 5 if (y // step) % 2 else 0)) != (y - 1) // step + (x // 5 if ((y - 1) // step) % 2 else 0):
            return stone[min(3, base + 1)]
        if n % 17 == 0:
            return stone[min(3, base + 1)]
        return stone[base]

    # slab: top diamond, left and right sides
    g.paint(polygon([(2, 75), (32, 90), (32, 95), (2, 80)]), lambda x, y: stone[2] if noise(x, y) % 15 else stone[3])
    g.paint(polygon([(32, 90), (62, 75), (62, 80), (32, 95)]), lambda x, y: stone[3] if noise(x, y) % 15 else stone[2])
    g.paint(polygon([(32, 60), (62, 75), (32, 90), (2, 75)]), lambda x, y: face_pick(x, y, "T", 0))
    # walls
    g.paint(polygon([(16, 75), (32, 83), (32, 59), (16, 51)]), lambda x, y: face_pick(x, y, "L", 5))
    g.paint(polygon([(32, 83), (48, 75), (48, 51), (32, 59)]), lambda x, y: face_pick(x, y, "R", 5))
    # doorway on the lit wall with a warm glow
    def bottom_y(x):
        return 75 + (x - 16) * 0.5
    g.paint(polygon([(21, bottom_y(21) - 11), (27, bottom_y(27) - 11), (27, bottom_y(27)), (21, bottom_y(21))]),
            lambda x, y: "k")
    g.paint(polygon([(22.5, bottom_y(22.5) - 8), (25.5, bottom_y(25.5) - 8), (25.5, bottom_y(25.5)), (22.5, bottom_y(22.5))]),
            lambda x, y: "G" if y < bottom_y(x) - 3 else "H")
    # roof
    g.paint(polygon([(10, 51), (32, 62), (32, 30)]), lambda x, y: "R" if (x + y) % 6 else "S")
    g.paint(polygon([(32, 62), (54, 51), (32, 30)]), lambda x, y: "S" if (x - y) % 6 else "T")
    # roof eave shadow line
    g.paint(polygon([(10, 51), (32, 62), (32, 59), (10, 48)]), lambda x, y: "T")
    g.paint(polygon([(32, 62), (54, 51), (54, 48), (32, 59)]), lambda x, y: "T")
    # moss on roof, walls and slab
    moss = OAK
    for x in range(64):
        for y in range(96):
            ch = g.c[y][x]
            if ch == ".":
                continue
            n = noise(x, y)
            if ch in "RS" and n % 8 == 0 and x < 36 and y < 50:
                g.put(x, y, moss[2 if n % 2 else 3])
            elif ch in "ABCD" and y >= 84 and n % 14 == 0:
                g.put(x, y, moss[3])
            elif ch in "ABC" and 60 <= y < 80 and n % 23 == 0:
                g.put(x, y, moss[2])
    # grass tufts on the slab corners
    for tx, ty in ((9, 76), (54, 76), (32, 62), (47, 86), (17, 86)):
        for dx, dy, i in ((0, 0, 1), (1, -1, 0), (-1, -1, 2), (0, -1, 1), (1, 0, 2)):
            g.put(tx + dx, ty + dy, moss[i])
    g.outline()
    return g


SPRITES = {
    "oak": make_oak,
    "pine": make_pine,
    "birch": make_birch,
    "willow": make_willow,
    "shrine": make_shrine,
}


def image_from_rows(rows):
    if not rows or not rows[0] or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError("rows must be non-empty and have equal lengths")
    image = Image.new("RGBA", (len(rows[0]), len(rows)), (0, 0, 0, 0))
    for y, row in enumerate(rows):
        for x, pixel in enumerate(row):
            if pixel != ".":
                image.putpixel((x, y), PALETTE[pixel])
    return image


def main(keys=None):
    os.makedirs(OUT_DIR, exist_ok=True)
    for key in keys or SPRITES:
        image = image_from_rows(SPRITES[key]().rows())
        colours = len({p for p in image.get_flattened_data() if p[3]})
        if colours > 16:
            sys.exit("%s uses %d colours (max 16)" % (key, colours))
        image.save(os.path.join(OUT_DIR, key + ".png"))
        print("wrote %s.png (%dx%d, %d colours)" % (key, image.width, image.height, colours))


if __name__ == "__main__":
    main(sys.argv[1:] or None)
