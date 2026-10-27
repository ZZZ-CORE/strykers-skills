---
name: strykers-player-image-integrity
description: Compares edited or AI-assisted images of Empire Strykers players against the originals to make sure faces, bodies, jerseys, numbers, badges, and sponsor marks were not changed or invented. Use whenever a player photo has been edited, retouched, cut out, extended, or run through an AI tool.
---

# Strykers Player Image Integrity

> New draft skill (October 2026), written from skill 07 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Real players must look like themselves, in their real kit.

## When to use

- After any edit or AI step on a photo of a player.

## Inputs

- The original photo.
- The edited image.
- The team roster (`ROSTER.md`) for the player's name and position. Jersey numbers there are TBD, so read numbers from the original photo, never from memory.

## Rules

- Allowed: cropping, resizing, background removal, color/contrast adjustments applied to the whole image, motion blur.
- Not allowed: changing faces, skin tone, hair, body shape, or expression; generating new body parts or players; changing jersey numbers, names, crests, or sponsor patches.

## Steps

1. Put the original and the edit side by side at the same size.
2. Check each item in the table.
3. Zoom in on faces, hands, numbers, and logos; AI errors often show up there.

## Output

| Check | Same as original? | Notes |
| --- | --- | --- |
| Face and expression | | |
| Skin tone and hair | | |
| Body shape and pose | | |
| Jersey number and name | | |
| Team crest and badges | | |
| Sponsor marks | | |
| Kit colors | | |
| Nothing added (extra people, limbs, objects) | | |

Overall: **OK** or **Needs correction**, with what to fix or a recommendation to go back to the original.

## If something is missing

- **No original available:** say the integrity check couldn't be done; do not call it OK.

## Before you finish

- Every material change to identity or uniform is listed.
