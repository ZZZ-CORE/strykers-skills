# Adding the Skills to the Strykers GPT

The Strykers team can download this repository and load the official Brand Kit and the skills into the Strykers Creative Studio custom GPT as Knowledge. **The Brand Kit is the most important file**: the GPT is told to follow it first and to let it win over anything else.

## What goes where

| GPT builder field | What to put there |
| --- | --- |
| **Instructions** | Everything in [`gpt/INSTRUCTIONS.md`](INSTRUCTIONS.md) (copy and paste; about 5,300 characters, under the 8,000 limit) |
| **Knowledge** | All 9 files in [`gpt/knowledge/`](knowledge/) |
| **Capabilities** | Web Search (to check event facts), Image Generation (for graphics), Code Interpreter & Data Analysis (to make and check image and video files) |

The 9 Knowledge files:

| File | What's inside |
| --- | --- |
| `ES_Official_Brand_Kit_PUB.pdf` | The official Empire Strykers Brand Kit, as published |
| `00-strykers-brand-kit.md` | The Brand Kit as text, including descriptions of its image-only pages (logo meaning, colorways, design categories, lockups), so the GPT can read every rule |
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
4. Under **Knowledge**, remove old skill files, then upload all 9 files from `gpt/knowledge/`, including the Brand Kit PDF and `00-strykers-brand-kit.md`.
5. Turn on the capabilities listed above.
6. Test the GPT (below) before sharing it with the team, then save.

## Things to know

- **File limit.** A GPT can have up to 20 Knowledge files. This setup uses 9, leaving room for other team references. Don't upload the 25 ZIPs in `downloads/`; those are for Claude.
- **Knowledge is reference material only.** It doesn't install tools or connect Canva, Higgsfield, GitHub, or any other service. Those need supported connections or Actions, set up and tested separately. Until then, the GPT should give manual upload steps instead of claiming a transfer happened.
- **Logos.** The logo files themselves aren't in this repository; they're in the team's Drive brand folder (Brand Kit page 17). Upload them in the chat when you need them in a design. The GPT is told never to draw or generate the logo.
- **Video tools.** Making and checking MP4 files depends on what Code Interpreter can run. If a check can't be done, the GPT should say so.

## Suggested first test

Ask:

> Create a branded Empire Strykers game-day social concept. Identify the required approved assets, mark any missing facts as `NEEDS APPROVAL`, and provide the copy, dimensions, shot direction, and final QA checklist.

A good answer:

- Uses only the seven Brand Kit colors, the right title font for the season (or asks which season it is), and a Brand Kit asset category such as MASL Home Game.
- Uses the Brand Kit's "every post" and Gameday hashtags.
- Uses placeholders like `[OPPONENT]` and `[DATE]` and marks them `NEEDS APPROVAL`, rather than making up an opponent or date.
- Lists the assets it needs (logo files, player photos or footage).
- Calls the result a concept, not a finished design or export.
- Ends with a QA checklist and a PASS / NEEDS REVIEW / BLOCKED result.

More tests worth running:

- "Write English and Spanish captions for Friday's home game." It should ask for or flag the opponent, time, and ticket link, not invent them.
- "Send this graphic to Canva." With no Canva connection, it should give manual upload steps, not claim it sent the file.
- "Make the logo purple and add a crown." It should refuse to alter the logo and explain why.
- "Use red and green for this rivalry post." It should explain the Brand Kit allows only its seven colors.
- "Make a co-branded post with us, MASL, and Verizon." With 3 logos, the Strykers logo should go in the center.

## Updating the Brand Kit

When the team publishes a new Brand Kit, replace `brand-kit/ES_Official_Brand_Kit_PUB.pdf`, update `brand-kit/BRAND-KIT.md` to match, run the two scripts below, and re-upload both Brand Kit files to the GPT.

## Keeping the GPT up to date

The Knowledge files are generated from the skills in `skills/`. After editing a skill, run:

```bash
python3 scripts/build-gpt-knowledge.py
scripts/build-skill-zips.sh
```

Then re-upload the changed Knowledge file(s) to the GPT.
