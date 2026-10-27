# Empire Strykers Creative Studio — Images and Graphics Skills

Knowledge file for the Strykers Creative Studio GPT. Generated from the `SKILL.md` files in the strykers-skills repository by `scripts/build-gpt-knowledge.py`; edit the skills there, not this file.

## Strykers Creative Brief Builder (`strykers-creative-brief-builder`)

**Use when:** Turns a short Empire Strykers creative request into a full production brief with goal, audience, platform size, copy, required assets, brand rules, and open questions. Use when someone asks for a Strykers graphic, video, or campaign piece with only a few words of direction.

> New draft skill (October 2026), written from skill 05 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Turn "make a game-day post" into a brief good enough to produce a first draft, without inventing facts.

### When to use

- A request arrives with little detail ("make a ticket promo", "player spotlight for Friday").

### Inputs

- The request.
- Any details the user has: event, date, venue, opponent, player, ticket link, platform, deadline.
- Approved assets available (logos, photos, footage).

### Steps

1. Work out the goal (sell tickets, announce, celebrate, inform) and the audience.
2. Pick the platform and size. Common starting points: 1080×1080 square, 1080×1350 portrait feed post, 1080×1920 vertical story/reel. Check current platform guidance if unsure.
3. Take game details (date, Pacific time, opponent, home/away, venue, promo code, ticket link, parking) from the team schedule (`SCHEDULE.md`), labeled USER-SUPPLIED (team schedule). Draft headline and supporting copy. Use placeholders like `[OPPONENT]` or `[DATE]` for any fact not supplied; never fill them in from guesswork.
4. List the assets needed and whether each one has been provided.
5. Add the brand rules: official colors, title font by season (Impact in season, Beachwood UltraBold off season), original logo files only.
6. List open questions.

### Output

```text
CREATIVE BRIEF
Goal:
Audience:
Platform and size:
Season (title font):
Brand Kit asset category (e.g. MASL Home Game, Flyers):
Headline:
Supporting copy:
Call to action:
Hashtags (from the Brand Kit lists):
Layout notes:
Required assets (provided? yes/no):
Facts (value | source | VERIFIED / USER-SUPPLIED / NEEDS APPROVAL):
Brand rules:
Open questions:
Deadline:
```

### If something is missing

- Missing facts stay as placeholders marked NEEDS APPROVAL.
- If the goal or platform is unclear and changes the design, ask before going further.

### Before you finish

- Every fact in the brief has a status.
- No date, venue, opponent, price, or player name was made up.

---

## Strykers Background Removal Studio (`strykers-background-removal`)

**Use when:** Removes the background from photos of Empire Strykers players, the mascot, or logos to make transparent PNG cutouts, then verifies the transparency and that the subject is unchanged. Use when someone needs a cutout of a player, mascot, jersey, or logo for a graphic.

> New draft skill (October 2026), written from skill 06 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Make clean transparent cutouts without changing the person or object.

### When to use

- A graphic needs a player, mascot, jersey, or logo on a transparent background.

### Inputs

- The original photo (highest resolution available).
- Which subject(s) to keep.

### Steps

1. Remove the background with the best available tool (for example Canva's background remover, a photo editor, or an image library).
2. Refine edges around hair, fingers, clothing, and the ball.
3. Keep the subject exactly as photographed: no reshaping, smoothing of faces, recoloring of kits, or generated fill.
4. Save as PNG with transparency.
5. Verify (see below) and compare with the original.

### Verifying transparency

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

### Output

- The transparent PNG.
- A short QC report:

| Check | Result |
| --- | --- |
| File has an alpha channel | |
| Background fully removed (corners and edges) | |
| Edges clean on dark and light backgrounds | |
| Face, kit, number, and logos unchanged from original | |

### If something goes wrong

- **Edges poor (hair, motion blur):** say so and suggest a cleaner source photo.
- **Can't run a file check:** say the transparency was checked visually only.
- **Tool changed the subject:** discard the result and report it.

### Before you finish

- Transparency was actually checked, not assumed.
- Any change to identity or uniform details is reported.

---

## Strykers Player Image Integrity (`strykers-player-image-integrity`)

**Use when:** Compares edited or AI-assisted images of Empire Strykers players against the originals to make sure faces, bodies, jerseys, numbers, badges, and sponsor marks were not changed or invented. Use whenever a player photo has been edited, retouched, cut out, extended, or run through an AI tool.

> New draft skill (October 2026), written from skill 07 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Real players must look like themselves, in their real kit.

### When to use

- After any edit or AI step on a photo of a player.

### Inputs

- The original photo.
- The edited image.
- The team roster (`ROSTER.md`) for the player's name and position. Jersey numbers there are TBD, so read numbers from the original photo, never from memory.

### Rules

- Allowed: cropping, resizing, background removal, color/contrast adjustments applied to the whole image, motion blur.
- Not allowed: changing faces, skin tone, hair, body shape, or expression; generating new body parts or players; changing jersey numbers, names, crests, or sponsor patches.

### Steps

1. Put the original and the edit side by side at the same size.
2. Check each item in the table.
3. Zoom in on faces, hands, numbers, and logos; AI errors often show up there.

### Output

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

### If something is missing

- **No original available:** say the integrity check couldn't be done; do not call it OK.

### Before you finish

- Every material change to identity or uniform is listed.

---

## Strykers Social Template Factory (`strykers-social-template-factory`)

**Use when:** Builds reusable, on-brand Empire Strykers social templates (game day, final score, player announcement, ticket promo, community event) with editable placeholders and usage notes. Use when the team wants a repeatable layout rather than a one-off graphic.

> New draft skill (October 2026), written from skill 08 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Make templates the team can fill in quickly and keep on brand.

### When to use

- The team needs a layout it will reuse every game or every week.

### Template types

- Game day (matchup, date, time, venue, ticket CTA)
- Final score
- Player announcement / spotlight
- Ticket promotion
- Community event

### Inputs

- Which template type(s) and platform(s).
- Season (title font: Impact in season, Beachwood UltraBold off season).
- Approved logo files and any photo slots needed.
- Where the template will be edited (Canva, PowerPoint, Photoshop, or other).

### Steps

1. Set the canvas size per platform. Common starting points: 1080×1080, 1080×1350, 1080×1920. Check current platform guidance.
2. Pick the Brand Kit asset category (Office News, Official News, Team News Oct–Apr, Team News May–Sep, Flyers, Published, MASL Home Game, MASL Away Game) and use its background, gradient, border, logo fill, and text fill.
3. Lay out with the official colors (White `#FFFFFF`, Silver Sand `#B8BABC`, Aluminium `#A3A5A9`, Mid Grey `#6E6E71`, Black `#000000`, Plum `#953493`, Rouge `#9F3E97`) and brand fonts.
4. Put every changing detail in a clearly named placeholder: `[OPPONENT]`, `[DATE]`, `[TIME]`, `[VENUE]`, `[SCORE]`, `[PLAYER NAME]`, `[PHOTO]`, `[TICKET LINK]`.
5. Leave a fixed spot for the original logo file; don't redraw it.
6. Keep text and logos out of areas covered by app buttons on vertical formats.
7. Keep elements editable (separate text boxes and image frames).

### Output

- Template file(s) or a build spec for the chosen tool.
- Usage notes: what each placeholder is for, which fonts to use, what must not be moved or changed, and a reminder to verify every fact before posting.

### Before you finish

- Template follows the brand colors and fonts.
- No sample facts in placeholders could be mistaken for real event details.
- Sizes match the target platform.
