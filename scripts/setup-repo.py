#!/usr/bin/env python3
"""
Initialize a target repository with AI coding toolkit configs.

Usage:
    python setup-repo.py <path-to-repo>
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

CONFIGS = [
    "AGENTS.md.template",
    ".cursorrules.template",
    ".claude.md.template",
]

VSCODE_CONFIG = ".vscode/settings.json.template"


def copy_template(toolkit_root: Path, repo: Path, template_name: str, dest_name: str | None = None) -> None:
    src = toolkit_root / "configs" / template_name
    if not src.exists():
        return
    dest = repo / (dest_name or template_name.replace(".template", ""))
    if dest.exists():
        print(f"Skipping existing: {dest}")
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    print(f"Created {dest}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Setup a repository with AI coding configs")
    parser.add_argument("repo", help="Path to target repository")
    parser.add_argument("--toolkit-root", default=str(Path(__file__).parent.parent), help="Path to ai-coding-toolkit")
    args = parser.parse_args()

    toolkit_root = Path(args.toolkit_root).resolve()
    repo = Path(args.repo).resolve()

    if not repo.is_dir():
        print(f"Error: {repo} is not a directory", file=sys.stderr)
        return 1

    for config in CONFIGS:
        copy_template(toolkit_root, repo, config)

    copy_template(toolkit_root, repo, VSCODE_CONFIG, ".vscode/settings.json")

    print(f"\nInitialized {repo} with AI coding toolkit configs.")
    print("Next steps:")
    print("  1. Edit AGENTS.md to match your project")
    print("  2. Run: python3 .ai-coding-toolkit/scripts/install-all.py (if using submodule)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
