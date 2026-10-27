---
name: strykers-typography-manager
description: Chooses and checks Empire Strykers fonts and text hierarchy (in-season vs off-season titles, subtitles, body, accent) for graphics, video, and documents. Use when setting type for any Strykers design or checking fonts in a draft.
---

# Strykers Brand Typography Manager

> New draft skill (October 2026), written from skill 03 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Pick the right fonts and make text easy to read. The official Brand Kit wins if it differs from the list below.

## Brand fonts

| Role | Font |
| --- | --- |
| Title, in season | Impact |
| Title, off season | Beachwood UltraBold |
| Subtitle | Dharma Gothic Exbold Italic |
| Body, professional | Futura Condensed Medium |
| Body, artsy | Sketchnote Text Italic |
| Accent | Snell Roundhand |

## When to use

- Setting type for a new design, video, or document.
- Checking a draft's fonts and readability.

## Inputs

- The design or brief, and the target platform.
- Season: in season or off season (ask if unclear).
- Tone: professional or artsy (ask if unclear).

## Steps

1. Choose the title font by season.
2. Choose body text by tone; use the accent font sparingly (a word or short phrase).
3. Set a clear hierarchy: one title, then subtitle, then body.
4. Check readability:
   - Text is big enough to read on a phone screen.
   - Strong contrast against the background.
   - Comfortable spacing; no text touching edges or other elements.
   - On video, text stays on screen long enough to read.
5. Confirm the actual font used matches the plan. If a font was substituted, name it.

## Output

A typography spec (role, font, size, color, where it appears) or a font check:

| Text element | Planned font | Font actually used | Readable? | Issue / fix |
| --- | --- | --- | --- | --- |

## If something is missing

- **Brand font not installed or not licensed in the tool:** use the closest available font, name it, and mark it NEEDS REVIEW.

## Before you finish

- Every substitution is named, never hidden.
- Font choices match the brand list or are marked NEEDS REVIEW.
