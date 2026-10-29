---
name: risk-register
description: Identify, assess, treat and review information security, privacy, third-party and AI risks using a documented 5x5 methodology, producing an audit-ready risk register (CSV) and treatment plan mapped to ISO 27001, SOC 2, GDPR and ISO 42001 controls. Use for "build a risk register", "risk assessment", "update our risks", "risk review", "what are our top risks", or ISO 27001 6.1.2/6.1.3 and SOC 2 CC3 work.
license: MIT
metadata:
  author: GRCMANA
  version: 0.1.0
  collection: risk-management
---

# Risk Register

You run the risk management lifecycle: identify → assess → treat → accept → review. The output is a register an auditor would accept as evidence for ISO 27001 6.1.2/6.1.3/8.2/8.3, SOC 2 CC3, and ISO 42001 6.1.2/6.1.3.

Read `references/grc-workspace.md` and `references/risk-methodology.md` first. If `grc/context/risk-methodology.md` exists, the organisation's own method overrides the default.

## Modes
- **build**: no register exists. Create the first one.
- **add**: assess one or more new risks (e.g. a new supplier, feature, incident or market).
- **review**: periodic review. Re-score, check treatment progress and overdue items, and flag stale risks.
- **report**: summarise the register for leadership (top risks, heat map, overdue treatments, acceptances pending).

## Context
Read `grc/context/company-profile.md`. If it's missing, ask at most five questions: what you sell, the data you hold, your cloud and core SaaS, headcount and remote model, and who is asking for compliance. Then suggest running `company-context`.

## Build workflow
1. **Identify.** Generate candidate risk scenarios *specific to this company* from the profile. Use the risk statement format in the methodology. Draw on:
   - the data held and where it lives
   - the tech stack and critical suppliers
   - people factors (remote work, BYOD, contractors)
   - the product (multi-tenancy, AI features, APIs)
   - the customer and regulatory drivers
   - known incident patterns for this company type (phishing to account takeover, cloud misconfiguration, credential leakage in code, insider and leaver access, supplier compromise, ransomware, data loss through AI tools, prompt injection in AI features)

   Aim for **12–25 risks**. Quality beats volume.
2. **Validate with the user.** Show the candidates as a short table (title, one-line scenario, category). Ask them to remove, merge or add. Don't score anything the user hasn't confirmed as relevant.
3. **Assess.** For each confirmed risk:
   - Propose inherent L and I, the existing controls (ask; don't assume), and residual L and I, with a **one-line rationale** for each score.
   - Ask about existing controls in batches by domain (identity, endpoints, cloud, development, suppliers, people).
4. **Treat.** For each risk above appetite (residual > 7 by default):
   - propose a treatment option
   - propose 1–3 specific planned controls, with `framework_refs` for the user's selected frameworks only (e.g. `ISO27001:A.8.8; SOC2:CC7.1; CE:Security update management`)
   - set a target score and propose an owner (role) and due date
5. **Accept.** Risks the user wants to retain above appetite get a rationale and an approval request. Leave `approved_by` / `approved_on` blank and list them as decisions pending.
6. **Write outputs** (below) and summarise: the top five risks, a heat map (5×5 text grid of residual scores), treatments due in 30/60/90 days, and acceptances pending.

## Review workflow
1. Load the register.
2. Flag:
   - overdue treatments
   - risks past `next_review`
   - High risks without an owner
   - accepted risks without approval
   - stale scores (unchanged for more than 12 months)
3. Ask what has changed since the last review (incidents, new suppliers, product changes, org changes, new customer requirements).
4. Re-score where it's justified, with a rationale. Update `last_reviewed` and `next_review`.
5. Write the review summary to `grc/risks/review-YYYY-MM-DD.md`. This is useful management review input for ISO 27001 9.3.

## Outputs
- `grc/risks/risk-register.csv`, with columns exactly as in `assets/risk-register-template.csv`. Preserve existing rows and IDs (`R-001`…). Never renumber.
- `grc/risks/treatment-plan.md`: the treatments grouped by owner and due date.
- `grc/risks/review-YYYY-MM-DD.md` (review mode)
- A run log in `grc/runs/`

## Guardrails
- Scores are **proposals with rationale**. The risk owner confirms them.
- Never count planned controls in residual scores.
- Never fill in approval fields.
- Map only to frameworks in the profile's selection, to avoid noise.
- If the user has a GRC platform, offer to format the CSV for import rather than duplicating systems of record.

## References
- `references/grc-workspace.md`
- `references/risk-methodology.md`
- `references/crosswalk.md`
