# Empire Strykers Creative Studio — Video Skills

Knowledge file for the Strykers Creative Studio GPT. Generated from the `SKILL.md` files in the strykers-skills repository by `scripts/build-gpt-knowledge.py`; edit the skills there, not this file.

## Strykers Video Promo (`strykers-video-promo`)

**Use when:** Create premium vertical Empire Strykers promotional videos from supplied source footage, preserving recognizable real frames and producing a verified 1080x1920 MP4.

> Original skill from the Strykers Creative Studio GPT. Its example on-screen lines ("TWO NATIONS. / ONE RIVALRY.", "USA VS MÉXICO.", "THE RIVALRY RETURNS.", "PICK A SIDE. / GET YOUR TICKETS.") came from one rivalry campaign: treat them as examples and replace them with approved copy for the current event. Use only the official brand colors unless the user confirms a campaign calls for red or green.

Create a 20–25 second, 1080×1920 vertical sports promo from the user’s supplied video. The supplied footage is the creative centerpiece: never invent players, stadium action, logos, or replacement soccer footage.

### Source-first rules

- Import the exact user-provided MP4 and use recognizable, unaltered frames throughout.
- Use multiple physically extracted time ranges from the source; do not rely on a still image or AI recreation.
- Preserve people’s identity. Cropping, speed changes, color treatment, and motion blur are allowed; generative alteration is not.
- Aim for at least 80% actual source-footage screen time.

### Default trailer structure

1. 0:00–0:03: strongest source moment; “TWO NATIONS. / ONE RIVALRY.”
2. 0:03–0:08: 2–3 distinct source clips; “USA VS MÉXICO.”
3. 0:08–0:15: energetic montage; “THE RIVALRY RETURNS.”
4. 0:15–0:20: source footage with verified event details.
5. 0:20–0:25: powerful source moment; “PICK A SIDE. / GET YOUR TICKETS.” Reserve a clean logo-safe area.

### Visual system

- Vertical 9:16, 1080×1920; bold condensed/Impact-like typography.
- Empire accents: #953493 and #9F3E97; use restrained red, green, and purple treatments.
- Prefer match cuts, speed ramps, subtle zooms, controlled flashes, and cinematic contrast.
- Use licensed audio when available; disclose any temporary/generated impact bed.

### Event copy and verification

Confirm date, venue, location, and ticket language against an official Empire Strykers or venue listing when possible. Otherwise use only user-supplied copy and flag it for approval.

### Required quality check

Verify the export exists and inspect metadata for 1080×1920, 20–25 seconds, and a playable H.264 stream. Review representative frames for multiple distinct source moments, visible typography, identity preservation, and a clean logo-safe area. Report the final absolute file path and unverified event claims.

---

## Strykers Video Storyboard Director (`strykers-storyboard-director`)

**Use when:** Plans Empire Strykers promo videos as a scene-by-scene storyboard and shot list (timing, framing, footage source, on-screen text, transitions, audio). Use before editing any game promo, player feature, ticket campaign, or social video.

> New draft skill (October 2026), written from skill 13 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Plan the video before cutting it, using footage the team actually has.

### When to use

- Before editing a game promo, player feature, ticket campaign, or social video.

### Inputs

- Goal, platform, and length (default for social promos: 20–25 seconds, vertical 1080×1920).
- Available footage and photos (list what's in them if possible).
- Approved copy and event facts, with their status.
- Music, if licensed or supplied.

### Steps

1. Review the available footage and pick the strongest real moments.
2. Build the sequence. A starting structure for a 25-second promo:

   | Time | Purpose |
   | --- | --- |
   | 0:00–0:03 | Hook: strongest moment + `[HOOK LINE]` |
   | 0:03–0:08 | 2–3 quick clips + `[MATCHUP OR THEME]` |
   | 0:08–0:15 | Energy montage + `[SUPPORTING LINE]` |
   | 0:15–0:20 | Event details (verified only): `[DATE] [VENUE]` |
   | 0:20–0:25 | Big moment + `[CALL TO ACTION]` + logo space |

3. For each scene, set framing, motion, and transition (match cuts, speed ramps, subtle zooms, controlled flashes).
4. Mark which footage covers each scene, and list anything missing.

### Output

| # | Time | Footage (file + timecode) | Framing | On-screen text | Motion / transition | Audio |
| --- | --- | --- | --- | --- | --- | --- |

Plus: a list of missing assets, and the status of every fact used (VERIFIED / USER-SUPPLIED / NEEDS APPROVAL).

### Rules

- Use real footage; don't plan scenes that require inventing players or game action.
- Placeholder copy stays in brackets until the team approves it.

### Before you finish

- Every scene has footage that exists, or is listed as a missing asset.

---

## Strykers Motion Graphics & Captions (`strykers-motion-captions`)

**Use when:** Specifies on-brand motion graphics for Empire Strykers videos (titles, lower thirds, score and match graphics) and prepares English and Spanish caption files with checked timing and placement. Use when a Strykers video needs graphics or subtitles.

> New draft skill (October 2026), written from skill 14 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Make video text look on brand and easy to read, in English and Spanish.

### When to use

- A Strykers video needs titles, name tags, score graphics, or subtitles.

### Inputs

- The video or storyboard.
- Approved copy, player names, and scores (with sources).
- Season (title font: Impact in season, Beachwood UltraBold off season).

### Steps

1. **Graphics spec.** For each graphic give: text, font, color (from `#FFFFFF`, `#B8BABC`, `#A3A5A9`, `#6E6E71`, `#000000`, `#953493`, `#9F3E97`), position, in/out time, and animation.
   - Title cards, lower thirds (player name and number), score / match-info bars.
2. **Captions.** Write English captions, then Spanish captions that carry the same meaning (not word-for-word).
   - 1–2 short lines per caption; on screen long enough to read (about 1 second minimum).
   - Keep text out of areas covered by app buttons on vertical video (roughly the bottom and right edges); check current platform guidance.
3. Deliver captions as `.srt` files (one per language), for example:

   ```text
   1
   00:00:00,000 --> 00:00:02,500
   [CAPTION TEXT]
   ```

4. Check every name, number, score, and date against the approved fact list.

### Output

- Graphics spec table.
- `captions-en.srt` and `captions-es.srt`.
- A note of which facts are VERIFIED and which still NEED APPROVAL.

### Rules

- Spanish copy should be reviewed by a fluent speaker on the team before publishing.
- Don't translate player names or the slogan "Inspire The Empire" unless the team has an approved version.

### Before you finish

- Captions match the audio and the verified facts.
- Timing and placement were checked against the video.

---

## Strykers Video Brand & Continuity Inspector (`strykers-video-continuity-qa`)

**Use when:** Reviews an Empire Strykers video for brand consistency, player fidelity, caption and sponsor accuracy, and AI glitches between frames, and reports exactly what was checked. Use on any edited or AI-generated Strykers video before approval.

> New draft skill (October 2026), written from skill 15 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Catch logo warping, face changes, wrong captions, and glitches before the video goes out.

### When to use

- Any edited or AI-generated video (for example, from Higgsfield) before approval.

### Inputs

- The video file.
- The original source footage and logo files, if available.
- The approved caption text and sponsor list.

### Steps

1. **Pull frames to review.** If you can run code, extract one frame per second plus frames at each cut:

   ```bash
   ffmpeg -i video.mp4 -vf fps=1 frames/frame_%03d.png
   ```

   If you can't, watch the video and note timestamps.
2. Check across frames:
   - **Logo:** same shape, color, and spelling every time it appears.
   - **Players:** faces, jerseys, and numbers stay the same and match the source.
   - **Glitches:** warping, flicker, melting edges, extra limbs, text that changes.
   - **Captions:** correct text, timing, and spelling.
   - **Sponsors:** correct names and logos.
3. Record the timestamp of every problem.

### Output

| Time | Issue | Severity (must fix / should fix) | Fix |
| --- | --- | --- | --- |

Plus a line saying how the review was done (for example, "frames every 1 s, 25 frames checked" or "watched once in full; no frame extraction").

### Before you finish

- Don't claim a frame-by-frame check unless frames were actually extracted and reviewed.

---

## Strykers Video Export Validator (`strykers-export-validator`)

**Use when:** Checks a finished Empire Strykers video file before release (format, codec, size, duration, frame rate, audio, captions, playback, approval status) and marks it READY or NOT READY. Use on every final MP4 before it is published or delivered.

> New draft skill (October 2026), written from skill 16 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Confirm the file really exists and meets the brief before anyone posts it.

### When to use

- On every final video before release.

### Default targets (unless the brief says otherwise)

- MP4 container, H.264 video
- 1080×1920 (9:16 vertical)
- 20–25 seconds
- Audio present (if the brief calls for it) and licensed or supplied by the team

### Steps

1. Confirm the file exists and note its name and size.
2. If you can run code, read the file's details:

   ```bash
   ffprobe -v error -show_entries format=duration:stream=codec_type,codec_name,width,height,r_frame_rate -of default=nw=1 video.mp4
   ```

3. Check that it plays all the way through without errors:

   ```bash
   ffmpeg -v error -i video.mp4 -f null -
   ```

   (No output means no decoding errors.)
4. Check captions are burned in or provided as files, as the brief requires.
5. Confirm the approval status (see the `strykers-approval-manager` skill).

### Output

| Check | Target | Actual | Pass? |
| --- | --- | --- | --- |
| File exists | yes | | |
| Container / codec | MP4 / H.264 | | |
| Size | 1080×1920 | | |
| Duration | 20–25 s | | |
| Frame rate | per brief | | |
| Audio | per brief | | |
| Captions | per brief | | |
| Plays without errors | yes | | |
| Approved | yes | | |

Status: **READY** only if every check passes; otherwise **NOT READY**, with what to fix.

### If something can't be checked

- **No way to run ffprobe/ffmpeg:** say which checks couldn't be done; the status can't be READY.

### Before you finish

- Never call a video complete without an actual file and successful checks.
