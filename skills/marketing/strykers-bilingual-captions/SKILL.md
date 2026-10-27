---
name: strykers-bilingual-captions
description: Writes English and Spanish social media captions in the Empire Strykers brand voice, with matching meaning, correct arena soccer terms, team-approved hashtags, and checked facts and calls to action. Use when a Strykers post needs caption copy in one or both languages.
---

# Strykers Bilingual Caption Writer

> New draft skill (October 2026), written from skill 19 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Write captions that sound like the Strykers in both English and Spanish.

## When to use

- A post, reel, or story needs caption copy.

## Inputs

- The post (image or video) and its goal.
- Verified facts (date, opponent, venue, ticket link).
- The team's approved hashtag list, if any.
- Platform (caption length and style vary).

## Brand voice

Follow the Brand Kit messaging: tagline "Empire Strykers: Inspiring the Empire Through Pro Arena Soccer"; motto "Inspire The Empire"; pillars Community First, Always; Fast, Fierce, and Fun; Underdog Spirit with Big League Swagger; Inspired by Legacy, Building for the Future; Open Doors, Open Hearts; Content That Connects; Inspire Your Empire. Favor the kit's frequently used phrases (Defend The Empire, We Are Empire, Beware The Empire, Rise With Empire, The Greatest Sport On Turf, Futbol Rapido Profesional, Inland Empire's Only True Professional Team).

## Steps

1. Write the English caption: hook, key detail, call to action.
2. Write the Spanish caption with the same meaning and energy; adapt, don't translate word for word.
3. Use the Brand Kit's branded terms, spelled exactly: Goal, Hattrick, Wallascora, Power Play, Power Kill, 6th Attacker, Golaso, Golazo, Blue Card, Yellow Card, Red Card, Fan Fest, Overtime. In Spanish, the sport is "Fútbol Rápido Profesional" (#FutbolRapidoProfesional); don't call it "futsal", which is a different sport.
4. Add hashtags from the Brand Kit: the "every post" list plus the closest topic list (Gameday, Camps & Clinics, Business Mixer, New Partner, New Player, Stryking Fury, Soccer In 60, TST) and any partner list. Use the spellings in `BRAND-KIT.md`, which corrects a few typos in the PDF (for example #InspireYourEmpire, not #InspireTYourEmpire).
5. Check names, dates, times, and the call to action against the fact list.

## Output

```text
EN:
[caption]

ES:
[caption]

Hashtags: [approved / suggested — needs approval]
Facts used: [fact — status]
```

Offer a short and a long version if the platform allows.

## Rules

- Spanish copy should be reviewed by a fluent team member before posting.
- Don't translate player names or the slogan unless the team has an approved version.

## Before you finish

- Both versions say the same thing, with the same facts.
- Every fact is VERIFIED or marked NEEDS APPROVAL.
