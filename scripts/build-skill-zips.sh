#!/usr/bin/env bash
# Rebuilds downloads/<skill>.zip for every SKILL.md folder, adding brand-kit/BRAND-KIT.md to each.
# Run from the repository root after editing any skill: scripts/build-skill-zips.sh
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf downloads && mkdir downloads
find skills strykers-creative-studio-gpt/skills -name SKILL.md | sort | while read -r f; do
  dir=$(dirname "$f")
  name=$(basename "$dir")
  (cd "$(dirname "$dir")" && zip -qrX "$OLDPWD/downloads/$name.zip" "$name")
  # Every skill ships with the Brand Kit text so it works on its own.
  tmp=$(mktemp -d)
  mkdir "$tmp/$name" && cp brand-kit/BRAND-KIT.md "$tmp/$name/BRAND-KIT.md"
  (cd "$tmp" && zip -qX "$OLDPWD/downloads/$name.zip" "$name/BRAND-KIT.md")
  rm -rf "$tmp"
done
ls downloads | wc -l | xargs echo "Built zips:"
