"""Conform the ТАШМА hero stills onto a common 1920x1080 (16:9) black canvas.

Every source has a pure-black studio background, so padding is visually invisible --
we scale each image to fit the canvas height and centre it, never cropping the subject.
"""
from pathlib import Path

from PIL import Image

SRC = Path(r"e:\tashma")
DST = Path(r"e:\tashma\tashma-honey\public\images\hero")

CANVAS = (1920, 1080)

# source filename -> conformed name (numbering follows the scroll story order)
MAPPING = (
    ("Image 1.png", "image-1-honeycomb-hero.png"),
    ("Image 2.png", "image-2-honey-begin-to-flow.png"),
    ("Iamge 3.png", "image-3-honey-dripping-down.png"),
    ("Image 4.png", "image-4-honey-into-jar.png"),
    ("Image 5.png", "image-5-honey-swirl.png"),
    ("Image 6.png", "image-6-honey-spoon-pour.png"),
)


def conform(src_path, dst_path, canvas=CANVAS):
    """Return a new canvas-sized image with src scaled to fit and centred on black."""
    with Image.open(src_path) as img:
        source = img.convert("RGB")

    cw, ch = canvas
    scale = min(cw / source.width, ch / source.height)
    size = (round(source.width * scale), round(source.height * scale))
    resized = source.resize(size, Image.LANCZOS)

    canvas_img = Image.new("RGB", canvas, (0, 0, 0))
    offset = ((cw - size[0]) // 2, (ch - size[1]) // 2)
    canvas_img.paste(resized, offset)
    canvas_img.save(dst_path, "PNG", optimize=True)
    return source.size, size, offset


def main():
    DST.mkdir(parents=True, exist_ok=True)

    for src_name, dst_name in MAPPING:
        src_path = SRC / src_name
        if not src_path.exists():
            raise SystemExit(f"missing source: {src_path}")

        original, scaled, offset = conform(src_path, DST / dst_name)
        pad = offset[0]
        print(
            f"{src_name:14s} {original[0]}x{original[1]}"
            f" -> {scaled[0]}x{scaled[1]} on {CANVAS[0]}x{CANVAS[1]}"
            f"  (pad {pad}px per side)  {dst_name}"
        )


if __name__ == "__main__":
    main()
