# ТАШМА — asset status

What exists, what the guide expected, and what is still optional.

## Done

| Asset | Path | Notes |
|---|---|---|
| Hero keyframes 1–6 | `public/images/hero/image-{1..6}-*.png` | Supplied by you, conformed to 1920×1080 on black |
| Hero keyframe 4 (v2) | `public/images/hero/image-4-honey-into-jar.png` | Regenerated 2026-09-18 (GPT Image 2.5) from image-5 as reference so the jar/label are identical across 4→7 |
| Hero keyframe 7 (v2) | `public/images/hero/image-7-hands-holding-jar.png` | Regenerated 2026-09-18 as native 16:9 from image-6; no padding, no feather hack |
| Hero clips 1, 2, 5 | `source/clips/v{1,2,5}-*.mp4` | FLUX 3 Video, 5s each, 1080p |
| Hero clips 3, 4, 6 (v2) | `source/clips-v2/v{3,4,6}-*.mp4` | MiniMax H3, 2K, 6.6s each. Clip 3 is now an explicit tilt-down; clip 6 starts from the native-16:9 hands frame |
| Conformed clips | `source/conformed/*.mp4` | All six at 1920×1080 / 24 fps, CRF 14 — the concat input |
| Merged hero video | `source/honey-story-final.mp4` | Hard-cut concat of `source/conformed`, 34.9 s, 1920×1080, 24 fps |
| Frame sequences | `public/frames/{hd,desktop,mobile}/frame_0001.webp …` | 523 frames @ 15 fps per tier: hd 1920w q80 (42 MB), desktop 1152w q72 (17 MB), mobile 640w q68 (7 MB). The hero preloader measures throughput on `desktop` and switches up or down |
| Edge feather | — | No longer needed: image-7 v2 is native 16:9. `feather.py` is kept for history only |
| Site | `public/index.html` | Single file, vanilla JS, GSAP + ScrollTrigger + Lenis from jsDelivr, fonts from Google Fonts (Cormorant Garamond + Inter, both with Cyrillic). Verified in Chromium at 1440×900 and 390×844. |

## FFmpeg

Not on PATH, but `imageio_ffmpeg` bundles one — Steps 3 and 4b were run with it:

```
python -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())"
```

Use that path anywhere the guide says `ffmpeg`.

## Skipped from the guide — optional polish

These were in the Assam Honey guide's Step 5. The master prompt has been written so the
page is complete **without** them; add any of these later as a scoped refinement.

| Guide asset | Status | If you want it |
|---|---|---|
| 3 varietal product shots | Not applicable | ТАШМА is one product |
| `bg-apiary-golden-hour.png` | Not generated | Macedonian meadow apiary at golden hour, same prompt shape as the guide's 5b |
| `bg-forest-twilight.png` | Not generated | Same, Macedonian hills |
| 3 lifestyle stills | Not generated | Dipper drizzle, honeycomb macro, honey on bread — guide 5c prompts work as-is |
| 3 ritual loop videos (`card-*.mp4`) | Not generated | ~4s loops from stills; the master prompt uses CSS Ken Burns over stills instead |

Rough credit cost if you want all of the above later: 5 images (≈5–10 each) + 3 short
loops (≈45 each at 1080p) ≈ 170–200 credits.

## Re-extracting frames

```
ffmpeg -f concat -safe 0 -i source/conformed/concat.txt -c copy source/honey-story-final.mp4
ffmpeg -i source/honey-story-final.mp4 -vf "fps=15,scale=1920:-2" -c:v libwebp -quality 80 public/frames/hd/frame_%04d.webp
ffmpeg -i source/honey-story-final.mp4 -vf "fps=15,scale=1152:-2" -c:v libwebp -quality 72 public/frames/desktop/frame_%04d.webp
ffmpeg -i source/honey-story-final.mp4 -vf "fps=15,scale=640:-2"  -c:v libwebp -quality 68 public/frames/mobile/frame_%04d.webp
```
Then set `TOTAL_FRAMES` in `public/index.html` to the count.
