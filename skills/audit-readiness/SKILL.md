---
name: audit-readiness
description: Run a readiness / gap assessment against ISO 27001, SOC 2, Cyber Essentials, GDPR or ISO 42001 — scoring each requirement, identifying gaps, estimating effort, and producing a prioritised remediation roadmap to Stage 1/Stage 2, Type I/Type II, or CE submission. Use for "are we ready for our audit", "gap assessment", "readiness assessment", "how far are we from ISO 27001 / SOC 2", or "what do we need before the auditor arrives".
license: MIT
metadata:
  author: GRCMANA
  version: 0.1.0
  collection: audit-evidence
  summary: "Scores how ready you are for audit and lays out the roadmap to get there."
  frameworks: "all"
---

# Audit Readiness

You assess how ready the organisation is for a specific audit or certification, and produce a roadmap the team can actually execute.

Read `references/grc-workspace.md`, `references/evidence-standards.md` and the relevant framework pack(s) first.

## Modes
- **quick**: a 20–30 minute interview-based readiness score per domain. Good for accidental owners and for sales conversations.
- **full**: a requirement-by-requirement assessment with evidence checks. Use this for a practitioner preparing for an audit.
- **multi**: one assessment across several selected frameworks, deduplicated using `references/crosswalk.md`.

## Context
Read `grc/context/company-profile.md` (framework selection, scope, target dates). Also use these if they exist:
- `grc/risks/risk-register.csv`
- `grc/policies/`
- `grc/evidence/evidence-tracker.csv`

These are evidence of maturity. **Inspect what's there**, don't just ask.

## Maturity scale (per requirement or domain)
| Score | Status | Meaning |
|---|---|---|
| 0 | Not started | Nothing in place |
| 1 | Ad hoc | Happens informally; no documentation or evidence |
| 2 | Documented | Policy/procedure exists; little operating evidence |
| 3 | Operating | Documented and operating, with evidence for the period |
| 4 | Audit-ready | Operating, evidenced, reviewed; sampling would pass |

## Full workflow
1. **Confirm the target**: framework, audit type (CE / CE+ / ISO Stage 1 / Stage 2 / SOC 2 Type I / Type II, or GDPR accountability review), scope, and target date.
2. **Build the requirement list** from the framework pack:
   - ISO: clauses 4–10, plus the Annex A controls applicable per the SoA. If there's no SoA yet, assess all of them and flag candidates for exclusion.
   - SOC 2: the CC series plus the selected categories.
   - CE: the five controls plus scoping.
   - GDPR: the accountability artefacts table.
   - ISO 42001: clauses plus Annex A.
3. **Assess** in batches by domain:
   - Ask what exists, and where.
   - Check files in `grc/`.
   - Score 0–4 with a one-line justification.
   - Note the evidence location.
4. **Gaps.** Anything below the required level is a gap. Stage 1 / Type I needs ≥2 on all requirements and ≥3 on mandatory documented information. Stage 2 / Type II / CE needs ≥3, ideally 4. For each gap, record the recommended action, owner (role), effort (S <1 day / M 1–5 days / L >5 days), dependency, and target date.
5. **Roadmap.** Sequence the gaps by dependency and critical path. Typically the order is: scope → risk assessment → SoA → policies → operating controls → evidence period → internal audit → management review → audit. Flag whether the target date is realistic and say what would make it so.

## Outputs
- `grc/audits/readiness-<framework>-YYYY-MM-DD.md`, containing:
  - executive summary (readiness %, RAG, go/no-go view on the target date)
  - domain heat map
  - requirement table: `ref, requirement (own words), score, evidence location, gap, action, owner, effort, due`
  - 30/60/90-day roadmap
  - top five risks to the audit date
- Offer next steps: the `evidence-request-list` skill for the evidence plan, and `policy-writer` for missing policies.
- A run log in `grc/runs/`.

## Guardrails
- A readiness assessment isn't an audit opinion. **Never** state the organisation will pass.
- Don't inflate scores. "Documented" isn't "operating" without records over time.
- Requirements are paraphrased. No copyrighted standard text.
- For CE, flag whether the current question set and requirements version should be confirmed with the certification body.

## References
- `references/grc-workspace.md`
- `references/evidence-standards.md`
- `references/crosswalk.md`
- Framework packs: `references/iso27001.md`, `soc2.md`, `cyber-essentials.md`, `gdpr.md`, `iso42001.md`
