---
name: strykers-sponsor-manager
description: Keeps Empire Strykers sponsor content correct (sponsor names, approved logo files, co-brand placement, campaign or contract requirements) and produces a co-brand brief and sponsor QA checklist. Use for any Strykers content that features or mentions a sponsor or partner.
---

# Strykers Sponsor & Partnership Manager

> New draft skill (October 2026), written from skill 20 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Get every sponsor's name, logo, and placement right.

## When to use

- Any content that shows or mentions a sponsor or partner.

## Inputs

- Sponsor name(s) as the team spells them.
- Sponsor-supplied logo files and any brand guidelines from the sponsor.
- Placement or mention requirements from the agreement or campaign (as summarized by the team).

## Steps

1. Build or update the sponsor reference:

   | Sponsor | Exact name | Logo file(s) | Placement rules | Required wording | Notes |
   | --- | --- | --- | --- | --- | --- |

2. Write the co-brand brief: where each logo goes, its size relative to the Strykers logo, and required wording.
3. Use only logo files supplied by the sponsor or the team; never redraw or AI-generate them.
4. Check the draft against the brief.
5. Flag anything contractual or unclear as NEEDS APPROVAL for the person who manages that sponsor.

## Output

- Co-brand brief.
- Sponsor QA checklist:

| Check | Result |
| --- | --- |
| Sponsor name spelled exactly | |
| Approved logo file used, unaltered | |
| Placement and size as agreed | |
| Required wording included | |
| Nothing implied that the sponsor didn't approve | |

## Rules

- Never guess a sponsor's name or relationship.
- Keep sponsor contracts and confidential files out of public storage, including this repository.

## Before you finish

- Every sponsor element matches the available approvals, or is marked NEEDS APPROVAL.
