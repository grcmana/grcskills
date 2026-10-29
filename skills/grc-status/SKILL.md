---
name: grc-status
description: Roll up the GRC workspace (risk register, policies, evidence tracker, readiness assessments, run logs) into a one-page programme status for leadership or the board — progress per framework, top risks, overdue actions, decisions needed, and next 30 days. Use for "GRC status", "compliance update", "board report", "where are we with ISO/SOC 2", "weekly compliance summary", or management review inputs (ISO 9.3).
license: MIT
metadata:
  author: GRCMANA
  version: 0.1.0
  collection: foundations
  summary: "Turns your workspace into a one-page status, board report or management review pack."
  frameworks: "all"
---

# GRC Status

You produce a one-page, decision-oriented status of the GRC programme from what's actually in the `grc/` workspace. Leadership needs to know: are we on track, what's at risk, and what do you need from me?

Read `references/grc-workspace.md` first.

## Inputs (read whatever exists)
- `grc/context/company-profile.md`: frameworks, target dates, drivers
- `grc/risks/risk-register.csv`: bands, overdue treatments, pending acceptances
- `grc/policies/`: count by status (draft / approved), overdue reviews
- `grc/evidence/evidence-tracker.csv`: status counts, overdue items, rejected items
- `grc/audits/readiness-*.md`: the latest readiness % per framework
- `grc/runs/`: activity since the last status

If the workspace is mostly empty, say so plainly and recommend the next skill to run, rather than producing a hollow report.

## Modes
- **exec**: one page for the CEO, leadership team or board. This is the default.
- **management-review**: structured to cover the ISO 27001 / ISO 42001 9.3 management review inputs:
  - status of actions from previous reviews
  - changes in external and internal issues
  - interested parties' needs
  - performance feedback: nonconformities, monitoring results, audit results, objectives
  - feedback from interested parties
  - risk assessment results and treatment plan status
  - opportunities for improvement

  Leave decision and output fields for humans to fill in.
- **weekly**: a short delta since the last status, for the working team.

## Exec report structure
1. **Headline**: one sentence on overall RAG and the key message.
2. **Framework progress**: a table of framework · target date · readiness % · RAG · trend.
3. **Top five risks**: residual score, owner, treatment status.
4. **Overdue and at risk**: treatments, evidence, policy approvals.
5. **Decisions needed**: risk acceptances pending, policy approvals, budget and resourcing asks. Be specific: what, by whom, by when.
6. **Next 30 days**: three to five commitments.

## Outputs
- `grc/status-YYYY-MM-DD.md` (or `grc/audits/management-review-YYYY-MM-DD.md` in management-review mode)
- A brief chat summary
- A run log in `grc/runs/`

## Guardrails
- Every number must come from workspace files. If data is missing, say "no data", and never estimate.
- RAG must follow a stated rule:
  - 🟢: on track for the target date
  - 🟠: at risk, recoverable with a stated action
  - 🔴: target date not achievable without a decision
- Don't soften bad news. Leadership needs it early.

## References
- `references/grc-workspace.md`
- `references/risk-methodology.md`
- `references/evidence-standards.md`
