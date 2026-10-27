#!/usr/bin/env python3
"""Rebuilds gpt/knowledge/ (Brand Kit, skills, workflow, roster, schedule), roster/ROSTER.md, and schedule/SCHEDULE.md.

Run from anywhere after editing any skill: python3 scripts/build-gpt-knowledge.py
"""
import collections
import csv
import datetime
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "gpt" / "knowledge"
ORIGINAL_VIDEO_SKILL = ROOT / "strykers-creative-studio-gpt/skills/strykers-video-promo/SKILL.md"
WORKFLOW = ROOT / "strykers-creative-studio-gpt/docs/WORKFLOW.md"
BRAND_KIT = ROOT / "brand-kit/BRAND-KIT.md"
ROSTER_TSV = ROOT / "roster/strykers-players.tsv"
ROSTER_MD = ROOT / "roster/ROSTER.md"
SCHEDULE_TSV = ROOT / "schedule/strykers-games.tsv"
SCHEDULE_MD = ROOT / "schedule/SCHEDULE.md"

CATEGORIES = [
    ("brand", "01-strykers-brand.md", "Brand"),
    ("images", "02-strykers-images.md", "Images and Graphics"),
    ("integrations", "03-strykers-integrations.md", "Canva and Higgsfield"),
    ("video", "04-strykers-video.md", "Video"),
    ("marketing", "05-strykers-marketing.md", "Marketing"),
    ("operations", "06-strykers-operations.md", "Team Operations"),
]

ORIGINAL_NOTE = (
    "> Original skill from the Strykers Creative Studio GPT. Its example on-screen lines "
    "(\"TWO NATIONS. / ONE RIVALRY.\", \"USA VS MÉXICO.\", \"THE RIVALRY RETURNS.\", "
    "\"PICK A SIDE. / GET YOUR TICKETS.\") were written for the USA vs Mexico pre-season event "
    "(PRE-001, Nov 8, 2026, in 09-strykers-schedule.md). For any other game, replace them with "
    "approved copy for that game. Its mention of red "
    "and green treatments is overridden by the Brand Kit, which allows only the seven official "
    "colors.\n"
)


def demote(body):
    """Push every Markdown heading down one level, leaving code blocks alone."""
    lines, in_code = [], False
    for line in body.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        elif not in_code and line.startswith("#"):
            line = "#" + line
        lines.append(line)
    return "\n".join(lines).strip() + "\n"


def section(path, note=""):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\nname: (.+)\ndescription: (.+)\n---\n(.*)", text, re.S)
    name, description, body = m.groups()
    body = demote(body)
    title, rest = body.split("\n", 1)
    return f"{title} (`{name}`)\n\n**Use when:** {description}\n\n{note}{rest.lstrip()}"


ROSTER_RULES = """\
# Empire Strykers Player Roster

Generated from `roster/strykers-players.tsv` (the team's roster file) by `scripts/build-gpt-knowledge.py`. Edit the TSV, not this file.

## Rules for using the roster

- **Spell names exactly as listed, including accents** (for example Marco Fabián, Steven Chávez). Use a nickname only where one is listed.
- **Jersey numbers are TBD for every player.** Never invent or guess a number. Use `[NUMBER]` marked NEEDS APPROVAL until the team confirms it.
- **Notes (stats, awards, contracts, past teams) come from the team.** Label them USER-SUPPLIED (team roster). Stats change every season, so confirm current numbers before publishing.
- **Only feature people on this roster as current players.** If a name isn't here, check with the team first.
- Robert Palmer is a player-coach and the Head Coach for 2026-27.
- Player photos and footage must show the real player, unaltered (see the Player Image Integrity skill).

## Roster ({count} players)

| ID | Name | Nickname | Position | Nationality | Jersey # | Notes |
| --- | --- | --- | --- | --- | --- | --- |
"""


def build_roster():
    with ROSTER_TSV.open(encoding="utf-8", newline="") as f:
        players = list(csv.DictReader(f, delimiter="\t"))
    rows = [
        "| " + " | ".join(p[k].strip().replace("|", "/") for k in
                          ("player_id", "name", "nickname", "position", "nationality", "jersey_number", "notes")) + " |"
        for p in players
    ]
    ROSTER_MD.write_text(ROSTER_RULES.format(count=len(players)) + "\n".join(rows) + "\n", encoding="utf-8")


SCHEDULE_RULES = """\
# Empire Strykers Game Schedule

Generated from `schedule/strykers-games.tsv` (the team's schedule file) by `scripts/build-gpt-knowledge.py`. Edit the TSV, not this file.

## Rules for using the schedule

- **Label schedule details USER-SUPPLIED (team schedule).** Schedules change: before publishing, confirm the date, time, and venue on the official site (https://www.theempirestrykers.com/) and mark anything unconfirmed NEEDS APPROVAL.
- **All times are Pacific** (PST until early March, PDT from March 14, 2027), including away games. Say "PT" in copy; convert to another time zone only if asked.
- **Matchups are written visitor first, home team second.** For home games the opponent is listed first (for example "San Diego Sockers vs Empire Strykers" is a home game at Toyota Arena). Use the Home/Away column, not the word order, to decide.
- **Never invent a time.** "TBD" stays `[TIME]` marked NEEDS APPROVAL.
- **Home games are at Toyota Arena**, 4000 E Ontario Center Pkwy, Ontario, CA 91764; parking $15 per car (https://www.toyota-arena.com/plan-your-visit/parking-guide). Use the Gameday hashtags from the Brand Kit, including #ToyotaArena, for home games.
- **Tickets:** the ticket link for every game is https://www.theempirestrykers.com/. Only use a promo code where one is listed.
- **PRE-001 (USA vs Mexico, Nov 8, 2026)** is a special pre-season international event at Toyota Arena, not a regular-season Strykers game. Promo code OPENER26. Its time is TBD.
{duplicates}
## Schedule ({count} games: {home} home, {away} away)

| Game ID | Date | Day | Time (Pacific) | Matchup (visitor vs home) | Home/Away | Venue | Promo code | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
"""


def build_schedule():
    with SCHEDULE_TSV.open(encoding="utf-8", newline="") as f:
        games = [{k.strip(): (v or "").strip() for k, v in row.items()} for row in csv.DictReader(f, delimiter="\t")]
    counts = collections.Counter(g["game_id"] for g in games)
    dups = sorted(i for i, n in counts.items() if n > 1)
    duplicates = ""
    if dups:
        duplicates = ("- **Repeated game IDs in the source file:** " + ", ".join(dups)
                      + ". Each is used for two different games; identify games by date and matchup, "
                      "and ask the team to correct the IDs.\n")
    rows = []
    for g in games:
        day = datetime.datetime.strptime(g["date"], "%m/%d/%Y").strftime("%a")
        cells = [g["game_id"], g["date"], day, g["time"], g["opponent"], g["home_away"].title(),
                 g["venue"], g["promo_code"] or "—", g["notes"] or "—"]
        rows.append("| " + " | ".join(c.replace("|", "/") for c in cells) + " |")
    home = sum(g["home_away"].lower() == "home" for g in games)
    SCHEDULE_MD.write_text(
        SCHEDULE_RULES.format(duplicates=duplicates, count=len(games), home=home, away=len(games) - home)
        + "\n".join(rows) + "\n",
        encoding="utf-8",
    )


def skill_number(path):
    m = re.search(r"skill (\d\d) in", path.read_text(encoding="utf-8"))
    return int(m.group(1)) if m else 0


def main():
    build_roster()
    build_schedule()
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.md"):
        old.unlink()
    (OUT / "00-strykers-brand-kit.md").write_text(BRAND_KIT.read_text(encoding="utf-8"), encoding="utf-8")
    shutil.copyfile(BRAND_KIT.with_name("ES_Official_Brand_Kit_PUB.pdf"), OUT / "ES_Official_Brand_Kit_PUB.pdf")
    for folder, filename, label in CATEGORIES:
        skills = sorted((ROOT / "skills" / folder).glob("*/SKILL.md"), key=skill_number)
        parts = []
        if folder == "video":
            parts.append(section(ORIGINAL_VIDEO_SKILL, ORIGINAL_NOTE + "\n"))
        parts += [section(p) for p in skills]
        header = (
            f"# Empire Strykers Creative Studio — {label} Skills\n\n"
            "Knowledge file for the Strykers Creative Studio GPT. Generated from the "
            "`SKILL.md` files in the strykers-skills repository by "
            "`scripts/build-gpt-knowledge.py`; edit the skills there, not this file.\n\n"
        )
        (OUT / filename).write_text(header + "\n---\n\n".join(parts), encoding="utf-8")
    workflow = WORKFLOW.read_text(encoding="utf-8")
    (OUT / "07-strykers-workflow.md").write_text(
        "# Empire Strykers Creative Studio — Video Production Workflow\n\n"
        "Knowledge file for the Strykers Creative Studio GPT, copied from the original GPT's "
        "`docs/WORKFLOW.md`.\n\n" + demote(workflow),
        encoding="utf-8",
    )
    shutil.copyfile(ROSTER_MD, OUT / "08-strykers-roster.md")
    shutil.copyfile(SCHEDULE_MD, OUT / "09-strykers-schedule.md")
    for f in sorted(OUT.glob("*.md")) + [OUT / "ES_Official_Brand_Kit_PUB.pdf"]:
        print(f"{f.relative_to(ROOT)}  {f.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
