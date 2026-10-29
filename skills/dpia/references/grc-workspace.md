# GRC Workspace Convention

All GRC Skills share one convention, so they work together whether they're installed one at a time or used inside **GRC OS**.

## Location
GRC data lives in a `grc/` folder at the root of the current project:

```
grc/
├── context/     company-profile.md, scope.md
├── risks/       risk-register.csv, treatment-plan.md, ai-impact-assessments/
├── policies/    <policy-name>.md, gap-review-YYYY-MM-DD.md
├── evidence/    evidence-tracker.csv, request-list-YYYY-MM-DD.md
├── audits/      readiness-<framework>-YYYY-MM-DD.md, ce-scope.md, dpia/
└── runs/        YYYY-MM-DD-<skill>-<slug>.md   (AI run log / audit trail)
```

If `grc/` doesn't exist, create only the subfolder you need. Tell the user that `grc/` contains sensitive governance data and **must not be committed to a public repository**. Suggest adding `grc/` to `.gitignore`, or keeping it in a private repo.

## Company context
Before doing substantive work, every skill:
1. Reads `grc/context/company-profile.md` if it exists. Use it silently, and don't re-ask what's there.
2. If it doesn't exist, asks **only** the context questions that skill needs (keep it to five or fewer). Then suggests running the `company-context` skill for a complete profile.
3. Never invents company facts. Unknowns are written as `TBC`.

## Human-in-the-loop fields
Any record that implies a decision has these fields, which **only a human fills in**:
`approved_by`, `approved_on`. Claude leaves them blank, or `PENDING`, and lists them under "decisions pending" in the run log.

## Run log
At the end of every skill run, write `grc/runs/YYYY-MM-DD-<skill>-<slug>.md`:

```markdown
---
skill: <skill-name>
date: YYYY-MM-DD
mode: <mode>
inputs: [files read]
outputs: [files created/changed]
decisions_pending: [items awaiting human approval]
---
## Summary
2–5 lines.
## Open questions
- ...
```

This gives the organisation an audit trail of AI-assisted GRC work. It's useful evidence for ISO 42001, and good practice for any auditor asking "how was this produced?"

## Guardrails
- Drafts are for review by a competent person. Never state or imply that the organisation "is compliant" or "is certified".
- Reference clause and control IDs and paraphrase. Never reproduce copyrighted standard text (ISO, AICPA).
- Not legal advice. Flag when a lawyer or DPO should review.
- Never request, store or echo secrets, credentials or individuals' personal data. Owners are recorded by role or name only.
- Framework packs carry an `as_of` date. Flag anything that may have changed since.
