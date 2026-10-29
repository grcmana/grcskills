#!/usr/bin/env python3
"""Sync shared knowledge into each skill's references/ folder, and validate skills.

Shared knowledge lives once in knowledge/. Each skill installed via `npx skills add`
must be self-contained, so the relevant files are copied into skills/<name>/references/.

Usage:
  python3 scripts/sync_references.py          # sync + validate
  python3 scripts/sync_references.py --check  # fail if anything is out of sync (CI)
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE = ROOT / "knowledge"
SKILLS = ROOT / "skills"

FW = ["frameworks/iso27001.md", "frameworks/soc2.md", "frameworks/cyber-essentials.md",
      "frameworks/gdpr.md", "frameworks/iso42001.md"]
BASE = ["methodology/grc-workspace.md"]

MAP: dict[str, list[str]] = {
    "company-context": BASE + ["frameworks/crosswalk.md"] + FW,
    "risk-register": BASE + ["methodology/risk-methodology.md", "frameworks/crosswalk.md"],
    "ai-impact-assessment": BASE + ["frameworks/iso42001.md", "frameworks/gdpr.md",
                                    "methodology/risk-methodology.md"],
    "policy-writer": BASE + ["methodology/writing-standards.md", "frameworks/crosswalk.md"] + FW,
    "policy-gap-review": BASE + ["methodology/writing-standards.md", "frameworks/crosswalk.md"] + FW,
    "audit-readiness": BASE + ["methodology/evidence-standards.md", "frameworks/crosswalk.md"] + FW,
    "evidence-request-list": BASE + ["methodology/evidence-standards.md", "frameworks/crosswalk.md"] + FW,
    "evidence-review": BASE + ["methodology/evidence-standards.md", "frameworks/crosswalk.md"],
    "cyber-essentials-scoping": BASE + ["frameworks/cyber-essentials.md"],
    "dpia": BASE + ["frameworks/gdpr.md", "methodology/risk-methodology.md"],
    "grc-status": BASE + ["methodology/risk-methodology.md", "methodology/evidence-standards.md"],
}

# Skill-specific references that are authored inside the skill (not synced).
LOCAL_REFS = {"policy-writer": ["policy-catalogue.md"]}
# policy-gap-review reuses the policy catalogue.
SHARED_LOCAL = {"policy-gap-review": [("policy-writer", "policy-catalogue.md")]}

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def frontmatter(text: str) -> dict[str, str]:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def main(check: bool) -> int:
    errors: list[str] = []
    drift: list[str] = []
    skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())

    for sd in skill_dirs:
        name = sd.name
        skill_md = sd / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"{name}: missing SKILL.md")
            continue
        fm = frontmatter(skill_md.read_text())
        if fm.get("name") != name:
            errors.append(f"{name}: frontmatter name '{fm.get('name')}' must match folder")
        if not NAME_RE.match(name) or len(name) > 64:
            errors.append(f"{name}: invalid skill name")
        desc = fm.get("description", "")
        if not desc or len(desc) > 1024:
            errors.append(f"{name}: description missing or > 1024 chars ({len(desc)})")
        if name not in MAP:
            errors.append(f"{name}: not registered in scripts/sync_references.py MAP")
            continue

        refs = sd / "references"
        refs.mkdir(exist_ok=True)
        wanted = {}
        for rel in MAP[name]:
            wanted[Path(rel).name] = KNOWLEDGE / rel
        for src_skill, fname in SHARED_LOCAL.get(name, []):
            wanted[fname] = SKILLS / src_skill / "references" / fname

        for fname, src in wanted.items():
            dst = refs / fname
            if not src.exists():
                errors.append(f"{name}: source missing {src}")
                continue
            if not dst.exists() or dst.read_bytes() != src.read_bytes():
                drift.append(f"{name}/references/{fname}")
                if not check:
                    shutil.copyfile(src, dst)

        allowed = set(wanted) | set(LOCAL_REFS.get(name, []))
        for f in refs.iterdir():
            if f.name not in allowed:
                drift.append(f"{name}/references/{f.name} (stale)")
                if not check:
                    f.unlink()

        # every references/ or assets/ path mentioned in SKILL.md must exist
        body = skill_md.read_text()
        for m in re.finditer(r"`((?:references|assets)/[\w./-]+)`", body):
            if not (sd / m.group(1)).exists() and not (check is False and Path(m.group(1)).name in wanted):
                errors.append(f"{name}: SKILL.md references missing file {m.group(1)}")

    for e in errors:
        print(f"ERROR  {e}")
    if check and drift:
        for d in drift:
            print(f"DRIFT  {d}")
        print("Run: python3 scripts/sync_references.py")
        return 1
    if not check:
        for d in drift:
            print(f"synced {d}")
    print(f"{len(skill_dirs)} skills checked, {len(errors)} errors, {len(drift)} {'drifted' if check else 'synced'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
