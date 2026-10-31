# DPIA: data protection impact assessments with your AI agent

The `dpia` skill helps your AI agent decide whether a new project needs a GDPR data protection impact assessment, and then drafts one that your data protection officer (DPO) or privacy lead can review and sign off. It covers both UK GDPR and EU GDPR, works from your real company context, and keeps the focus where the law puts it: on risk to the people whose data you process, not risk to your company.

## What it does

A DPIA is the record that shows you thought about privacy before you started a risky kind of processing, not after a complaint arrived. Under Article 35 it is mandatory when processing is likely to result in a high risk to individuals, and it is good practice well beyond that. In reality, most teams either skip the screening step or produce a long document that nobody reads.

The skill works in three modes:

- **Screen** (the default for a new project): checks the processing against the high-risk indicators and your regulator's published list, then records whether a DPIA is required, recommended or not needed, and why.
- **Draft**: produces a full DPIA covering the description of processing, consultation, necessity and proportionality, risks to individuals, measures, residual risk and a blank sign-off block.
- **Review**: revisits an existing DPIA when the processing changes or the review date arrives.

Recording a "not required" outcome with its rationale matters as much as a full assessment. It is accountability evidence that you asked the question.

## Who it's for

- **GRC practitioners and privacy professionals:** the skill does the structured first draft, cross-references security measures to your ISO 27001 or SOC 2 controls, and leaves the judgement calls, consultation and sign-off with you.
- **Accidental owners** (founders, CTOs, product leads): you get a plain-English answer to "do we need a DPIA for this feature?" and, if you do, a properly structured draft to take to your DPO or adviser, without needing to know Article 35 first.

## When to use it

Use it before you start processing, ideally at the design stage, when changes are still cheap. Typical triggers:

- "Do we need a DPIA for this?" or "privacy impact assessment" for a new feature or product
- Introducing AI or other innovative technology that uses personal data
- Profiling, scoring or automated decisions that significantly affect people
- Systematic monitoring of employees, customers or public spaces
- Special category data (such as health) or data about children or other vulnerable people
- Combining datasets from different sources, or processing at large scale
- A significant change to processing that already has a DPIA

Don't use it for a general privacy programme review or a records of processing exercise; those belong in `company-context` and `audit-readiness`. If the project is an AI system, run `ai-impact-assessment` as well: the DPIA covers data protection, while the AI impact assessment covers wider impacts on people.

## How it works

1. **Context.** The skill reads `grc/context/company-profile.md` silently. If there is no profile, it asks at most five questions and suggests running `company-context`.
2. **Screening.** It checks the processing against the Article 35 high-risk indicators. Where two or more apply, a DPIA is usually required. It reminds you to check the supervisory authority's list: the ICO for the UK, or the relevant EU authority.
3. **Describe the processing.** Nature, scope, context and purposes; data categories and data subjects; sources, recipients and processors; retention; international transfers; and the systems involved.
4. **Consultation.** Who has been, or should be, consulted: the DPO, security, processors, and data subjects or their representatives where that is appropriate.
5. **Necessity and proportionality.** Lawful basis (Article 6, plus Article 9 for special category data), purpose limitation, minimisation, accuracy, retention, transparency, rights, processor contracts (Article 28) and the transfer mechanism.
6. **Risks to individuals.** Each risk gets a source, a potential harm (for example discrimination, financial loss, distress or loss of control over data), a likelihood and a severity.
7. **Measures and residual risk.** Mitigations per risk, their effect, and the residual risk, with security measures linked to your existing controls.
8. **Outcome.** If high residual risk remains, the skill flags that prior consultation with the regulator is required under Article 36 before processing starts.
9. **Sign-off.** Measures approval, residual risk approval, DPO advice and review date are left blank for people to complete.

## What you get

```
grc/
├── audits/dpia/
│   ├── <project>-screening-YYYY-MM-DD.md   # screen mode
│   └── <project>-YYYY-MM-DD.md             # draft mode, from the DPIA template
├── risks/risk-register.csv                 # optional rows, category "privacy"
└── runs/YYYY-MM-DD-dpia-<project>.md       # AI run log
```

The run log records which files the skill read and wrote, plus the decisions still waiting for a human. That gives you an audit trail showing how AI was used to produce the assessment, which is useful evidence for ISO 42001 and a good answer to any auditor who asks how a document was produced.

## Worked example

_This scenario is fictional._

A 40-person B2B analytics company wants to add a "churn risk" score to its product. The score uses customers' end-user activity data and a machine-learning model, and account managers would see it next to each user's name. The head of product asks the agent:

> We're adding an ML churn-risk score per end user. Do we need a DPIA?

In screen mode, the skill reads the company profile, asks two follow-up questions (whether the score will drive any automated action, and whether the company acts as controller or processor for this data), then records its screening. Three indicators apply: evaluation or scoring, innovative technology (machine learning), and large-scale processing of behavioural data. Its conclusion is that a DPIA is required, with the rationale written down.

The team asks for a draft. One risk row reads, in part:

```
Risk: End users are scored without knowing, and account managers treat
      a high score as a reason to restrict support.
Harm: Loss of control over data; unfair treatment.   Likelihood: possible
Severity: significant   Overall: medium
Measures: update the privacy notice; no automated action on the score;
          human review before any account decision; quarterly bias check.
Residual: low (pending DPO review)
```

The skill also notes that the controller-or-processor question changes who must carry out the DPIA, flags the UK rules on automated decision-making (Articles 22A–22D, introduced by the Data (Use and Access) Act 2025) for the DPO's attention, and suggests running `ai-impact-assessment` on the model itself. The sign-off block is left empty.

## Frameworks covered

- **UK GDPR and EU GDPR:** Article 35 (when a DPIA is required and what it must contain), Article 36 (prior consultation), Articles 5, 6 and 9 (principles and lawful bases), Article 25 (privacy by design and default) and Article 28 (processor contracts). For the UK, it reflects the Data (Use and Access) Act 2025 changes, including Articles 22A–22D on automated decisions.
- **ISO 27001 and SOC 2:** security measures in the DPIA are linked to existing controls where you have them.
- **ISO 42001:** pairs with the AI impact assessment when AI processes personal data.

The GDPR knowledge pack carries an `as_of` date. UK data protection law and ICO guidance are still changing, so check the official source for anything that may have moved since then.

## Guardrails

- **Not legal advice.** The conclusion, and any decision to consult the regulator, needs review by your DPO or privacy lead, and legal counsel where appropriate.
- **No real personal data in the DPIA.** It describes categories of data and data subjects, never individuals.
- **Candid by design.** The skill won't downgrade a risk to "low" to help a project through. A DPIA that understates risk protects nobody.
- **Humans approve.** Approval fields and the sign-off block are always left blank or marked `PENDING`.

## FAQ

### Is a DPIA legally required for every project?

No. It is required when processing is likely to result in a high risk to individuals. The skill's screen mode checks that and records the outcome, which is worth keeping even when the answer is "not required".

### Can an AI agent write our DPIA for us?

It can write a well-structured first draft quickly. The assessment of risk, the consultation and the sign-off remain the responsibility of your organisation and its DPO.

### What happens if high risk remains after mitigation?

Under Article 36 you must consult the supervisory authority before starting the processing. The skill flags this clearly in the outcome section; it does not contact the regulator for you.

### Does it work for both UK and EU GDPR?

Yes. The core DPIA requirements are the same, and the skill flags where UK-specific changes, such as the automated decision-making rules, are relevant.

## Related skills

- [`company-context`](../company-context/): builds the profile the DPIA reads, including data categories and processors.
- [`ai-impact-assessment`](../ai-impact-assessment/): assesses wider impacts of AI systems; run it alongside a DPIA for AI features.
- [`risk-register`](../risk-register/): carries privacy risks from the DPIA into your main register.
- [`policy-writer`](../policy-writer/): drafts the privacy and data protection policies the DPIA relies on.
