#!/usr/bin/env python3
"""
Sync installed skills from upstream GitHub repositories.

Tracks a curated list of external skills and pulls updates on demand.
Never auto-installs new skills; only updates skills already in the allowlist.

Usage:
    # Show available updates
    python sync-external-skills.py --check

    # Update all tracked skills after review
    python sync-external-skills.py --apply

    # Add a skill to the tracking list
    python sync-external-skills.py --add skill-name --repo https://github.com/org/repo.git --path skills/skill-name
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLKIT_ROOT = Path(__file__).parent.parent
TRACK_FILE = TOOLKIT_ROOT / "external-skills.json"
HOME = Path.home()

AGENT_PATHS = {
    "kimi": HOME / ".kimi" / "skills",
    "codex": HOME / ".codex" / "skills",
    "claude": HOME / ".claude" / "skills",
    "cursor": HOME / ".cursor" / "skills",
    "opencode": HOME / ".config" / "opencode" / "skills",
}


def load_tracking() -> dict:
    if not TRACK_FILE.exists():
        return {"skills": []}
    return json.loads(TRACK_FILE.read_text(encoding="utf-8"))


def save_tracking(data: dict) -> None:
    TRACK_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def run(cmd: list[str], cwd: Path | None = None) -> str:
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{result.stderr}")
    return result.stdout


def clone_repo(url: str) -> Path:
    tmp = tempfile.TemporaryDirectory()
    run(["git", "clone", "--depth", "1", url, tmp.name])
    return Path(tmp.name)


def get_skill_dirs(repo_path: Path, rel_path: str) -> list[Path]:
    target = repo_path / rel_path
    if not target.exists():
        return []
    if (target / "SKILL.md").exists():
        return [target]
    return [d for d in target.iterdir() if (d / "SKILL.md").exists()]


def check_updates() -> list[dict]:
    tracking = load_tracking()
    updates: list[dict] = []

    for skill in tracking.get("skills", []):
        name = skill["name"]
        repo = skill["repo"]
        path = skill.get("path", name)
        agents = skill.get("agents", ["kimi"])

        try:
            repo_path = clone_repo(repo)
            upstream_dirs = get_skill_dirs(repo_path, path)
            if not upstream_dirs:
                print(f"⚠️ {name}: skill not found at {path} in upstream")
                continue

            upstream = upstream_dirs[0] / "SKILL.md"
            upstream_text = upstream.read_text(encoding="utf-8")

            for agent in agents:
                installed = AGENT_PATHS[agent] / name / "SKILL.md"
                if not installed.exists():
                    print(f"[WARN] {name}: not installed for {agent}")
                    continue

                installed_text = installed.read_text(encoding="utf-8")
                if installed_text != upstream_text:
                    updates.append({
                        "name": name,
                        "agent": agent,
                        "repo": repo,
                        "path": path,
                    })
                    print(f"[UPDATE] {name} ({agent}): update available")
                else:
                    print(f"[OK] {name} ({agent}): up to date")
        except Exception as e:
            print(f"[ERROR] {name}: failed to check - {e}")

    return updates


def apply_updates(updates: list[dict]) -> None:
    for update in updates:
        name = update["name"]
        agent = update["agent"]
        repo = update["repo"]
        path = update["path"]

        try:
            repo_path = clone_repo(repo)
            upstream_dirs = get_skill_dirs(repo_path, path)
            if not upstream_dirs:
                continue

            source_dir = upstream_dirs[0]
            target_dir = AGENT_PATHS[agent] / name

            if target_dir.exists():
                shutil.rmtree(target_dir)
            shutil.copytree(source_dir, target_dir)
            print(f"[OK] Updated {name} for {agent}")
        except Exception as e:
            print(f"[ERROR] Failed to update {name} for {agent}: {e}")


def add_skill(name: str, repo: str, path: str, agents: list[str]) -> None:
    tracking = load_tracking()
    for skill in tracking["skills"]:
        if skill["name"] == name:
            print(f"Skill {name} already tracked")
            return

    tracking["skills"].append({
        "name": name,
        "repo": repo,
        "path": path,
        "agents": agents,
    })
    save_tracking(tracking)
    print(f"Added {name} to tracking list")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync external agent skills")
    parser.add_argument("--check", action="store_true", help="Check for available updates")
    parser.add_argument("--apply", action="store_true", help="Apply available updates")
    parser.add_argument("--add", help="Add a skill to tracking")
    parser.add_argument("--repo", help="GitHub repo URL for --add")
    parser.add_argument("--path", help="Relative path in repo for --add")
    parser.add_argument("--agents", nargs="+", default=["kimi"], help="Target agents for --add")
    args = parser.parse_args()

    if args.add:
        if not args.repo or not args.path:
            print("--add requires --repo and --path", file=sys.stderr)
            return 1
        add_skill(args.add, args.repo, args.path, args.agents)
        return 0

    if args.check:
        updates = check_updates()
        print(f"\n{len(updates)} update(s) available")
        return 0

    if args.apply:
        updates = check_updates()
        if not updates:
            print("No updates to apply")
            return 0
        print(f"\nApplying {len(updates)} update(s)...")
        apply_updates(updates)
        return 0

    print("Use --check, --apply, or --add")
    return 1


if __name__ == "__main__":
    sys.exit(main())
