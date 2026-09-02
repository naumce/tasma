# ТАШМА — hero clip prompts

Six start→end clips, adapted from the Assam Honey guide to match the images that actually
exist. All frames are conformed to **1920×1080 (16:9)**, subject centred on black.

| Clip | Start | End | Save as |
|------|-------|-----|---------|
| 1 | image-1 honeycomb hero | image-2 begins to flow | `v1-honeycomb-to-flow.mp4` |
| 2 | image-2 begins to flow | image-3 dripping down | `v2-flow-to-dripping.mp4` |
| 3 | image-3 dripping down | image-4 honey into jar | `v3-dripping-to-jar.mp4` |
| 4 | image-4 honey into jar | image-5 honey swirl | `v4-jar-to-swirl.mp4` |
| 5 | image-5 honey swirl | image-6 spoon pour | `v5-swirl-to-spoon.mp4` |
| 6 | image-6 spoon pour | image-7 hands holding jar | `v6-spoon-to-hands.mp4` |

## Deviations from the printed guide

- **Clip 5 is reversed.** The guide's image-6 was a spoon *lifting* honey out of the jar.
  The actual image-6 shows a spoon *pouring* honey down into the jar, so the prompt
  describes a spoon descending and pouring, not a lift. Fighting the still would produce a
  morph the model can't resolve cleanly.
- **Clip 6 drops the spoon before the hands arrive.** The end frame has no spoon in it, so
  the clip has to move it out of frame before the hands enter.
- **The jar is branded.** Every jar-side prompt states the ТАШМА label must stay legible and
  unchanged — video models drift on small text, and the label is the product.

---

## Clip 1 — Honeycomb → First Flow

```text
Ultra slow motion seamless transformation. A single premium honeycomb floats in darkness
under a warm amber spotlight against a pure black background. After a moment of complete
stillness, the honeycomb begins to soften and release thick golden honey, and one small
honeybee gently drifts away from the upper left edge toward the right. The honey strands
start forming naturally along the lower edge and the image smoothly evolves toward the
second frame. Camera completely locked, zero movement, no shake, no cuts, no text, no
watermarks.
```

## Clip 2 — First Flow → Full Dripping

```text
Ultra slow motion seamless transformation. Thick golden honey is beginning to flow from the
honeycomb under a warm amber spotlight on a pure black background. The honey stretches
downward in elegant glossy strands, becoming longer and heavier with realistic viscosity
until it becomes a full dripping cascade reaching toward the bottom of the frame. The bee
leaves the frame early and does not return. Camera completely locked, zero movement, no
shake, no cuts, no text, no watermarks.
```

## Clip 3 — Dripping → Pour into Jar

```text
Ultra slow motion seamless transformation. Thick liquid honey drips downward in long
molten-gold strands on a pure black background under warm amber light. A clear glass honey
jar with a dark amber label rises smoothly into position beneath the dripping strands and
the honey begins pouring into it in a single continuous stream, creating soft glowing
ripples and subtle splashes as the jar starts filling. The honeycomb rises out of frame as
the jar settles into the centre. The jar label stays sharp, legible and unchanged. Camera
completely locked, zero movement, no shake, no cuts, no text, no watermarks.
```

## Clip 4 — Jar Pour → Swirl

```text
Ultra slow motion seamless transformation. A clear glass jar with a dark amber ТАШМА label
is being filled with glowing golden honey under a dramatic amber spotlight on a pure black
background. The pouring stream folds into the honey already in the jar, forming an elegant
spiralling swirl and concentric ripples across the surface, tiny bubbles rising gently
through the amber liquid as the level rises. The label text remains sharp, legible and
completely unchanged throughout. Camera completely locked, zero movement, no shake, no
cuts, no text, no watermarks.
```

## Clip 5 — Swirl → Spoon Pour

```text
Ultra slow motion seamless transformation. Golden honey ripples and settles inside a glass
jar with a dark amber ТАШМА label under warm amber light on a pure black background. The
pouring stream from above thins and breaks, and a golden spoon descends smoothly into the
upper frame, tilting so that a thick ribbon of honey runs off its edge and falls in one
continuous glossy strand down into the jar, raising slow concentric rings on the surface.
The label text remains sharp, legible and completely unchanged. Camera completely locked,
zero movement, no shake, no cuts, no text, no watermarks.
```

## Clip 6 — Spoon Pour → Hands Holding Jar

```text
Ultra slow motion seamless transformation. A golden spoon pours a thick ribbon of honey
into a glass jar with a dark amber ТАШМА label on a pure black background under warm amber
light. The ribbon thins, the last strand settles into the surface, and the spoon glides
gently up and out of frame, leaving the filled jar alone in the exact centre. After a
moment of stillness, two realistic human hands begin entering the frame very slowly from
behind the jar -- fingers first, then palms -- moving forward with calm intention to
support the jar from the back and sides. Only the hands are visible, no face and no body.
As the hands make contact with the glass, the amber glow from the honey begins illuminating
the skin with warm golden light, softly tinting the fingers where they touch the jar. The
jar remains perfectly centred and still and its label stays sharp and unchanged, the warmth
shared through the glass, the ritual complete. Camera completely locked, zero movement.
Ultra slow motion, cinematic, photorealistic, no text, no watermarks.
```
