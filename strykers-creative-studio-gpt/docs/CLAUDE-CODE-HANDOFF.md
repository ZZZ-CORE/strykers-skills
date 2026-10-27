# Claude Code Handoff

## Repository context

- GitHub repository: `git@github.com:ZZZ-CORE/strykers-skills.git`
- Custom GPT: https://chatgpt.com/g/g-6acfd1f572bc8191b3a6c1ce9e4063ca-strykers-creative-studio
- Primary purpose: maintain the instructions and reusable skills that power the Empire Strykers creative workflow.

Use this message when giving the repository to Claude Code:

> You are working in the Empire Strykers Creative Studio repository. Read `CLAUDE.md` first, then read `README.md`, `GPT-INSTRUCTIONS.md`, `skills/strykers-video-promo/SKILL.md`, `docs/WORKFLOW.md`, `docs/24-SKILL-LIBRARY.md`, and `references/stryker_agent_skill.md`. Preserve authentic source footage, player identity, brand integrity, and verified event facts. Do not add credentials or invent event details. Before changing anything, inspect the current Git status and explain the intended edit. After changing files, check the Markdown for consistency and summarize the exact files changed, verification performed, and any items marked `NEEDS APPROVAL`.

If the repository is not cloned yet, clone `git@github.com:ZZZ-CORE/strykers-skills.git`, enter the directory, and read `CLAUDE.md` before making changes.

## Suggested first Claude Code prompt

```text
Review this repository as the source of truth for the Empire Strykers Creative Studio custom GPT. Read CLAUDE.md and all linked project documents, including the proposed 24-skill library and supplied Canva/Higgsfield routing reference. Check for contradictions, missing setup information, unclear instructions, and gaps between proposed and implemented skills. Do not edit yet. Return a concise audit with recommended changes prioritized as critical, useful, or optional.
```
