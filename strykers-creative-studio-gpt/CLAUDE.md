# Claude Code Project Brief

## Project

This repository is the working source of truth for the Empire Strykers Creative Studio custom GPT:

https://chatgpt.com/g/g-6acfd1f572bc8191b3a6c1ce9e4063ca-strykers-creative-studio

The intended GitHub repository is:

`git@github.com:ZZZ-CORE/strykers-skills.git`

The goal is to maintain reusable instructions and production skills for premium Empire Strykers promotional content, especially short-form vertical videos made from authentic team footage.

## Repository map

- `GPT-INSTRUCTIONS.md` — paste-ready instructions for the custom GPT.
- `skills/strykers-video-promo/SKILL.md` — detailed video-production skill.
- `docs/WORKFLOW.md` — intake, creative, technical QA, and handoff process.
- `docs/24-SKILL-LIBRARY.md` — proposed 24-skill architecture and roadmap.
- `references/stryker_agent_skill.md` — supplied Higgsfield and Canva routing reference.
- `README.md` — project overview and GitHub setup.

## Rules for changes

- Preserve the Empire Strykers identity and use the exact brand name.
- Do not invent players, match action, stadiums, logos, sponsors, tickets, dates, venues, or event claims.
- Treat user-supplied footage as the creative centerpiece; protect recognizable frames and player identity.
- Keep event-specific facts out of generic instructions unless they are verified by an official source.
- Keep instructions concise, practical, and usable by a custom GPT.
- Do not add credentials, API keys, private media, or copyrighted assets to the repository.
- Prefer Markdown documentation unless an executable tool is specifically requested.

## Custom GPT integration

When updating the workflow:

1. Update `GPT-INSTRUCTIONS.md` for high-level GPT behavior.
2. Update `skills/strykers-video-promo/SKILL.md` for production-specific rules.
3. Update `docs/WORKFLOW.md` if the human handoff or QA process changes.
4. Check that the three documents do not contradict one another.
5. Summarize what changed and identify any claims that still need approval.

## Required video standards

- Default output: 1080×1920 vertical MP4.
- Default duration: 20–25 seconds.
- Target at least 80% authentic source-footage screen time.
- Verify a playable H.264 stream, multiple distinct source moments, readable typography, and a clean logo-safe area.
- Report the final absolute output path and any unverified event details.

## First tasks for Claude Code

When first opening this repository:

1. Read this file, `README.md`, `GPT-INSTRUCTIONS.md`, `skills/strykers-video-promo/SKILL.md`, and `docs/WORKFLOW.md`.
2. Check the working tree and current branch before editing.
3. Do not rewrite the creative rules without explaining why.
4. If asked to add a new skill, mirror the existing skill format and update the README file map.
5. After edits, review the Markdown for consistency and provide a concise change summary.
- Treat the 24-skill library as proposed specifications, not completed implementations. Track implementation status explicitly.
- Use the supplied agent-skill reference as routing guidance only; do not claim a Canva or Higgsfield action occurred without verified tool evidence.
