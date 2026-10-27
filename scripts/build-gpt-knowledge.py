#!/usr/bin/env python3
"""Rebuilds gpt/knowledge/: the Brand Kit text, then one Markdown file per skill category.

Run from anywhere after editing any skill: python3 scripts/build-gpt-knowledge.py
"""
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "gpt" / "knowledge"
ORIGINAL_VIDEO_SKILL = ROOT / "strykers-creative-studio-gpt/skills/strykers-video-promo/SKILL.md"
WORKFLOW = ROOT / "strykers-creative-studio-gpt/docs/WORKFLOW.md"
BRAND_KIT = ROOT / "brand-kit/BRAND-KIT.md"

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
    "\"PICK A SIDE. / GET YOUR TICKETS.\") came from one rivalry campaign: treat them as "
    "examples and replace them with approved copy for the current event. Its mention of red "
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


def skill_number(path):
    m = re.search(r"skill (\d\d) in", path.read_text(encoding="utf-8"))
    return int(m.group(1)) if m else 0


def main():
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
    for f in sorted(OUT.glob("*.md")) + [OUT / "ES_Official_Brand_Kit_PUB.pdf"]:
        print(f"{f.relative_to(ROOT)}  {f.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
