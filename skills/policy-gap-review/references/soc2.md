---
framework: SOC 2 (AICPA Trust Services Criteria 2017, with revised points of focus 2022)
as_of: 2026-10-29
type: attestation report (not a certification)
licence_note: Own-words summary. Criteria IDs referenced; AICPA text not reproduced.
---

# SOC 2 — Practitioner Pack

## What it is
An **attestation report** issued by a licensed CPA firm on a service organisation's controls relevant to the Trust Services Criteria (TSC). It's mainly a US market expectation, and a common ask from US enterprise buyers of SaaS. **It is not a certification.** Say "we have a SOC 2 Type II report", not "we are SOC 2 certified".

- **Type I**: controls are suitably designed and implemented **at a point in time**.
- **Type II**: controls are suitably designed **and operated effectively over a period**, typically 3–12 months. The first Type II window is often 3–6 months, then 12 months after that.
- **Bridge letter**: a management letter covering the gap between the report period end and today.

## The report (what buyers read)
1. The auditor's opinion (unqualified, qualified, adverse or disclaimer)
2. Management's assertion
3. **System description**: services, infrastructure, software, people, procedures, data, boundaries, subservice organisations (carve-out vs inclusive method) and **complementary user entity controls (CUECs)**
4. Criteria, controls, tests performed and results (Type II includes exceptions)

## Trust Services Categories
| Category | Required? | Criteria |
|---|---|---|
| Security (Common Criteria) | **Always** | CC1–CC9 |
| Availability | Optional | A1 |
| Processing Integrity | Optional | PI1 |
| Confidentiality | Optional | C1 |
| Privacy | Optional | P1–P8 |

Pick optional categories based on customer commitments and contracts, not to "look comprehensive". Each one adds audit scope and cost.

## Common Criteria (own words)
| Series | Theme | What it covers |
|---|---|---|
| CC1 | Control environment | Integrity and ethics, board/leadership oversight, structure, competence, accountability (COSO-based) |
| CC2 | Communication & information | Quality information, internal and external communication of security responsibilities |
| CC3 | Risk assessment | Objectives, risk identification and analysis, fraud risk, assessing significant change |
| CC4 | Monitoring | Ongoing and separate evaluations, communicating deficiencies |
| CC5 | Control activities | Selecting and deploying controls, technology controls, policies and procedures |
| CC6 | Logical & physical access | Access provisioning and deprovisioning, authentication, access reviews, encryption, boundary protection, endpoint and malware protection |
| CC7 | System operations | Vulnerability detection, monitoring, incident detection, response and recovery |
| CC8 | Change management | Authorised, tested, approved changes to infrastructure, data and software |
| CC9 | Risk mitigation | Business disruption risk, vendor and business partner risk |

## Evidence auditors sample most (Type II)
- Joiner / mover / leaver tickets matched against HR records and access removal times
- Quarterly access reviews with reviewer sign-off
- Change tickets: PR approvals, testing, separation of duties for production deploys
- Vulnerability scans and pen test reports, with remediation within stated SLAs
- Incident tickets and post-incident reviews, or evidence of a tabletop exercise if there were no incidents
- Security awareness training completion
- Background checks (where policy requires them)
- Vendor reviews (SOC reports from critical subprocessors, reviewed with CUECs considered)
- Backup and restore tests
- Risk assessment (at least annually) and board or leadership oversight minutes

## Common failure points
- Writing controls the team can't operate consistently for 6–12 months. Fewer, real controls beat many aspirational ones.
- A policy that says "quarterly" when reviews actually happen annually, which becomes an exception
- No population evidence (auditors sample from complete populations, e.g. all leavers in the period)
- Treating a compliance-automation platform as the controls. The platform collects evidence; your people operate the controls.
