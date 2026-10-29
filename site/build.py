#!/usr/bin/env python3
"""Build the grcskills.io landing page from skills/*/SKILL.md.

Usage: python3 site/build.py   -> writes site/dist/index.html
Deploy site/dist/ to any static host (Vercel, Netlify, Cloudflare Pages, GitHub Pages).
Set NEWSLETTER_ACTION (env var) to your newsletter provider's form endpoint.
"""
from __future__ import annotations

import html
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
OUT = ROOT / "site" / "dist"
TEMPLATE = ROOT / "site" / "template.html"

FRAMEWORKS = {
    "ISO 27001": r"ISO 27001|ISO/IEC 27001",
    "SOC 2": r"SOC 2",
    "Cyber Essentials": r"Cyber Essentials",
    "GDPR": r"GDPR",
    "ISO 42001": r"ISO 42001|ISO/IEC 42001",
}
COLLECTIONS = {
    "foundations": "Foundations",
    "risk-management": "Risk management",
    "policy-management": "Policy management",
    "audit-evidence": "Audit & evidence",
    "frameworks": "Frameworks",
}
# One-line plain-English summaries for the catalogue (descriptions are written for agents).
SUMMARY = {
    "company-context": "Builds the company profile, scope and framework choice every other skill reads.",
    "grc-status": "Turns your workspace into a one-page status, board report or management review pack.",
    "risk-register": "Identifies, scores and treats your risks, with each treatment mapped to controls.",
    "ai-impact-assessment": "Inventories your AI and assesses its risks and impacts on people.",
    "policy-writer": "Recommends the policies you actually need and drafts them for your stack.",
    "policy-gap-review": "Reviews your existing policies the way an auditor would.",
    "audit-readiness": "Scores how ready you are for audit and lays out the roadmap to get there.",
    "evidence-request-list": "Plans what evidence to collect, from which system, by whom and when.",
    "evidence-review": "Checks collected evidence before your auditor sees it.",
    "cyber-essentials-scoping": "Scopes Cyber Essentials and finds the hard fails before you submit.",
    "dpia": "Screens for and drafts a GDPR data protection impact assessment.",
}


def parse(skill_md: Path) -> dict:
    text = skill_md.read_text()
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S).group(1)
    get = lambda k: (re.search(rf"^\s*{k}:\s*(.+)$", fm, re.M) or [None, ""])[1].strip()
    name, desc = get("name"), get("description")
    return {
        "name": name,
        "summary": SUMMARY.get(name, desc.split(" — ")[0][:160]),
        "collection": COLLECTIONS.get(get("collection"), "Other"),
        "version": get("version"),
        "frameworks": frameworks_for(name, desc),
    }


# Skills that are framework-agnostic, regardless of which frameworks their description names.
ALL_FRAMEWORKS = {"grc-status", "evidence-review", "risk-register", "company-context"}


def frameworks_for(name: str, desc: str) -> list[str]:
    if name in ALL_FRAMEWORKS:
        return ["All five"]
    found = [f for f, rx in FRAMEWORKS.items() if re.search(rx, desc)]
    return ["All five"] if not found or len(found) == len(FRAMEWORKS) else found


def main() -> None:
    skills = [parse(p / "SKILL.md") for p in sorted(SKILLS.iterdir()) if (p / "SKILL.md").exists()]
    order = list(COLLECTIONS.values())
    skills.sort(key=lambda s: (order.index(s["collection"]) if s["collection"] in order else 99, s["name"]))
    rows = []
    for s in skills:
        fw = "".join(f'<span class="fw">{html.escape(f)}</span>' for f in s["frameworks"])
        rows.append(
            f'<tr data-fw="{html.escape("|".join(s["frameworks"]))}">'
            f'<td class="skill"><a href="https://github.com/grcmana/grcskills/tree/main/skills/{s["name"]}">'
            f'<code>{s["name"]}</code></a><span class="coll">{html.escape(s["collection"])}</span></td>'
            f'<td>{html.escape(s["summary"])}</td><td class="fws">{fw}</td>'
            f'<td class="inst"><button class="copy small" data-copy="npx skills add grcmana/grcskills@{s["name"]}" '
            f'aria-label="Copy install command for {s["name"]}">Copy</button></td></tr>'
        )
    page = (TEMPLATE.read_text()
            .replace("{{ROWS}}", "\n".join(rows))
            .replace("{{COUNT}}", str(len(skills)))
            .replace("{{NEWSLETTER_ACTION}}", html.escape(os.environ.get("NEWSLETTER_ACTION", "#")))
            .replace("{{SKILLS_JSON}}", json.dumps([s["name"] for s in skills])))
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.html").write_text(page)
    print(f"Built {OUT / 'index.html'} with {len(skills)} skills")


if __name__ == "__main__":
    main()
