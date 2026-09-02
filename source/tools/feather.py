"""Feather the left/right padding boundary of the hands frame.

image-7 was a 4:5 still padded onto a 16:9 black canvas. The forearms ran to the edge of the
original frame, so after padding they end in a hard vertical cut against black. This fades
the outermost band of the content region to black so the arms dissolve into the dark instead.

Applied to the still itself and to the extracted hero frames of clip 6 (frames 505-605), which
end on that same still. Frames earlier in clip 6 have nothing but black in the feather zones, so
the mask is a no-op there.
"""
from pathlib import Path

from PIL import Image, ImageChops

HERO = Path(r"e:\tashma\tashma-honey\public\images\hero\image-7-hands-holding-jar.png")
FRAMES = Path(r"e:\tashma\tashma-honey\public\frames")
FIRST_HAND_FRAME, LAST_FRAME = 505, 605

FEATHER_PX = 200          # width of the fade band at 1920px scale
THRESHOLD = 20            # luminance above which a column counts as content


def content_extent(image):
    """Leftmost and rightmost columns holding anything brighter than the padding."""
    gray = image.convert("L")
    width, height = gray.size
    peaks = [gray.crop((x, 0, x + 1, height)).getextrema()[1] for x in range(width)]
    lit = [x for x, value in enumerate(peaks) if value > THRESHOLD]
    return (lit[0], lit[-1]) if lit else (0, width - 1)


def smoothstep(t):
    return t * t * (3 - 2 * t)


def build_mask(width, height, left, right, feather):
    """Horizontal luminance mask: 0 outside the content, ramping to 255 inside it."""
    row = bytearray(width)
    for x in range(width):
        if x < left or x > right:
            value = 0.0
        elif x < left + feather:
            value = smoothstep((x - left) / feather)
        elif x > right - feather:
            value = smoothstep((right - x) / feather)
        else:
            value = 1.0
        row[x] = int(round(value * 255))
    return Image.frombytes("L", (width, 1), bytes(row)).resize((width, height))


def feather(path, left, right, feather_px):
    with Image.open(path) as img:
        source = img.convert("RGB")
    mask = build_mask(source.width, source.height, left, right, feather_px)
    black = Image.new("RGB", source.size, (0, 0, 0))
    result = Image.composite(source, black, mask)
    result.save(path, "JPEG" if path.suffix.lower() == ".jpg" else "PNG", quality=92, optimize=True)


def main():
    with Image.open(HERO) as img:
        left, right = content_extent(img.convert("RGB"))
        scale = 960 / img.width
    print(f"image-7 content spans x={left}..{right} of {HERO.name}; feather {FEATHER_PX}px")
    feather(HERO, left, right, FEATHER_PX)

    f_left, f_right, f_px = round(left * scale), round(right * scale), round(FEATHER_PX * scale)
    for n in range(FIRST_HAND_FRAME, LAST_FRAME + 1):
        feather(FRAMES / f"frame_{n:04d}.jpg", f_left, f_right, f_px)
    print(f"feathered frames {FIRST_HAND_FRAME}..{LAST_FRAME} at x={f_left}..{f_right}, {f_px}px")


if __name__ == "__main__":
    main()
