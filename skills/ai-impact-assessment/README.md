# AI impact assessment: inventory and assess your AI systems with your AI agent

The `ai-impact-assessment` skill helps your AI agent build an inventory of the AI your organisation builds and uses, and then assess each system's risks to the organisation and its effects on people. It produces ISO/IEC 42001-style evidence, flags when a GDPR DPIA or legal review is needed, and covers both AI features in your product and the AI tools your staff use every day.

## What it does

Most companies use AI in the product they sell and in the tools their team uses. Customers and auditors ask the same questions about both: what AI do you use, who could it affect, and what have you done about the risks?

The skill separates two things ISO 42001 treats differently. An **AI risk assessment** looks at risk to the organisation, such as legal, contractual and reputational exposure. An **AI system impact assessment** looks at effects on individuals, groups and society.

It works in three modes:

- **Inventory**: builds or updates a register of your AI systems, covering product features and staff tools.
- **Screen**: a ten-minute triage that decides whether a system needs a full assessment, a DPIA, or neither.
- **Assess**: a full impact and risk assessment for one AI system or feature, with controls mapped to ISO 42001 Annex A.

## Who it's for

- **GRC practitioners and engineers:** the skill does the structured groundwork: the inventory, screening, impact table and Annex A mapping. You still own the severity judgements, consultation and the decision to proceed.
- **Accidental owners** (founders, CTOs, product leads): you get a plain-English answer to "is our AI feature risky?" and a documented assessment to show customers or an auditor, without needing to read ISO 42001 first.

## When to use it

- "AI inventory" or "what AI do we use?" when starting AI governance or preparing for ISO 42001
- "Is our AI feature risky?" or "AI impact assessment" before launching an AI feature
- "AI risk assessment" when a customer questionnaire asks how you govern AI
- Adopting a new AI tool for staff, or changing model or vendor

Don't use it as a substitute for a DPIA when an AI system processes personal data in a high-risk way; screen mode will point you to `dpia`, and the two work best together. For the organisation's wider security and privacy risks, use `risk-register`.

## How it works

1. **Context.** The skill reads `grc/context/company-profile.md`, especially the AI section. For each system it establishes your role: provider, developer, or user of third-party AI. Most startups are both, and the role shapes which controls apply.
2. **Inventory.** It records each system's purpose, role, model or vendor, deployment, users, affected parties, personal data and automated decisions, human oversight, risk tier and owner.
3. **Screen.** Six questions: does it process personal data; does it make or materially support decisions about people (such as hiring, credit, access to services or performance); is its output shown to customers or the public without human review; could failure, bias or misuse cause harm; is it in a regulated domain or a possible EU AI Act high-risk category; and what do the model supplier's terms say about data use, retention and training. Two or more "yes" answers, or "yes" to the decisions question, means a full assessment.
4. **Describe.** It documents purpose, intended use and foreseeable misuse, data flows, model and vendor, and human oversight points.
5. **Impact assessment.** For each affected party it rates likelihood and severity of harm across fairness and bias, transparency and explainability, privacy, safety and wellbeing, security (such as prompt injection and data leakage), accountability and contestability, reliability and accuracy, and environmental impact.
6. **Organisational risks.** Legal and regulatory, contractual, reputational, supplier dependency, data leakage through prompts, intellectual property and liability for hallucinated output.
7. **Controls.** Treatments are mapped to ISO 42001 Annex A, with GDPR or ISO 27001 references where relevant.
8. **Register and decision.** Material AI risks are added to the risk register under category `ai`. The proceed decision is left as `PENDING HUMAN DECISION`.

## What you get

```
grc/
├── risks/
│   ├── ai-inventory.csv                            # inventory mode
│   ├── ai-impact-assessments/<system-slug>-YYYY-MM-DD.md   # assess mode
│   └── risk-register.csv                           # rows added, category "ai"
└── runs/YYYY-MM-DD-ai-impact-assessment-<slug>.md  # AI run log
```

The assessment template covers system description, impacts, organisational risks, controls, conclusion and review triggers (such as a model change, new data source or accuracy drift). If no risk register exists, the skill offers to create one.

The run log records what was read and written and which decisions await a human, which is useful ISO 42001 evidence in its own right.

## Worked example

_This scenario is fictional._

Acme Analytics is a fictional 40-person UK B2B SaaS analytics company. It plans to add a churn-risk score for each end user of its customers' accounts, produced by a machine-learning model trained on product activity data. Account managers would see the score next to each end user's name. A DPIA screening has already concluded a DPIA is required. The head of product asks:

> Run a full AI impact assessment on the churn-risk score before we launch.

In assess mode, the skill reads the company profile and records Acme's role as developer and provider of the model. It asks who can see the score, whether anything happens automatically, and how the model will be monitored, then works through the eight impact dimensions. One row of the impact table reads:

```
Dimension:   Fairness & bias
Impact:      Users with irregular activity patterns (part-time staff,
             people on leave) are scored as high churn risk and receive
             less attention or support.
Affected:    Customers' end users        Likelihood: 3   Severity: 3
Score:       9 (Medium)
Mitigation:  Validate the model across activity segments before launch
             (ISO42001:A.6.2.4); monitor score distribution monthly
             (ISO42001:A.6.2.6); explain the score in user documentation
             (ISO42001:A.8.2).
```

Under organisational risks it records a contractual risk: some customer agreements may limit how activity data can be used for new purposes. It adds two rows to `grc/risks/risk-register.csv` under category `ai`, links the assessment to the existing DPIA, and leaves the conclusion as `PENDING HUMAN DECISION` with `approved_by` and `approved_on` blank.

## Frameworks covered

- **ISO/IEC 42001:2023:** clause 4 (determining your role), 6.1.2 (AI risk assessment), 6.1.3 (AI risk treatment), 6.1.4 (AI system impact assessment) and 8.2–8.4 (performing them in practice). Annex A.5 covers assessing impacts of AI systems (the template references A.5.2–A.5.5), with treatments drawn from A.6.2.4 (verification and validation), A.6.2.6 (operation and monitoring), A.8.2 (user information), A.9 (responsible use) and A.10.3 (suppliers).
- **GDPR:** Article 35 DPIA triggers for AI that processes personal data, and the automated decision-making rules: Article 22 in the EU, and Articles 22A–22D in the UK, introduced by the Data (Use and Access) Act 2025 and in effect since 5 February 2026.
- **EU AI Act:** the skill flags systems that may fall into a high-risk category, but classification must be confirmed by legal counsel.

The ISO 42001 and GDPR knowledge packs carry an `as_of` date. AI regulation and guidance are moving quickly, so check the official source for anything that may have changed since then.

## Guardrails

- **Not legal advice.** EU AI Act classification, and any automated decision-making conclusion, needs review by legal counsel or your DPO.
- **Proportionate.** The skill won't overstate risk for low-stakes internal tooling.
- **Humans approve.** Assessment conclusions and acceptance of residual risk need a human decision; approval fields stay blank or `PENDING`.
- **No claims of conformity.** An assessment is evidence towards ISO 42001, not a statement that you meet it or will achieve certification.
- **No secrets or personal data.** The assessment describes categories of people and data, never individuals.

## FAQ

### What is the difference between an AI risk assessment and an AI impact assessment?

A risk assessment looks at risk to your organisation, such as fines, lost contracts or reputational damage. An impact assessment looks at effects on the people, groups and society the system touches. ISO 42001 expects both.

### Do we need to assess the AI tools our staff use, not just our product?

They belong in the inventory, because staff use of AI tools is a common route for data leakage. Screen mode keeps low-stakes tools proportionate.

### Does an AI impact assessment replace a DPIA?

No. If the system processes personal data, screen mode flags whether a DPIA is needed, and the two assessments cover different ground. Run `dpia` alongside it.

### Will this tell us whether our system is high-risk under the EU AI Act?

It flags systems that may be, based on the screening questions. The classification itself must be confirmed by legal counsel.

## Related skills

- [`company-context`](../company-context/): builds the profile, including the AI section this skill reads first.
- [`dpia`](../dpia/): assesses data protection risk when an AI system processes personal data.
- [`risk-register`](../risk-register/): holds the material AI risks this skill adds under category `ai`.
- [`policy-writer`](../policy-writer/): drafts the AI policy and acceptable use rules for staff AI tools.
