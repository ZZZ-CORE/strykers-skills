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

## Skills

**Built** means the skill has a `SKILL.md` you can download and use now. **Planned** means it was only described in `docs/24-SKILL-LIBRARY.md`; that file has each one's full description, inputs, and outputs if you want to build it.

### Video

| Skill | What it does | Status |
| --- | --- | --- |
| Strykers Video Promo | Turns real game footage into a 20–25 second vertical (1080×1920) promo video, keeping players recognizable and checking the final file before handoff | **Built** |
| Video Storyboard Director | Plans scenes, shots, timing, and transitions for promo videos | Planned |
| Motion Graphics & Captions | Specifies titles, lower thirds, score graphics, and English/Spanish captions | Planned |
| Video Brand & Continuity Inspector | Reviews finished video for logo, player, caption, and sponsor accuracy | Planned |
| Video Export Validator | Checks format, size, length, frame rate, audio, and captions before release | Planned |

### Brand

| Skill | What it does | Status |
| --- | --- | --- |
| Brand Guardian | Applies the official colors, fonts, logo rules, and messaging to any creative | Planned |
| Logo & Lockup Validator | Checks logos and sponsor co-branding are used correctly and not altered | Planned |
| Brand Typography Manager | Picks the right in-season or off-season fonts and text hierarchy | Planned |
| Brand QA Inspector | Final brand check that marks an asset PASS, NEEDS REVIEW, or BLOCKED | Planned |

### Images and graphics

| Skill | What it does | Status |
| --- | --- | --- |
| Creative Brief Builder | Turns a short request into a full design brief | Planned |
| Background Removal Studio | Cuts out players, the mascot, or logos onto a transparent background | Planned |
| Player Image Integrity | Makes sure AI edits don't change players' faces, jerseys, or numbers | Planned |
| Social Template Factory | Builds reusable game-day, final-score, player, ticket, and community templates | Planned |

### Canva and Higgsfield

| Skill | What it does | Status |
| --- | --- | --- |
| Canva Export & Handoff | Prepares a graphic for Canva as a PNG, editable file, or team template | Planned |
| Canva Brand Kit Setup | Guides setting up the Strykers brand inside Canva | Planned |
| Higgsfield Video Handoff | Prepares an image and motion brief for animating in Higgsfield | Planned |
| Integration & Account Checker | Checks which creative tools are actually connected | Planned |

### Marketing

| Skill | What it does | Status |
| --- | --- | --- |
| Campaign Style Selector | Recommends a campaign look while keeping to the brand rules | Planned |
| Game & Player Fact Checker | Checks opponents, dates, venues, scores, and player names | Planned |
| Bilingual Caption Writer | Writes English and Spanish social captions in the Strykers voice | Planned |
| Sponsor & Partnership Manager | Keeps sponsor names, logos, and placement correct | Planned |

### Team operations

| Skill | What it does | Status |
| --- | --- | --- |
| Creative Approval Manager | Tracks drafts, revision requests, and sign-off before release | Planned |
| Asset Library & Rights Manager | Keeps track of approved assets and where they can be used | Planned |
| Platform Format Optimizer | Resizes and checks graphics and video for each social platform | Planned |
| Content Calendar & Performance | Plans the content calendar and reviews what performed well | Planned |

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
