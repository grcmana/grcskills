---
name: evidence-request-list
description: Generate a deduplicated, control-mapped evidence request list and evidence tracker (CSV) for ISO 27001, SOC 2, Cyber Essentials Plus, GDPR and ISO 42001 — with owners, source systems, frequency and due dates, so one artefact satisfies multiple frameworks. Use for "evidence list", "PBC list", "what evidence do we need", "prepare for the auditor", "evidence collection plan", or "set up evidence tracking".
license: MIT
metadata:
  author: GRCMANA
  version: 0.1.0
  collection: audit-evidence
---

# Evidence Request List

You produce the evidence plan: exactly what to collect, from which system, by whom, how often, and for which requirements. **Collect once, use many times.**

Read `references/grc-workspace.md` and `references/evidence-standards.md` first.

## Modes
- **plan**: build the evidence tracker for the selected frameworks and the audit type. This is the default.
- **pbc**: turn an auditor's "provided by client" (PBC) request list, which the user supplies, into a tracker with owners and the sources mapped.
- **refresh**: roll the tracker forward to a new period: reset status, keep recurring items, update due dates.

## Context
Read:
- `grc/context/company-profile.md`, for the frameworks, tooling (source systems) and owners
- `grc/audits/readiness-*.md`, if present, to focus on the gaps

## Plan workflow
1. **Identify the requirements in scope** for the selected frameworks and audit type, using the framework packs.
2. **Group by domain** (`references/crosswalk.md`), and write one evidence request per real artefact, mapped to every framework it serves. Example: *"IdP export of all users with MFA status"* maps to `ISO27001:A.5.17,A.8.5; SOC2:CC6.1; CE:User access control`.
3. **Make each request specific and collectable:**
   - name the **source system** from the profile, e.g. "Google Workspace Admin → Users → export with 2SV status", not "identity system"
   - state the **period or date** required (Type II: full period with samples; Stage 1: current)
   - state the **frequency** (one-off, per event, monthly, quarterly, annual)
   - name the **owner** (role)
   - set a **due date**, working back from the audit date
4. **Mark population-based items**, e.g. "list of all leavers in the period with their termination date". Auditors sample from these.
5. **Flag automation candidates**: evidence that could later be pulled via API or connector (IdP, cloud config, ticketing, MDM, code host).

## Outputs
- `grc/evidence/evidence-tracker.csv`, using the columns in `assets/evidence-tracker-template.csv`. IDs are `E-001`… and are never renumbered.
- `grc/evidence/request-list-YYYY-MM-DD.md`: a human-friendly list grouped by owner, so you can send each owner their section.
- A summary in chat: the total number of requests, the count deduplicated across frameworks, the top owners by load, the earliest due items, and the automation candidates.
- A run log in `grc/runs/`.

## Guardrails
- The tracker stores **locations**, not the evidence itself. Never paste secrets or personal data into it.
- Don't request evidence for controls the organisation has excluded, e.g. ISO SoA exclusions or SOC 2 categories not selected.
- Use the auditor's wording only when the user supplies it (pbc mode). Otherwise paraphrase the requirements.

## References
- `references/grc-workspace.md`
- `references/evidence-standards.md`
- `references/crosswalk.md`
- Framework packs: `references/iso27001.md`, `soc2.md`, `cyber-essentials.md`, `gdpr.md`, `iso42001.md`
