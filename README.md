# strykers-skills

Saved skills and instructions built for the Empire Strykers marketing team (called "Seth's team" in some of the files). Download them to reuse in Claude, ChatGPT, or as plain checklists.

## What's here

### `strykers-creative-studio-gpt/` — from the retired Strykers Creative Studio GPT

Saved exactly as exported before the GPT was removed.

| File | What it is | Reuse it for |
| --- | --- | --- |
| `skills/strykers-video-promo/SKILL.md` | Step-by-step skill for 20–25 second vertical promo videos (1080×1920) cut from real game footage | Making Reels/TikTok/Shorts promos |
| `GPT-INSTRUCTIONS.md` | The GPT's full instructions | Setting up a new GPT or Claude project |
| `docs/WORKFLOW.md` | Intake → creative → technical check → handoff checklist | Any video request, with or without AI |
| `docs/24-SKILL-LIBRARY.md` | Brand colors and fonts, plus a plan for 24 more skills | Brand reference; ideas for future skills (only the video promo skill was built) |
| `references/stryker_agent_skill.md` | Pasted Canva and Higgsfield tool notes | Background only |
| `README.md`, `CLAUDE.md`, `docs/CLAUDE-CODE-HANDOFF.md` | The old project's setup notes | Not needed for reuse |

## How to download

- **Everything:** on the repository's GitHub page, click the green **Code** button, then **Download ZIP**.
- **One file:** open the file on GitHub and click the download icon (or **Raw**, then save the page).

## How to reuse

**In Claude (as a skill):** put the `strykers-video-promo` folder (the folder holding `SKILL.md`) into a ZIP file, then upload it in Claude under **Settings → Capabilities → Skills**. Claude will use it when you ask for a Strykers promo video.

**In ChatGPT (as a new GPT):** create a GPT, paste `GPT-INSTRUCTIONS.md` into **Instructions**, and upload `SKILL.md`, `WORKFLOW.md`, and `24-SKILL-LIBRARY.md` as **Knowledge**. Turn on **Code Interpreter** so it can cut and check video files. Don't upload `CLAUDE.md` or the handoff file; they're setup notes, not instructions.

**Without AI:** use `docs/WORKFLOW.md` as a checklist for any promo.

## Check before you reuse

- **Example copy is event-specific.** The default video script uses "TWO NATIONS. / ONE RIVALRY.", "USA VS MÉXICO." and "PICK A SIDE. / GET YOUR TICKETS." Replace these with copy for your event.
- **Colors and fonts.** The official palette and fonts are listed in `docs/24-SKILL-LIBRARY.md`. The video skill also mentions red and green, which aren't in that palette, so use them only for campaigns that call for them. Check everything against the current official Brand Kit.
- **Facts.** Confirm dates, venues, opponents, and ticket details with an official source before publishing.
- **This repository is public.** Don't add logos, fonts, player photos, footage, sponsor files, or passwords here; keep those in the team's private storage.
