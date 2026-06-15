#!/usr/bin/env python3
"""
Validate all SKILL.md files in the toolkit.

Checks:
- Required YAML frontmatter (name, description)
- name matches directory name
- No README/CHANGELOG inside skill folders
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).parent.parent / "skills"
REQUIRED_KEYS = {"name", "description"}
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_simple_yaml(text: str) -> dict[str, str]:
    """Parse simple key: value YAML lines. Does not support nested structures."""
    result: dict[str, str] = {}
    for line in text.splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and value:
            result[key] = value
    return result


def validate_skill(skill_file: Path) -> list[str]:
    errors: list[str] = []
    rel = skill_file.relative_to(SKILL_ROOT)
    text = skill_file.read_text(encoding="utf-8")

    match = FRONTMATTER_RE.match(text)
    if not match:
        errors.append(f"{rel}: missing YAML frontmatter")
        return errors

    meta = parse_simple_yaml(match.group(1))
    missing = REQUIRED_KEYS - set(meta.keys())
    if missing:
        errors.append(f"{rel}: missing frontmatter keys: {sorted(missing)}")

    name = meta.get("name")
    if name:
        expected_dir = skill_file.parent.name
        if name != expected_dir:
            errors.append(f"{rel}: name '{name}' does not match directory '{expected_dir}'")

    for forbidden in ("README.md", "CHANGELOG.md", "INSTALLATION_GUIDE.md", "QUICK_REFERENCE.md"):
        if (skill_file.parent / forbidden).exists():
            errors.append(f"{rel}: forbidden file '{forbidden}' inside skill folder")

    return errors


def main() -> int:
    if not SKILL_ROOT.exists():
        print(f"Error: skill root not found: {SKILL_ROOT}", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    skills = sorted(SKILL_ROOT.rglob("SKILL.md"))
    for skill_file in skills:
        all_errors.extend(validate_skill(skill_file))

    if all_errors:
        print("Validation failed:", file=sys.stderr)
        for err in all_errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"All {len(skills)} skills validated successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
