# Empire Strykers Creative Studio — Team Operations Skills

Knowledge file for the Strykers Creative Studio GPT. Generated from the `SKILL.md` files in the strykers-skills repository by `scripts/build-gpt-knowledge.py`; edit the skills there, not this file.

## Strykers Creative Approval Manager (`strykers-approval-manager`)

**Use when:** Tracks Empire Strykers creative through draft, review, changes, approval, and release, records who approved what and when, and blocks final release without independent approval. Use when work goes up for review, when feedback comes in, or before any final export or post.

> New draft skill (October 2026), written from skill 21 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Keep a clear record of who reviewed and approved each piece before it goes out.

### When to use

- Work goes up for review, feedback arrives, or something is about to be released.

### Statuses

- **DRAFT:** being made.
- **IN REVIEW:** sent to a reviewer.
- **CHANGES REQUESTED:** reviewer asked for edits.
- **APPROVED:** an approver other than the creator signed off.
- **RELEASED:** exported or posted.

### Steps

1. Log each asset with its creator and current status.
2. Record every change request (who, when, what).
3. When approval comes in, record the approver, date, and how it was given (comment, email, message).
4. Check the approver is not the creator when independent approval is required.
5. Allow release only from APPROVED, and only after the brand check, fact check, and (for video) export check are done.

### Output

| Asset | Version | Creator | Status | Reviewer / approver | Date | Evidence | Notes / changes requested |
| --- | --- | --- | --- | --- | --- | --- | --- |

And a release decision: **Release** or **Hold** (with the reason).

### Rules

- The creator can't approve their own work when independent approval is required.
- The AI can't approve anything; only a person on the team can.
- "Looks good" in passing isn't approval unless the team agrees it counts; record exactly what was said.

### Before you finish

- Every APPROVED or RELEASED asset has a named approver and evidence.

---

## Strykers Asset Library & Rights Manager (`strykers-asset-library`)

**Use when:** Builds and maintains an inventory of approved Empire Strykers creative assets (logos, player photos, video clips, templates, music) with source, version, owner, and usage rights, and flags missing permissions. Use when organizing team assets or checking whether an asset can be used.

> New draft skill (October 2026), written from skill 22 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Know where every asset came from and whether you're allowed to use it.

### When to use

- Organizing the team's assets.
- Before using a photo, clip, logo, or song: "can we use this?"

### Steps

1. List each asset with the fields below.
2. Record where it came from (team photographer, league, sponsor, player, stock, music library).
3. Record usage rights: where it can be used, for how long, and any credit required.
4. Flag assets with unknown source or rights as **Rights unknown — don't use until confirmed**.
5. Flag expired or expiring rights.

### Output

| Asset | Type | Version | Source | Owner / contact | Allowed uses | Expires | Credit needed | Stored at | Rights status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Rights status: **Cleared**, **Limited** (say how), **Unknown**, or **Expired**.

### Rules

- Store the actual files in the team's private storage. Don't add logos, fonts, player photos, footage, music, or sponsor files to public places, including this public GitHub repository. The inventory can point to where they are.
- Player images may have their own rules; follow the team's policy.

### Before you finish

- Every asset in use traces to a source and a rights status.

---

## Strykers Platform Format Optimizer (`strykers-platform-optimizer`)

**Use when:** Prepares Empire Strykers graphics and videos for each publishing platform (sizes, aspect ratios, safe zones, text readability, export quality) and makes platform-specific versions. Use when one piece of content needs to go out on several platforms, or before export.

> New draft skill (October 2026), written from skill 23 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Make each version look right on the platform it's posted to.

### When to use

- Before exporting, or when adapting one piece for several platforms.

### Common starting sizes

Platform rules change, so confirm against each platform's current guidance before relying on these.

| Use | Size | Ratio |
| --- | --- | --- |
| Stories, Reels, TikTok, Shorts | 1080×1920 | 9:16 |
| Feed post, portrait | 1080×1350 | 4:5 |
| Feed post, square | 1080×1080 | 1:1 |
| Landscape video / web | 1920×1080 | 16:9 |

### Steps

1. List the target platforms.
2. For each, set the size and reframe; don't stretch or squash.
3. Keep text and logos inside the safe zone. On vertical video, the top, bottom, and right edges are often covered by app buttons and captions.
4. Check text is readable on a phone at actual size.
5. Export at good quality (for video, H.264 MP4 unless the platform asks otherwise) and check each file.

### Output

- One file per platform, named clearly (for example `gameday_[DATE]_story_1080x1920.png`).
- Formatting report:

| Platform | File | Size | Safe zone OK | Text readable | Notes |
| --- | --- | --- | --- | --- | --- |

### Before you finish

- Each file was checked at its final size.
- Sizes used were confirmed against current platform guidance, or the report says they weren't.

---

## Strykers Content Calendar & Performance (`strykers-content-calendar`)

**Use when:** Plans and tracks the Empire Strykers content calendar (campaign themes, deadlines, production stages) and reviews engagement data the team supplies to recommend improvements. Use for weekly or season planning, tracking what's in production, or reviewing how posts performed.

> New draft skill (October 2026), written from skill 24 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Plan what goes out when, track it, and learn from real results.

### When to use

- Planning a week, a month, or a season.
- Checking what's in production.
- Reviewing how content performed.

### Inputs

- The verified game schedule and key dates (promos, community events, holidays).
- Campaign themes and goals.
- Who is responsible for each piece.
- Performance data exported from the platforms, if reviewing results.

### Steps

1. **Plan.** Build the calendar around the game dates in the team schedule (`SCHEDULE.md`; times are Pacific, matchups listed visitor first). Confirm dates on the official site before publishing. Typical game-week beats: announcement, countdown, game day, final score, recap.
2. **Track.** Give each piece a stage: Idea → Brief → In production → In review → Approved → Scheduled → Posted.
3. **Review.** Using only the data supplied, compare posts by reach, engagement rate, video views/watch time, link clicks, and ticket sales if available.
4. **Recommend.** Suggest changes backed by that data (for example, "vertical video averaged 2× the engagement of static posts across these 12 posts").

### Output

Calendar:

| Date | Platform | Content | Campaign | Owner | Stage | Due |
| --- | --- | --- | --- | --- | --- | --- |

Performance summary: what worked, what didn't, and 3–5 recommendations, each tied to the numbers.

### Rules

- Never make up performance numbers or trends. With no data, say so and stick to planning.
- Dates in the calendar come from a verified schedule, or are marked NEEDS APPROVAL.

### Before you finish

- Every performance claim points to actual data.
