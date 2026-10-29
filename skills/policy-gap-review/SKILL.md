---
name: policy-gap-review
description: Review existing policies against ISO 27001, SOC 2, Cyber Essentials, GDPR and ISO 42001 requirements and auditor expectations — flagging missing coverage, untestable statements, unkeepable commitments, missing document control, and contradictions with actual practice. Use for "review our policies", "gap check this policy", "are our policies audit-ready", "policy review", or annual policy review cycles.
license: MIT
metadata:
  author: GRCMANA
  version: 0.1.0
  collection: policy-management
---

# Policy Gap Review

You review policies the way a certification body auditor or SOC 2 auditor would: coverage first, then quality, then consistency with reality.

Read `references/grc-workspace.md` and `references/writing-standards.md` first.

## Inputs
- Policies in `grc/policies/`, or files or folders the user points to (Markdown, DOCX, PDF). Read them in full.
- `grc/context/company-profile.md`, for the framework selection and actual practices.
- Optional: an evidence tracker or risk register, to check that policy claims match reality.

## Modes
- **set**: review the whole policy set for coverage against the selected frameworks. This is the default.
- **single**: deep review of one policy.
- **annual**: the annual review cycle. Check currency, changes in the organisation or frameworks, and review and approval dates.

## Review checks
**A. Coverage (set mode).** Map each policy to the domains in `references/crosswalk.md` and the expectations in `references/policy-catalogue.md`. Report uncovered requirements per framework, e.g. "No supplier security coverage → ISO 27001 A.5.19–A.5.23, SOC 2 CC9.2".

**B. Document control.** Check for:
- an owner
- an approver and approval date
- a version
- a review cycle, and that it's not overdue
- a classification
- revision history

**C. Statement quality.** For each statement, check:
- **Testability**: can an auditor ask "show me"?
- **Keepability**: frequencies and SLAs that look unrealistic for this organisation's size. Flag these as **Type II exception risks**.
- **Specificity**: vague words ("appropriate", "regularly", "where possible") with no definition
- **Policy vs procedure**: procedural detail that should move out of the policy

**D. Consistency.**
- Contradictions between policies (e.g. password rules that differ).
- Contradictions with practice in the company profile, e.g. the policy says "MDM on all devices" but the profile says BYOD without MDM.
- Under Cyber Essentials, any policy permitting something the scheme fails on (unsupported software, no MFA on cloud services, patching slower than 14 days).

**E. Framework-specific must-haves.** For example:
- ISO 27001 5.2 policy content: objectives framework, commitment to requirements and continual improvement
- GDPR: 72-hour breach notification, and data subject request handling
- ISO 42001: AI policy aligned to the organisation's AI role

## Severity
- **Major**: a missing required coverage, or a contradiction with practice that would likely cause a nonconformity or exception.
- **Minor**: weak wording, missing document control, an overdue review.
- **Observation**: an improvement opportunity.

## Outputs
1. `grc/policies/gap-review-YYYY-MM-DD.md` with:
   - an executive summary (3–5 lines)
   - a coverage matrix: domain × framework → policy or gap
   - a findings table: `id, policy, section, finding, severity, framework_refs, recommendation`
   - quick wins: fixable in under an hour each
2. Offer to fix specific findings using the `policy-writer` conventions. Make edits only with the user's go-ahead, and bump the version and revision history.
3. A run log in `grc/runs/`.

## Guardrails
- Review against framework expectations, and never claim a policy "complies".
- Don't rewrite policies wholesale unless asked. Propose targeted fixes.
- Quote at most short fragments of the user's own policies, which is fine. Never quote standard text.

## References
- `references/grc-workspace.md`
- `references/writing-standards.md`
- `references/policy-catalogue.md`
- `references/crosswalk.md`
- Framework packs: `references/iso27001.md`, `soc2.md`, `cyber-essentials.md`, `gdpr.md`, `iso42001.md`
