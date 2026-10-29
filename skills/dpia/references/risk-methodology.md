# Risk Methodology (default)

A simple, defensible, scenario-based method. It's aligned to ISO 27001 6.1.2 (repeatable, consistent and comparable results), informed by ISO/IEC 27005 and ISO/IEC 23894, and works for SOC 2 CC3. Organisations can replace it with their own. If `grc/context/risk-methodology.md` exists, use that instead.

## 1. Risk statement
Write each risk as a scenario:
> **[Threat/cause]** exploits **[vulnerability/condition]** affecting **[asset/process]**, leading to **[impact on confidentiality, integrity, availability, privacy, or people (for AI)]**.

Bad: "Ransomware". Good: "Ransomware delivered via phishing encrypts the shared drive because backups are online and untested, halting customer onboarding for days."

## 2. Scoring: 5×5
**Likelihood (L)**, over the next 12 months, given current controls:
| Score | Label | Guide |
|---|---|---|
| 1 | Rare | Not expected; < 5% |
| 2 | Unlikely | Could happen; 5–25% |
| 3 | Possible | Might well happen; 25–50% |
| 4 | Likely | Probably will; 50–80% |
| 5 | Almost certain | Expected; > 80% or already happening |

**Impact (I)**: take the highest applicable row:
| Score | Label | Financial | Customers / reputation | Legal / regulatory | Operations |
|---|---|---|---|---|---|
| 1 | Negligible | < 0.1% revenue | Unnoticed | None | < 1 hr disruption |
| 2 | Minor | 0.1–1% | Few customers, quickly resolved | Minor breach, no notification | < 1 day |
| 3 | Moderate | 1–3% | Several customers; complaints | Notifiable incident, likely no action | 1–3 days |
| 4 | Major | 3–10% | Key customer loss; press | Regulator investigation; contract breach | 3–7 days |
| 5 | Severe | > 10% | Existential; widespread loss of trust | Significant fine or enforcement | > 7 days or permanent |

**Score = L × I** (1–25).

| Band | Score | Default response |
|---|---|---|
| 🔴 High | 15–25 | Treat now. Exec owner. Review monthly. |
| 🟠 Medium | 8–14 | Treat within plan. Review quarterly. |
| 🟢 Low | 1–7 | Accept or monitor. Review annually. |

Risk appetite default: residual risk should be **≤ 7**, unless formally accepted by an executive with `approved_by`.

## 3. Inherent vs residual
- **Inherent**: the score assuming the key controls fail or are absent.
- **Residual**: the score with the current controls actually in place. Don't count planned controls.
- **Target**: the expected score after treatment is complete.

## 4. Treatment options
**Modify** (mitigate with controls) · **Retain** (accept) · **Avoid** (stop the activity) · **Share** (transfer, e.g. insurance or contract).
Each treated risk needs controls with framework references, an owner, a due date, and a target score.

## 5. Acceptance
Accepted risks need a rationale, an `approved_by` (a named executive) and `approved_on`, plus a review date. Claude never fills in approval fields.

## 6. Review cadence
- Full reassessment at least annually.
- Reassess on significant change: new product, new market, new supplier, M&A, major incident, new framework.
- Highs monthly, mediums quarterly.

## Register columns
`risk_id, title, scenario, category, asset_or_process, owner, likelihood_inherent, impact_inherent, score_inherent, existing_controls, likelihood_residual, impact_residual, score_residual, band, treatment, planned_controls, framework_refs, target_score, due_date, status, approved_by, approved_on, last_reviewed, next_review`

Categories: `security`, `privacy`, `ai`, `third-party`, `operational`, `compliance`, `people`.
