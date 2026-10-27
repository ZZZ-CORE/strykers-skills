---
name: strykers-motion-captions
description: Specifies on-brand motion graphics for Empire Strykers videos (titles, lower thirds, score and match graphics) and prepares English and Spanish caption files with checked timing and placement. Use when a Strykers video needs graphics or subtitles.
---

# Strykers Motion Graphics & Captions

> New draft skill (October 2026), written from skill 14 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Make video text look on brand and easy to read, in English and Spanish.

## When to use

- A Strykers video needs titles, name tags, score graphics, or subtitles.

## Inputs

- The video or storyboard.
- Approved copy, player names, and scores (with sources).
- Season (title font: Impact in season, Beachwood UltraBold off season).

## Steps

1. **Graphics spec.** For each graphic give: text, font, color (from White `#FFFFFF`, Silver Sand `#B8BABC`, Aluminium `#A3A5A9`, Mid Grey `#6E6E71`, Black `#000000`, Plum `#953493`, Rouge `#9F3E97`), position, in/out time, and animation.
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

## Output

- Graphics spec table.
- `captions-en.srt` and `captions-es.srt`.
- A note of which facts are VERIFIED and which still NEED APPROVAL.

## Rules

- Spanish copy should be reviewed by a fluent speaker on the team before publishing.
- Spell branded terms exactly as in the Brand Kit (Hattrick, Wallascora, Power Play, Power Kill, 6th Attacker, Golaso, Golazo, Blue Card).
- Don't translate player names or the slogan "Inspire The Empire" unless the team has an approved version.

## Before you finish

- Captions match the audio and the verified facts.
- Timing and placement were checked against the video.
