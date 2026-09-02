# ТАШМА — asset status

What exists, what the guide expected, and what is still optional.

## Done

| Asset | Path | Notes |
|---|---|---|
| Hero keyframes 1–6 | `public/images/hero/image-{1..6}-*.png` | Supplied by you, conformed to 1920×1080 on black |
| Hero keyframe 7 | `public/images/hero/image-7-hands-holding-jar.png` | Generated (Nano Banana, 2 variants, B chosen), scale-matched to image-6 at 1.16× |
| Hero clips 1–6 | `source/clips/v{1..6}-*.mp4` | FLUX 3 Video, 5s each, 1080p, 16:9, no audio. Kept outside `public/` — they are source material, not site assets |
| Merged hero video | `source/honey-story-final.mp4` | Steps 3: hard-cut concat, 30.25 s, 1920×1080, 24 fps |
| Frame sequence | `public/frames/frame_0001.jpg … frame_0605.jpg` | Step 4b: 20 fps, 960×540, `-q:v 4`, 23 MB total |
| Edge feather | `image-7` + frames 505–605 | Image-7's forearms hit the 4:5 frame edge, so after padding to 16:9 they hard-cut against black. A 200px horizontal fade at the padding boundary is applied to the still and to the clip-6 frames. **If you ever re-extract frames, re-apply it** (`feather.py`). |
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
