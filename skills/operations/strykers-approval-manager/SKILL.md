---
name: strykers-approval-manager
description: Tracks Empire Strykers creative through draft, review, changes, approval, and release, records who approved what and when, and blocks final release without independent approval. Use when work goes up for review, when feedback comes in, or before any final export or post.
---

# Strykers Creative Approval Manager

> New draft skill (October 2026), written from skill 21 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

> **Brand Kit first:** follow the Empire Strykers Official Brand Kit (`BRAND-KIT.md`, included in this skill's ZIP and in the repository's `brand-kit/` folder with the original PDF). It wins over anything in this skill.

Keep a clear record of who reviewed and approved each piece before it goes out.

## When to use

- Work goes up for review, feedback arrives, or something is about to be released.

## Statuses

- **DRAFT:** being made.
- **IN REVIEW:** sent to a reviewer.
- **CHANGES REQUESTED:** reviewer asked for edits.
- **APPROVED:** an approver other than the creator signed off.
- **RELEASED:** exported or posted.

## Steps

1. Log each asset with its creator and current status.
2. Record every change request (who, when, what).
3. When approval comes in, record the approver, date, and how it was given (comment, email, message).
4. Check the approver is not the creator when independent approval is required.
5. Allow release only from APPROVED, and only after the brand check, fact check, and (for video) export check are done.

## Output

| Asset | Version | Creator | Status | Reviewer / approver | Date | Evidence | Notes / changes requested |
| --- | --- | --- | --- | --- | --- | --- | --- |

And a release decision: **Release** or **Hold** (with the reason).

## Rules

- The creator can't approve their own work when independent approval is required.
- The AI can't approve anything; only a person on the team can.
- "Looks good" in passing isn't approval unless the team agrees it counts; record exactly what was said.

## Before you finish

- Every APPROVED or RELEASED asset has a named approver and evidence.
