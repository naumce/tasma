"""Conform the generated image-7 onto the 1920x1080 hero canvas.

The generator frames the jar slightly smaller than image-6 does, so image-7 gets a
zoom multiplier to bring the jar back to the same on-screen size. Everything else
matches conform.py: fit to canvas height, centre on black.
"""
import sys
from pathlib import Path

from PIL import Image

SRC = Path(
    r"C:\Users\Naum\AppData\Local\Temp\claude\e--tashma"
    r"\38345b7a-e563-4fca-a58c-74635e53e51b\scratchpad\v7b.png"
)
HERO = Path(r"e:\tashma\tashma-honey\public\images\hero")
DST = HERO / "image-7-hands-holding-jar.png"
COMPARE = SRC.parent / "compare-6-7.png"

CANVAS = (1920, 1080)


def conform(source, canvas=CANVAS, zoom=1.0):
    """Scale source to fit the canvas height (times zoom) and centre it on black."""
    cw, ch = canvas
    scale = min(cw / source.width, ch / source.height) * zoom
    size = (round(source.width * scale), round(source.height * scale))
    resized = source.resize(size, Image.LANCZOS)

    out = Image.new("RGB", canvas, (0, 0, 0))
    out.paste(resized, ((cw - size[0]) // 2, (ch - size[1]) // 2))
    return out


def jar_span(image, band=0.62):
    """Rough width of the lit subject on one scanline, used to compare jar scale."""
    row = round(image.height * band)
    pixels = image.convert("L").crop((0, row, image.width, row + 1)).getdata()
    lit = [x for x, value in enumerate(pixels) if value > 60]
    return (lit[0], lit[-1], lit[-1] - lit[0]) if lit else (0, 0, 0)


def main():
    zoom = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0

    with Image.open(SRC) as img:
        source = img.convert("RGB")

    conformed = conform(source, zoom=zoom)
    conformed.save(DST, "PNG", optimize=True)

    with Image.open(HERO / "image-6-honey-spoon-pour.png") as img:
        six = img.convert("RGB")

    print(f"zoom {zoom}  -> {DST.name}")
    print(f"  image-6 lit span at 0.62h: {jar_span(six)}")
    print(f"  image-7 lit span at 0.62h: {jar_span(conformed)}")

    # stack the two frames so the jar scale can be compared by eye
    strip = Image.new("RGB", (CANVAS[0] // 2, CANVAS[1]), (0, 0, 0))
    strip.paste(six.resize((CANVAS[0] // 2, CANVAS[1] // 2), Image.LANCZOS), (0, 0))
    strip.paste(
        conformed.resize((CANVAS[0] // 2, CANVAS[1] // 2), Image.LANCZOS),
        (0, CANVAS[1] // 2),
    )
    strip.save(COMPARE, "PNG")
    print(f"  comparison -> {COMPARE}")


if __name__ == "__main__":
    main()
