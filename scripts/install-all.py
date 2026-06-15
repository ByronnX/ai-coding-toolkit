#!/usr/bin/env python3
"""
Install ai-coding-toolkit skills and configs onto the current machine.

Supports Kimi Code CLI, Codex CLI, Claude Code, Cursor, OpenCode, etc.
"""

from __future__ import annotations

import argparse
import os
import platform
import shutil
import sys
from pathlib import Path

HOME = Path.home()

AGENT_DIRS = {
    "kimi": HOME / ".kimi" / "skills",
    "codex": HOME / ".codex" / "skills",
    "claude": HOME / ".claude" / "skills",
    "cursor": HOME / ".cursor" / "skills",
    "opencode": HOME / ".config" / "opencode" / "skills",
    "gemini": HOME / ".gemini" / "skills",
    "copilot": HOME / ".copilot" / "skills",
    "windsurf": HOME / ".codeium" / "windsurf" / "skills",
}

GLOBAL_CONFIG = HOME / ".ai-coding-toolkit"


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def find_leaf_skills(root: Path) -> list[Path]:
    """Find all directories containing SKILL.md under root."""
    skills: list[Path] = []
    if not root.exists():
        return skills
    for dirpath, dirnames, filenames in os.walk(root):
        p = Path(dirpath)
        if "SKILL.md" in filenames:
            skills.append(p)
            dirnames.clear()  # Don't recurse into skill dirs
    return sorted(skills)


def sync_skills(toolkit_root: Path, agents: list[str], dry_run: bool) -> None:
    # Order matters: core skills take precedence over external auto-synced skills.
    # External skills that conflict with core are skipped.
    skill_sources = [
        (toolkit_root / "skills" / "core", "core"),
        (toolkit_root / "skills" / "external", "external"),
    ]

    for agent in agents:
        dest = AGENT_DIRS[agent]
        ensure_dir(dest)
        installed: set[str] = set()

        for source, source_name in skill_sources:
            for skill_dir in find_leaf_skills(source):
                name = skill_dir.name
                target = dest / name

                if name in installed:
                    print(f"Skipped {source_name}/{name}: conflicts with already-installed skill")
                    continue

                if dry_run:
                    print(f"[dry-run] would sync {name} -> {target}")
                    installed.add(name)
                    continue

                if target.exists():
                    if target.is_symlink():
                        target.unlink()
                    else:
                        shutil.rmtree(target)
                shutil.copytree(skill_dir, target)
                installed.add(name)
                print(f"Synced {agent}: {name} ({source_name})")


def install_global_symlink(toolkit_root: Path, dry_run: bool) -> None:
    if dry_run:
        print(f"[dry-run] would symlink {toolkit_root} -> {GLOBAL_CONFIG}")
        return
    if GLOBAL_CONFIG.exists() or GLOBAL_CONFIG.is_symlink():
        try:
            GLOBAL_CONFIG.unlink()
        except OSError:
            shutil.rmtree(GLOBAL_CONFIG)
    try:
        if platform.system() == "Windows":
            import _winapi
            _winapi.CreateJunction(str(toolkit_root), str(GLOBAL_CONFIG))
        else:
            GLOBAL_CONFIG.symlink_to(toolkit_root, target_is_directory=True)
        print(f"Linked {GLOBAL_CONFIG} -> {toolkit_root}")
    except Exception as e:
        print(f"Warning: could not create symlink: {e}. Copying instead.", file=sys.stderr)
        shutil.copytree(toolkit_root, GLOBAL_CONFIG)
        print(f"Copied {GLOBAL_CONFIG}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Install ai-coding-toolkit")
    parser.add_argument("--toolkit-root", default=str(Path(__file__).parent.parent), help="Path to ai-coding-toolkit")
    parser.add_argument("--agents", nargs="+", choices=list(AGENT_DIRS.keys()), default=list(AGENT_DIRS.keys()), help="Which agents to install skills for")
    parser.add_argument("--no-global-link", action="store_true", help="Do not create ~/.ai-coding-toolkit link")
    parser.add_argument("--dry-run", action="store_true", help="Print what would be done without changing files")
    args = parser.parse_args()

    toolkit_root = Path(args.toolkit_root).resolve()
    print(f"Installing from: {toolkit_root}")

    sync_skills(toolkit_root, args.agents, args.dry_run)

    if not args.no_global_link:
        install_global_symlink(toolkit_root, args.dry_run)

    print("\nDone. Restart your agent CLI to load new skill metadata.")
    print("Verify with:")
    print("  ls ~/.kimi/skills/")
    print("  ls ~/.codex/skills/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
