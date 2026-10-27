---
name: strykers-brand-guardian
description: Applies the official Empire Strykers brand (colors, fonts, logos, messaging) to any creative request and reviews work for brand compliance. Use when creating or reviewing any Empire Strykers graphic, video, caption, or campaign.
---

# Strykers Brand Guardian

> New draft skill (October 2026), written from skill 01 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Keep every Empire Strykers deliverable on brand. The official Empire Strykers Brand Kit is the authority; the basics below are a summary and lose to the Brand Kit wherever they differ.

## Brand basics

- **Name:** always "Empire Strykers" (with a "y").
- **Colors:** `#FFFFFF`, `#B8BABC`, `#A3A5A9`, `#6E6E71`, `#000000`, `#953493`, `#9F3E97`.
- **Titles:** Impact in season; Beachwood UltraBold off season.
- **Subtitles:** Dharma Gothic Exbold Italic.
- **Body text:** Futura Condensed Medium (professional) or Sketchnote Text Italic (artsy).
- **Accent text:** Snell Roundhand.
- **Messaging:** "Inspire The Empire"; Inland Empire community; family-friendly professional arena soccer; team pride, energy, and inclusivity.

## When to use

- At the start of any Empire Strykers creative request, to set the brand rules for it.
- When reviewing a draft for brand problems.

## Inputs

- The creative request and target platform.
- The official Brand Kit and approved asset files (logos, photos), if available.
- Whether the campaign is in season or off season.

## Steps

1. Ask for the Brand Kit and approved assets. If they aren't available, use the brand basics above and say the Brand Kit wasn't checked.
2. Confirm in season or off season (ask if unclear) to choose the title font.
3. Write a brand-locked brief: colors, fonts, logo file to use, tone of messaging, and platform size.
4. Use only original logo files supplied by the team. Never redraw, recolor, retype, or AI-generate a logo. If no logo file is available, leave a clearly marked logo space.
5. For a review, check every item in the compliance table below and give a specific fix for each problem.

## Output

A brand brief (for new work) or a compliance summary (for reviews):

| Item | Rule | Status (OK / Fix / Not checked) | Fix |
| --- | --- | --- | --- |
| Colors | Official palette only | | |
| Title font | Impact / Beachwood UltraBold by season | | |
| Other fonts | Subtitle, body, accent per brand basics | | |
| Logo | Original approved file, unaltered | | |
| Team name | "Empire Strykers" spelled exactly | | |
| Messaging | On-brand tone; no invented claims | | |
| Player and sponsor images | Approved, unaltered | | |

## If something is missing

- **Font not available:** name the closest available substitute and mark it NEEDS REVIEW.
- **Color outside the palette:** flag it; allow it only if the user confirms the campaign calls for it.
- **Brand Kit not provided:** say so in the summary.

## Before you finish

- Every row in the table has a status; anything not actually checked says "Not checked".
- Nothing is called compliant without being looked at.
