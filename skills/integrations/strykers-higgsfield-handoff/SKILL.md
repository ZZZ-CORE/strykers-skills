---
name: strykers-higgsfield-handoff
description: Prepares an Empire Strykers image for Higgsfield video (animate it, add cinematic motion, or use it as a video concept reference), writes the motion brief, and reviews the returned video. Use when someone wants to turn a Strykers graphic or photo into motion in Higgsfield.
---

# Strykers Higgsfield Video Handoff

> New draft skill (October 2026), written from skill 11 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Take a still image into Higgsfield without losing the logo or the players' real look.

## When to use

- The user wants to animate or add motion to a Strykers image.

## Steps

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

## Rules

- AI motion can warp logos, faces, and numbers. Check every returned video.
- Don't claim an upload or generation happened without a tool result.

## Output

- Source image, motion brief, upload steps or job status, and a review checklist:

| Check | Result |
| --- | --- |
| Logo stays intact in every part of the video | |
| Player faces and numbers unchanged | |
| Text readable and correct | |
| Motion looks natural, no glitches | |

## Before you finish

- Job status matches what the tool reported.
- The returned video was reviewed before being called usable.
