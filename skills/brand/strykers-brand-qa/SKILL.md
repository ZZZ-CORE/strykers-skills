---
name: strykers-brand-qa
description: Final brand check of an Empire Strykers asset before approval or export, covering logos, colors, fonts, messaging, facts, and layout, ending in PASS, NEEDS REVIEW, or BLOCKED. Use as the last step before any Strykers asset is approved, exported, or published.
---

# Strykers Brand QA Inspector

> New draft skill (October 2026), written from skill 04 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Give a final, evidence-based brand verdict on a finished asset.

## When to use

- Right before an asset goes for approval, export, or publishing.

## Inputs

- The finished asset (image, video, PDF, or design link).
- The Brand Kit or brand basics (colors `#FFFFFF`, `#B8BABC`, `#A3A5A9`, `#6E6E71`, `#000000`, `#953493`, `#9F3E97`; fonts per season).
- The fact list for the asset (dates, venue, opponent, prices), with sources if available.

## Steps

Check each item and record what you actually looked at:

1. **Logos:** original approved artwork, unaltered, readable.
2. **Colors:** within the official palette (or a confirmed campaign exception).
3. **Fonts:** correct by season and role; substitutions named.
4. **Name and messaging:** "Empire Strykers" spelled exactly; tone is family-friendly and on brand.
5. **Facts:** every date, venue, opponent, price, and player name is verified or marked NEEDS APPROVAL.
6. **People:** players' faces, jerseys, and numbers are unaltered.
7. **Layout:** text readable on a phone; nothing important cut off or under platform buttons.
8. **Consistency:** matches other assets in the same campaign.

## Status

- **PASS:** every check was performed and passed.
- **NEEDS REVIEW:** a minor issue, or a check couldn't be performed (for example, no Brand Kit or source to compare).
- **BLOCKED:** a serious problem: altered or AI-made logo, changed player identity, wrong team name, invented or wrong facts, or a restricted asset. Must be fixed before release.

## Output

| Check | What was looked at | Result | Fix |
| --- | --- | --- | --- |

Then the overall status (PASS / NEEDS REVIEW / BLOCKED) and the list of fixes in priority order.

## Before you finish

- PASS is given only when every check was actually performed and passed.
- Any check you couldn't do is listed as such, which makes the result NEEDS REVIEW at best.
