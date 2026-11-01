#!/usr/bin/env python3
"""Build catalog.json from the repo's content, and validate that content.

catalog.json is the ONLY interface between this repo and the grcskills.io website.
It's attached to each tagged release by .github/workflows/release.yml, and the website
builds from a pinned release. Contributors' text reaches the site only as data, and
the site must sanitise any Markdown it renders (see docs/catalog-schema-2.md).

Sources:
  skills/<name>/SKILL.md     frontmatter metadata (agent-facing)
  skills/<name>/README.md    human-facing skill page (800-1500 words, fixed headings)
  collections/<slug>.md      category pages: title, order, intro
  contributors/<handle>.md   opt-in contributor profiles, keyed by GitHub handle

Schema 2 is a strict superset of schema 1: every schema-1 field is unchanged.

Usage: python3 scripts/build_catalog.py [--out dist/catalog.json] [--version v0.1.0]
                                        [--require-readmes]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRAMEWORKS = ["ISO 27001", "SOC 2", "Cyber Essentials", "GDPR", "ISO 42001"]

# The skill page contract. H2 headings, in this order. The site may rely on them.
README_SECTIONS = [
    "What it does",
    "Who it's for",
    "When to use it",
    "How it works",
    "What you get",
    "Worked example",
    "Frameworks covered",
    "Guardrails",
    "FAQ",
    "Related skills",
]
README_WORDS = (800, 1500)
COLLECTION_WORDS = (100, 400)
BIO_WORDS = (20, 300)
MIN_FAQ = 3

# Contributor profiles are public personal data, so only these fields are allowed.
CONTRIBUTOR_FIELDS = {"name", "github", "kind", "role", "website", "linkedin"}
CONTRIBUTOR_KINDS = {"person", "organisation"}
HANDLE_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,38})$")
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


# ---------------------------------------------------------------- helpers
def split_frontmatter(text: str) -> tuple[str, str]:
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    return (m.group(1), text[m.end():]) if m else ("", text)


def field(fm: str, key: str) -> str:
    m = re.search(rf"^\s*{key}:\s*(.+)$", fm, re.M)
    return m.group(1).strip().strip('"').strip("'") if m else ""


def top_level_fields(fm: str) -> dict[str, str]:
    out = {}
    for line in fm.splitlines():
        if line and not line.startswith((" ", "#")) and ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def strip_code(md: str) -> str:
    md = re.sub(r"```.*?```", " ", md, flags=re.S)
    return re.sub(r"`[^`\n]*`", " code ", md)


def word_count(md: str) -> int:
    text = strip_code(md)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # keep link text only
    text = re.sub(r"[#>*_|\-]+", " ", text)
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’.:/]*", text))


def raw_html(md: str) -> list[str]:
    return re.findall(r"<[A-Za-z/!][^>\n]*>", strip_code(md))


# ---------------------------------------------------------------- loaders
def load_collections(errors: list[str]) -> list[dict]:
    cols = []
    for f in sorted((ROOT / "collections").glob("*.md")):
        fm, body = split_frontmatter(f.read_text())
        slug, title, order = f.stem, field(fm, "title"), field(fm, "order")
        where = f"collections/{f.name}"
        if not SLUG_RE.match(slug):
            errors.append(f"{where}: file name must be a lowercase-hyphen slug")
        if not title:
            errors.append(f"{where}: frontmatter 'title' is required")
        if not order.isdigit():
            errors.append(f"{where}: frontmatter 'order' must be a whole number")
        n = word_count(body)
        if not COLLECTION_WORDS[0] <= n <= COLLECTION_WORDS[1]:
            errors.append(f"{where}: intro is {n} words; must be {COLLECTION_WORDS[0]}-{COLLECTION_WORDS[1]}")
        if raw_html(body):
            errors.append(f"{where}: raw HTML is not allowed")
        cols.append({"slug": slug, "title": title, "order": int(order) if order.isdigit() else 999,
                     "intro_markdown": body.strip(), "skills": []})
    cols.sort(key=lambda c: (c["order"], c["slug"]))
    return cols


def load_contributors(errors: list[str]) -> dict[str, dict]:
    people = {}
    for f in sorted((ROOT / "contributors").glob("*.md")):
        if f.name.upper() == "README.MD":
            continue
        where = f"contributors/{f.name}"
        fm, body = split_frontmatter(f.read_text())
        fields = top_level_fields(fm)
        handle = f.stem
        extra = set(fields) - CONTRIBUTOR_FIELDS
        if extra:
            errors.append(f"{where}: fields not allowed: {sorted(extra)} (allowed: {sorted(CONTRIBUTOR_FIELDS)})")
        if not HANDLE_RE.match(handle):
            errors.append(f"{where}: file name must be your GitHub handle in lowercase")
        if fields.get("github", "").lower() != handle:
            errors.append(f"{where}: 'github' must match the file name")
        if not fields.get("name"):
            errors.append(f"{where}: 'name' is required")
        kind = fields.get("kind", "person")
        if kind not in CONTRIBUTOR_KINDS:
            errors.append(f"{where}: 'kind' must be one of {sorted(CONTRIBUTOR_KINDS)}")
        if len(fields.get("role", "")) > 80:
            errors.append(f"{where}: 'role' must be 80 characters or fewer")
        for k in ("website", "linkedin"):
            if fields.get(k) and not fields[k].startswith("https://"):
                errors.append(f"{where}: '{k}' must be an https:// URL")
        if fields.get("linkedin") and not fields["linkedin"].startswith("https://www.linkedin.com/"):
            errors.append(f"{where}: 'linkedin' must be a https://www.linkedin.com/ URL")
        n = word_count(body)
        if not BIO_WORDS[0] <= n <= BIO_WORDS[1]:
            errors.append(f"{where}: bio is {n} words; must be {BIO_WORDS[0]}-{BIO_WORDS[1]}")
        if raw_html(body):
            errors.append(f"{where}: raw HTML is not allowed")
        people[handle] = {
            "handle": handle,
            "name": fields.get("name", ""),
            "kind": kind,
            "role": fields.get("role", ""),
            "links": {k: fields[k] for k in ("website", "linkedin") if fields.get(k)},
            "github_url": f"https://github.com/{handle}",
            "avatar": f"https://github.com/{handle}.png",
            "bio_markdown": body.strip(),
            "skills": [],
        }
    return people


def check_readme(name: str, md: str, skill_names: set[str], errors: list[str]) -> dict:
    where = f"skills/{name}/README.md"
    lines = md.lstrip().splitlines()
    if not lines or not lines[0].startswith("# "):
        errors.append(f"{where}: must start with a '# ' title")
    h2 = re.findall(r"^## (.+?)\s*$", strip_code(md), re.M)
    if h2 != README_SECTIONS:
        errors.append(f"{where}: H2 sections must be exactly, in order: {README_SECTIONS} (found {h2})")
    n = word_count(md)
    if not README_WORDS[0] <= n <= README_WORDS[1]:
        errors.append(f"{where}: {n} words; must be {README_WORDS[0]}-{README_WORDS[1]} (code blocks excluded)")
    faq = re.search(r"^## FAQ\s*$(.*?)(?=^## |\Z)", md, re.M | re.S)
    questions = re.findall(r"^### (.+?)\s*$", faq.group(1), re.M) if faq else []
    if len(questions) < MIN_FAQ:
        errors.append(f"{where}: FAQ needs at least {MIN_FAQ} '### ' questions")
    related = re.search(r"^## Related skills\s*$(.*?)(?=^## |\Z)", md, re.M | re.S)
    links = re.findall(r"\]\(\.\./([a-z0-9-]+)/?\)", related.group(1)) if related else []
    for target in links:
        if target not in skill_names:
            errors.append(f"{where}: related skill '{target}' does not exist")
    if raw_html(md):
        errors.append(f"{where}: raw HTML is not allowed: {raw_html(md)[:3]}")
    if re.search(r"\b(is|are) (fully )?(compliant|certified)\b", md, re.I):
        errors.append(f"{where}: don't state or imply an organisation 'is compliant' or 'certified'")
    return {"markdown": md.strip(), "words": n, "faq": questions, "related": links}


# ---------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "dist" / "catalog.json"))
    ap.add_argument("--version", default="dev")
    ap.add_argument("--require-readmes", action="store_true",
                    help="fail if any skill has no README.md (turn on once every skill has one)")
    args = ap.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    collections = load_collections(errors)
    by_slug = {c["slug"]: c for c in collections}
    contributors = load_contributors(errors)

    skill_dirs = [sd for sd in sorted((ROOT / "skills").iterdir()) if (sd / "SKILL.md").exists()]
    skill_names = {sd.name for sd in skill_dirs}
    skills = []
    for sd in skill_dirs:
        fm, _ = split_frontmatter((sd / "SKILL.md").read_text())
        name, summary = field(fm, "name"), field(fm, "summary")
        coll, fws = field(fm, "collection"), field(fm, "frameworks")
        if not summary or len(summary) > 140:
            errors.append(f"{name}: metadata.summary missing or > 140 chars")
        if coll not in by_slug:
            errors.append(f"{name}: metadata.collection must be one of {list(by_slug)} (see collections/)")
        fw_list = FRAMEWORKS if fws == "all" else [f.strip() for f in fws.split(",") if f.strip()]
        bad = [f for f in fw_list if f not in FRAMEWORKS]
        if not fw_list or bad:
            errors.append(f"{name}: metadata.frameworks must be 'all' or a comma list of {FRAMEWORKS}")

        authors = [a.strip().lower() for a in field(fm, "author").split(",") if a.strip()]
        if not authors:
            errors.append(f"{name}: metadata.author is required (GitHub handle(s), comma-separated)")
        for a in authors:
            if a in contributors:
                contributors[a]["skills"].append(name)
            else:
                errors.append(f"{name}: author '{a}' has no profile at contributors/{a}.md")

        readme_path = sd / "README.md"
        if readme_path.exists():
            readme = check_readme(name, readme_path.read_text(), skill_names, errors)
        else:
            readme = None
            (errors if args.require_readmes else warnings).append(f"{name}: no README.md skill page yet")

        if coll in by_slug:
            by_slug[coll]["skills"].append(name)
        skills.append({
            # schema 1 fields (unchanged)
            "name": name,
            "summary": summary,
            "description": field(fm, "description"),
            "collection": by_slug[coll]["title"] if coll in by_slug else coll,
            "frameworks": fw_list,
            "all_frameworks": fws == "all",
            "version": field(fm, "version"),
            "path": f"skills/{name}",
            "install": f"npx skills add grcmana/grcskills@{name}",
            # schema 2 additions
            "collection_slug": coll,
            "authors": authors,
            "readme": readme,
        })

    for w in warnings:
        print(f"WARN   {w}")
    for e in errors:
        print(f"ERROR  {e}")
    if errors:
        return 1

    order = [c["slug"] for c in collections]
    skills.sort(key=lambda s: (order.index(s["collection_slug"]), s["name"]))
    for c in collections:
        c["skills"].sort()
    people = sorted(contributors.values(), key=lambda p: (-len(p["skills"]), p["name"].lower()))

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({
        "schema": 2,
        "release": args.version,
        "repo": "grcmana/grcskills",
        "install_all": "npx skills add grcmana/grcskills",
        "frameworks": FRAMEWORKS,
        "collections": [c["title"] for c in collections],  # schema 1 shape
        "collection_pages": collections,                     # schema 2
        "contributors": people,                              # schema 2
        "skills": skills,
    }, indent=2, ensure_ascii=False) + "\n")
    pages = sum(1 for s in skills if s["readme"])
    print(f"Wrote {out} ({len(skills)} skills, {pages} skill pages, {len(collections)} collections, "
          f"{len(people)} contributors, release {args.version})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
