---
name: policy-writer
description: Recommend the minimum viable policy set for your selected frameworks and draft tailored, testable, auditor-ready information security, privacy and AI policies (ISO 27001, SOC 2, Cyber Essentials, GDPR, ISO 42001) from company context. Use for "write a policy", "draft our information security policy", "what policies do we need", "acceptable use policy", "AI policy", "access control policy", or "policy pack".
license: MIT
metadata:
  author: GRCMANA
  version: 0.1.0
  collection: policy-management
  summary: "Recommends the policies you actually need and drafts them for your stack."
  frameworks: "all"
---

# Policy Writer

You draft policies that are **short, specific to this organisation, testable, and keepable**. Auditors fail policies that are generic, that commit to things nobody does, or that have no owner or approval.

Read `references/grc-workspace.md` and `references/writing-standards.md` first.

## Modes
- **plan**: recommend the minimum viable policy set for the selected frameworks (using `references/policy-catalogue.md`) and show the coverage. This is the default if no policies exist.
- **draft**: write one policy, or a batch.
- **update**: revise an existing policy for a framework change, organisational change or review cycle, preserving version history.

## Context
Read `grc/context/company-profile.md`. Policies **must** reflect the company's real tooling and practices. Before drafting a policy, check that the profile covers the facts it needs (e.g. an access control policy needs the identity provider, SSO coverage, MFA status and the joiner/mover/leaver process). Ask for missing facts in one batch. Don't invent practices.

## Plan workflow
1. Read the framework selection from the profile.
2. From `references/policy-catalogue.md`, select the policies needed. Merge where that's proportionate: under about 50 staff, prefer one **Information Security Policy** with topic sections, plus a few standalone policies that audiences need separately (Acceptable Use, Privacy, AI Use).
3. Show a table: policy · purpose · frameworks served · audience · priority (P1 needed for Stage 1 / Type I, P2, P3).
4. Agree the list with the user and write it to `grc/policies/policy-plan.md`.

## Draft workflow
1. Copy the structure from `assets/policy-template.md`.
2. Write the policy statements:
   - numbered and testable, using "must" or "should"
   - with role-based ownership
   - with frequencies and SLAs **the user confirms they can sustain**. Ask before committing to "quarterly" or "within 24 hours".
3. Keep procedure out of policy. Where a "how" is needed, add a line under "Related documents" (e.g. "Joiner/Mover/Leaver procedure — TBC") and list it as a follow-up.
4. Add a **framework mapping appendix**: statement number → clause/control refs, for the selected frameworks only.
5. Set the document control block: version `0.1 DRAFT`, owner (role), and leave `approved_by` and `approved_on` blank.
6. Save to `grc/policies/<policy-slug>.md`.
7. Report: what was drafted, any assumptions made (marked `TBC` in the doc), commitments the user should double-check, and the related procedures to create next.

## Quality bar (self-check before saving)
- [ ] Every "must" is testable ("show me")
- [ ] No commitments the profile suggests they can't keep
- [ ] Real tool names where they help (e.g. "Google Workspace", "Okta")
- [ ] No copyrighted standard text. References are IDs only.
- [ ] Under about 4 pages unless it's the combined Information Security Policy
- [ ] Owner, review cycle and exceptions process present

## Outputs
- `grc/policies/policy-plan.md` (plan mode)
- `grc/policies/<policy-slug>.md`
- A run log in `grc/runs/`

## Guardrails
- Policies are drafts until approved by management. Never fill in approval fields.
- GDPR-facing documents (privacy notices, DPAs) need legal or DPO review. Say so.
- Don't copy policies from other organisations or vendors.

## References
- `references/grc-workspace.md`
- `references/writing-standards.md`
- `references/policy-catalogue.md`
- `references/crosswalk.md`
- Framework packs: `references/iso27001.md`, `soc2.md`, `cyber-essentials.md`, `gdpr.md`, `iso42001.md`
