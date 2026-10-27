# Empire Strykers Creative Studio — Canva and Higgsfield Skills

Knowledge file for the Strykers Creative Studio GPT. Generated from the `SKILL.md` files in the strykers-skills repository by `scripts/build-gpt-knowledge.py`; edit the skills there, not this file.

## Strykers Canva Export & Handoff (`strykers-canva-handoff`)

**Use when:** After an Empire Strykers graphic is made, offers three ways to continue in Canva (finished PNG, editable PPTX, or reusable team template), prepares the chosen file, and gives import steps. Use when a graphic is done and the user may want to edit or reuse it in Canva.

> New draft skill (October 2026), written from skill 09 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Get finished graphics into Canva in the form the user needs.

### When to use

- Right after generating or finishing a graphic.

### Steps

1. Run a brand check first (see the `strykers-brand-qa` skill). Don't hand off a BLOCKED asset.
2. Offer three options:
   1. **Finished PNG:** one flat image, ready to upload to Canva and post.
   2. **Editable PPTX:** text, shapes, and images as separate pieces where possible, for importing into Canva and editing.
   3. **Reusable team template:** a layout with placeholders the team can copy for future posts.
3. Prepare the chosen format.
4. Hand off:
   - **If a Canva connection is available**, use it and report only what the tool confirms (for example, a returned design link or ID).
   - **If not**, give manual steps:
     - PNG: in Canva, open **Uploads**, upload the file, and add it to a design.
     - PPTX: in Canva, upload or import the PowerPoint file; check fonts and layout after import.
     - Template: create the design in Canva, then share it with the team or save it as a template if the team's Canva plan supports that.

### Rules

- Don't promise that every layer will stay editable after a PPTX import; flattened images and unsupported fonts may not.
- Don't say a file is in Canva unless a connected tool confirmed it.
- Brand fonts may need to be uploaded to Canva by the team (license permitting).

### Output

- The file in the chosen format.
- Import instructions.
- Connection status: "Sent to Canva (link)" only with tool confirmation; otherwise "Not sent; manual upload steps above".

### Before you finish

- The brand check was done before handoff.
- No direct Canva transfer or full editability is claimed without evidence.

---

## Strykers Canva Brand Kit Setup (`strykers-canva-brand-kit`)

**Use when:** Guides the team through setting up the Empire Strykers Brand Kit in Canva (logos, colors, fonts, templates, sharing) and produces a setup checklist and asset inventory. Use when setting up or auditing the Strykers brand inside Canva.

> New draft skill (October 2026), written from skill 10 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Set up Canva so everyone on the team designs on brand by default.

### When to use

- First-time Canva brand setup, or checking that the existing setup is complete.

### Inputs

- Approved logo files in every Brand Kit colorway: primary crest, secondary jet mark, and wordmark (from the team's Drive brand folder).
- Official colors: White `#FFFFFF`, Silver Sand `#B8BABC`, Aluminium `#A3A5A9`, Mid Grey `#6E6E71`, Black `#000000`, Plum `#953493`, Rouge `#9F3E97`.
- Brand fonts (all from Adobe Fonts), with confirmation the license allows using them in Canva.
- Existing templates to include.
- Who should have edit vs view access.

### Steps

1. Confirm the team's Canva plan supports Brand Kits and brand templates; features vary by plan.
2. In Canva's brand area, create or open the Empire Strykers Brand Kit.
3. Add logos (original files only), the colors above, and fonts (Impact, Beachwood UltraBold, Dharma Gothic Exbold Italic, Futura Condensed Medium, Sketchnote Text Italic, Snell Roundhand) where licensed.
4. Add approved templates, ideally one per Brand Kit asset category (Office News, Official News, Team News Oct–Apr and May–Sep, Flyers, Published, MASL Home Game, MASL Away Game), and set them as brand templates if available.
5. Set team access and add a short guide on which templates to use when.
6. Spot-check a few existing designs against the kit.

### Output

| Item | Set up? | Evidence | Notes |
| --- | --- | --- | --- |
| Brand Kit created | | | |
| Logos added (list) | | | |
| Colors added | | | |
| Fonts added (list; license OK?) | | | |
| Templates added | | | |
| Team access set | | | |

Plus an inventory of assets loaded, and anything still missing.

### Before you finish

- Each "Set up" item is backed by evidence (a screenshot, a connected-tool result such as a listed brand kit, or the user's confirmation), not assumed.
- No fonts uploaded without license confirmation.

---

## Strykers Higgsfield Video Handoff (`strykers-higgsfield-handoff`)

**Use when:** Prepares an Empire Strykers image for Higgsfield video (animate it, add cinematic motion, or use it as a video concept reference), writes the motion brief, and reviews the returned video. Use when someone wants to turn a Strykers graphic or photo into motion in Higgsfield.

> New draft skill (October 2026), written from skill 11 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Take a still image into Higgsfield without losing the logo or the players' real look.

### When to use

- The user wants to animate or add motion to a Strykers image.

### Steps

1. Offer three options:
   1. **Animate the image** (bring the still to life).
   2. **Cinematic motion or effects** (camera moves, light, particles).
   3. **Concept reference** (use the image as a guide for a new video).
2. Prepare the source image: highest resolution, cropped to the target aspect ratio (for example 9:16 vertical), with the original logo intact.
3. Write a motion brief:

   ```text
   Goal:
   Option (1, 2, or 3):
   Aspect ratio and length:
   Motion (what moves, how, how fast):
   Keep unchanged: logo, player faces, jerseys, numbers, text
   Mood:
   ```

4. Ask before spending credits or submitting paid jobs.
5. **If Higgsfield tools are connected:** submit, keep the job ID, and report the job's real state (submitted, pending, failed, or completed). Report completion only when the finished video is returned.
6. **If not connected:** give the user the image, the brief, and steps to upload it on the Higgsfield site.
7. Review the returned video (see the `strykers-video-continuity-qa` skill).

### Rules

- AI motion can warp logos, faces, and numbers. Check every returned video.
- Don't claim an upload or generation happened without a tool result.

### Output

- Source image, motion brief, upload steps or job status, and a review checklist:

| Check | Result |
| --- | --- |
| Logo stays intact in every part of the video | |
| Player faces and numbers unchanged | |
| Text readable and correct | |
| Motion looks natural, no glitches | |

### Before you finish

- Job status matches what the tool reported.
- The returned video was reviewed before being called usable.

---

## Strykers Integration & Account Checker (`strykers-account-checker`)

**Use when:** Checks which creative tools (such as Canva and Higgsfield) are actually connected and authorized in the current AI workspace, and explains manual alternatives for those that aren't. Use before any step that depends on sending work to an outside tool, or when someone asks what's connected.

> New draft skill (October 2026), written from skill 12 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Know what's really connected before promising anything.

### When to use

- Before a handoff to Canva, Higgsfield, or another tool.
- When the user asks "is Canva connected?"

### Steps

1. Look at the tools actually available in this session.
2. For each tool the workflow needs, try a harmless read-only action (for example, list brand kits or search designs) to confirm access.
3. Sort each into:
   - **Connected:** a read-only action succeeded.
   - **Not connected:** the tool isn't available or returned an authorization error.
   - **Unverified:** the tool exists but you couldn't confirm access.
4. For anything not connected, give the manual alternative (download the file and upload it on the tool's website).

### Rules

- Never ask for, display, or store passwords, API keys, or tokens.
- A tool appearing in a list is not proof it works; only a successful action is.

### Output

| Tool | Status (Connected / Not connected / Unverified) | Evidence | What you can do / manual alternative |
| --- | --- | --- | --- |

### Before you finish

- Every "Connected" status has a successful tool result behind it.
