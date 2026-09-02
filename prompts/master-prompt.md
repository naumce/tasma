# ТАШМА — master prompt for Antigravity

Adapted from Step 7 of the Assam Honey guide. Two structural changes from the original:

1. **Copy is Macedonian**, matching the label (`Природен Органски Мед`).
2. **One product, not three varietals.** The guide's LITCHI / MUSTARD / WILD FOREST
   explainer becomes three chapters of one honey's story — потекло (origin), процес
   (process), чистота (purity) — keeping the identical sticky-panel and rail mechanics.

The performance rules for the hero canvas are unchanged from the guide, and are the part
you must not let an AI "simplify" later.

---

> **MASTER PROMPT — PASTE INTO ANTIGRAVITY**

```text
Build index.html for ТАШМА, a natural organic honey brand from North Macedonia. All
visible copy on the page must be in Macedonian (Cyrillic). The site must feel dark,
cinematic, premium, and editorial -- a single continuous scroll story, not a template with
sections bolted together. Use vanilla HTML, CSS, and JavaScript, single-file structure
(index.html only, no build tools, no npm). Use GSAP + ScrollTrigger for scroll-linked
motion and Lenis for smooth scrolling.

CRITICAL PERFORMANCE RULE -- read this before writing the hero section:
Do NOT preload every hero frame before revealing the page -- that produces a long blank
loading screen and feels sluggish. Instead:
- Preload only the first 40 frames, then hide the loading screen and reveal the page.
- As the user scrolls, load frames just-in-time using a rolling cache: keep a window of
about 60 frames decoded on each side of the current scroll position, and prefetch about 15
frames ahead in the current scroll direction so scrubbing never looks frozen.
- Prune frames outside that window from the cache (let them be garbage collected) as the
user scrolls past them.
- Draw the current frame to a canvas sized to window.innerWidth/innerHeight *
devicePixelRatio, using a cover-fit (never stretch or letterbox).
- Frame index = 1 + Math.round(progress * (TOTAL_FRAMES - 1)), progress computed from
getBoundingClientRect() on the pinned hero track -- never window.scrollY alone.
- Count the actual number of files in public/frames/ and use that as TOTAL_FRAMES -- path
pattern frames/frame_0001.jpg through frames/frame_XXXX.jpg (4-digit padded).
- Do NOT use a <video> element or video.currentTime for the hero. Canvas + frame sequence
only -- this is the same technique Apple uses on its own product pages, chosen specifically
because video.currentTime seeking is unreliable across browsers and devices.
- The hero frames are 16:9 with the subject centred; cover-fit on every viewport. On phones
the crop keeps the jar fully in view. Reduce the pinned track length on narrow viewports.
- Name the frames array 'frames' and any other image arrays (e.g. product-panel images)
something distinct like 'panelImages' -- never reuse one generic variable name for both.

USE EVERY ASSET -- nothing should be left unused:

Hero frames: frames/frame_0001.jpg through the last extracted frame -- the hero canvas
sequence itself.

images/hero/ (image-1 through image-7) -- these are the storyboard the frame sequence was
built from. Do not place them directly as page images; image-1-honeycomb-hero.png may be
used as a static fallback/poster shown behind the canvas before the first frames load, and
image-7-hands-holding-jar.png may be used as the poster for the newsletter section.

Build the page in this order:

1. HERO -- canvas frame-sequence per the performance rules above.
Text overlays (opacity 0 default, fade transition 0.6s ease):
progress 0.15-0.25: ТАШМА -- 96px serif display font weight 300, off-white, centered
progress 0.35-0.45: Природен органски мед. -- 28px italic, off-white, centered
progress 0.55-0.67: ОД КОШНИЦА ДО ТЕГЛА -- 60px serif display, off-white, centered
progress 0.70-0.80: Една капка. Илјада цветови. -- 12px uppercase letter-spacing 4px,
off-white, top 10% left 8%
Nav: ТАШМА fixed top-left, КОНТАКТ fixed top-right, small uppercase tracked-out serif,
z-index 100.
Progress bar: fixed 2px right edge, dim gold background, bright gold fill, height grows 0
to 100vh with scroll.

2. STICKY EXPLAINER -- ONE PRODUCT, THREE CHAPTERS
Left 50%: sticky image, starts image-4-honey-into-jar.png, swaps via IntersectionObserver
as the right panels scroll (panel 2 -> image-5-honey-swirl.png, panel 3 ->
image-7-hands-holding-jar.png).
Right 50%: three 100vh panels, CSS sticky only (no GSAP pin here):
Panel 1 ПОТЕКЛО -- "Од ридовите, не од фабрика." Меѓу ливадите и шумите, таму каде што
пчелите сами го бираат цветот.
Panel 2 ПРОЦЕС -- "Полека, како што треба." Без загревање, без филтрирање под притисок --
медот се точи каков што е.
Panel 3 ЧИСТОТА -- "100% природно. Ништо повеќе." Само мед. Без додаден шеќер, без
конзерванси, без боја.

3. HORIZONTAL COLLECTION RAIL
Pinned GSAP horizontal scroll, no black gaps, 4 panels:
Panel 1: image-1-honeycomb-hero.png with "МЕДОТ ТАШМА" centered.
Panel 2: image-3-honey-dripping-down.png with "СУРОВ" and a one-line caption.
Panel 3: image-5-honey-swirl.png with "НЕФИЛТРИРАН".
Panel 4: image-7-hands-holding-jar.png with "НАШ".

4. STACKING RITUAL CARDS
3 sticky cards. Background is a slow CSS Ken Burns pan over
image-2-honey-begin-to-flow.png, image-6-honey-spoon-pour.png and
image-7-hands-holding-jar.png respectively -- no video files are used on this page.
Numbers 01/02/03 + words ТОЧИ / ЗЕМИ / ВКУСИ:
ТОЧИ -- "Лента злато, право од саќето."
ЗЕМИ -- "Полека, без брзање, точно како што треба."
ВКУСИ -- "Таму каде што ритуалот застанува во тишина."

5. PARALLAX STATEMENT
image-3-honey-dripping-down.png full-bleed with a dark overlay, slow parallax.
"Природна сладост, / недопрена." large italic serif.
Tagline: "ТАШМА -- од првата берба."

6. REVERSE COLUMNS
3-column grid using image-1-honeycomb-hero.png, alternating vertical parallax.
"Собран од дивото." italic overlay centered.

7. PRODUCT SECTION
One large product card, not a three-up grid: image-4-honey-into-jar.png, name ТАШМА,
subtitle "Природен Органски Мед", a short paragraph, and the registration line
"Р.Б.О 243103326" in small dim text. Hover: lift + glow border.

8. NEWSLETTER
image-7-hands-holding-jar.png background with dark overlay. "Придружи се на ритуалот."
centered. Email input with placeholder "твојата е-пошта" + button "ПРИЈАВИ СЕ".

9. FOOTER
Minimal, dark, brand name centered, copyright line "© ТАШМА".

Design rules -- do not deviate:
- Off-white for ALL text -- headings, nav, product names. Gold accent color is NEVER used
as text color, only for buttons, accent lines, card borders, and the progress bar.
- Warm serif display font for all headings, clean sans-serif for body/labels. The serif
MUST support Cyrillic -- verify the chosen font renders Ш, Ж, Ќ, Љ, Њ correctly and pick
a Cyrillic-capable family if it does not.
- Use overflow-x: clip on html and body -- NOT overflow-x: hidden, that breaks sticky
positioning.
- End the script with ScrollTrigger.refresh().

After building, verify in the browser: confirm the loading screen disappears quickly (well
under a second, since it only waits for 40 frames, not the full sequence), confirm
scrolling the hero feels smooth with no stutter, confirm all Cyrillic text renders without
missing glyphs or tofu boxes, and confirm every image listed above appears somewhere on
the page.
```

---

## What changed and why

| Guide original | ТАШМА version | Reason |
|---|---|---|
| Three varietal panels | Потекло / Процес / Чистота | One SKU — three chapters of one story, same mechanics |
| `images/product/` (3 jars) | Single product section | No varietal photography exists |
| `videos/card-*.mp4` ritual loops | CSS Ken Burns over stills | Loop clips not generated — see [assets-todo.md](assets-todo.md) |
| `images/backgrounds/` apiary + forest | Hero stills reused | No background plates generated yet |
| English editorial copy | Macedonian | Matches the label |
| Cover-fit at all sizes | Contain-fit under 900px | 16:9 source would crop the jar on phones |
