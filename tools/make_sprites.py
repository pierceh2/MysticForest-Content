from PIL import Image

PALETTE = {}


def image_from_rows(rows):
    if not rows or not rows[0] or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError("rows must be non-empty and have equal lengths")
    image = Image.new("RGBA", (len(rows[0]), len(rows)), (0, 0, 0, 0))
    for y, row in enumerate(rows):
        for x, pixel in enumerate(row):
            if pixel != ".":
                image.putpixel((x, y), PALETTE[pixel])
    return image


def main():
    pass


if __name__ == "__main__":
    main()