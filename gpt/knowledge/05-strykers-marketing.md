# Empire Strykers Creative Studio — Marketing Skills

Knowledge file for the Strykers Creative Studio GPT. Generated from the `SKILL.md` files in the strykers-skills repository by `scripts/build-gpt-knowledge.py`; edit the skills there, not this file.

## Strykers Campaign Style Selector (`strykers-campaign-style-selector`)

**Use when:** Recommends two or three creative directions for an Empire Strykers campaign from the team's approved references and inspiration, while keeping the official brand rules in charge. Use when starting a new campaign or when the team wants fresh looks.

> New draft skill (October 2026), written from skill 17 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Find a fresh look for a campaign that still looks like the Empire Strykers.

### When to use

- Kicking off a campaign, or when the team wants new creative ideas.

### Inputs

- Campaign goal and audience (for example, sell tickets for a rivalry game, promote family night).
- Inspiration the team provides (for example, PostPick styles or past posts they liked).
- Season and platforms.

### Steps

1. Restate the objective in one line.
2. Propose 2–3 directions. For each:
   - Name and one-line idea.
   - Look: layout, imagery, motion.
   - How it uses the brand: colors (White `#FFFFFF`, Silver Sand `#B8BABC`, Aluminium `#A3A5A9`, Mid Grey `#6E6E71`, Black `#000000`, Plum `#953493`, Rouge `#9F3E97`), title font by season, original logo.
   - Which Brand Kit messaging pillar it expresses (for example Fast, Fierce, and Fun or Community First, Always) and its Brand Kit asset category.
   - Where inspiration conflicts with brand rules, say which rule wins (the brand does).
   - Example headline using placeholders (`[OPPONENT]`, `[DATE]`).
3. Recommend one and say why. The Brand Kit's guide: be bold, be original, bring heritage, bring futuristic flair.

### Output

- Direction comparison table and a short visual brief for the chosen direction.

### Rules

- Inspiration never overrides the official Brand Kit.
- Don't copy another team's or brand's design.

### Before you finish

- Each direction is shown to fit the brand rules.

---

## Strykers Game & Player Fact Checker (`strykers-fact-checker`)

**Use when:** Checks every fact in Empire Strykers graphics and copy (opponents, dates, times, venues, scores, player names, prices) against official sources and labels each VERIFIED, USER-SUPPLIED, NEEDS APPROVAL, or CONFLICT. Use before any Strykers content with event or player details is published.

> New draft skill (October 2026), written from skill 18 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

No wrong dates, misspelled names, or made-up details in published content.

### When to use

- Before publishing anything with game, ticket, or player details.

### Inputs

- The draft copy or graphic.
- Any sources the user has (schedule, roster, ticket page).

### What counts as an official source

- The Empire Strykers' own website, schedule, roster, or official social accounts.
- The league's official site.
- The venue's official site or the official ticketing page.

Use what you can actually open; don't guess a website address.

### Steps

1. List every fact in the content: opponent, date, start time, venue, city, score, player names and numbers, prices, promo details.
2. Check each against an official source. Check branded terms and hashtags against the Brand Kit spelling. Check player names, nicknames, and positions against the team roster (`ROSTER.md`); roster stats and awards count as USER-SUPPLIED (team roster), and every jersey number is TBD, so any number in the content is NEEDS APPROVAL. Check dates, times, opponents, venues, and promo codes against the team schedule (`SCHEDULE.md`); those count as USER-SUPPLIED (team schedule) until confirmed on the official site. Times there are Pacific, and matchups are listed visitor first.
3. Label each:
   - **VERIFIED:** matches an official source (give the source).
   - **USER-SUPPLIED:** given by the user; not independently checked.
   - **NEEDS APPROVAL:** couldn't be checked; a team member must confirm.
   - **CONFLICT:** sources disagree (show both).
4. For time-sensitive facts (dates, times, prices, availability), note when you checked.

### Output

| Fact | Value in draft | Source | Checked on | Status |
| --- | --- | --- | --- | --- |

Then a list of approved fields ready to use, and anything still blocking publication.

### Rules

- Never fill in a missing fact with a guess.
- A fact with CONFLICT or NEEDS APPROVAL status shouldn't be published until resolved.

### Before you finish

- Every fact in the content has a status.

---

## Strykers Bilingual Caption Writer (`strykers-bilingual-captions`)

**Use when:** Writes English and Spanish social media captions in the Empire Strykers brand voice, with matching meaning, correct arena soccer terms, team-approved hashtags, and checked facts and calls to action. Use when a Strykers post needs caption copy in one or both languages.

> New draft skill (October 2026), written from skill 19 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Write captions that sound like the Strykers in both English and Spanish.

### When to use

- A post, reel, or story needs caption copy.

### Inputs

- The post (image or video) and its goal.
- Verified facts (date, opponent, venue, ticket link).
- The team's approved hashtag list, if any.
- Platform (caption length and style vary).

### Brand voice

Follow the Brand Kit messaging: tagline "Empire Strykers: Inspiring the Empire Through Pro Arena Soccer"; motto "Inspire The Empire"; pillars Community First, Always; Fast, Fierce, and Fun; Underdog Spirit with Big League Swagger; Inspired by Legacy, Building for the Future; Open Doors, Open Hearts; Content That Connects; Inspire Your Empire. Favor the kit's frequently used phrases (Defend The Empire, We Are Empire, Beware The Empire, Rise With Empire, The Greatest Sport On Turf, Futbol Rapido Profesional, Inland Empire's Only True Professional Team).

### Steps

1. Write the English caption: hook, key detail, call to action.
2. Write the Spanish caption with the same meaning and energy; adapt, don't translate word for word.
3. Use the Brand Kit's branded terms, spelled exactly: Goal, Hattrick, Wallascora, Power Play, Power Kill, 6th Attacker, Golaso, Golazo, Blue Card, Yellow Card, Red Card, Fan Fest, Overtime. In Spanish, the sport is "Fútbol Rápido Profesional" (#FutbolRapidoProfesional); don't call it "futsal", which is a different sport.
4. Add hashtags from the Brand Kit: the "every post" list plus the closest topic list (Gameday, Camps & Clinics, Business Mixer, New Partner, New Player, Stryking Fury, Soccer In 60, TST) and any partner list. Use the spellings in `BRAND-KIT.md`, which corrects a few typos in the PDF (for example #InspireYourEmpire, not #InspireTYourEmpire).
5. Check names, dates, times, and the call to action against the fact list. Spell player names and nicknames exactly as in the team roster (`ROSTER.md`), including accents (Marco Fabián, "El Niño de Oro"); don't state a jersey number (all are TBD).

### Output

```text
EN:
[caption]

ES:
[caption]

Hashtags: [approved / suggested — needs approval]
Facts used: [fact — status]
```

Offer a short and a long version if the platform allows.

### Rules

- Spanish copy should be reviewed by a fluent team member before posting.
- Don't translate player names or the slogan unless the team has an approved version.

### Before you finish

- Both versions say the same thing, with the same facts.
- Every fact is VERIFIED or marked NEEDS APPROVAL.

---

## Strykers Sponsor & Partnership Manager (`strykers-sponsor-manager`)

**Use when:** Keeps Empire Strykers sponsor content correct (sponsor names, approved logo files, co-brand placement, campaign or contract requirements) and produces a co-brand brief and sponsor QA checklist. Use for any Strykers content that features or mentions a sponsor or partner.

> New draft skill (October 2026), written from skill 20 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Get every sponsor's name, logo, and placement right.

### When to use

- Any content that shows or mentions a sponsor or partner.

### Inputs

- Sponsor name(s) as the team spells them.
- Sponsor-supplied logo files and any brand guidelines from the sponsor.
- Placement or mention requirements from the agreement or campaign (as summarized by the team).

### Steps

1. Build or update the sponsor reference:

   | Sponsor | Exact name | Logo file(s) | Placement rules | Required wording | Notes |
   | --- | --- | --- | --- | --- | --- |

2. Write the co-brand brief using the Brand Kit lockup rules: logos separated by thin divider lines; with 2 logos, Strykers on the left (horizontal) or top (vertical); with 3 or more, Strykers in the center if the number is odd, on the left if even. Add each logo's size and the required wording.
   For social posts, add the Brand Kit's "every post" hashtags plus that partner's hashtags (for example National CORE / Hope Thru Housing, Loma Linda, Stater Bros, Verizon).
3. Use only logo files supplied by the sponsor or the team; never redraw or AI-generate them.
4. Check the draft against the brief.
5. Flag anything contractual or unclear as NEEDS APPROVAL for the person who manages that sponsor.

### Output

- Co-brand brief.
- Sponsor QA checklist:

| Check | Result |
| --- | --- |
| Sponsor name spelled exactly | |
| Approved logo file used, unaltered | |
| Placement and size as agreed | |
| Required wording included | |
| Nothing implied that the sponsor didn't approve | |

### Rules

- Never guess a sponsor's name or relationship.
- Keep sponsor contracts and confidential files out of public storage, including this repository.

### Before you finish

- Every sponsor element matches the available approvals, or is marked NEEDS APPROVAL.
