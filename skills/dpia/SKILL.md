---
name: dpia
description: Screen for and draft a GDPR Data Protection Impact Assessment (Art. 35, UK & EU) — describing processing, assessing necessity and proportionality, identifying risks to individuals' rights and freedoms, and recording mitigations and residual risk for DPO/legal review. Use for "DPIA", "do we need a DPIA", "privacy impact assessment", "PIA", "new feature processes personal data", or before launching processing involving new tech, profiling, monitoring or special category data.
license: MIT
metadata:
  author: GRCMANA
  version: 0.1.0
  collection: frameworks
---

# DPIA (Data Protection Impact Assessment)

You help the organisation decide whether a DPIA is needed, then draft one that a DPO or privacy lead can review and sign off. A DPIA looks at **risk to individuals**, not risk to the company.

Read `references/grc-workspace.md` and `references/gdpr.md` first.

> Not legal advice. A DPIA conclusion, and any prior consultation with the regulator (Art. 36), needs review by the DPO or privacy lead, and legal counsel where appropriate.

## Modes
- **screen**: decide whether a DPIA is required or recommended. This is the default for a new project.
- **draft**: a full DPIA.
- **review**: an existing DPIA after change, or on its review date.

## Screening
A DPIA is **required** for processing likely to result in high risk (Art. 35). Indicators, where two or more usually means you need one:
- evaluation or scoring, including profiling
- automated decisions with legal or similarly significant effect
- systematic monitoring
- sensitive or special category data, or data about criminal offences
- large-scale processing
- matching or combining datasets
- data about vulnerable people, including children and employees
- innovative technology, **including AI**
- processing that prevents people exercising rights or using a service
- invisible processing, or tracking location or behaviour

Also check the supervisory authority's published list of processing that requires a DPIA (ICO for the UK, the relevant EU authority otherwise). Record the screening outcome and its rationale even when the answer is "not required". That is accountability evidence.

## Draft workflow
1. **Describe the processing:** nature, scope, context and purposes; the data categories and subjects; sources; recipients and processors; retention; international transfers; the systems involved. Use `grc/context/company-profile.md`, plus questions.
2. **Consultation:** who has been or should be consulted (DPO, security, processors, data subjects or their representatives where appropriate).
3. **Necessity and proportionality:**
   - lawful basis (Art. 6, plus Art. 9 if special category data)
   - purpose limitation
   - data minimisation
   - accuracy
   - retention
   - transparency (privacy notice updates)
   - how rights are supported
   - processor contracts (Art. 28)
   - transfer mechanism
4. **Risks to individuals.** For each one, set out:
   - the source and the potential harm (e.g. discrimination, identity fraud, financial loss, distress, loss of control over data, reputational damage, physical harm)
   - likelihood (remote / possible / probable) and severity (minimal / significant / severe), giving overall low / medium / high
5. **Measures:** mitigations per risk, the effect on the risk, and residual risk. Link security measures to ISO 27001 / SOC 2 controls where they exist.
6. **Outcome:** residual risk summary. If **high residual risk remains**, flag that prior consultation with the supervisory authority is required (Art. 36) before processing starts.
7. **Sign-off block:** measures approved by, residual risk approved by, DPO advice, whether the DPO advice was accepted, and review date. Leave all of these blank for humans to fill in.

## Outputs
- `grc/audits/dpia/<project-slug>-screening-YYYY-MM-DD.md` (screen mode)
- `grc/audits/dpia/<project-slug>-YYYY-MM-DD.md`, built from `assets/dpia-template.md`
- Optionally, risk register rows (category `privacy`)
- A run log in `grc/runs/`

## Guardrails
- Don't record real individuals' personal data in the DPIA. Describe categories.
- Don't conclude "low risk" to make a project pass. Be candid. The DPIA protects the organisation too.
- For AI processing, also suggest the `ai-impact-assessment` skill.

## References
- `references/grc-workspace.md`
- `references/gdpr.md`
- `references/risk-methodology.md`
