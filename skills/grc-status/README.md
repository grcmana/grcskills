# GRC status: one-page compliance reports for leadership and the board

The `grc-status` skill helps your AI agent turn what's already in your GRC workspace into a one-page, decision-oriented status report. It reads your risk register, policies, evidence tracker, readiness assessments and run logs, then tells leadership three things: are we on track, what's at risk, and what do you need from me? It can also produce an ISO management review pack or a short weekly update for the working team.

## What it does

Most compliance updates fail in one of two ways. Either they are a long list of activity that hides the one decision the board needs to make, or they are optimistic estimates that nobody can trace back to evidence. This skill avoids both. Every number in the report comes from a file in `grc/`, and every RAG rating follows a stated rule.

The skill works in three modes:

- **Exec** (the default): one page for the CEO, leadership team or board, covering framework progress, top risks, overdue items, decisions needed and the next 30 days.
- **Management review**: a pack structured around the ISO 27001 and ISO 42001 clause 9.3 management review inputs, with the decision and output fields left for people to fill in.
- **Weekly**: a short summary of what has changed since the last status, for the people doing the work.

If the workspace is mostly empty, the skill says so plainly and recommends which skill to run next, rather than producing a hollow report.

## Who it's for

- **GRC practitioners and engineers:** the skill does the roll-up you would otherwise build by hand each month, counting statuses, finding overdue treatments and pending acceptances, and pulling the latest readiness figures. You still own the narrative, the judgement on trends and the conversation with leadership.
- **Accidental owners** (founders, CTOs, ops leads): you get a board-ready page in plain English that shows where the programme stands and exactly which decisions are waiting on you, without having to read every register yourself.

## When to use it

- "GRC status", "compliance update", "where are we with ISO?" or "where are we with SOC 2?"
- Preparing a board report or a leadership team update
- A "weekly compliance summary" for the working team
- Gathering management review inputs before an ISO 27001 or ISO 42001 management review (clause 9.3)
- Before an investor, customer or audit conversation where you need a clear position

Don't use it to assess readiness in the first place: run `audit-readiness` to produce the readiness percentages this skill reports. If you have no workspace yet, start with `company-context`.

## How it works

1. **Read the workspace.** The skill reads whatever exists: `grc/context/company-profile.md` (frameworks, target dates, drivers), `grc/risks/risk-register.csv` (bands, overdue treatments, pending acceptances), `grc/policies/` (counts by draft or approved, overdue reviews), `grc/evidence/evidence-tracker.csv` (status counts, overdue and rejected items), the latest `grc/audits/readiness-*.md` per framework, and `grc/runs/` for activity since the last status.
2. **Check there's enough to report.** If the workspace is mostly empty, it tells you and recommends the next skill instead of filling gaps.
3. **Choose the mode.** Exec by default; management review or weekly if you ask.
4. **Apply the RAG rule.** Green means on track for the target date. Amber means at risk but recoverable with a stated action. Red means the target date can't be achieved without a decision.
5. **Build the report.** For exec mode: a one-sentence headline with overall RAG; a framework table (target date, readiness %, RAG, trend); the top five risks with residual score, owner and treatment status; overdue and at-risk items; decisions needed (what, by whom, by when); and three to five commitments for the next 30 days.
6. **Mark the gaps.** Where data is missing, the report says "no data". It never estimates.
7. **Hand over.** It writes the report and the run log, and gives a brief summary in chat. Decisions in the report are for people to take.

## What you get

```
grc/
├── status-YYYY-MM-DD.md                       # exec or weekly mode
├── audits/management-review-YYYY-MM-DD.md     # management-review mode
└── runs/YYYY-MM-DD-grc-status-<slug>.md       # AI run log
```

The **status report** is the one-page summary for leadership or the team. In management-review mode, the **management review pack** covers the clause 9.3 inputs, with the decisions and outputs left blank for the review meeting to complete.

The **run log** records which files were read and written and which decisions are still pending, giving you an audit trail of how the report was produced. You also get a brief summary in chat.

## Worked example

_This scenario is fictional._

Acme Analytics is a fictional 40-person UK B2B SaaS analytics company, three months into an ISO 27001 programme with Cyber Essentials already under way. Its workspace holds a company profile, a risk register, six policies, an evidence tracker and a recent ISO 27001 readiness assessment. Before the quarterly board meeting, the CEO types:

> Give me a GRC status for the board. Where are we with ISO 27001 and Cyber Essentials?

The skill runs in exec mode. It reads the target dates from the profile, the latest readiness percentage from the ISO 27001 readiness assessment, the risk bands and pending acceptances from the register, policy statuses, and evidence statuses from the tracker. There is no readiness assessment for Cyber Essentials, so it reports "no data" for its readiness and RAG rather than guessing, and lists running `audit-readiness` as a next step. An excerpt:

```
Headline: 🟠 ISO 27001 at risk for the March target; recoverable if the
board approves an internal auditor this month.

| Framework        | Target     | Readiness | RAG | Trend   |
|------------------|------------|-----------|-----|---------|
| ISO 27001        | 2027-03-31 | 58%       | 🟠  | up      |
| Cyber Essentials | 2026-12-15 | no data   | no data | no data |

Decisions needed:
1. Accept risk R-007 (legacy reporting server, residual 9) or fund
   its decommissioning. Owner: CTO. By: 2026-11-20.
2. Approve 2 draft policies (access control, supplier security).
   Owner: CEO. By: 2026-11-30.
3. Budget for an independent internal auditor. Owner: CEO. By: 2026-11-30.
```

The overdue section lists three evidence items past their due date and one rejected item. The skill does not fill in the risk acceptance; R-007's `approved_by` stays blank and appears under decisions pending in the run log.

## Frameworks covered

This skill reports on whichever frameworks your company profile selects, so it applies across ISO 27001, ISO 42001, SOC 2, Cyber Essentials and GDPR. It doesn't carry framework packs of its own; framework facts come from the files other skills have already produced.

- **ISO 27001 and ISO 42001, clause 9.3:** management-review mode covers the inputs the clause expects: status of actions from previous reviews, changes in external and internal issues, the needs of interested parties, performance feedback (nonconformities, monitoring results, audit results and objectives), feedback from interested parties, risk assessment results and treatment plan status, and opportunities for improvement.
- **Risk methodology:** risk bands follow the shared 5×5 method (high 15–25, medium 8–14, low 1–7), aligned to ISO 27001 6.1.2 and SOC 2 CC3, unless your organisation has its own methodology in `grc/context/risk-methodology.md`.
- **Evidence standards:** evidence statuses and quality ratings follow the shared evidence standards used across the library.

Where reported figures depend on framework packs with an `as_of` date, check the official source for anything that may have changed since then.

## Guardrails

- **Every number is traceable.** Figures come only from workspace files. Missing data is shown as "no data" and never estimated.
- **A stated RAG rule.** Ratings follow the green, amber and red definitions above, not instinct.
- **Bad news early.** The skill won't soften a red or bury an overdue item. Leadership needs to know while there's still time to act.
- **Humans decide.** Risk acceptances, policy approvals and management review outputs are left for people. Approval fields stay blank or `PENDING`.
- **No claims of conformance.** A high readiness percentage is reported as readiness, never as a sign the organisation has achieved certification.
- **No personal data or secrets.** Owners appear by role or name only.

## FAQ

### What if our workspace is nearly empty?

The skill will say so plainly and recommend the next skill to run, usually `company-context`, `risk-register` or `audit-readiness`. It won't produce a report padded with guesses.

### Where does the readiness percentage come from?

From the latest `grc/audits/readiness-*.md` file for each framework, produced by the `audit-readiness` skill. If there isn't one, the report shows "no data".

### Can it prepare our ISO management review?

Yes. Management-review mode structures the pack around the clause 9.3 inputs for ISO 27001 and ISO 42001. The decisions and outputs are left blank for the meeting to complete and minute.

### How is a weekly update different from the exec report?

The weekly mode is a short summary of what has changed since the last status, aimed at the working team. The exec report is a one-page position for leadership with decisions and commitments.

## Related skills

- [`company-context`](../company-context/): supplies the frameworks, target dates and drivers the status reports against.
- [`audit-readiness`](../audit-readiness/): produces the readiness percentages shown in the framework table.
- [`risk-register`](../risk-register/): provides the top risks, overdue treatments and pending acceptances.
- [`evidence-review`](../evidence-review/): keeps the evidence tracker statuses accurate before you report them.
- [`policy-writer`](../policy-writer/): drafts the policies whose approval status the report tracks.
