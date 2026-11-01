# Audit readiness: gap assessments and remediation roadmaps with your AI agent

The `audit-readiness` skill helps your AI agent work out how far you are from a specific audit or certification, and what to do about it. It scores each requirement of ISO 27001, SOC 2, Cyber Essentials, GDPR or ISO 42001 on a 0–4 scale, identifies and sizes the gaps, and turns them into a sequenced roadmap to your audit or submission date.

## What it does

Most teams find out how ready they are when the auditor asks for something that doesn't exist. A readiness assessment moves that discovery forward, while there is still time to fix things.

The skill works in three modes:

- **Quick**: a 20–30 minute interview that gives a readiness score per domain. Useful for a first view, or when a buyer asks "how close are you?".
- **Full**: a requirement-by-requirement assessment with evidence checks, for a practitioner preparing for an actual audit.
- **Multi**: one assessment across several frameworks at once, deduplicated with the shared crosswalk so that a control serving ISO 27001 and SOC 2 is assessed once.

The output is an honest score, gaps with owners and effort, and a view on whether your target date is realistic. It is a planning tool, not an audit opinion.

## Who it's for

- **GRC practitioners and engineers:** the skill builds the requirement list, inspects what already exists in `grc/`, and drafts scores, gaps and a 30/60/90-day plan. You still own each score, the scope and Statement of Applicability decisions, and the date conversation with leadership.
- **Accidental owners** (founders, CTOs, ops leads): you get a plain answer to "how far are we?", a red/amber/green view and a prioritised to-do list, without needing to know the clauses first.

## When to use it

Typical triggers:

- "Are we ready for our audit?" or "what do we need before the auditor arrives?"
- "Gap assessment" or "readiness assessment" for a named framework
- "How far are we from ISO 27001 / SOC 2?"
- A customer has asked for a certificate or report and you need to commit to a date
- Moving from Stage 1 to Stage 2, or from Type I to Type II

Don't use it to build the evidence plan; that is `evidence-request-list`. Use `cyber-essentials-scoping` for a detailed Cyber Essentials inventory and `policy-gap-review` for a close read of policies.

## How it works

1. **Context.** The skill reads `grc/context/company-profile.md` for framework selection, scope and target dates. If there is no profile, it asks at most five questions and suggests running `company-context`.
2. **Inspect what exists.** It looks at `grc/risks/risk-register.csv`, `grc/policies/` and `grc/evidence/evidence-tracker.csv` where present. It inspects these rather than just asking.
3. **Confirm the target.** Framework, audit type (CE, CE+, ISO Stage 1 or Stage 2, SOC 2 Type I or Type II, or a GDPR accountability review), scope and target date.
4. **Build the requirement list** from the framework pack. For ISO, that is clauses 4–10 plus the Annex A controls in the SoA; with no SoA yet, it assesses all of them and flags exclusion candidates.
5. **Assess by domain.** For each requirement it asks what exists, checks the files, gives a 0–4 score with a one-line justification, and notes the evidence location.
6. **Identify gaps.** Anything below the required level is a gap, with a recommended action, owner (role), effort (S under a day, M one to five days, L over five days), dependency and target date.
7. **Roadmap.** Gaps are sequenced by dependency and critical path (typically scope, risk assessment, SoA, policies, operating controls, evidence period, internal audit, management review), and the skill flags whether the date is realistic.

The scores are drafts for a human to challenge before the plan goes to leadership.

## What you get

```
grc/
├── audits/readiness-<framework>-YYYY-MM-DD.md   # the readiness assessment
└── runs/YYYY-MM-DD-audit-readiness-<slug>.md    # AI run log
```

The readiness file contains an executive summary (readiness percentage, RAG status and a go/no-go view on the target date), a domain heat map, a requirement table (`ref, requirement (own words), score, evidence location, gap, action, owner, effort, due`), a 30/60/90-day roadmap and the top five risks to the audit date. The run log records the files read and written and the decisions awaiting a human.

The maturity scale is the same for every framework:

| Score | Status | Meaning |
|---|---|---|
| 0 | Not started | Nothing in place |
| 1 | Ad hoc | Happens informally, with no documentation or evidence |
| 2 | Documented | A policy or procedure exists, with little operating evidence |
| 3 | Operating | Documented and operating, with evidence for the period |
| 4 | Audit-ready | Operating, evidenced and reviewed; a sample would hold up |

For Stage 1 or Type I, the skill expects at least 2 on every requirement and at least 3 on mandatory documented information. For Stage 2, Type II or Cyber Essentials, it expects at least 3, ideally 4.

## Worked example

_This scenario is fictional._

Acme Analytics is a fictional 40-person UK B2B SaaS analytics company. A large customer has asked for ISO 27001, and the CTO asks the agent:

> We want ISO 27001 Stage 1 by 15 March 2027. Run a full readiness assessment and tell me honestly if the date works.

In full mode, the skill reads the profile, finds six policies in `grc/policies/` and a risk register with owners but no treatment dates. With no SoA yet, it assesses all 93 Annex A controls and flags some physical controls as exclusion candidates for the CTO to decide, as the team works remotely. It scores the information security policy at 2 (approved but never reviewed), access reviews at 1 (done informally in chat, with no record) and the internal audit programme at 0.

An excerpt of `grc/audits/readiness-iso27001-2026-11-02.md`:

```
Executive summary
Target:     ISO 27001:2022 Stage 1, 2027-03-15 (scope: Acme platform and
            supporting cloud environment)
Readiness:  38%   RAG: Amber
Go/no-go:   No-go on the current plan. Realistic if the SoA is approved by
            mid-December and an independent internal auditor is booked
            for February.

ref     requirement (own words)            score evidence location   gap action                          owner    effort due
6.1.3d  SoA justifying Annex A selection   0     none                yes Draft SoA from risk treatment   CTO      M      2026-12-11
A.5.18  Access rights reviewed regularly   1     chat thread only    yes Run and record quarterly review IT lead  S      2026-12-04
9.2     Internal audit programme           0     none                yes Appoint independent auditor     CEO      M      2027-02-12

Top risk to the audit date: internal audit cannot be carried out by the
person who built the ISMS; no independent resource is identified yet.
```

The skill offers to run `evidence-request-list` against the gaps, and logs the SoA exclusions as a pending decision.

## Frameworks covered

- **ISO 27001:2022:** clauses 4–10 and the mandatory documented information, such as scope (4.3), risk processes and SoA (6.1.2, 6.1.3), internal audit (9.2) and management review (9.3), plus the 93 Annex A controls. It reflects Amendment 1 (2024) on climate change in 4.1 and 4.2.
- **SOC 2:** the Common Criteria CC1–CC9, plus A1, PI1, C1 or P1–P8 if selected. Type I covers design at a point in time; Type II covers operation over a period, typically 3–12 months.
- **Cyber Essentials:** scoping and the five controls under Requirements v3.3 (Danzell question set), including mandatory MFA on cloud services and the 14-day patching window.
- **GDPR (UK and EU):** the accountability artefacts, including the RoPA (Article 30), DPAs (Article 28), DPIAs (Article 35) and breach procedure (Articles 33–34).
- **ISO 42001:2023:** clauses 4–10, including the AI system impact assessment (6.1.4), plus Annex A (A.2–A.10).

Each framework pack, and the crosswalk used in multi mode, carries an `as_of` date. Check the official source for anything that may have changed since; Cyber Essentials usually updates every April.

## Guardrails

- **Not an audit opinion.** The skill never states that the organisation will pass.
- **No score inflation.** "Documented" is not "operating" without records over time.
- **Own words only.** Requirements are paraphrased with their IDs. No copyrighted ISO or AICPA text is reproduced.
- **Cyber Essentials version check.** It flags that the current question set and requirements version should be confirmed with your certification body.
- **Humans approve.** Scope, SoA and date decisions are listed as pending; approval fields stay blank or `PENDING`.
- **No secrets or personal data.** Owners are recorded by role; evidence by location.

## FAQ

### How long does a readiness assessment take?

Quick mode takes 20–30 minutes of conversation. Full mode goes requirement by requirement and checks evidence, so it runs in batches by domain.

### Can it tell us whether we will pass the audit?

No. It shows your gaps against the level an auditor typically expects and whether your date looks realistic. The outcome is for the certification body or CPA firm to decide.

### We don't have a Statement of Applicability yet. Is that a problem?

Not for the assessment. The skill assesses every Annex A control and flags candidates for exclusion, which gives you a head start on the SoA itself.

### Can we assess ISO 27001 and SOC 2 together?

Yes, that is what multi mode is for. It uses the crosswalk to assess shared domains once and then shows coverage for each framework.

## Related skills

- [`company-context`](../company-context/): builds the profile, scope and target dates the assessment reads.
- [`evidence-request-list`](../evidence-request-list/): turns the gaps into a control-mapped evidence plan with owners and due dates.
- [`policy-writer`](../policy-writer/): drafts the missing policies the assessment identifies.
- [`risk-register`](../risk-register/): builds the risk assessment and treatment plan that ISO 27001 and SOC 2 expect.
- [`grc-status`](../grc-status/): rolls readiness into a one-page leadership update.
