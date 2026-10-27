---
name: strykers-account-checker
description: Checks which creative tools (such as Canva and Higgsfield) are actually connected and authorized in the current AI workspace, and explains manual alternatives for those that aren't. Use before any step that depends on sending work to an outside tool, or when someone asks what's connected.
---

# Strykers Integration & Account Checker

> New draft skill (October 2026), written from skill 12 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Know what's really connected before promising anything.

## When to use

- Before a handoff to Canva, Higgsfield, or another tool.
- When the user asks "is Canva connected?"

## Steps

1. Look at the tools actually available in this session.
2. For each tool the workflow needs, try a harmless read-only action (for example, list brand kits or search designs) to confirm access.
3. Sort each into:
   - **Connected:** a read-only action succeeded.
   - **Not connected:** the tool isn't available or returned an authorization error.
   - **Unverified:** the tool exists but you couldn't confirm access.
4. For anything not connected, give the manual alternative (download the file and upload it on the tool's website).

## Rules

- Never ask for, display, or store passwords, API keys, or tokens.
- A tool appearing in a list is not proof it works; only a successful action is.

## Output

| Tool | Status (Connected / Not connected / Unverified) | Evidence | What you can do / manual alternative |
| --- | --- | --- | --- |

## Before you finish

- Every "Connected" status has a successful tool result behind it.
