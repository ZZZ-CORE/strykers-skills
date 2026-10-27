# Empire Strykers Creative Studio

Welcome, Strykers team! This repository helps our creative tools make on-brand graphics, videos, captions, and campaign materials. It holds the official Brand Kit and the skills for the Strykers Creative Studio custom GPT (in some of the files the team is called "Seth's team"). The skills also work in Claude or as plain checklists.

## Brand first

**The [Empire Strykers Official Brand Kit](brand-kit/ES_Official_Brand_Kit_PUB.pdf) is the most important file here.** Every skill and the GPT follow it first, and it wins over anything else. A text version, [`brand-kit/BRAND-KIT.md`](brand-kit/BRAND-KIT.md), lists every rule: the seven official colors, logo colorways, fonts, design categories, co-branded lockups, messaging, hashtags, and arena soccer terms.

Use approved Strykers logos, colors, fonts, player images, sponsors, and event information. When something is not verified, mark it `NEEDS APPROVAL` rather than guessing.

**Setting up the custom GPT?** Follow [`gpt/SETUP.md`](gpt/SETUP.md): paste [`gpt/INSTRUCTIONS.md`](gpt/INSTRUCTIONS.md) into Instructions and upload the 9 files in [`gpt/knowledge/`](gpt/knowledge/) (Brand Kit included) as Knowledge.

## What's here

| Folder | What it is |
| --- | --- |
| `brand-kit/` | The official Brand Kit PDF and its full text version |
| `gpt/` | Everything for the custom GPT: setup guide, Instructions, and 9 Knowledge files (Brand Kit plus all 25 skills) |
| `downloads/` | One ready-to-upload ZIP per skill, for Claude (each includes the Brand Kit text) |
| `skills/` | The 24 skills from the 24-skill plan, written as usable `SKILL.md` files (October 2026) |
| `strykers-creative-studio-gpt/` | Exact backup of the original Strykers Creative Studio GPT files, including its one original skill (`strykers-video-promo`) |
| `scripts/` | `build-gpt-knowledge.py` and `build-skill-zips.sh` rebuild the Knowledge files and ZIPs after a skill is edited |

## Skills

**Original** = used in the Strykers Creative Studio GPT. **New draft** = written in October 2026 from the GPT's 24-skill plan (`strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`) and not yet tested in real production, so check the results the first few times you use one.

### Video

| Skill | What it does | Status | Download |
| --- | --- | --- | --- |
| [Strykers Video Promo](strykers-creative-studio-gpt/skills/strykers-video-promo/SKILL.md) | Turns real game footage into a 20–25 second vertical (1080×1920) promo video, keeping players recognizable and checking the final file | Original | [ZIP](downloads/strykers-video-promo.zip) |
| [Video Storyboard Director](skills/video/strykers-storyboard-director/SKILL.md) | Plans scenes, shots, timing, text, and transitions before editing | New draft | [ZIP](downloads/strykers-storyboard-director.zip) |
| [Motion Graphics & Captions](skills/video/strykers-motion-captions/SKILL.md) | Specifies titles, name tags, and score graphics; writes English and Spanish caption files | New draft | [ZIP](downloads/strykers-motion-captions.zip) |
| [Video Brand & Continuity Inspector](skills/video/strykers-video-continuity-qa/SKILL.md) | Reviews finished video for logo warping, face changes, glitches, and caption or sponsor errors | New draft | [ZIP](downloads/strykers-video-continuity-qa.zip) |
| [Video Export Validator](skills/video/strykers-export-validator/SKILL.md) | Checks format, size, length, audio, playback, and approval before release; READY or NOT READY | New draft | [ZIP](downloads/strykers-export-validator.zip) |

### Brand

| Skill | What it does | Status | Download |
| --- | --- | --- | --- |
| [Brand Guardian](skills/brand/strykers-brand-guardian/SKILL.md) | Applies the official colors, fonts, logo rules, and messaging to any creative | New draft | [ZIP](downloads/strykers-brand-guardian.zip) |
| [Logo & Lockup Validator](skills/brand/strykers-logo-validator/SKILL.md) | Checks logos and sponsor co-branding are the real artwork, used correctly | New draft | [ZIP](downloads/strykers-logo-validator.zip) |
| [Brand Typography Manager](skills/brand/strykers-typography-manager/SKILL.md) | Picks in-season or off-season fonts and checks text is readable | New draft | [ZIP](downloads/strykers-typography-manager.zip) |
| [Brand QA Inspector](skills/brand/strykers-brand-qa/SKILL.md) | Final brand check before release; PASS, NEEDS REVIEW, or BLOCKED | New draft | [ZIP](downloads/strykers-brand-qa.zip) |

### Images and graphics

| Skill | What it does | Status | Download |
| --- | --- | --- | --- |
| [Creative Brief Builder](skills/images/strykers-creative-brief-builder/SKILL.md) | Turns a short request into a full design brief, without making up facts | New draft | [ZIP](downloads/strykers-creative-brief-builder.zip) |
| [Background Removal Studio](skills/images/strykers-background-removal/SKILL.md) | Cuts out players, the mascot, or logos onto a transparent background and checks the result | New draft | [ZIP](downloads/strykers-background-removal.zip) |
| [Player Image Integrity](skills/images/strykers-player-image-integrity/SKILL.md) | Makes sure edits don't change players' faces, jerseys, or numbers | New draft | [ZIP](downloads/strykers-player-image-integrity.zip) |
| [Social Template Factory](skills/images/strykers-social-template-factory/SKILL.md) | Builds reusable game-day, final-score, player, ticket, and community templates | New draft | [ZIP](downloads/strykers-social-template-factory.zip) |

### Canva and Higgsfield

| Skill | What it does | Status | Download |
| --- | --- | --- | --- |
| [Canva Export & Handoff](skills/integrations/strykers-canva-handoff/SKILL.md) | Gets a finished graphic into Canva as a PNG, editable file, or team template | New draft | [ZIP](downloads/strykers-canva-handoff.zip) |
| [Canva Brand Kit Setup](skills/integrations/strykers-canva-brand-kit/SKILL.md) | Guides setting up the Strykers logos, colors, fonts, and templates in Canva | New draft | [ZIP](downloads/strykers-canva-brand-kit.zip) |
| [Higgsfield Video Handoff](skills/integrations/strykers-higgsfield-handoff/SKILL.md) | Prepares an image and motion brief for animating in Higgsfield, then reviews the video | New draft | [ZIP](downloads/strykers-higgsfield-handoff.zip) |
| [Integration & Account Checker](skills/integrations/strykers-account-checker/SKILL.md) | Checks which creative tools are actually connected before relying on them | New draft | [ZIP](downloads/strykers-account-checker.zip) |

### Marketing

| Skill | What it does | Status | Download |
| --- | --- | --- | --- |
| [Campaign Style Selector](skills/marketing/strykers-campaign-style-selector/SKILL.md) | Suggests 2–3 campaign looks that stay on brand | New draft | [ZIP](downloads/strykers-campaign-style-selector.zip) |
| [Game & Player Fact Checker](skills/marketing/strykers-fact-checker/SKILL.md) | Checks opponents, dates, venues, scores, names, and prices against official sources | New draft | [ZIP](downloads/strykers-fact-checker.zip) |
| [Bilingual Caption Writer](skills/marketing/strykers-bilingual-captions/SKILL.md) | Writes English and Spanish social captions in the Strykers voice | New draft | [ZIP](downloads/strykers-bilingual-captions.zip) |
| [Sponsor & Partnership Manager](skills/marketing/strykers-sponsor-manager/SKILL.md) | Keeps sponsor names, logos, placement, and required wording correct | New draft | [ZIP](downloads/strykers-sponsor-manager.zip) |

### Team operations

| Skill | What it does | Status | Download |
| --- | --- | --- | --- |
| [Creative Approval Manager](skills/operations/strykers-approval-manager/SKILL.md) | Tracks drafts, feedback, and sign-off; blocks release without independent approval | New draft | [ZIP](downloads/strykers-approval-manager.zip) |
| [Asset Library & Rights Manager](skills/operations/strykers-asset-library/SKILL.md) | Keeps an inventory of approved assets and where each can be used | New draft | [ZIP](downloads/strykers-asset-library.zip) |
| [Platform Format Optimizer](skills/operations/strykers-platform-optimizer/SKILL.md) | Resizes and checks graphics and video for each social platform | New draft | [ZIP](downloads/strykers-platform-optimizer.zip) |
| [Content Calendar & Performance](skills/operations/strykers-content-calendar/SKILL.md) | Plans the content calendar and reviews real performance data | New draft | [ZIP](downloads/strykers-content-calendar.zip) |

## How to download

- **Everything:** on the repository's GitHub page, click the green **Code** button, then **Download ZIP**.
- **One skill:** click its **ZIP** link above, then click the download icon on the next page.

## How to use

**In the Strykers custom GPT (main use):** follow [`gpt/SETUP.md`](gpt/SETUP.md). Use the Instructions and the 9 Knowledge files in `gpt/`, not the individual ZIPs; a GPT allows only 20 Knowledge files.

**In Claude (as skills):** download a skill's ZIP and upload it in Claude under **Settings → Capabilities → Skills**. Repeat for each skill you want.

**Without AI:** every `SKILL.md` is readable as a checklist. Open it on GitHub and follow the steps.

## Check before you reuse

- **Follow the Brand Kit.** Only the seven official colors; logos only from the team's Drive brand folder, never redrawn; fonts from Adobe Fonts.
- **Original GPT files.** The original GPT's instructions and video skill include event-specific example copy ("TWO NATIONS. / ONE RIVALRY.", "USA VS MÉXICO.", "PICK A SIDE. / GET YOUR TICKETS.") and mention red and green, which the Brand Kit doesn't allow. Replace the copy for your event. The new skills use placeholders like `[OPPONENT]` instead.
- **Facts.** Confirm dates, venues, opponents, and ticket details with an official source before publishing.
- **This repository is public.** The Brand Kit here is the published version. Don't add logo files, font files, player photos, footage, sponsor contracts, or passwords; keep those in the team's private storage.

## Editing a skill

Edit its `SKILL.md` (or `brand-kit/BRAND-KIT.md`), then run both scripts from the repository root so the GPT Knowledge files and ZIPs match:

```bash
python3 scripts/build-gpt-knowledge.py
scripts/build-skill-zips.sh
```

Then re-upload the changed Knowledge file to the GPT.

Thanks for helping us **Inspire The Empire!**
