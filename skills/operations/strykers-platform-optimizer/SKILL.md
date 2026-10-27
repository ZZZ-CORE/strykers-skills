---
name: strykers-platform-optimizer
description: Prepares Empire Strykers graphics and videos for each publishing platform (sizes, aspect ratios, safe zones, text readability, export quality) and makes platform-specific versions. Use when one piece of content needs to go out on several platforms, or before export.
---

# Strykers Platform Format Optimizer

> New draft skill (October 2026), written from skill 23 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Make each version look right on the platform it's posted to.

## When to use

- Before exporting, or when adapting one piece for several platforms.

## Common starting sizes

Platform rules change, so confirm against each platform's current guidance before relying on these.

| Use | Size | Ratio |
| --- | --- | --- |
| Stories, Reels, TikTok, Shorts | 1080×1920 | 9:16 |
| Feed post, portrait | 1080×1350 | 4:5 |
| Feed post, square | 1080×1080 | 1:1 |
| Landscape video / web | 1920×1080 | 16:9 |

## Steps

1. List the target platforms.
2. For each, set the size and reframe; don't stretch or squash.
3. Keep text and logos inside the safe zone. On vertical video, the top, bottom, and right edges are often covered by app buttons and captions.
4. Check text is readable on a phone at actual size.
5. Export at good quality (for video, H.264 MP4 unless the platform asks otherwise) and check each file.

## Output

- One file per platform, named clearly (for example `gameday_[DATE]_story_1080x1920.png`).
- Formatting report:

| Platform | File | Size | Safe zone OK | Text readable | Notes |
| --- | --- | --- | --- | --- | --- |

## Before you finish

- Each file was checked at its final size.
- Sizes used were confirmed against current platform guidance, or the report says they weren't.
