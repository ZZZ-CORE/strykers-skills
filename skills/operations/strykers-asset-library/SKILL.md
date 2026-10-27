---
name: strykers-asset-library
description: Builds and maintains an inventory of approved Empire Strykers creative assets (logos, player photos, video clips, templates, music) with source, version, owner, and usage rights, and flags missing permissions. Use when organizing team assets or checking whether an asset can be used.
---

# Strykers Asset Library & Rights Manager

> New draft skill (October 2026), written from skill 22 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Know where every asset came from and whether you're allowed to use it.

## When to use

- Organizing the team's assets.
- Before using a photo, clip, logo, or song: "can we use this?"

## Steps

1. List each asset with the fields below.
2. Record where it came from (team photographer, league, sponsor, player, stock, music library).
3. Record usage rights: where it can be used, for how long, and any credit required.
4. Flag assets with unknown source or rights as **Rights unknown — don't use until confirmed**.
5. Flag expired or expiring rights.

## Output

| Asset | Type | Version | Source | Owner / contact | Allowed uses | Expires | Credit needed | Stored at | Rights status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Rights status: **Cleared**, **Limited** (say how), **Unknown**, or **Expired**.

## Rules

- Store the actual files in the team's private storage. Don't add logos, fonts, player photos, footage, music, or sponsor files to public places, including this public GitHub repository. The inventory can point to where they are.
- Player images may have their own rules; follow the team's policy.

## Before you finish

- Every asset in use traces to a source and a rights status.
