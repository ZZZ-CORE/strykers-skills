#!/usr/bin/env bash
# Rebuilds downloads/<skill>.zip for every SKILL.md folder.
# Run from the repository root after editing any skill: scripts/build-skill-zips.sh
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf downloads && mkdir downloads
find skills strykers-creative-studio-gpt/skills -name SKILL.md | sort | while read -r f; do
  dir=$(dirname "$f")
  name=$(basename "$dir")
  (cd "$(dirname "$dir")" && zip -qrX "$OLDPWD/downloads/$name.zip" "$name")
done
ls downloads | wc -l | xargs echo "Built zips:"
