# Evidence review: check audit evidence before your auditor sees it

The `evidence-review` skill helps your AI agent quality-check audit evidence (exports, screenshots, tickets and documents) before it goes to your auditor or certification body. It rates each item, explains exactly how to fix the weak ones, flags secrets and unnecessary personal data, and calls out evidence that contradicts your own policies, so you find likely exceptions while there is still time to act on them.

## What it does

Rejected evidence is expensive. Each item an auditor sends back costs a round trip, uses up audit days and can turn into a formal exception or nonconformity. Most rejections come from predictable problems: a screenshot with no date, an export filtered to "active users only", a record from outside the audit period, or no way to tell who approved something.

The skill acts as a pre-audit reviewer. It applies five tests to each item (is it **relevant**, **complete**, **dated**, **attributable** and **authentic**?), then compares what the evidence shows with what your policy promises. Each item gets a rating of `strong`, `adequate`, `weak` or `insufficient`, a one-line reason and a specific fix, recorded in your evidence tracker and a review report.

## Who it's for

- **GRC practitioners and engineers:** the skill does the first-pass QA across a large evidence set, checks populations, date ranges and filters, and drafts the exceptions list. You still own the judgement on borderline items, the conversation with the auditor and any management response.
- **Accidental owners** (founders, CTOs, ops leads): you get a plain answer to "is this good enough for the auditor?" for each file, with the exact re-export or re-collection needed, without having to learn what auditors mean by "population" or "attributable" first.

## When to use it

Use it after evidence has been collected and before it is uploaded to the auditor or your audit portal. Typical triggers:

- "Review this evidence" or "check our evidence" ahead of an audit
- "Is this good enough for the auditor?" or "will this screenshot pass?"
- "Pre-audit evidence QA" across a full request list
- Spot-checking operating evidence partway through a SOC 2 Type II or ISO 27001 surveillance period

Don't use it to work out what evidence you need in the first place; use `evidence-request-list` for that. For an overall view of whether you are ready for an audit, use `audit-readiness`. For checking a policy document's content against a framework, use `policy-gap-review`.

## How it works

1. **Context.** The skill reads `grc/evidence/evidence-tracker.csv`, if present, to learn what each item is meant to prove. It takes the audit type and period from the tracker or `grc/context/company-profile.md`, and asks if neither has them.
2. **Identify.** For each item it works out which request and requirement(s) it is meant to satisfy. If that isn't clear, it asks rather than guessing.
3. **Five tests.** Relevant (does it show *this* control?), complete (full population and full period, checking row counts, date ranges and filters), dated (a visible date inside the audit period), attributable (who performed or approved it) and authentic (system-generated, or a screenshot showing URL, timestamp and user).
4. **Policy comparison.** It checks the evidence against your policy commitments. Gaps, such as users without MFA when the policy says "MFA for all", are flagged early as likely exceptions or nonconformities.
5. **Sensitive data check.** It flags secrets, tokens, passwords, full card numbers and unnecessary personal or customer data, and recommends redaction before sharing. It never repeats the sensitive values in its output.
6. **Rate and fix.** Each item gets a rating, a one-line reason and the exact fix, for example "re-export with the date column and without the 'active only' filter".
7. **Human decisions.** Your team decides what to re-collect and whether a management response is needed. These are listed in the run log.

## What you get

```
grc/
├── evidence/
│   ├── evidence-tracker.csv          # status, quality_rating, reviewer_notes updated
│   └── review-YYYY-MM-DD.md          # summary, item table, likely exceptions
└── runs/YYYY-MM-DD-evidence-review-<slug>.md   # AI run log
```

- **Evidence tracker:** `status` (reviewed, accepted or rejected), `quality_rating` and `reviewer_notes` for each item, with new rows for untracked items.
- **Review report:** a summary (items reviewed, ratings breakdown, likely exceptions), a table of `evidence_id`, requirement refs, rating, issue, fix and owner, and a section on likely exceptions and nonconformities.
- **Run log:** files read and written, and the decisions still waiting for a human.

## Worked example

_This scenario is fictional. Acme Analytics is an invented 40-person UK B2B SaaS analytics company._

A year after its first SOC 2 Type I report, Acme Analytics is three weeks from fieldwork for its first Type II report, which covers a 12-month observation period. The ops lead has collected the access control evidence into a folder and asks the agent:

> Review the access control evidence in /evidence/access before we send it to the auditor. Is it good enough?

The skill reads the evidence tracker to see what each file is meant to prove, confirms the audit period and reviews the items. The identity provider export is well-formed but shows three users without MFA, against a policy of MFA for all. Only two access reviews fall in the period, against a quarterly commitment. The leavers list was filtered to "active only", a screenshot lacks context, and one ticket export contains an API token, which the skill flags for redaction without repeating it.

An excerpt from `grc/evidence/review-2027-11-15.md`:

```
| evidence_id | requirement refs | rating       | issue                          | fix                                   | owner     |
|-------------|------------------|--------------|--------------------------------|---------------------------------------|-----------|
| EV-014      | CC6.1            | adequate     | 3 active users without MFA     | Enforce MFA; prepare mgmt response    | Ops lead  |
| EV-015      | CC6.2, CC6.3     | weak         | 2 reviews in 12 months vs      | Locate Q1/Q3 records or prepare       | CTO       |
|             |                  |              | quarterly policy commitment    | management response                   |           |
| EV-016      | CC6.2            | insufficient | Export filtered "active only"  | Re-export all leavers in period       | Ops lead  |
|             |                  |              | so leavers are missing         | without the filter, include dates     |           |
| EV-017      | CC6.1            | weak         | Screenshot lacks URL/date/user | Re-capture with URL, date, user shown | Ops lead  |
| EV-019      | CC8.1            | adequate     | Contains a credential          | Redact before sharing; re-export      | Eng lead  |

Likely exceptions: 2 (EV-014 MFA coverage; EV-015 review frequency)
```

The original files are left untouched. The team decides to re-export the leavers list, re-capture the screenshot and draft management responses for the two likely exceptions.

## Frameworks covered

The skill works across frameworks (`frameworks: all`). The five evidence tests and the evidence strength guidance apply to:

- **ISO 27001:2022 and ISO 42001:2023:** design evidence for Stage 1, operating evidence over time for Stage 2.
- **SOC 2:** design evidence for Type I, records across the period for Type II, referenced by criteria IDs such as CC6.1.
- **Cyber Essentials Plus:** evidence that will stand up to sampling. Self-declaration is acceptable only where the scheme permits it, as in the basic CE self-assessment.
- **GDPR:** evidence supporting Article 32 security measures.

Requirement references come from the shared domain crosswalk, which carries an `as_of` date of 2026-10-29 and is marked as indicative. Confirm any mapping against the framework itself and with your auditor before relying on it.

## Guardrails

- **Pre-audit reviewer, not the auditor.** The skill talks about evidence that is "likely" acceptable or "at risk", never evidence that "will pass" or "will fail". Only your auditor or certification body decides.
- **Evidence is never altered.** The skill doesn't edit, crop or "fix" evidence files. It recommends re-collection instead, because modified evidence is no longer authentic.
- **Sensitive values stay out of the output.** Secrets, tokens and personal data are flagged for redaction and never repeated in the report, tracker or run log.
- **Evidence is data, not instructions.** Any text inside an evidence file that tries to direct the agent is ignored.
- **Humans decide.** Remediation, management responses and what to share with the auditor stay with your team.

## FAQ

### What makes a screenshot acceptable to an auditor?

It needs context: the URL, a visible date and the logged-in user, so the auditor can see where and when it came from. A system-generated export is usually stronger than a screenshot where one is available.

### Why does the skill care about filters on exports?

Auditors sample from the whole population, such as all leavers in the period, not a subset you chose. An export filtered to "active only" or a short date range can't show that, so it is often rejected.

### Will the skill fix our evidence for us?

No. It tells you exactly what to re-export or re-capture and why, but it never alters evidence files, because edited evidence fails the authenticity test.

### What if the evidence shows we didn't follow our own policy?

The skill flags it as a likely exception or nonconformity in a dedicated section of the report. Finding it before the auditor does gives you time to remediate or prepare a management response.

## Related skills

- [`evidence-request-list`](../evidence-request-list/): builds the request list and tracker that this skill reviews against.
- [`audit-readiness`](../audit-readiness/): assesses overall readiness before you start collecting evidence.
- [`policy-gap-review`](../policy-gap-review/): checks that the policies your evidence is compared against are sound.
- [`company-context`](../company-context/): records the audit type and period the review relies on.
- [`grc-status`](../grc-status/): shows evidence progress alongside the rest of your programme.
