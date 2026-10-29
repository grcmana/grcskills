#!/usr/bin/env python3
"""Build catalog.json from skills/*/SKILL.md frontmatter.

catalog.json is the ONLY interface between this repo and the grcskills.io website.
It's attached to each tagged release by .github/workflows/release.yml, and the website
builds from a pinned release. Contributors' text reaches the site only as data.

Usage: python3 scripts/build_catalog.py [--out dist/catalog.json] [--version v0.1.0]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRAMEWORKS = ["ISO 27001", "SOC 2", "Cyber Essentials", "GDPR", "ISO 42001"]
COLLECTIONS = {
    "foundations": "Foundations",
    "risk-management": "Risk management",
    "policy-management": "Policy management",
    "audit-evidence": "Audit & evidence",
    "frameworks": "Frameworks",
}


def field(fm: str, key: str) -> str:
    m = re.search(rf"^\s*{key}:\s*(.+)$", fm, re.M)
    return m.group(1).strip().strip('"') if m else ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "dist" / "catalog.json"))
    ap.add_argument("--version", default="dev")
    args = ap.parse_args()

    errors, skills = [], []
    for sd in sorted((ROOT / "skills").iterdir()):
        md = sd / "SKILL.md"
        if not md.exists():
            continue
        fm = re.match(r"^---\n(.*?)\n---\n", md.read_text(), re.S).group(1)
        name, summary = field(fm, "name"), field(fm, "summary")
        coll, fws = field(fm, "collection"), field(fm, "frameworks")
        if not summary or len(summary) > 140:
            errors.append(f"{name}: metadata.summary missing or > 140 chars")
        if coll not in COLLECTIONS:
            errors.append(f"{name}: metadata.collection must be one of {list(COLLECTIONS)}")
        fw_list = FRAMEWORKS if fws == "all" else [f.strip() for f in fws.split(",") if f.strip()]
        bad = [f for f in fw_list if f not in FRAMEWORKS]
        if not fw_list or bad:
            errors.append(f"{name}: metadata.frameworks must be 'all' or a comma list of {FRAMEWORKS}")
        skills.append({
            "name": name,
            "summary": summary,
            "description": field(fm, "description"),
            "collection": COLLECTIONS.get(coll, coll),
            "frameworks": fw_list,
            "all_frameworks": fws == "all",
            "version": field(fm, "version"),
            "path": f"skills/{name}",
            "install": f"npx skills add grcmana/grcskills@{name}",
        })

    for e in errors:
        print(f"ERROR  {e}")
    if errors:
        return 1
    order = list(COLLECTIONS.values())
    skills.sort(key=lambda s: (order.index(s["collection"]), s["name"]))
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({
        "schema": 1,
        "release": args.version,
        "repo": "grcmana/grcskills",
        "install_all": "npx skills add grcmana/grcskills",
        "frameworks": FRAMEWORKS,
        "collections": order,
        "skills": skills,
    }, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {out} ({len(skills)} skills, release {args.version})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
