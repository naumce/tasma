"""Rebuild the hero frame sequence from the six clips.

    python source/tools/rebuild_hero.py            # conform -> merge -> extract -> seams
    python source/tools/rebuild_hero.py seams      # only report the biggest frame jumps

CLIP_SOURCES says which file feeds each slot; everything is conformed to 1920x1080 / 24 fps
so the concat can stream-copy. After extracting, TOTAL_FRAMES in public/index.html is
updated to the new count. Remember to bump ASSET_VERSION there too: /frames is immutable.
"""
import re
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg
import numpy as np
from PIL import Image

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
PROJECT = Path(__file__).resolve().parents[2]
SOURCE = PROJECT / "source"
CONFORMED = SOURCE / "conformed"
MASTER = SOURCE / "honey-story-final.mp4"
FRAMES = PROJECT / "public" / "frames"
PAGE = PROJECT / "public" / "index.html"

CLIP_SOURCES = (
    ("v1-honeycomb-to-flow.mp4", SOURCE / "clips" / "v1-honeycomb-to-flow.mp4"),
    ("v2-flow-to-dripping.mp4", SOURCE / "clips" / "v2-flow-to-dripping.mp4"),
    ("v3-dripping-to-jar.mp4", SOURCE / "clips-nectra" / "v3-dripping-to-jar.mp4"),
    ("v4-jar-to-swirl.mp4", SOURCE / "clips-nectra" / "v4-jar-to-swirl.mp4"),
    ("v5-swirl-to-spoon.mp4", SOURCE / "clips-nectra" / "v5-swirl-to-spoon.mp4"),
    ("v6-spoon-to-hands.mp4", SOURCE / "clips-nectra" / "v6-spoon-to-hands.mp4"),
)

FPS = 15
TIERS = (("hd", 1920, 80), ("desktop", 1152, 72), ("mobile", 640, 68))


def ffmpeg(*args):
    result = subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", *args],
                            capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(f"ffmpeg failed: {' '.join(args)[:200]}\n{result.stderr[-1500:]}")


def conform():
    """Scale + crop to 1920x1080 (FLUX pads to 1088, MiniMax outputs 2560x1440)."""
    CONFORMED.mkdir(parents=True, exist_ok=True)
    for name, src in CLIP_SOURCES:
        if not src.exists():
            raise SystemExit(f"missing clip: {src}")
        ffmpeg("-i", str(src), "-an",
               "-vf", "scale=1920:1080:force_original_aspect_ratio=increase:flags=lanczos,"
                      "crop=1920:1080,format=yuv420p",
               "-r", "24", "-c:v", "libx264", "-preset", "slow", "-crf", "14",
               "-movflags", "+faststart", str(CONFORMED / name))
        print(f"conformed {name}")


def merge():
    concat = CONFORMED / "concat.txt"
    concat.write_text("".join(f"file '{name}'\n" for name, _ in CLIP_SOURCES), encoding="utf-8")
    ffmpeg("-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", str(MASTER))
    print(f"merged -> {MASTER.name}")


def extract():
    procs = []
    for tier, width, quality in TIERS:
        out = FRAMES / tier
        out.mkdir(parents=True, exist_ok=True)
        for old in out.glob("frame_*.webp"):
            old.unlink()
        procs.append(subprocess.Popen(
            [FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-i", str(MASTER),
             "-vf", f"fps={FPS},scale={width}:-2", "-c:v", "libwebp", "-quality", str(quality),
             str(out / "frame_%04d.webp")]))
    if any(p.wait() != 0 for p in procs):
        raise SystemExit("frame extraction failed")

    counts = {tier: len(list((FRAMES / tier).glob("frame_*.webp"))) for tier, _, _ in TIERS}
    if len(set(counts.values())) != 1:
        raise SystemExit(f"tier frame counts differ: {counts}")
    total = counts["hd"]
    html = PAGE.read_text(encoding="utf-8")
    html, n = re.subn(r"const TOTAL_FRAMES = \d+;", f"const TOTAL_FRAMES = {total};", html)
    if n != 1:
        raise SystemExit("TOTAL_FRAMES not found in index.html")
    PAGE.write_text(html, encoding="utf-8")
    print(f"extracted {total} frames per tier; TOTAL_FRAMES updated")


def seams(top=8):
    files = sorted((FRAMES / "mobile").glob("frame_*.webp"))
    prev, steps = None, []
    for f in files:
        cur = np.asarray(Image.open(f).convert("L"), dtype=np.float32)
        if prev is not None:
            steps.append(float(np.abs(cur - prev).mean()))
        prev = cur
    steps = np.array(steps)
    print(f"median step {np.median(steps):.2f}; biggest jumps (frame -> frame, step):")
    for i in np.argsort(steps)[::-1][:top]:
        print(f"  {i + 1:4d} -> {i + 2:4d}  {steps[i]:.2f}")


def main():
    step = sys.argv[1] if len(sys.argv) > 1 else "all"
    if step == "seams":
        seams()
        return
    conform()
    merge()
    extract()
    seams()


if __name__ == "__main__":
    main()
