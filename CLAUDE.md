# Maintainer notes for agents working on this repo

This repo is a **library of portable GRC agent skills** distributed with `npx skills add grcmana/grcskills` and listed on grcskills.io. You're editing the library, not running a GRC programme.

- Shared knowledge lives in `knowledge/`. **Never edit `skills/*/references/` copies directly.** Edit `knowledge/`, then run `python3 scripts/sync_references.py`.
- Each skill must stay self-contained and follow `knowledge/methodology/grc-workspace.md`.
- `SKILL.md` frontmatter: `name` equals the folder name, and `description` is 1024 characters or fewer and describes what the skill does and when to use it.
- Never add copyrighted standard text (ISO, AICPA). Use IDs and own-words summaries.
- Bump `metadata.version` in a skill when you change its behaviour. Update the `as_of` date in a framework pack when you change its facts.
- Run `python3 scripts/sync_references.py --check` before committing.
- The grcskills.io website lives in a separate private repo. This repo's only interface to it is `catalog.json`, built by `scripts/build_catalog.py` and attached to tagged releases. Keep `metadata.summary` and `metadata.frameworks` accurate.
