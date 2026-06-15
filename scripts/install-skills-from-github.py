#!/usr/bin/env python3
"""
Batch install agent skills from a GitHub repository or local path to multiple agents.

Supports: Kimi, Codex, Claude Code, Cursor, OpenCode, Gemini CLI, GitHub Copilot, Windsurf.

Usage:
    # Install all skills from a GitHub repo to all detected agents
    python install-skills-from-github.py https://github.com/VoltAgent/awesome-agent-skills.git

    # Install to specific agents only
    python install-skills-from-github.py https://github.com/VoltAgent/awesome-agent-skills.git --agents kimi cursor

    # Install from local directory
    python install-skills-from-github.py ./awesome-agent-skills

    # Install only skills matching a pattern
    python install-skills-from-github.py ./awesome-agent-skills --filter "code|review|test"

    # Dry run
    python install-skills-from-github.py ./awesome-agent-skills --dry-run
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HOME = Path.home()

AGENT_PATHS = {
    "kimi": HOME / ".kimi" / "skills",
    "codex": HOME / ".codex" / "skills",
    "claude": HOME / ".claude" / "skills",
    "cursor": HOME / ".cursor" / "skills",
    "opencode": HOME / ".config" / "opencode" / "skills",
    "gemini": HOME / ".gemini" / "skills",
    "copilot": HOME / ".copilot" / "skills",
    "windsurf": HOME / ".codeium" / "windsurf" / "skills",
}

# Some agents also support project-level paths, but we focus on global install here.


def is_skill_dir(path: Path) -> bool:
    return path.is_dir() and (path / "SKILL.md").exists()


def find_skill_folders(root: Path) -> list[Path]:
    """Find all leaf directories containing SKILL.md, flattening nested structures."""
    skills: list[Path] = []

    # Direct children first (typical structure: repo/skills/<name>/SKILL.md)
    for child in sorted(root.iterdir()):
        if is_skill_dir(child):
            skills.append(child)
        elif child.is_dir():
            # Recurse one more level for category-organized repos
            for grandchild in sorted(child.iterdir()):
                if is_skill_dir(grandchild):
                    skills.append(grandchild)

    # Also handle deeply nested cases by walking until we find SKILL.md
    # but avoid returning parent directories that contain sub-skills.
    if not skills:
        for dirpath, dirnames, filenames in os.walk(root):
            p = Path(dirpath)
            if "SKILL.md" in filenames:
                # Ensure this isn't a parent of another skill dir
                if not any(is_skill_dir(d) for d in p.iterdir() if d.is_dir()):
                    skills.append(p)

    return sorted(set(skills))


def clone_repo(url: str, dest: Path) -> None:
    print(f"Cloning {url} ...")
    subprocess.run(["git", "clone", "--depth", "1", url, str(dest)], check=True)


def normalize_skill_name(name: str) -> str:
    """Normalize directory name to kebab-case, lowercase, alphanumeric + hyphen."""
    name = name.lower().replace("_", "-").replace(" ", "-")
    name = re.sub(r"[^a-z0-9-]", "", name)
    name = re.sub(r"-+", "-", name).strip("-")
    return name or "unnamed-skill"


def install_skill(skill_src: Path, agent_dir: Path, dry_run: bool) -> str | None:
    name = normalize_skill_name(skill_src.name)
    target = agent_dir / name

    if dry_run:
        return f"[dry-run] would install {name} -> {target}"

    agent_dir.mkdir(parents=True, exist_ok=True)

    if target.exists():
        if target.is_symlink():
            target.unlink()
        else:
            shutil.rmtree(target)

    shutil.copytree(skill_src, target)
    return f"Installed {name} -> {target}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Batch install agent skills")
    parser.add_argument("source", help="GitHub URL or local path to skill repository")
    parser.add_argument("--agents", nargs="+", choices=list(AGENT_PATHS.keys()), help="Target agents")
    parser.add_argument("--filter", help="Regex filter on skill name")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be installed")
    parser.add_argument("--keep-clone", action="store_true", help="Keep cloned repository (default: temp dir)")
    args = parser.parse_args()

    source = args.source
    is_url = source.startswith(("http://", "https://", "git@"))

    if is_url:
        if args.keep_clone:
            clone_dir = Path(".") / Path(source).stem
            clone_dir.mkdir(exist_ok=True)
        else:
            tmp = tempfile.TemporaryDirectory()
            clone_dir = Path(tmp.name)
        clone_repo(source, clone_dir)
        root = clone_dir
    else:
        root = Path(source).resolve()
        if not root.exists():
            print(f"Error: path not found: {root}", file=sys.stderr)
            return 1

    skill_folders = find_skill_folders(root)
    if not skill_folders:
        print(f"No SKILL.md folders found in {root}", file=sys.stderr)
        return 1

    if args.filter:
        pattern = re.compile(args.filter, re.IGNORECASE)
        skill_folders = [s for s in skill_folders if pattern.search(s.name)]

    agents = args.agents or list(AGENT_PATHS.keys())

    print(f"Found {len(skill_folders)} skill(s) in {root}")
    print(f"Target agents: {', '.join(agents)}\n")

    installed = 0
    for skill_src in skill_folders:
        print(f"Skill: {skill_src.name}")
        for agent in agents:
            agent_dir = AGENT_PATHS[agent]
            result = install_skill(skill_src, agent_dir, args.dry_run)
            if result:
                print(f"  {result}")
                installed += 1
        print()

    action = "Would install" if args.dry_run else "Installed"
    print(f"{action} {installed} skill-instance(s) across {len(agents)} agent(s).")
    print("Restart your agent CLI to load new skill metadata.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
