# Empire Strykers Creative Studio — Brand Skills

Knowledge file for the Strykers Creative Studio GPT. Generated from the `SKILL.md` files in the strykers-skills repository by `scripts/build-gpt-knowledge.py`; edit the skills there, not this file.

## Strykers Brand Guardian (`strykers-brand-guardian`)

**Use when:** Applies the official Empire Strykers brand (colors, fonts, logos, messaging) to any creative request and reviews work for brand compliance. Use when creating or reviewing any Empire Strykers graphic, video, caption, or campaign.

> New draft skill (October 2026), written from skill 01 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Keep every Empire Strykers deliverable on brand. The official Empire Strykers Brand Kit is the authority; the basics below are a summary and lose to the Brand Kit wherever they differ.

### Brand basics

- **Name:** always "Empire Strykers" (with a "y").
- **Colors:** `#FFFFFF`, `#B8BABC`, `#A3A5A9`, `#6E6E71`, `#000000`, `#953493`, `#9F3E97`.
- **Titles:** Impact in season; Beachwood UltraBold off season.
- **Subtitles:** Dharma Gothic Exbold Italic.
- **Body text:** Futura Condensed Medium (professional) or Sketchnote Text Italic (artsy).
- **Accent text:** Snell Roundhand.
- **Messaging:** "Inspire The Empire"; Inland Empire community; family-friendly professional arena soccer; team pride, energy, and inclusivity.

### When to use

- At the start of any Empire Strykers creative request, to set the brand rules for it.
- When reviewing a draft for brand problems.

### Inputs

- The creative request and target platform.
- The official Brand Kit and approved asset files (logos, photos), if available.
- Whether the campaign is in season or off season.

### Steps

1. Ask for the Brand Kit and approved assets. If they aren't available, use the brand basics above and say the Brand Kit wasn't checked.
2. Confirm in season or off season (ask if unclear) to choose the title font.
3. Write a brand-locked brief: colors, fonts, logo file to use, tone of messaging, and platform size.
4. Use only original logo files supplied by the team. Never redraw, recolor, retype, or AI-generate a logo. If no logo file is available, leave a clearly marked logo space.
5. For a review, check every item in the compliance table below and give a specific fix for each problem.

### Output

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

### If something is missing

- **Font not available:** name the closest available substitute and mark it NEEDS REVIEW.
- **Color outside the palette:** flag it; allow it only if the user confirms the campaign calls for it.
- **Brand Kit not provided:** say so in the summary.

### Before you finish

- Every row in the table has a status; anything not actually checked says "Not checked".
- Nothing is called compliant without being looked at.

---

## Strykers Logo & Lockup Validator (`strykers-logo-validator`)

**Use when:** Checks that Empire Strykers logos, wordmarks, and sponsor co-branding are the original approved artwork, used at correct proportions, placement, contrast, and colorway. Use when a design includes any Strykers or partner logo, or before exporting branded work.

> New draft skill (October 2026), written from skill 02 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Make sure every logo in a design is the real, approved artwork used correctly.

### When to use

- A design contains the Empire Strykers logo, wordmark, or a partner/sponsor logo.
- Before a branded asset is exported or published.

### Inputs

- The design to check (image, PDF, video frame, or Canva design).
- The original approved logo files and any logo usage rules from the Brand Kit.
- Partner/sponsor logo files and placement requirements, if co-branded.

### Steps

1. Compare each logo in the design with the original approved file, side by side.
2. Check:
   - **Artwork:** same shapes, lettering, and details; nothing redrawn, retyped, or AI-generated.
   - **Proportions:** not stretched, squashed, skewed, or cropped.
   - **Colorway:** an approved version (for example full color, all white, all black) per the Brand Kit.
   - **Contrast:** clearly readable against the background.
   - **Clear space and placement:** not crowded by text or other graphics; not covered by platform buttons or captions.
   - **Co-branding:** partner logos placed and sized as approved; neither logo altered to fit.
3. Treat any AI-generated or reconstructed logo as a failure, even if it looks close.

### Output

| Logo | Location in design | Check | Result (Pass / Fail / Not checked) | Fix |
| --- | --- | --- | --- | --- |

Finish with an overall result: **Pass** only if every logo passes every check.

### If something is missing

- **No original file to compare against:** mark the logo "Not checked" and ask for the approved file.
- **Low-resolution logo:** flag it and ask for a vector or high-resolution version.

### Before you finish

- No altered or AI-made logo is marked Pass.
- Every logo in the design is listed.

---

## Strykers Brand Typography Manager (`strykers-typography-manager`)

**Use when:** Chooses and checks Empire Strykers fonts and text hierarchy (in-season vs off-season titles, subtitles, body, accent) for graphics, video, and documents. Use when setting type for any Strykers design or checking fonts in a draft.

> New draft skill (October 2026), written from skill 03 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Pick the right fonts and make text easy to read. The official Brand Kit wins if it differs from the list below.

### Brand fonts

| Role | Font |
| --- | --- |
| Title, in season | Impact |
| Title, off season | Beachwood UltraBold |
| Subtitle | Dharma Gothic Exbold Italic |
| Body, professional | Futura Condensed Medium |
| Body, artsy | Sketchnote Text Italic |
| Accent | Snell Roundhand |

### When to use

- Setting type for a new design, video, or document.
- Checking a draft's fonts and readability.

### Inputs

- The design or brief, and the target platform.
- Season: in season or off season (ask if unclear).
- Tone: professional or artsy (ask if unclear).

### Steps

1. Choose the title font by season.
2. Choose body text by tone; use the accent font sparingly (a word or short phrase).
3. Set a clear hierarchy: one title, then subtitle, then body.
4. Check readability:
   - Text is big enough to read on a phone screen.
   - Strong contrast against the background.
   - Comfortable spacing; no text touching edges or other elements.
   - On video, text stays on screen long enough to read.
5. Confirm the actual font used matches the plan. If a font was substituted, name it.

### Output

A typography spec (role, font, size, color, where it appears) or a font check:

| Text element | Planned font | Font actually used | Readable? | Issue / fix |
| --- | --- | --- | --- | --- |

### If something is missing

- **Brand font not installed or not licensed in the tool:** use the closest available font, name it, and mark it NEEDS REVIEW.

### Before you finish

- Every substitution is named, never hidden.
- Font choices match the brand list or are marked NEEDS REVIEW.

---

## Strykers Brand QA Inspector (`strykers-brand-qa`)

**Use when:** Final brand check of an Empire Strykers asset before approval or export, covering logos, colors, fonts, messaging, facts, and layout, ending in PASS, NEEDS REVIEW, or BLOCKED. Use as the last step before any Strykers asset is approved, exported, or published.

> New draft skill (October 2026), written from skill 04 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Give a final, evidence-based brand verdict on a finished asset.

### When to use

- Right before an asset goes for approval, export, or publishing.

### Inputs

- The finished asset (image, video, PDF, or design link).
- The Brand Kit or brand basics (colors `#FFFFFF`, `#B8BABC`, `#A3A5A9`, `#6E6E71`, `#000000`, `#953493`, `#9F3E97`; fonts per season).
- The fact list for the asset (dates, venue, opponent, prices), with sources if available.

### Steps

Check each item and record what you actually looked at:

1. **Logos:** original approved artwork, unaltered, readable.
2. **Colors:** within the official palette (or a confirmed campaign exception).
3. **Fonts:** correct by season and role; substitutions named.
4. **Name and messaging:** "Empire Strykers" spelled exactly; tone is family-friendly and on brand.
5. **Facts:** every date, venue, opponent, price, and player name is verified or marked NEEDS APPROVAL.
6. **People:** players' faces, jerseys, and numbers are unaltered.
7. **Layout:** text readable on a phone; nothing important cut off or under platform buttons.
8. **Consistency:** matches other assets in the same campaign.

### Status

- **PASS:** every check was performed and passed.
- **NEEDS REVIEW:** a minor issue, or a check couldn't be performed (for example, no Brand Kit or source to compare).
- **BLOCKED:** a serious problem: altered or AI-made logo, changed player identity, wrong team name, invented or wrong facts, or a restricted asset. Must be fixed before release.

### Output

| Check | What was looked at | Result | Fix |
| --- | --- | --- | --- |

Then the overall status (PASS / NEEDS REVIEW / BLOCKED) and the list of fixes in priority order.

### Before you finish

- PASS is given only when every check was actually performed and passed.
- Any check you couldn't do is listed as such, which makes the result NEEDS REVIEW at best.
