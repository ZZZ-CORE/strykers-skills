---
name: strykers-export-validator
description: Checks a finished Empire Strykers video file before release (format, codec, size, duration, frame rate, audio, captions, playback, approval status) and marks it READY or NOT READY. Use on every final MP4 before it is published or delivered.
---

# Strykers Video Export Validator

> New draft skill (October 2026), written from skill 16 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Confirm the file really exists and meets the brief before anyone posts it.

## When to use

- On every final video before release.

## Default targets (unless the brief says otherwise)

- MP4 container, H.264 video
- 1080×1920 (9:16 vertical)
- 20–25 seconds
- Audio present (if the brief calls for it) and licensed or supplied by the team

## Steps

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

## Output

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

## If something can't be checked

- **No way to run ffprobe/ffmpeg:** say which checks couldn't be done; the status can't be READY.

## Before you finish

- Never call a video complete without an actual file and successful checks.
