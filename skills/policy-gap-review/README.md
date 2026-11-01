# Policy gap review: check your policies the way an auditor would

The `policy-gap-review` skill helps your AI agent review your existing security, privacy and AI policies against ISO 27001, SOC 2, Cyber Essentials, GDPR and ISO 42001 expectations. It produces a dated gap review with a coverage matrix, a severity-rated findings table and a list of quick wins, so you can fix the problems before an auditor or customer finds them.

## What it does

Most policy sets look fine until someone reads them against the framework and against what the company actually does. Then the problems appear: a topic nobody covered, a missing approval date, a "monthly" review that happens yearly, or a device rule that contradicts real practice. Under SOC 2 Type II, each unkept commitment can become an exception.

The skill reviews in the order an auditor would: coverage first, then quality, then consistency with reality. It works in three modes:

- **Set** (the default): reviews the whole policy set for coverage against your selected frameworks.
- **Single**: a deep review of one policy.
- **Annual**: the annual review cycle, checking currency, changes in the organisation or the frameworks, and review and approval dates.

Every finding is rated Major, Minor or Observation and comes with a recommendation, so you know what to fix first.

## Who it's for

- **GRC practitioners and engineers:** the skill does the line-by-line read, the mapping to clause and control IDs and the cross-checks between policies. You still judge severity in context and agree fixes with policy owners.
- **Accidental owners** (founders, CTOs, ops leads): you get a plain answer to "are our policies audit-ready?" with a short list of what to fix and why, without needing to know the frameworks first.

## When to use it

Typical triggers:

- "Review our policies" or "are our policies audit-ready?" before a Stage 1 audit, a SOC 2 Type I or the start of a Type II period
- "Gap check this policy" for a single document you inherited, bought or drafted
- "Policy review" as part of the annual review cycle
- After a significant change, such as a new device approach, a new framework or a reorganisation

Don't use it if you have no policies yet; use `policy-writer` in plan mode to work out what you need. For a view of your whole programme rather than its documents, use `audit-readiness`.

## How it works

1. **Read the inputs.** The skill reads policies in `grc/policies/`, or files and folders you point it to (Markdown, DOCX or PDF), in full. It reads `grc/context/company-profile.md` for your framework selection and actual practices. If there is no profile, it asks at most five questions and suggests running `company-context`. Optionally, it reads an evidence tracker or risk register to check that policy claims match reality.
2. **Coverage (set mode).** It maps each policy to the domains in its framework crosswalk and the expectations in its policy catalogue, and reports uncovered requirements per framework, for example "No supplier security coverage → ISO 27001 A.5.19–A.5.23, SOC 2 CC9.2".
3. **Document control.** It checks each policy for an owner, an approver and approval date, a version, a review cycle that isn't overdue, a classification and revision history.
4. **Statement quality.** For each statement it checks testability (can an auditor ask "show me"?), keepability (frequencies or SLAs that look unrealistic for your size, flagged as Type II exception risks), specificity (undefined words such as "appropriate", "regularly" or "where possible") and procedural detail that should move out of the policy.
5. **Consistency.** It looks for contradictions between policies (such as differing password rules), contradictions with practice in your profile, and, under Cyber Essentials, anything a policy permits that the scheme fails on.
6. **Framework must-haves.** For example, ISO 27001 5.2 policy content, GDPR breach notification and data subject request handling, and an ISO 42001 AI policy aligned to your AI role.
7. **Report and offer fixes.** It writes the gap review, then offers to fix specific findings using the `policy-writer` conventions. You decide: edits are made only with your go-ahead, and each edited policy gets a version bump and a revision history entry.

## What you get

```
grc/
├── policies/gap-review-YYYY-MM-DD.md            # the gap review
└── runs/YYYY-MM-DD-policy-gap-review-<slug>.md  # AI run log
```

The gap review contains:

- an executive summary of three to five lines
- a coverage matrix: each domain against each selected framework, showing the policy that covers it or the gap
- a findings table with `id, policy, section, finding, severity, framework_refs, recommendation`
- quick wins: findings you can fix in under an hour each

The run log records which files the skill read and wrote, and the decisions still waiting for a human: an audit trail of how the review was produced, useful for ISO 42001 and for any auditor who asks.

## Worked example

_This scenario is fictional._

Acme Analytics is a fictional 40-person UK B2B SaaS analytics company with ISO 27001, SOC 2 and GDPR in scope. It has five policies, written two years ago from a template pack, and its Stage 1 audit is ten weeks away. The head of operations asks:

> Are our policies audit-ready? Our Stage 1 is in ten weeks.

In set mode, the skill reads all five policies in full and the company profile, which records that staff use their own laptops without mobile device management (MDM). It maps the policies to the crosswalk domains and finds no coverage for suppliers or for secure development and change. It then checks document control, statement quality and consistency. Part of the findings table reads:

```
id   | policy          | section | finding                                  | severity | framework_refs           | recommendation
F-01 | (none)          | -       | No supplier security coverage, including | Major    | ISO 27001 A.5.19-A.5.23; | Add a supplier section or
     |                 |         | cloud and AI vendors                     |          | SOC 2 CC9.2; GDPR Art. 28| standalone policy
F-03 | Info Security   | 4.2     | Says MDM on all devices; profile records | Major    | ISO 27001 A.8.1;         | Align policy with real
     |                 |         | BYOD without MDM                         |          | SOC 2 CC6.8              | practice or adopt MDM
F-06 | Incident Resp.  | 3.1     | No personal data breach handling or      | Major    | GDPR Arts. 33-34;        | Add breach assessment and
     |                 |         | 72-hour notification step                |          | ISO 27001 A.5.24-A.5.28  | notification statements
F-09 | Access Control  | 3.5     | "Monthly" access reviews; size and       | Minor    | SOC 2 CC6.2, CC6.3       | Commit to a frequency
     |                 |         | records suggest this is not sustained    |          |                          | the team can sustain
F-11 | All             | header  | No approval date or review cycle         | Minor    | ISO 27001 5.2            | Complete document control
```

The executive summary leads with the coverage gaps and the MDM contradiction, as the findings most likely to cause a nonconformity. Quick wins include completing document control and replacing "regularly" with defined frequencies. The skill then offers to draft the supplier section and fix F-03 and F-06 using `policy-writer`, and waits for the go-ahead.

## Frameworks covered

- **ISO 27001:2022:** clause 5.2 (information security policy content) and the Annex A controls that policies should address, including A.5.15–A.5.18 (access), A.5.19–A.5.23 (suppliers and cloud), A.5.24–A.5.28 (incidents), A.8.8 (vulnerabilities) and A.8.25–A.8.32 (development and change).
- **SOC 2:** the Common Criteria CC1–CC9, with attention to commitments that would become Type II exceptions.
- **Cyber Essentials (Requirements v3.3):** policies that permit unsupported software, cloud services without MFA, or patching slower than 14 days.
- **UK GDPR and EU GDPR:** accountability (Articles 5(2) and 24), processors (Article 28), breach notification within 72 hours (Articles 33–34) and data subject request handling.
- **ISO 42001:2023:** an AI policy (clause 5.2 and A.2) aligned to your role as an AI provider, user or both.

Each framework pack carries an `as_of` date, and the crosswalk mappings are indicative. Frameworks change (Cyber Essentials usually every April), so check the official source for anything that may have moved since then.

## Guardrails

- **Expectations, not verdicts.** The skill reviews against framework expectations and never says a policy "complies" or that you meet a standard.
- **Targeted fixes only.** It doesn't rewrite policies wholesale unless asked, and it edits nothing without your go-ahead.
- **Humans approve.** Approval fields stay blank, and decisions pending are listed in the run log.
- **No standard text.** It may quote short fragments of your own policies, but never ISO or AICPA text; references are IDs only.
- **Not legal advice.** GDPR findings on breach handling or privacy documents should be checked with your DPO or legal counsel.
- **No secrets or personal data.** Findings refer to roles and documents, not individuals.

## FAQ

### What's the difference between a Major and a Minor finding?

A Major is missing required coverage, or a contradiction with practice that would likely cause a nonconformity or exception. A Minor is weak wording, missing document control or an overdue review; an Observation is an improvement opportunity.

### Can it review policies in Word or PDF?

Yes. It reads Markdown, DOCX and PDF files, either in `grc/policies/` or wherever you point it.

### Will it fix the problems for me?

It offers to, using the `policy-writer` conventions, but only edits with your go-ahead. Each changed policy gets a version bump and a revision history entry.

### Does a clean review mean we'll pass the audit?

No. A review with no Major findings reduces the risk of policy findings, but the audit also tests whether you operate what the policies say. Use `audit-readiness` and `evidence-review` for that side.

## Related skills

- [`policy-writer`](../policy-writer/): drafts missing policies and applies the fixes this review recommends.
- [`company-context`](../company-context/): builds the profile the review checks policies against.
- [`audit-readiness`](../audit-readiness/): assesses readiness across your whole programme, not just its documents.
- [`evidence-review`](../evidence-review/): checks whether evidence backs up what the policies commit to.
- [`risk-register`](../risk-register/): an optional input for checking that policy claims match reality.
