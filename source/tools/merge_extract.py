"""Steps 3 + 4b of the guide, driven by the ffmpeg bundled with imageio_ffmpeg.

Step 3  -- hard-cut concat of the six hero clips into honey-story-final.mp4
Step 4b -- extract that video into public/frames/frame_%04d.jpg at 20 fps, 960px wide
"""
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

PROJECT = Path(r"e:\tashma\tashma-honey")
CLIPS = PROJECT / "source" / "clips"
FRAMES = PROJECT / "public" / "frames"
MERGED = PROJECT / "source" / "honey-story-final.mp4"
CONCAT_LIST = CLIPS / "concat.txt"

ORDER = (
    "v1-honeycomb-to-flow.mp4",
    "v2-flow-to-dripping.mp4",
    "v3-dripping-to-jar.mp4",
    "v4-jar-to-swirl.mp4",
    "v5-swirl-to-spoon.mp4",
    "v6-spoon-to-hands.mp4",
)

# guide's extraction settings: fps=20, 960px wide, -q:v 4
EXTRACT_FPS = 20
EXTRACT_WIDTH = 960
JPEG_QUALITY = 4


def run(args):
    result = subprocess.run([FFMPEG, "-hide_banner", "-y", *args], capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(f"ffmpeg failed:\n{result.stderr[-2000:]}")
    return result


def merge():
    """Concat with re-encode so every clip lands on one identical stream layout.

    FLUX emits 1920x1088 (height padded to a multiple of 16); the padding is black, so a
    centred crop back to 1080 costs nothing and avoids resampling the whole frame.
    """
    missing = [name for name in ORDER if not (CLIPS / name).exists()]
    if missing:
        raise SystemExit(f"missing clips: {missing}")

    CONCAT_LIST.write_text(
        "".join(f"file '{(CLIPS / name).as_posix()}'\n" for name in ORDER), encoding="utf-8"
    )
    run([
        "-f", "concat", "-safe", "0", "-i", str(CONCAT_LIST),
        "-an",
        "-vf", "crop=1920:1080,format=yuv420p",
        "-r", "24",
        "-c:v", "libx264", "-preset", "slow", "-crf", "16",
        "-movflags", "+faststart",
        str(MERGED),
    ])
    print(f"merged -> {MERGED} ({MERGED.stat().st_size // 1024} KB)")


def extract():
    if FRAMES.exists():
        for old in FRAMES.glob("frame_*.jpg"):
            old.unlink()
    FRAMES.mkdir(parents=True, exist_ok=True)

    run([
        "-i", str(MERGED),
        "-vf", f"fps={EXTRACT_FPS},scale={EXTRACT_WIDTH}:-1",
        "-q:v", str(JPEG_QUALITY),
        str(FRAMES / "frame_%04d.jpg"),
    ])
    frames = sorted(FRAMES.glob("frame_*.jpg"))
    total_kb = sum(f.stat().st_size for f in frames) // 1024
    print(f"extracted {len(frames)} frames -> {FRAMES}  ({total_kb} KB total)")


def main():
    step = sys.argv[1] if len(sys.argv) > 1 else "all"
    if step in ("merge", "all"):
        merge()
    if step in ("extract", "all"):
        extract()


if __name__ == "__main__":
    main()
