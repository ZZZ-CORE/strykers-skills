---
name: strykers-creative-brief-builder
description: Turns a short Empire Strykers creative request into a full production brief with goal, audience, platform size, copy, required assets, brand rules, and open questions. Use when someone asks for a Strykers graphic, video, or campaign piece with only a few words of direction.
---

# Strykers Creative Brief Builder

> New draft skill (October 2026), written from skill 05 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Turn "make a game-day post" into a brief good enough to produce a first draft, without inventing facts.

## When to use

- A request arrives with little detail ("make a ticket promo", "player spotlight for Friday").

## Inputs

- The request.
- Any details the user has: event, date, venue, opponent, player, ticket link, platform, deadline.
- Approved assets available (logos, photos, footage).

## Steps

1. Work out the goal (sell tickets, announce, celebrate, inform) and the audience.
2. Pick the platform and size. Common starting points: 1080×1080 square, 1080×1350 portrait feed post, 1080×1920 vertical story/reel. Check current platform guidance if unsure.
3. Take game details (date, Pacific time, opponent, home/away, venue, promo code, ticket link, parking) from the team schedule (`SCHEDULE.md`), labeled USER-SUPPLIED (team schedule). Draft headline and supporting copy. Use placeholders like `[OPPONENT]` or `[DATE]` for any fact not supplied; never fill them in from guesswork.
4. List the assets needed and whether each one has been provided.
5. Add the brand rules: official colors, title font by season (Impact in season, Beachwood UltraBold off season), original logo files only.
6. List open questions.

## Output

```text
CREATIVE BRIEF
Goal:
Audience:
Platform and size:
Season (title font):
Brand Kit asset category (e.g. MASL Home Game, Flyers):
Headline:
Supporting copy:
Call to action:
Hashtags (from the Brand Kit lists):
Layout notes:
Required assets (provided? yes/no):
Facts (value | source | VERIFIED / USER-SUPPLIED / NEEDS APPROVAL):
Brand rules:
Open questions:
Deadline:
```

## If something is missing

- Missing facts stay as placeholders marked NEEDS APPROVAL.
- If the goal or platform is unclear and changes the design, ask before going further.

## Before you finish

- Every fact in the brief has a status.
- No date, venue, opponent, price, or player name was made up.
