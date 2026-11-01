# Risk register: identify, score and treat your risks with your AI agent

The `risk-register` skill helps your AI agent build and maintain a risk register that an auditor would accept as evidence, with every treatment mapped to the controls in the frameworks you have chosen. It covers information security, privacy, third-party, operational and AI risks, uses a documented 5×5 scoring method, and works from your real company context rather than a generic list of threats.

## What it does

Auditors for ISO 27001 and SOC 2 expect to see that you identified your risks, scored them consistently, decided what to do about each and reviewed them over time. Many teams instead download a generic threat list or keep a spreadsheet untouched since the last audit.

The skill runs the full lifecycle (identify, assess, treat, accept, review) in four modes:

- **Build**: no register exists yet. It proposes 12–25 risk scenarios specific to your company, scores the ones you confirm and writes the first register and treatment plan.
- **Add**: assesses one or more new risks, for example a new supplier, feature, incident or market.
- **Review**: the periodic review. It re-scores where justified, checks treatment progress and flags overdue or stale items.
- **Report**: summarises the register for leadership, with top risks, a heat map, overdue treatments and acceptances pending.

## Who it's for

- **GRC practitioners and engineers:** the skill drafts scenarios, proposes scores with a rationale for each, and maps planned controls to your selected frameworks. You still own the methodology, the final scores, the owners and the conversation with leadership about risk appetite.
- **Accidental owners** (founders, CTOs, ops leads): you get a clear answer to "what are our top risks and what are we doing about them?", in a format auditors recognise, without knowing ISO 27001 first.

## When to use it

- "Build a risk register" or "do a risk assessment" at the start of an ISO 27001 or SOC 2 programme
- "Update our risks" after a new supplier, product launch, incident or new customer requirement
- "Risk review" when the annual or quarterly review is due, or before a management review meeting
- "What are our top risks?" when the board, an investor or a customer asks

Don't use it to assess the wider impact of an AI system on people; use `ai-impact-assessment`, which adds its material AI risks to this register. For a GDPR assessment of a specific processing activity, use `dpia`.

## How it works

1. **Context.** The skill reads `grc/context/company-profile.md` silently. If it is missing, it asks at most five questions (what you sell, the data you hold, your cloud and core SaaS, headcount and remote model, and who is asking for compliance) and suggests running `company-context`. If `grc/context/risk-methodology.md` exists, your own method replaces the default.
2. **Identify.** It drafts risk scenarios from your profile (data, tech stack, suppliers, people, product and common incident patterns for companies like yours), each written as a scenario rather than a single word like "ransomware".
3. **Validate.** You see the candidates as a short table and remove, merge or add. Nothing is scored until you have confirmed it is relevant.
4. **Assess.** For each confirmed risk it proposes inherent and residual likelihood and impact on a 1–5 scale, with a one-line rationale per score. It asks about your existing controls in batches by domain (identity, endpoints, cloud, development, suppliers, people) rather than assuming them.
5. **Treat.** For each risk above appetite (residual score above 7 by default), it proposes a treatment option, one to three specific planned controls with framework references, a target score, an owner by role and a due date.
6. **Accept.** Risks you choose to retain above appetite get a rationale and an approval request. The approval fields stay blank for a named executive to complete.
7. **Summarise.** It writes the outputs and gives you the top five risks, a 5×5 text heat map of residual scores, treatments due in 30, 60 and 90 days, and acceptances pending.

Review mode flags overdue treatments, risks past review, High risks with no owner, unapproved acceptances and scores unchanged for over 12 months, then asks what has changed.

## What you get

```
grc/
├── risks/
│   ├── risk-register.csv            # the register, IDs R-001, R-002 ...
│   ├── treatment-plan.md            # treatments grouped by owner and due date
│   └── review-YYYY-MM-DD.md         # review mode only
└── runs/YYYY-MM-DD-risk-register-<slug>.md   # AI run log
```

The register has a fixed set of 24 columns, from `risk_id` and `scenario` to `approved_by` and `next_review`. Existing rows and IDs are never renumbered. If you use a GRC platform, the skill offers to format the CSV for import rather than creating a second system of record.

The run log records what was read and written and which decisions await a human.

## Worked example

_This scenario is fictional._

Acme Analytics is a fictional 40-person UK B2B SaaS analytics company. A large customer has asked for SOC 2, and the board wants ISO 27001 within a year. Its company profile is already in place, with both frameworks selected. The CTO asks the agent:

> Build our first risk register. We're working towards SOC 2 and ISO 27001.

The skill drafts 19 candidate scenarios, from phishing-led account takeover to customer data pasted into public AI tools. The CTO removes two, merges two about leavers' access and adds one about a single engineer holding all the production deployment knowledge. It then asks about existing controls domain by domain, starting with identity.

One row in `grc/risks/risk-register.csv` reads, in part:

```
risk_id:          R-004
title:            Admin account takeover via phishing
scenario:         A phishing email captures an admin's cloud console
                  credentials because admins use app-based MFA that can be
                  phished, exposing all customer analytics data.
category:         security
inherent:         L4 x I5 = 20
existing_controls: MFA enforced (authenticator app); annual phishing training
residual:         L3 x I4 = 12   band: Medium
treatment:        Modify
planned_controls: Phishing-resistant keys for admin accounts; separate
                  admin identities; alerting on admin sign-ins
framework_refs:   ISO27001:A.5.17; ISO27001:A.8.5; SOC2:CC6.1
target_score:     4
owner:            Head of Engineering     due_date: 2027-01-31
approved_by:      (blank)                 approved_on: (blank)
```

The CTO decides to retain one Medium risk about reliance on a single cloud region for now. The skill records the rationale, leaves `approved_by` and `approved_on` blank, and lists it under decisions pending in the run log.

## Frameworks covered

- **ISO 27001:2022:** 6.1.2 (risk assessment), 6.1.3 (risk treatment), 8.2 and 8.3 (performing them in practice) and 9.3 (management review, fed by review mode). Planned controls reference Annex A controls such as A.8.8 for vulnerability management.
- **SOC 2 Trust Services Criteria:** CC3.1–CC3.4 (risk assessment) and CC9.1 (risk mitigation).
- **ISO 42001:2023:** 6.1.2 and 6.1.3 for AI risks, which share the same register under category `ai`.
- **GDPR:** risk-based obligations in Articles 24, 32 and 35 are reflected in `privacy` risks.
- **Cyber Essentials:** treatments can reference control themes such as security update management.

The default method is a scenario-based 5×5 approach aligned to ISO 27001 6.1.2 and informed by ISO/IEC 27005 and ISO/IEC 23894. Framework references come from a domain-level crosswalk that carries an `as_of` date and is marked indicative, so verify mappings against the framework itself before relying on them in an audit.

## Guardrails

- **Scores are proposals.** Every score comes with a rationale, and the risk owner confirms it.
- **No credit for planned controls.** Residual scores count only the controls actually in place today.
- **Humans approve.** `approved_by` and `approved_on` are never filled in by the skill; acceptances are listed as decisions pending.
- **Less noise.** Treatments map only to your selected frameworks.
- **No claims of conformity.** A register is evidence for an audit, not a statement that you meet a standard.
- **No secrets or personal data.** Owners are recorded by role or name. Keep `grc/` out of public repositories.

## FAQ

### How many risks should a startup's register have?

The skill aims for 12–25 in a first build. Specific scenarios you actually treat are stronger evidence than a long generic list.

### What is the difference between inherent and residual risk?

Inherent risk assumes your key controls fail or are absent; residual risk counts only the controls actually in place now. The target score is where you expect to be once planned treatments are complete.

### Can we use our own risk methodology?

Yes. Put it in `grc/context/risk-methodology.md` and the skill uses it instead of the default 5×5 method.

### Who should approve accepted risks?

A named executive. The default appetite is a residual score of 7 or below, and anything retained above that needs a rationale and an executive approval, which the skill leaves blank for them.

## Related skills

- [`company-context`](../company-context/): builds the profile the skill uses to draft company-specific scenarios and pick frameworks.
- [`ai-impact-assessment`](../ai-impact-assessment/): assesses AI systems and adds material AI risks to this register.
- [`dpia`](../dpia/): assesses privacy risk for specific processing and can add `privacy` rows here.
- [`audit-readiness`](../audit-readiness/): shows which of the planned controls you already have against each framework.
- [`grc-status`](../grc-status/): rolls the register's top risks, overdue treatments and pending acceptances into a one-page status for leadership.
