---
name: strykers-bilingual-captions
description: Writes English and Spanish social media captions in the Empire Strykers brand voice, with matching meaning, correct arena soccer terms, team-approved hashtags, and checked facts and calls to action. Use when a Strykers post needs caption copy in one or both languages.
---

# Strykers Bilingual Caption Writer

> New draft skill (October 2026), written from skill 19 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Write captions that sound like the Strykers in both English and Spanish.

## When to use

- A post, reel, or story needs caption copy.

## Inputs

- The post (image or video) and its goal.
- Verified facts (date, opponent, venue, ticket link).
- The team's approved hashtag list, if any.
- Platform (caption length and style vary).

## Brand voice

Energetic, proud, family-friendly, inclusive, rooted in the Inland Empire community. Brand line: "Inspire The Empire."

## Steps

1. Write the English caption: hook, key detail, call to action.
2. Write the Spanish caption with the same meaning and energy; adapt, don't translate word for word.
3. Use arena soccer terms the team already uses. If unsure of a Spanish term, ask. Don't call it "futsal"; that's a different sport.
4. Add hashtags only from the team's approved list. If there's no list, suggest a few and mark them for approval.
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
