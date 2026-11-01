# Evidence request list: control-mapped evidence plans with your AI agent

The `evidence-request-list` skill helps your AI agent plan exactly what audit evidence to collect, from which system, by whom, how often and by when. It produces a deduplicated evidence tracker (CSV) and a per-owner request list for ISO 27001, SOC 2, Cyber Essentials Plus, GDPR and ISO 42001, mapping each artefact to every requirement it serves so you collect it once and use it many times.

## What it does

Evidence collection is where audit preparation loses weeks. Requests are vague, the same export is gathered three times for three frameworks, and a missed quarterly review goes unnoticed until the auditor samples it.

The skill writes one specific, collectable request per real artefact, with a source system, period, frequency, owner and due date. It works in three modes:

- **Plan** (the default): builds the evidence tracker for your selected frameworks and audit type.
- **PBC**: turns a "provided by client" request list that your auditor has sent you into a tracker with owners and source systems mapped.
- **Refresh**: rolls the tracker forward to a new period, resetting status, keeping recurring items and updating due dates.

The tracker records where evidence lives, not the evidence itself.

## Who it's for

- **GRC practitioners and engineers:** the skill does the cross-framework mapping and deduplication, marks population-based items and flags automation candidates. You still confirm scope, chase owners and judge what comes back.
- **Accidental owners** (founders, CTOs, ops leads): you get a clear list of who needs to export what from which tool, and by when, that you can forward to each person, without needing to read the control set first.

## When to use it

Typical triggers:

- "What evidence do we need?" or "prepare for the auditor"
- "Evidence list", "evidence collection plan" or "set up evidence tracking"
- "PBC list", when your auditor has sent their request list and you need to assign it
- Straight after an `audit-readiness` assessment, to turn the gaps into an evidence plan
- The start of a new SOC 2 Type II period or ISO surveillance cycle, to refresh the tracker

Don't use it to check evidence already collected; that is `evidence-review`. If you don't yet know your frameworks or audit type, run `company-context` and `audit-readiness` first.

## How it works

1. **Context.** The skill reads `grc/context/company-profile.md` for your frameworks, tooling (the source systems) and owners, and any `grc/audits/readiness-*.md` assessment so it can focus on the gaps. If there is no profile, it asks at most five questions and suggests running `company-context`.
2. **Requirements in scope.** It identifies the requirements for your frameworks and audit type from the framework packs.
3. **Group by domain and deduplicate.** Using the shared crosswalk, it writes one request per real artefact and maps it to every framework it serves. For example, an identity provider export of all users with MFA status maps to ISO 27001 A.5.17 and A.8.5, SOC 2 CC6.1 and the Cyber Essentials user access control requirement.
4. **Make each request collectable.** Each request names the source system from your profile ("Google Workspace Admin, Users, export with 2SV status", not "identity system"), the period or date (the full period with samples for Type II; current state for Stage 1), the frequency (one-off, per event, monthly, quarterly or annual), the owner by role, and a due date worked back from the audit date.
5. **Mark population-based items**, such as a list of all leavers in the period with termination dates. Auditors sample from these, so they must be complete.
6. **Flag automation candidates**: evidence that could later come from an API or connector, such as the identity provider, cloud configuration, ticketing, MDM or code host.

A human decides scope, confirms owners and sends the requests.

## What you get

```
grc/
├── evidence/
│   ├── evidence-tracker.csv               # the tracker, IDs E-001 onwards
│   └── request-list-YYYY-MM-DD.md         # requests grouped by owner
└── runs/YYYY-MM-DD-evidence-request-list-<slug>.md   # AI run log
```

- **`evidence-tracker.csv`** uses the columns in the skill's template: `evidence_id, request, domain, framework_refs, owner, source_system, frequency, period_or_date, population_based, automation_candidate, location, status, quality_rating, reviewer_notes, due_date, last_collected`. IDs run from `E-001` and are never renumbered, so references stay stable across refreshes.
- **`request-list-YYYY-MM-DD.md`** is the human-friendly version, grouped by owner, so you can send each person their own section.
- **A summary in chat**: the total number of requests, how many were deduplicated across frameworks, the owners carrying the most load, the earliest due items, and the automation candidates.
- **The run log** records the files read and written and anything waiting for a human decision.

## Worked example

_This scenario is fictional._

Acme Analytics is a fictional 40-person UK B2B SaaS analytics company. It has just run a readiness assessment for ISO 27001 Stage 1 and is also preparing a first SOC 2 Type I report, with both audits planned for March 2027. Its profile lists Google Workspace, AWS, GitHub and Jira. The CTO asks the agent:

> Build our evidence list for ISO 27001 Stage 1 and SOC 2 Type I. Both audits are in March. Focus on the gaps from the readiness report.

In plan mode, the skill reads the profile and `grc/audits/readiness-iso27001-2026-11-02.md`. Both audits look at design at a point in time, so it asks for current-state evidence. Grouping by domain means one access review record serves both frameworks, and due dates work back from the earlier audit.

Its chat summary reads, in part:

```
58 requests across 16 domains; 23 serve both ISO 27001 and SOC 2.
Top owners by load: CTO (17), IT lead (14), Head of People (9).
Earliest due: E-004 SoA approval record, E-011 MFA export (2026-12-04).
Automation candidates: 12 (Google Workspace, AWS, GitHub, Jira).
```

Two rows from `grc/evidence/evidence-tracker.csv`:

```
evidence_id,request,domain,framework_refs,owner,source_system,frequency,period_or_date,population_based,automation_candidate,location,status,quality_rating,reviewer_notes,due_date,last_collected
E-011,Export of all users with 2SV status,Identity & access control,"ISO27001:A.5.17,A.8.5; SOC2:CC6.1",IT lead,Google Workspace Admin > Users > export with 2SV status,quarterly,current,yes,yes,TBC,requested,,,2026-12-04,
E-019,Record of most recent user access review with reviewer sign-off,Identity & access control,"ISO27001:A.5.18; SOC2:CC6.2",CTO,Jira (access review ticket),quarterly,current,no,no,TBC,requested,,,2026-12-18,
```

The team completes `location`, `quality_rating` and `reviewer_notes` as evidence comes in.

## Frameworks covered

- **ISO 27001:2022:** the mandatory documented information in clauses 4–10, such as scope (4.3), policy (5.2), SoA (6.1.3 d), internal audit (9.2) and management review (9.3), plus the Annex A controls you have selected. SoA exclusions are not requested.
- **SOC 2:** the Common Criteria CC1–CC9 and only the optional categories you have selected. Type I asks for evidence at a point in time; Type II asks for records across the period, typically 3–12 months, with populations to sample from.
- **Cyber Essentials Plus:** evidence for the five controls under Requirements v3.3 and the Danzell question set, including MFA on cloud services and patching within 14 days, ahead of the hands-on technical audit.
- **GDPR (UK and EU):** the accountability artefacts, such as the RoPA (Article 30), DPAs and subprocessor list (Article 28), DPIAs (Article 35) and the breach log (Articles 33–34).
- **ISO 42001:2023:** the minimum artefacts for an AI management system, such as the AI system inventory, AI policy (5.2), impact assessments (6.1.4) and the SoA against Annex A.

Requests are framed around the five evidence tests: relevant, complete, dated, attributable and authentic. The framework packs and the domain crosswalk carry an `as_of` date, and the crosswalk mappings are indicative, so confirm them against the framework and check the official source for anything that may have changed.

## Guardrails

- **Locations, not evidence.** The tracker records where an artefact lives. It never holds secrets, credentials or individuals' personal data.
- **Nothing out of scope.** The skill won't request evidence for controls you have excluded, such as ISO SoA exclusions or SOC 2 categories you haven't selected.
- **Own words unless you supply theirs.** Requirements are paraphrased with their IDs. The auditor's wording is used only in PBC mode, when you provide their list.
- **Owners by role.** Owners are recorded by role or name only, and unknown details are written as `TBC`, not invented.
- **Humans decide.** The skill plans the evidence; people collect it, judge its quality and agree it with the auditor.

## FAQ

### What is a PBC list?

"Provided by client" is the list of documents and records an auditor asks you to supply. In PBC mode the skill takes the list your auditor sends and turns it into a tracker with owners and source systems.

### How does one piece of evidence cover several frameworks?

Each request is mapped to every requirement it serves in the `framework_refs` column, using the domain crosswalk. An identity provider export with MFA status, for example, can serve ISO 27001, SOC 2 and Cyber Essentials Plus at once.

### Should we upload the evidence into the tracker?

No. Keep evidence in your system of record, such as a shared drive or GRC platform, and record its location in the tracker. Redact secrets and unnecessary personal data before sharing anything.

### What happens when a new audit period starts?

Run refresh mode. It resets status, keeps recurring items and updates due dates, without renumbering the evidence IDs.

## Related skills

- [`audit-readiness`](../audit-readiness/): identifies the gaps that the evidence plan focuses on.
- [`evidence-review`](../evidence-review/): checks collected evidence for quality and updates the tracker before the auditor sees it.
- [`company-context`](../company-context/): supplies the frameworks, source systems and owners the requests are built from.
- [`cyber-essentials-scoping`](../cyber-essentials-scoping/): builds the device and cloud inventory that Cyber Essentials Plus evidence depends on.
- [`grc-status`](../grc-status/): reports evidence progress and overdue items to leadership.
