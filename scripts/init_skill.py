#!/usr/bin/env python3
"""
Initialize a new SKILL.md from template.

Usage:
    python init_skill.py <skill-name> [--path skills/...]

Example:
    python init_skill.py api-rate-limiting --path skills/02-development
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MAX_NAME_LEN = 64
ALLOWED = set("abcdefghijklmnopqrstuvwxyz0123456789-")

SKILL_TEMPLATE = """---
name: {name}
description: [TODO: What this skill does and exactly when to trigger it. Include task keywords users will say.]
---

# {title}

## Overview

[TODO: 1-2 sentences on what this skill enables.]

## When to use

- [TODO: Trigger condition 1]
- [TODO: Trigger condition 2]

## Workflow

1. [TODO: Step 1]
2. [TODO: Step 2]
3. [TODO: Step 3]

## Output format

[TODO: Describe the expected output structure.]

## Notes

- [TODO: Prerequisites, limitations, or cross-platform notes.]
"""


def validate_name(name: str) -> None:
    if not name:
        raise ValueError("Skill name cannot be empty")
    if len(name) > MAX_NAME_LEN:
        raise ValueError(f"Skill name must be <= {MAX_NAME_LEN} chars")
    if name[0] == "-" or name[-1] == "-":
        raise ValueError("Skill name cannot start or end with a hyphen")
    if not set(name).issubset(ALLOWED):
        invalid = set(name) - ALLOWED
        raise ValueError(f"Invalid characters in skill name: {sorted(invalid)}")


def title_case(name: str) -> str:
    return " ".join(part.capitalize() for part in name.split("-"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a new skill from template")
    parser.add_argument("name", help="Skill name (kebab-case)")
    parser.add_argument("--path", default="skills", help="Parent directory for the skill")
    args = parser.parse_args()

    try:
        validate_name(args.name)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    parent = Path(args.path)
    skill_dir = parent / args.name
    if skill_dir.exists():
        print(f"Error: {skill_dir} already exists", file=sys.stderr)
        return 1

    skill_dir.mkdir(parents=True)
    skill_file = skill_dir / "SKILL.md"
    skill_file.write_text(
        SKILL_TEMPLATE.format(name=args.name, title=title_case(args.name)),
        encoding="utf-8",
    )

    print(f"Created {skill_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
