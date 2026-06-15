#!/usr/bin/env python3
"""
Automatically sync skills from upstream sources into this toolkit.

Usage:
    python sync-from-sources.py              # Full sync
    python sync-from-sources.py --dry-run    # Preview changes
    python sync-from-sources.py --source awesome-agent-skills  # Sync only one source
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

TOOLKIT_ROOT = Path(__file__).parent.parent
SOURCES_FILE = TOOLKIT_ROOT / "sources.json"
REGISTRY_FILE = TOOLKIT_ROOT / "registry.json"
SKILLS_DIR = TOOLKIT_ROOT / "skills" / "external"

# Keep core skills separate; external skills go here.
CORE_DIR = TOOLKIT_ROOT / "skills" / "core"

# Minimum quality heuristics
MIN_DESCRIPTION_LEN = 30


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def run(cmd: list[str], cwd: Path | None = None) -> str:
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{result.stderr}")
    return result.stdout.strip()


def clone_repo(url: str) -> Path:
    tmp = tempfile.TemporaryDirectory()
    run(["git", "clone", "--depth", "1", url, tmp.name])
    return Path(tmp.name)


def get_git_commit(repo_path: Path) -> str:
    return run(["git", "rev-parse", "--short", "HEAD"], cwd=repo_path)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and value:
                result[key] = value
    return result


def normalize_name(name: str) -> str:
    name = name.lower().replace("_", "-").replace(" ", "-")
    name = re.sub(r"[^a-z0-9-]", "", name)
    name = re.sub(r"-+", "-", name).strip("-")
    return name or "unnamed-skill"


def is_coding_skill(skill_dir: Path, source_config: dict) -> bool:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return False

    text = skill_file.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)
    description = meta.get("description", "")
    name = meta.get("name", skill_dir.name)

    # Basic quality gate
    if len(description) < MIN_DESCRIPTION_LEN:
        return False

    # Check excluded paths
    rel_parts = skill_dir.relative_to(skill_dir.anchor if skill_dir.is_absolute() else Path(".")).parts
    for exclude in source_config.get("exclude_paths", []):
        if exclude in rel_parts:
            return False

    # Keyword filter
    keywords = source_config.get("include_keywords", [])
    if not keywords:
        return True

    haystack = f"{name} {description} {text[:2000]}".lower()
    return any(kw.lower() in haystack for kw in keywords)


def find_all_skill_dirs(repo_path: Path, source_config: dict) -> list[Path]:
    """Find all coding-relevant skill directories in a cloned repo."""
    skills: list[Path] = []
    exclude = set(source_config.get("exclude_paths", []))

    for dirpath, dirnames, filenames in os.walk(repo_path):
        p = Path(dirpath)
        # Skip excluded dirs early
        dirnames[:] = [d for d in dirnames if d not in exclude]

        if "SKILL.md" in filenames:
            if is_coding_skill(p, source_config):
                skills.append(p)
            # Don't recurse into skill dirs
            dirnames.clear()

    return skills


def get_repo_path(source: dict) -> Path:
    """Use local clone if available; otherwise clone from remote."""
    if "local_clone" in source:
        local_path = Path(source["local_clone"])
        if not local_path.is_absolute():
            local_path = TOOLKIT_ROOT / local_path
        if local_path.exists():
            print(f"Using local clone: {local_path}")
            return local_path
        print(f"Local clone not found: {local_path}, falling back to remote")
    return clone_repo(source["repo"])


def sync_source(source: dict, dry_run: bool) -> list[dict]:
    name = source["name"]
    repo = source["repo"]
    print(f"\n=== Syncing source: {name} ===")

    repo_path = get_repo_path(source)
    commit = get_git_commit(repo_path)
    print(f"Upstream commit: {commit}")

    skill_dirs = find_all_skill_dirs(repo_path, source)
    print(f"Found {len(skill_dirs)} coding skill(s)")

    synced: list[dict] = []
    target_root = SKILLS_DIR / name

    for skill_dir in skill_dirs:
        text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        skill_name = normalize_name(meta.get("name", skill_dir.name))

        target = target_root / skill_name
        synced.append({
            "name": skill_name,
            "source": name,
            "source_repo": repo,
            "source_commit": commit,
            "description": meta.get("description", ""),
            "synced_at": datetime.now(timezone.utc).isoformat(),
        })

        if dry_run:
            print(f"  [dry-run] would sync {skill_name}")
            continue

        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(skill_dir, target, ignore=shutil.ignore_patterns(".git"))
        print(f"  Synced {skill_name}")

    return synced


def clean_removed(registry: dict, dry_run: bool) -> None:
    """Remove external skill dirs that are no longer in registry."""
    registered = {
        (entry["source"], entry["name"])
        for entry in registry.get("skills", [])
    }

    if not SKILLS_DIR.exists():
        return

    for source_dir in SKILLS_DIR.iterdir():
        if not source_dir.is_dir():
            continue
        for skill_dir in source_dir.iterdir():
            if not skill_dir.is_dir():
                continue
            key = (source_dir.name, skill_dir.name)
            if key not in registered:
                if dry_run:
                    print(f"  [dry-run] would remove orphaned {key}")
                else:
                    shutil.rmtree(skill_dir)
                    print(f"  Removed orphaned {key}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync external skills from upstream sources")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without applying")
    parser.add_argument("--source", help="Sync only one source by name")
    args = parser.parse_args()

    config = load_json(SOURCES_FILE)
    registry = load_json(REGISTRY_FILE)

    sources = config.get("sources", [])
    if args.source:
        sources = [s for s in sources if s["name"] == args.source and s.get("enabled", True)]
        if not sources:
            print(f"Source not found or disabled: {args.source}", file=sys.stderr)
            return 1
    else:
        sources = [s for s in sources if s.get("enabled", True)]

    new_entries: list[dict] = []
    for source in sources:
        try:
            entries = sync_source(source, args.dry_run)
            new_entries.extend(entries)
        except Exception as e:
            print(f"[ERROR] Failed to sync {source['name']}: {e}", file=sys.stderr)
            # Continue with other sources

    if not args.dry_run:
        registry["updated_at"] = datetime.now(timezone.utc).isoformat()
        registry["skills"] = new_entries
        save_json(REGISTRY_FILE, registry)
        clean_removed(registry, args.dry_run)
        print(f"\n[OK] Synced {len(new_entries)} skills. Registry saved to {REGISTRY_FILE}")
    else:
        print(f"\n[dry-run] Would sync {len(new_entries)} skills.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
