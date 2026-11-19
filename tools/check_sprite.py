# check_sprite.py: python3 tools/check_sprite.py path/to/sprite.png tree|landmark   (checks one PNG against the sprite rules)
import sys
from PIL import Image
path, kind = sys.argv[1], sys.argv[2]
want = (32, 48) if kind == "tree" else (64, 96)
img = Image.open(path)
assert img.mode == "RGBA", f"mode is {img.mode}, must be RGBA"
assert img.size == want, f"size is {img.size}, must be {want}"
px = img.load(); w, h = img.size
alphas = {px[x, y][3] for x in range(w) for y in range(h)}
assert alphas <= {0, 255}, f"alpha values {sorted(alphas)}; only 0 and 255 allowed"
assert 255 in alphas, "the sprite is empty"
opaque = lambda x, y: px[x, y][3] == 255
assert not any(opaque(0, y) or opaque(w - 1, y) for y in range(h)), "an opaque pixel touches the left or right edge"
assert not any(opaque(x, 0) for x in range(w)), "an opaque pixel touches the top edge"
low = max(y for y in range(h) if any(opaque(x, y) for x in range(w)))
if kind == "tree":
    assert 36 <= low <= 44, f"lowest opaque row is {low}; a tree's foot should end around row 40, 8 rows above the bottom edge"
else:
    assert low >= h - 8, f"lowest opaque row is {low}; a landmark's base should reach down near the bottom corner (row {h - 1})"
assert len({px[x, y] for x in range(w) for y in range(h) if opaque(x, y)}) <= 16, "more than 16 colours"
print("OK", path)
