---
name: strykers-video-continuity-qa
description: Reviews an Empire Strykers video for brand consistency, player fidelity, caption and sponsor accuracy, and AI glitches between frames, and reports exactly what was checked. Use on any edited or AI-generated Strykers video before approval.
---

# Strykers Video Brand & Continuity Inspector

> New draft skill (October 2026), written from skill 15 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Catch logo warping, face changes, wrong captions, and glitches before the video goes out.

## When to use

- Any edited or AI-generated video (for example, from Higgsfield) before approval.

## Inputs

- The video file.
- The original source footage and logo files, if available.
- The approved caption text and sponsor list.

## Steps

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

## Output

| Time | Issue | Severity (must fix / should fix) | Fix |
| --- | --- | --- | --- |

Plus a line saying how the review was done (for example, "frames every 1 s, 25 frames checked" or "watched once in full; no frame extraction").

## Before you finish

- Don't claim a frame-by-frame check unless frames were actually extracted and reviewed.
