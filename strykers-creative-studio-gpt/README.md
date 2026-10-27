# Empire Strykers Creative Studio

Reusable creative-production guidance for the Empire Strykers custom GPT and team.

This repository is the source of truth for the Strykers video-promo workflow: authentic user-supplied footage, protected player identity, verified event details, and final media QA.

## Included

- `GPT-INSTRUCTIONS.md` — paste-ready custom GPT instructions.
- `CLAUDE.md` — project instructions for Claude Code.
- `skills/strykers-video-promo/SKILL.md` — reusable production skill.
- `docs/WORKFLOW.md` — human handoff and quality-control checklist.
- `docs/CLAUDE-CODE-HANDOFF.md` — copy-paste handoff prompt for Claude Code.
- `docs/24-SKILL-LIBRARY.md` — proposed 24-skill architecture and implementation roadmap.
- `references/stryker_agent_skill.md` — supplied Higgsfield and Canva routing reference.

The 24-skill library is a planning specification. A skill is not considered implemented merely because it is listed there; Claude Code should add and verify each `SKILL.md` as the team prioritizes it.

## Using this with the custom GPT

Open the [Strykers Creative Studio GPT](https://chatgpt.com/g/g-6acfd1f572bc8191b3a6c1ce9e4063ca-strykers-creative-studio), use `GPT-INSTRUCTIONS.md` as its instruction source, and upload the skill file or repository contents as Knowledge.

## GitHub setup

```bash
git add .
git commit -m "Add Empire Strykers creative studio workflow"
git branch -M main
git remote add origin https://github.com/ORG/empire-strykers-creative-studio.git
git push -u origin main
```

Replace `ORG` with the team’s GitHub organization or username.
