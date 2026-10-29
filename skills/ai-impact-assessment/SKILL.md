---
name: ai-impact-assessment
description: Inventory AI systems and run AI risk and AI system impact assessments aligned to ISO/IEC 42001 (6.1.2, 6.1.4, Annex A.5) with GDPR DPIA triggers — covering AI in your product and staff use of AI tools. Use for "AI risk assessment", "AI impact assessment", "ISO 42001", "AI governance", "is our AI feature risky", "AI inventory", or before launching an AI feature.
license: MIT
metadata:
  author: GRCMANA
  version: 0.1.0
  collection: risk-management
---

# AI Impact Assessment

You help the organisation govern AI responsibly and produce ISO 42001-style evidence:
- an **AI system inventory**
- **AI risk assessments**, which look at risk to the organisation
- **AI system impact assessments**, which look at effects on individuals, groups and society (ISO 42001 6.1.4 and A.5)

Read `references/grc-workspace.md` and `references/iso42001.md` first.

## Modes
- **inventory**: build or update `grc/risks/ai-inventory.csv`, covering product AI features *and* AI tools staff use.
- **assess**: a full impact and risk assessment for one AI system or feature.
- **screen**: a quick triage (10 minutes) to decide whether a full assessment or a GDPR DPIA is needed.

## Context
Read `grc/context/company-profile.md`, especially section 5 (AI). Establish the organisation's **role** for each system: provider, developer, or user/customer of third-party AI.

## Inventory fields
`ai_system_id, name, description, intended_purpose, role (provider/developer/user), model_or_vendor, deployment (product/internal), users, affected_parties, personal_data (y/n), automated_decisions (y/n), human_oversight, risk_tier (low/medium/high), assessment_status, owner, last_reviewed`

## Screening questions (screen mode)
1. Does it process personal data? If yes, consider a DPIA (use the `dpia` skill).
2. Does it make or materially support decisions about people (hiring, credit, access to services, performance)? If yes, it's high impact, and GDPR Art. 22 needs checking.
3. Is its output shown to customers or the public without human review?
4. Could failure, bias or misuse cause harm to individuals, groups or society?
5. Is it in a regulated domain, or could it fall into a high-risk category under the EU AI Act? If so, flag it for legal review.
6. Who supplies the model, and what do their terms say about data use, retention and training?

Two or more "yes" answers, or "yes" to Q2, means you run a full assessment.

## Assess workflow
1. **Describe** the system: its purpose, intended use and foreseeable misuse, users, affected parties, data flows (inputs, training or fine-tuning data, outputs), model and vendor, and the human oversight points.
2. **Impact assessment.** For each affected party, assess potential effects across:
   - fairness and bias
   - transparency and explainability
   - privacy
   - safety and wellbeing
   - security (prompt injection, data leakage, model abuse)
   - accountability and contestability
   - reliability and accuracy
   - environmental impact

   Rate severity and likelihood using `references/risk-methodology.md`, adapting the "Impact" table to harm to people.
3. **AI risk assessment.** Capture the organisational risks: legal and regulatory, contractual, reputational, supplier dependency, data leakage through prompts, IP, hallucination liability.
4. **Controls.** Map proposed treatments to ISO 42001 Annex A, e.g.:
   - A.6.2.4 verification and validation
   - A.6.2.6 operation and monitoring
   - A.8.2 user information
   - A.9 responsible use
   - A.10.3 suppliers

   Plus GDPR or ISO 27001 refs where they're relevant.
5. **Add** the material AI risks to `grc/risks/risk-register.csv` (category `ai`). If it doesn't exist, offer to create it via the `risk-register` conventions.

## Outputs
- `grc/risks/ai-inventory.csv`
- `grc/risks/ai-impact-assessments/<system-slug>-YYYY-MM-DD.md`, built from `assets/ai-impact-assessment-template.md`
- Risk register rows (category `ai`)
- A run log in `grc/runs/`

## Guardrails
- Not legal advice. **EU AI Act classification must be confirmed by legal counsel.**
- Don't overstate risk for low-stakes internal tooling. Proportionality matters.
- Assessment conclusions and residual risk acceptance need human approval.

## References
- `references/grc-workspace.md`
- `references/iso42001.md`
- `references/gdpr.md`
- `references/risk-methodology.md`
