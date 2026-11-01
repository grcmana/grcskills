# Company context: the GRC profile every other skill reads

The `company-context` skill helps your AI agent build a single, reviewed profile of your organisation: what you sell, who is asking for assurance, what data you handle, your tech stack, who owns security, and which frameworks to prioritise. Every other GRC skill reads this profile, so it is the first thing to run.

## What it does

Generic GRC is useless GRC: a risk register or policy written without knowing your business reads like a template. This skill captures the facts once, in `grc/context/company-profile.md`, so the rest of the library can be specific to you and stop asking the same questions.

It also recommends frameworks without deciding for you, explaining which of Cyber Essentials, SOC 2, ISO 27001, GDPR and ISO 42001 fit your drivers, and where effort overlaps.

The skill works in three modes:

- **Create** (the default when no profile exists): builds the profile from your documents, public website and a short interview.
- **Refresh**: reviews an existing profile with you, updates what has changed and bumps the `last_reviewed` date.
- **Scope**: drafts an ISMS, AIMS or certification scope statement from the profile.

## Who it's for

- **GRC practitioners and engineers:** the skill turns pitch decks, architecture docs, past questionnaire answers and contract clauses into a structured profile and a first-draft scope statement. You still own the framework choice, the scope boundaries and the justification of any exclusions.
- **Accidental owners** (founders, CTOs, ops leads): you answer a few plain questions at a time, each with a one-line reason for asking, and get a clear view of which frameworks matter for your customers and in what order. You don't need to know what an ISMS is before you start.

## When to use it

- Starting a compliance programme, or onboarding someone new to GRC
- A customer asks for a certification or report: "do we need SOC 2 or ISO 27001?"
- "Set up my company context", "which framework do we need", "scope our ISMS"
- Preparing a scope statement before an ISO 27001 or ISO 42001 certification audit
- Something material has changed, such as a new product, market or AI feature (use refresh mode)

Don't use it to assess risks, write policies or check audit readiness. Run `risk-register`, `policy-writer` or `audit-readiness` once the profile exists. For a Cyber Essentials-specific scope (devices, cloud services, BYOD), use `cyber-essentials-scoping`.

## How it works

1. **Mode.** The skill checks for `grc/context/company-profile.md`. If it's missing, it runs in create mode; if it exists, it offers refresh or scope.
2. **Gather inputs.** It starts with files you point to (pitch deck, policies, architecture docs, questionnaire responses, contract clauses), then your public website if you give a URL and web tools are available. Web findings are used only for public facts and confirmed with you.
3. **Experience check.** Early on it asks whether you've run a compliance programme before, and records `user_experience` as `practitioner` or `accidental-owner`. Accidental owners get a one-line explanation of why each question matters.
4. **Interview.** It asks in batches of three to five questions, skipping what it already knows. Topics are business, drivers (who is asking for what, by when), data, technology, AI, people and governance, and constraints such as budget and capacity.
5. **Recommend frameworks.** It explains which frameworks fit and why, using the crosswalk to show shared effort. You decide.
6. **Write the profile.** Known facts go in; unknowns are marked `TBC` with a follow-up question in the open questions section.
7. **Draft the scope.** In scope mode, or in create mode when a certification is targeted, it drafts a scope statement in the style of ISO 27001 4.3 and ISO 42001 4.3.
8. **Hand over.** It summarises the top three priorities, the recommended frameworks with reasons, and the suggested next skill, usually `risk-register`. The approval fields stay blank for a person to complete.

## What you get

```
grc/
├── context/
│   ├── company-profile.md               # the profile every skill reads
│   └── scope.md                         # scope mode, or create mode if certifying
└── runs/YYYY-MM-DD-company-context-<slug>.md   # AI run log
```

The **company profile** has nine sections, from business and data through to framework selection (status, priority and rationale) and open questions. Its frontmatter carries an owner, review dates and blank `approved_by` and `approved_on` fields.

The **scope statement** covers in-scope and out-of-scope entities, locations, systems, processes and interfaces, with a justification for each exclusion. It stays a draft until a person approves it.

The **run log** records files read and written and decisions awaiting a human: an audit trail for ISO 42001 and for any auditor asking how a document was produced.

## Worked example

_This scenario is fictional._

Acme Analytics is a fictional 40-person UK B2B SaaS analytics company. A large UK retailer has sent a security questionnaire asking for ISO 27001, and a US prospect has mentioned SOC 2. The CTO has never run a compliance programme and types:

> Set up our company context. We've got a retailer asking for ISO 27001 and a US prospect asking about SOC 2. Our deck and architecture doc are in /docs.

The skill finds no profile, so it runs in create mode. It reads the deck and architecture doc, asks whether the CTO has run a programme before, and records `user_experience: accidental-owner`. Its first batch of four questions covers the retailer's deadline, the urgency of the US deal, where customer data is hosted and whether the product uses third-party AI models, each with a one-line reason.

It then writes the profile. An excerpt from the framework selection section:

```
| Framework        | Status      | Priority | Rationale                                         |
|------------------|-------------|----------|---------------------------------------------------|
| Cyber Essentials | not-started | 1        | Fast UK baseline; retailer supply chain; weeks    |
| ISO 27001        | not-started | 2        | Named retailer ask; UK/EU default; pairs with 42001 |
| SOC 2            | not-started | 3        | US prospect; Type I first if the deal is urgent   |
| GDPR             | applies     | n/a      | Processes UK/EU personal data; question is maturity |
| ISO 42001        | not-started | TBC      | Uses third-party LLM API in product; confirm ask  |

Open questions:
- Retailer deadline for ISO 27001: TBC (ask procurement contact)
- Is the US deal time-critical? TBC
```

Because a certification is targeted, it also drafts `grc/context/scope.md`, with the production platform and cloud hosting in scope and the marketing website out of scope pending a justification. In chat, it suggests `risk-register` next. The `approved_by` and `approved_on` fields are left blank.

## Frameworks covered

The skill draws on five framework packs plus a domain-level crosswalk:

- **ISO 27001:2022:** context and scope (clause 4, including the 4.3 scope requirement), with clauses 4–10 mandatory and Annex A controls selected through risk treatment.
- **SOC 2:** an attestation report against the Trust Services Criteria, not a certification. Type I covers design at a point in time; Type II covers operation over a period.
- **Cyber Essentials v3.3:** the UK baseline of five technical controls, with whole-organisation scope by default and certification valid for 12 months.
- **UK GDPR and EU GDPR:** applies by law where you process UK or EU personal data; the profile records your controller or processor role.
- **ISO 42001:2023:** the AI management system standard, sharing clauses 4–10 with ISO 27001 so the two can run as one management system.

The crosswalk maps 18 control domains across all five frameworks; it is indicative, so confirm mappings against the framework itself. Every pack carries an `as_of` date, and Cyber Essentials updates annually, so check the official source for anything that may have changed since.

## Guardrails

- **No invented facts.** Anything the skill can't confirm is written as `TBC`, with a follow-up question.
- **No personal data.** Owners are recorded by role, or by name plus role. It never asks for or stores secrets or credentials.
- **Recommends, doesn't decide.** The framework choice and its priority are yours.
- **Humans approve.** The profile and scope statement are drafts until a person fills in `approved_by` and `approved_on`.
- **Status, not claims.** The profile records progress, never that you meet a standard.
- **Keep it private.** `grc/` holds sensitive governance data. Add it to `.gitignore` or keep it in a private repository.

## FAQ

### Do I need to run this before the other skills?

It's strongly recommended. Other skills can ask up to five context questions of their own, but each one then suggests running `company-context` for a complete profile.

### Which framework should a UK startup start with?

It depends on who is asking. Cyber Essentials is often the right first step because it's quick and low-cost; ISO 27001 or SOC 2 follow named customer demands.

### Can it read our website instead of interviewing us?

Partly. With a URL and web tools available, it uses your public site for public facts and confirms them with you; internal details still come from you or your documents.

### How often should we refresh the profile?

Whenever something material changes, such as a new product, market, AI feature or major customer ask, and at least by the `next_review` date. Refresh mode updates what's changed and bumps `last_reviewed`.

## Related skills

- [`risk-register`](../risk-register/): the usual next step; builds a risk register specific to your business from the profile.
- [`audit-readiness`](../audit-readiness/): assesses readiness against the frameworks the profile selects.
- [`cyber-essentials-scoping`](../cyber-essentials-scoping/): turns the profile's technology section into a Cyber Essentials scope.
- [`policy-writer`](../policy-writer/): drafts policies that reflect your real tools, owners and data.
- [`grc-status`](../grc-status/): reports progress against the target dates the profile records.
