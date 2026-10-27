---
name: strykers-background-removal
description: Removes the background from photos of Empire Strykers players, the mascot, or logos to make transparent PNG cutouts, then verifies the transparency and that the subject is unchanged. Use when someone needs a cutout of a player, mascot, jersey, or logo for a graphic.
---

# Strykers Background Removal Studio

> New draft skill (October 2026), written from skill 06 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Make clean transparent cutouts without changing the person or object.

## When to use

- A graphic needs a player, mascot, jersey, or logo on a transparent background.

## Inputs

- The original photo (highest resolution available).
- Which subject(s) to keep.

## Steps

1. Remove the background with the best available tool (for example Canva's background remover, a photo editor, or an image library).
2. Refine edges around hair, fingers, clothing, and the ball.
3. Keep the subject exactly as photographed: no reshaping, smoothing of faces, recoloring of kits, or generated fill.
4. Save as PNG with transparency.
5. Verify (see below) and compare with the original.

## Verifying transparency

Don't trust a preview checkerboard alone. If you can run code, check the file:

```python
from PIL import Image
im = Image.open("cutout.png")
print(im.mode)                      # should be RGBA (or LA)
alpha = im.getchannel("A")
print(alpha.getextrema())           # should include 0 (transparent) and 255 (opaque)
w, h = im.size
print([alpha.getpixel(p) for p in [(0, 0), (w-1, 0), (0, h-1), (w-1, h-1)]])  # corners usually 0
```

Also view the cutout on both a dark and a light background to spot halos or leftover background.

## Output

- The transparent PNG.
- A short QC report:

| Check | Result |
| --- | --- |
| File has an alpha channel | |
| Background fully removed (corners and edges) | |
| Edges clean on dark and light backgrounds | |
| Face, kit, number, and logos unchanged from original | |

## If something goes wrong

- **Edges poor (hair, motion blur):** say so and suggest a cleaner source photo.
- **Can't run a file check:** say the transparency was checked visually only.
- **Tool changed the subject:** discard the result and report it.

## Before you finish

- Transparency was actually checked, not assumed.
- Any change to identity or uniform details is reported.
