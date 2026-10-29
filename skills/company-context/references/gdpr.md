---
framework: EU GDPR (Regulation (EU) 2016/679) and UK GDPR + Data Protection Act 2018
as_of: 2026-10-29
type: law (not a certification)
licence_note: GDPR is EU law; article references used. Not legal advice.
---

# GDPR (EU & UK) — Practitioner Pack

> GRC OS gives practitioner guidance, **not legal advice**. Escalate to a lawyer or DPO for novel processing, cross-border transfers, regulatory contact, or breaches with high risk to individuals.

## What it is
Law governing the processing of personal data. Applies to organisations established in the EU/UK, and to those outside that offer goods or services to, or monitor, people in the EU/UK (Art. 3).
- **UK GDPR** sits alongside the Data Protection Act 2018. The UK has made reforms via the **Data (Use and Access) Act 2025**, which is being phased in. Check ICO guidance for current UK positions on legitimate interests, automated decision-making, cookies and subject access requests.
- There's no "GDPR certification" for organisations in common use. Compliance is shown through **accountability** (Art. 5(2)).

## Roles
- **Controller**: decides the purposes and means of processing. Most of the obligations sit here.
- **Processor**: processes on the controller's documented instructions. Needs an Art. 28 contract (DPA), and its own obligations apply (e.g. Art. 30(2), 32, 33(2)).
- SaaS companies are usually **processors** for customer data and **controllers** for their own employee, marketing and account data.

## Principles (Art. 5)
Lawfulness, fairness and transparency · purpose limitation · data minimisation · accuracy · storage limitation · integrity and confidentiality (security) · **accountability**: be able to demonstrate all of the above.

## Lawful bases (Art. 6)
Consent · contract · legal obligation · vital interests · public task · legitimate interests (document a Legitimate Interests Assessment).
Special category data (Art. 9) and criminal offence data (Art. 10) need an additional condition.

## Individuals' rights (Arts. 12–22)
Information/transparency · access · rectification · erasure · restriction · portability · objection · rights related to automated decision-making. The standard response time is **one month**, extendable in some cases.

## Accountability artefacts (what a customer, auditor or regulator asks for)
| Artefact | Article | Notes |
|---|---|---|
| Record of Processing Activities (RoPA) | 30 | The limited exemption for <250 staff rarely applies in practice to SaaS |
| Privacy notice(s) | 13–14 | Customer-facing, employee and candidate notices |
| Lawful basis register / LIAs | 6 | Often combined with the RoPA |
| Data Processing Agreements | 28 | With customers (as processor) and subprocessors |
| Subprocessor list | 28 | Published, with a change-notification mechanism |
| DPIAs | 35 | Required for high-risk processing (new tech, large-scale special category data, systematic monitoring, profiling with significant effects). Consult the regulator first if high residual risk remains (Art. 36). |
| Security measures | 32 | Risk-appropriate technical and organisational measures. ISO 27001 / SOC 2 / CE evidence helps here. |
| Breach procedure and log | 33–34 | Notify the supervisory authority within **72 hours** of becoming aware, unless the breach is unlikely to result in risk. Tell individuals without undue delay if the risk is high. Log **all** breaches. Processors notify controllers without undue delay. |
| International transfer mechanism | 44–49 | Adequacy, SCCs (EU), the IDTA or UK Addendum (UK), plus transfer risk assessments |
| DPO appointment (if required) | 37–39 | Required for public authorities, large-scale systematic monitoring, or large-scale special category data |
| Data retention schedule | 5(1)(e) | Enforce it, don't just document it |
| Privacy by design and default | 25 | Shown through your SDLC and DPIA process |

## Fines
- EU: up to €20m or 4% of global annual turnover, whichever is higher, for the most serious infringements.
- UK: up to £17.5m or 4%.

## Crossovers
- ISO 27001 A.5.34 covers privacy and protection of PII.
- ISO/IEC 27701 extends an ISMS into a Privacy Information Management System.
- The SOC 2 Privacy category (P1–P8) is optional.
- ISO 42001 A.7 covers data for AI systems. Pair it with a DPIA for AI processing personal data.
