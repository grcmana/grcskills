# Policy writer: the policies you actually need, drafted for your stack

The `policy-writer` skill helps your AI agent work out the minimum set of security, privacy and AI policies your chosen frameworks expect, then draft each one around the tools and practices you really use. It covers ISO 27001, SOC 2, Cyber Essentials, GDPR and ISO 42001, and produces short, numbered, testable drafts that your leadership reviews and approves.

## What it does

Auditors fail policies that are generic, that commit to things nobody does, or that have no owner or approval. A downloaded template pack often has all three problems, and under a SOC 2 Type II period every commitment you can't keep becomes an exception.

The skill works in three modes:

- **Plan** (the default if no policies exist): recommends the minimum viable policy set for your selected frameworks and shows the coverage.
- **Draft**: writes one policy, or a batch, from a standard template.
- **Update**: revises an existing policy for a framework change, an organisational change or a review cycle, keeping its version history.

The result is a policy set you can defend line by line: every "must" is something an auditor can ask you to show, and every frequency is one you confirmed you can sustain.

## Who it's for

- **GRC practitioners and engineers:** the skill does the plan, the first drafts and the clause mapping, and enforces testability and proportionality. You still own the commitments you put your name to, and management approval.
- **Accidental owners** (founders, CTOs, ops leads): you get a straight answer to "what policies do we need?" and drafts that describe your actual setup, without first learning the frameworks.

## When to use it

Typical triggers:

- "What policies do we need?" or "policy pack" at the start of an ISO 27001, SOC 2 or Cyber Essentials project
- "Write a policy", "draft our information security policy", "acceptable use policy" or "access control policy"
- "AI policy" when staff adopt AI tools, or for ISO 42001
- A policy that needs updating after a new tool, a reorganisation or a framework change

Don't use it to judge whether your current policies are good enough; run `policy-gap-review` first, then use this skill to fix what it finds. To assess a specific high-risk project, use `dpia`.

## How it works

1. **Context.** The skill reads `grc/context/company-profile.md` silently, including your framework selection. If there is no profile, it asks at most five questions and suggests running `company-context`.
2. **Plan.** Using its policy catalogue, it selects the policies your frameworks expect. Under about 50 staff it prefers one Information Security Policy with topic sections, plus a few standalone policies that audiences need separately: Acceptable Use, Privacy and AI Use.
3. **Agree the list.** It shows a table of policy, purpose, frameworks served, audience and priority (P1 for Stage 1, Type I or a Cyber Essentials submission; P2 before Stage 2 or a Type II period; P3 for maturity). You agree the list before it is saved.
4. **Check facts before drafting.** It checks the profile covers what each policy needs; access control, for example, needs your identity provider, SSO coverage, MFA status and joiner/mover/leaver process. It asks for missing facts in one batch and never invents a practice.
5. **Draft.** It writes numbered statements using "must" and "should", with role-based owners. Before committing to "quarterly" or "within 24 hours", it asks whether you can sustain it.
6. **Keep procedure out.** Where a "how" is needed, it adds a line under Related documents (for example "Joiner/Mover/Leaver procedure — TBC") as a follow-up.
7. **Map and control.** It adds a mapping appendix (statement number to clause or control IDs, selected frameworks only) and sets version `0.1 DRAFT` with an owner role. The `approved_by` and `approved_on` fields stay blank.
8. **Self-check and report.** Before saving it checks testability, keepability, real tool names, no standard text, length (under about four pages unless it's the combined policy), and an owner, review cycle and exceptions process. It then reports assumptions marked `TBC`, commitments to double-check and procedures to write next.

## What you get

```
grc/
├── policies/
│   ├── policy-plan.md                      # plan mode
│   └── <policy-slug>.md                    # one file per drafted policy
└── runs/YYYY-MM-DD-policy-writer-<slug>.md # AI run log
```

Each policy has document control, purpose, scope, statements, roles, exceptions, related documents, a mapping appendix and revision history, with the first row marking the draft as AI-assisted.

The run log records which files the skill read and wrote, and the approvals still waiting for a human: an audit trail of how each policy was produced, useful for ISO 42001 and for any auditor who asks.

## Worked example

_This scenario is fictional._

Acme Analytics is a fictional 40-person UK B2B SaaS analytics company preparing for ISO 27001 and a first SOC 2 Type I report, with GDPR in scope. Its profile records Google Workspace, Okta, GitHub and AWS. The CTO asks:

> We're starting ISO 27001 and SOC 2. What policies do we need, and can you draft the access control section first?

In plan mode, the skill reads the profile and, because Acme is under 50 staff, proposes one Information Security Policy with topic sections, plus standalone Acceptable Use, Incident Response, Risk Management, Data Protection and AI Use policies. Access control, as a section, is P1. The CTO agrees and the plan is saved.

The profile doesn't say whether MFA is enforced in AWS or how leavers are removed, so the skill asks both in one batch, and asks whether quarterly access reviews are sustainable. The CTO says six-monthly is realistic. Part of the draft reads:

```
3.4  Access to production AWS accounts must be granted only through
     Okta, approved by the system owner, and recorded in a ticket.
3.5  MFA must be enforced for all Okta, Google Workspace, GitHub and
     AWS accounts.
3.6  Access to production systems must be reviewed by the system
     owner at least every six months, and the review recorded.
3.7  Leavers' Okta accounts must be disabled no later than their
     last working day.

Related documents
- Joiner/Mover/Leaver procedure — TBC

Appendix A (excerpt)
| 3.4 | A.5.15, A.5.18 | CC6.1, CC6.2 |
| 3.6 | A.5.18         | CC6.2, CC6.3 |
```

The report flags the six-month review as a commitment to confirm, lists the joiner/mover/leaver procedure as the next document, and leaves both approval fields blank.

## Frameworks covered

- **ISO 27001:2022:** clause 5.2 (the information security policy) and the Annex A controls that imply policies, such as A.5.1, A.5.10, A.5.15–A.5.18, A.5.19–A.5.23, A.5.24–A.5.28 and A.8.8.
- **SOC 2:** the Common Criteria, including CC1, CC2 and CC5.3 for the top-level policy, CC6 for access, CC7 for incidents, CC8.1 for change and CC9.2 for vendors.
- **Cyber Essentials (Requirements v3.3):** policy coverage for the technical controls, including MFA on cloud services and the 14-day rule for critical and high-risk updates.
- **UK GDPR and EU GDPR:** Articles 5(2) and 24 (accountability), 25 (privacy by design), 28 (processors), 32 (security) and 33–34 (breach handling, including the 72-hour notification).
- **ISO 42001:2023:** clause 5.2 and A.2 (the AI policy) and A.9 (responsible use of AI systems by staff).

Each framework pack carries an `as_of` date, and the mappings are indicative. Frameworks change (Cyber Essentials usually every April), so check the official source for anything that may have moved since then.

## Guardrails

- **Drafts until approved.** Every policy is version `0.1 DRAFT`. The skill never fills in `approved_by` or `approved_on`; management approval is yours.
- **No invented practices.** Unknown facts are marked `TBC`, and frequencies or SLAs are only written in once you confirm you can keep them.
- **No copying.** It won't copy other organisations' or vendors' policies, or reproduce ISO or AICPA text.
- **Not legal advice.** GDPR-facing documents such as privacy notices and DPAs need legal or DPO review, and the skill says so.
- **No claims of conformity.** The skill never says your policies meet a standard.
- **No secrets or personal data.** Policy text uses role names, not people's names.

## FAQ

### How many policies does a startup really need?

Fewer than most template packs suggest. Under about 50 staff, the skill usually recommends one combined Information Security Policy plus a handful of standalone policies such as Acceptable Use and, where relevant, Data Protection and AI Use.

### Can we just use a template pack instead?

You can, but generic policies often commit you to practices you don't follow, which auditors find. The skill drafts from your real tools and asks before committing to any deadline.

### Why does it ask so many questions before drafting?

A policy describing an MFA setup you don't have will contradict your evidence. It asks for missing facts in one batch and marks anything still unknown as `TBC`.

### Will the drafts get us certified?

Policies alone won't achieve certification. The drafts are written to stand up to an auditor's "show me", but you still need management approval, controls that operate, and a passed audit.

## Related skills

- [`company-context`](../company-context/): builds the profile the policies are drafted from, including tools, practices and framework selection.
- [`policy-gap-review`](../policy-gap-review/): reviews existing policies the way an auditor would; use it to decide what to draft or update.
- [`risk-register`](../risk-register/): holds the risk-assessed exceptions that every drafted policy's exceptions section points to.
- [`audit-readiness`](../audit-readiness/): shows where the policy set sits in your wider readiness for an audit.
- [`dpia`](../dpia/): assesses specific high-risk processing that the data protection policy commits you to assess.
