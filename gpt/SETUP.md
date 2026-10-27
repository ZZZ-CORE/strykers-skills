# Adding the Skills to the Strykers GPT

The Strykers team can download this repository and load the skills into the Strykers Creative Studio custom GPT as Knowledge.

## What goes where

| GPT builder field | What to put there |
| --- | --- |
| **Instructions** | Everything in [`gpt/INSTRUCTIONS.md`](INSTRUCTIONS.md) (copy and paste; about 4,400 characters, under the 8,000 limit) |
| **Knowledge** | The 7 files in [`gpt/knowledge/`](knowledge/) |
| **Capabilities** | Web Search (to check event facts), Image Generation (for graphics), Code Interpreter & Data Analysis (to make and check image and video files) |

The 7 Knowledge files:

| File | Skills inside |
| --- | --- |
| `01-strykers-brand.md` | Brand Guardian, Logo & Lockup Validator, Brand Typography Manager, Brand QA Inspector |
| `02-strykers-images.md` | Creative Brief Builder, Background Removal Studio, Player Image Integrity, Social Template Factory |
| `03-strykers-integrations.md` | Canva Export & Handoff, Canva Brand Kit Setup, Higgsfield Video Handoff, Integration & Account Checker |
| `04-strykers-video.md` | Strykers Video Promo (original), Video Storyboard Director, Motion Graphics & Captions, Video Brand & Continuity Inspector, Video Export Validator |
| `05-strykers-marketing.md` | Campaign Style Selector, Game & Player Fact Checker, Bilingual Caption Writer, Sponsor & Partnership Manager |
| `06-strykers-operations.md` | Creative Approval Manager, Asset Library & Rights Manager, Platform Format Optimizer, Content Calendar & Performance |
| `07-strykers-workflow.md` | Video production workflow (intake, creative pass, technical pass, handoff) |

## Steps

1. Download the repository: on GitHub, click the green **Code** button, then **Download ZIP**, and unzip it.
2. Open the Strykers Creative Studio GPT in the GPT builder and go to **Configure**.
3. Replace the **Instructions** with the contents of `gpt/INSTRUCTIONS.md`.
4. Under **Knowledge**, remove old skill files, then upload the 7 files from `gpt/knowledge/`.
5. Turn on the capabilities listed above.
6. Optionally, upload the official Brand Kit (as a PDF) as an extra Knowledge file. Don't put the Brand Kit, logos, or fonts in this GitHub repository, because it's public.
7. Test the GPT (below) before sharing it with the team, then save.

## Things to know

- **File limit.** A GPT can have up to 20 Knowledge files. This setup uses 7, leaving room for the Brand Kit and other team references. Don't upload the 25 ZIPs in `downloads/`; those are for Claude.
- **Knowledge is reference material only.** It doesn't install tools or connect Canva, Higgsfield, GitHub, or any other service. Those need supported connections or Actions, set up and tested separately. Until then, the GPT should give manual upload steps instead of claiming a transfer happened.
- **Logos.** Upload official logo files in the chat when you need them in a design. The GPT is told never to draw or generate the logo.
- **Video tools.** Making and checking MP4 files depends on what Code Interpreter can run. If a check can't be done, the GPT should say so.

## Suggested first test

Ask:

> Create a branded Empire Strykers game-day social concept. Identify the required approved assets, mark any missing facts as `NEEDS APPROVAL`, and provide the copy, dimensions, shot direction, and final QA checklist.

A good answer:

- Uses the official colors and the right title font for the season (or asks which season it is).
- Uses placeholders like `[OPPONENT]` and `[DATE]` and marks them `NEEDS APPROVAL`, rather than making up an opponent or date.
- Lists the assets it needs (logo files, player photos or footage).
- Calls the result a concept, not a finished design or export.
- Ends with a QA checklist and a PASS / NEEDS REVIEW / BLOCKED result.

More tests worth running:

- "Write English and Spanish captions for Friday's home game." It should ask for or flag the opponent, time, and ticket link, not invent them.
- "Send this graphic to Canva." With no Canva connection, it should give manual upload steps, not claim it sent the file.
- "Make the logo purple and add a crown." It should refuse to alter the logo and explain why.

## Keeping the GPT up to date

The Knowledge files are generated from the skills in `skills/`. After editing a skill, run:

```bash
python3 scripts/build-gpt-knowledge.py
scripts/build-skill-zips.sh
```

Then re-upload the changed Knowledge file(s) to the GPT.
