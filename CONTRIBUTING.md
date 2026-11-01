# Contributing to GRC Skills

Thanks for helping GRC practitioners work smarter. Contributions from practitioners (auditors, GRC engineers, CISOs, privacy pros, and accidental owners with hard-won lessons) are the whole point.

## Ways to contribute
- **Fix or improve a framework pack.** Corrections, version updates (e.g. the annual Cyber Essentials update), and common failure points.
- **Improve a skill.** A better workflow, sharper questions, better outputs.
- **Propose a new skill.** Open an issue first using the "New skill" template, so we can check it fits and doesn't overlap.
- **Report real-world results.** What worked, and what an auditor pushed back on.

## Ground rules
1. **No copyrighted standard text.** Reference clause and control IDs and summarise in your own words. Don't paste ISO, AICPA or other licensed content. PRs containing it will be closed.
2. **No client or confidential data.** Examples must be fictional.
3. **Human in the loop.** Skills must never fill in approval fields or claim an organisation "is compliant" or "certified".
4. **Follow the workspace convention.** Read and write under `grc/` as described in `knowledge/methodology/grc-workspace.md`, and write a run log.
5. **Self-contained skills.** A skill must work when installed alone. Put shared knowledge in `knowledge/`, register it in `scripts/sync_references.py`, and run the sync.
6. **Proportionate.** Write for real organisations, including 10-person startups. No gold-plating.

## Skill structure
```
skills/<skill-name>/
├── SKILL.md       # required: frontmatter name (= folder name), description (≤1024 chars),
│                  #   metadata: author, version, collection, summary (≤140 chars), frameworks
├── README.md      # the skill's page on grcskills.io (for people, not the agent)
├── references/    # synced knowledge + skill-specific references
└── assets/        # templates (CSV/MD) the skill fills in
```

## Skill pages (README.md)
Each skill has a human-facing page at `skills/<name>/README.md`. It's shown on GitHub and published to grcskills.io when a release is cut. `SKILL.md` tells the agent what to do; the README tells people why and when to use the skill.

Copy [`templates/skill-README.md`](templates/skill-README.md) and keep its ten `##` headings exactly. CI checks:
- 800–1,500 words (code blocks don't count)
- the headings, in order
- at least three FAQ questions as `###` headings
- related-skill links point to real skills
- no raw HTML, and no claim that an organisation "is compliant" or "certified"

The worked example must be fictional. [`skills/dpia/README.md`](skills/dpia/README.md) is the reference example. New skills need a README to be merged.

## Categories
A skill's category is `metadata.collection` in `SKILL.md`. Categories are defined in `collections/<slug>.md`: a title, a display order, and a 100–400 word introduction for the category page. Propose a new category in an issue first.

## Get credited
Add a profile at `contributors/<your-github-handle>.md` (see [`contributors/README.md`](contributors/README.md)) and add your handle to `metadata.author` in any skill you wrote, e.g. `author: grcmana, your-handle`. Profiles are optional and public; only name, role, website, LinkedIn and a short bio are accepted.

Name skills in lowercase-with-hyphens, after the job to be done (e.g. `supplier-risk`, not `tprm-v2`). The `description` must say **what the skill does and when to use it**, including the phrases practitioners actually type.

## Before opening a PR
```bash
python3 scripts/sync_references.py          # sync shared knowledge into skills
python3 scripts/sync_references.py --check  # what CI runs
python3 scripts/build_catalog.py            # validates metadata, skill pages, categories and profiles
```

`metadata.summary` is the one-line, plain-English description shown on grcskills.io. `metadata.frameworks` is `all` or a comma-separated list of `ISO 27001, SOC 2, Cyber Essentials, GDPR, ISO 42001`. The website is maintained separately and updates only when maintainers cut a release.
Then test your skill in at least one agent (e.g. Claude Code) against the fictional Acme Analytics example in [GRC OS](https://github.com/grcmana/grc-os).

## Licence
By contributing, you agree your contribution is licensed under the MIT licence.
