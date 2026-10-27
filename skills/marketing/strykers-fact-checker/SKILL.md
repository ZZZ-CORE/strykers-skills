---
name: strykers-fact-checker
description: Checks every fact in Empire Strykers graphics and copy (opponents, dates, times, venues, scores, player names, prices) against official sources and labels each VERIFIED, USER-SUPPLIED, NEEDS APPROVAL, or CONFLICT. Use before any Strykers content with event or player details is published.
---

# Strykers Game & Player Fact Checker

> New draft skill (October 2026), written from skill 18 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

No wrong dates, misspelled names, or made-up details in published content.

## When to use

- Before publishing anything with game, ticket, or player details.

## Inputs

- The draft copy or graphic.
- Any sources the user has (schedule, roster, ticket page).

## What counts as an official source

- The Empire Strykers' own website, schedule, roster, or official social accounts.
- The league's official site.
- The venue's official site or the official ticketing page.

Use what you can actually open; don't guess a website address.

## Steps

1. List every fact in the content: opponent, date, start time, venue, city, score, player names and numbers, prices, promo details.
2. Check each against an official source. Check branded terms and hashtags against the Brand Kit spelling.
3. Label each:
   - **VERIFIED:** matches an official source (give the source).
   - **USER-SUPPLIED:** given by the user; not independently checked.
   - **NEEDS APPROVAL:** couldn't be checked; a team member must confirm.
   - **CONFLICT:** sources disagree (show both).
4. For time-sensitive facts (dates, times, prices, availability), note when you checked.

## Output

| Fact | Value in draft | Source | Checked on | Status |
| --- | --- | --- | --- | --- |

Then a list of approved fields ready to use, and anything still blocking publication.

## Rules

- Never fill in a missing fact with a guess.
- A fact with CONFLICT or NEEDS APPROVAL status shouldn't be published until resolved.

## Before you finish

- Every fact in the content has a status.
