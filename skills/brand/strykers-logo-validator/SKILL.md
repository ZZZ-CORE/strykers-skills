---
name: strykers-logo-validator
description: Checks that Empire Strykers logos, wordmarks, and sponsor co-branding are the original approved artwork, used at correct proportions, placement, contrast, and colorway. Use when a design includes any Strykers or partner logo, or before exporting branded work.
---

# Strykers Logo & Lockup Validator

> New draft skill (October 2026), written from skill 02 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Make sure every logo in a design is the real, approved artwork used correctly.

## When to use

- A design contains the Empire Strykers logo, wordmark, or a partner/sponsor logo.
- Before a branded asset is exported or published.

## Inputs

- The design to check (image, PDF, video frame, or Canva design).
- The original approved logo files and any logo usage rules from the Brand Kit.
- Partner/sponsor logo files and placement requirements, if co-branded.

## Steps

1. Compare each logo in the design with the original approved file, side by side.
2. Check:
   - **Artwork:** same shapes, lettering, and details; nothing redrawn, retyped, or AI-generated.
   - **Proportions:** not stretched, squashed, skewed, or cropped.
   - **Colorway:** an approved version (for example full color, all white, all black) per the Brand Kit.
   - **Contrast:** clearly readable against the background.
   - **Clear space and placement:** not crowded by text or other graphics; not covered by platform buttons or captions.
   - **Co-branding:** partner logos placed and sized as approved; neither logo altered to fit.
3. Treat any AI-generated or reconstructed logo as a failure, even if it looks close.

## Output

| Logo | Location in design | Check | Result (Pass / Fail / Not checked) | Fix |
| --- | --- | --- | --- | --- |

Finish with an overall result: **Pass** only if every logo passes every check.

## If something is missing

- **No original file to compare against:** mark the logo "Not checked" and ask for the approved file.
- **Low-resolution logo:** flag it and ask for a vector or high-resolution version.

## Before you finish

- No altered or AI-made logo is marked Pass.
- Every logo in the design is listed.
