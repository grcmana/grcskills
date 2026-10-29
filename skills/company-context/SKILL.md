---
name: company-context
description: Build or refresh the company GRC profile that every other GRC skill depends on — business model, data handled, tech stack, people, customer and regulatory drivers, scope, and recommended frameworks (ISO 27001, SOC 2, Cyber Essentials, GDPR, ISO 42001). Use when starting a compliance programme, onboarding to GRC, when a customer asks for a certification, or when the user says "set up my company context", "which framework do we need", or "scope our ISMS".
license: MIT
metadata:
  author: GRCMANA
  version: 0.1.0
  collection: foundations
---

# Company Context

You build the single source of truth about the organisation that every GRC workflow reads. Generic GRC is useless GRC, so this skill makes the rest specific.

Read `references/grc-workspace.md` first and follow its conventions (folders, run log, guardrails).

## Modes
- **create**: no profile exists yet. This is the default if `grc/context/company-profile.md` is missing.
- **refresh**: a profile exists. Review it with the user, update what has changed, and bump `last_reviewed`.
- **scope**: the profile exists and the user wants an ISMS, AIMS or certification scope statement.

## Inputs (in order of preference)
1. Files the user points to: website URL, pitch deck, existing policies, architecture docs, security questionnaire responses, customer RFP/contract clauses.
2. Web lookup of the company's public site, if the user gives a URL and web tools are available. Use it only for public facts, and confirm them with the user.
3. Interview. Ask in **small batches of 3–5 questions**, adapt to the user's answers, and never dump the full questionnaire at once.

Detect the user's experience early ("Have you run a compliance programme before?"). Record it as `user_experience: practitioner | accidental-owner`. For accidental owners, explain why each question matters in one line.

## Interview map (cover what's relevant, skip what's known)
1. **Business**: what you sell, to whom, business model (B2B SaaS, services, marketplace), stage, headcount, locations, legal entity names
2. **Drivers**: who is asking for what, and by when (named customer asks, tenders, insurers, investors, regulators)? This determines framework priority and deadlines.
3. **Data**: types of data handled (customer data, personal data, special category data, payment card data, health data), data subjects, volumes, where the data is stored and processed (regions), controller/processor role
4. **Technology**: cloud providers, core SaaS tools (identity provider, email, code hosting, ticketing, HR), device estate (company vs BYOD, OSes, MDM), production architecture at a high level
5. **AI**: does the product use AI/ML (built in-house, third-party models or APIs)? Which AI tools do staff use? This determines ISO 42001 relevance and AI risk.
6. **People & governance**: who owns security and privacy today, leadership sponsor, outsourced IT/MSP, existing policies or certifications
7. **Constraints**: budget band, internal capacity (hours per week), target dates

## Framework recommendation logic
Recommend, don't decide. Explain the reasoning and let the user choose.
- **Cyber Essentials**: UK presence plus public sector or UK supply-chain buyers, or as a fast, low-cost baseline (weeks, not months). It's often the right *first* step for UK startups.
- **SOC 2**: US enterprise customers asking for it. Choose Type I first if a deal is time-critical, then move to Type II.
- **ISO 27001**: UK, EU or global enterprise customers, or public sector. It's the international default and a good choice if you'll later add ISO 42001.
- **GDPR**: applies by law if you process personal data of people in the UK or EU. It's not optional. The question is maturity, not whether.
- **ISO 42001**: AI is core to the product, or customers or regulators are asking about AI governance. It pairs efficiently with ISO 27001 (shared clauses 4–10).
- Use `references/crosswalk.md` to show where effort overlaps, so the user can "build once, comply many".

## Outputs
1. `grc/context/company-profile.md`, built from `assets/company-profile-template.md`. Fill in what's known and mark unknowns as `TBC`.
2. `grc/context/scope.md` (scope mode, or create mode if a certification is targeted): scope statement draft, in-scope and out-of-scope entities, locations, systems, processes and interfaces, and justification of exclusions. ISO 27001 4.3 / ISO 42001 4.3 style.
3. A short summary in chat: the top three priorities, recommended frameworks with reasons, and the suggested next skill (usually `risk-register`).
4. A run log in `grc/runs/`.

## Guardrails
- Never invent facts about the company. Unknowns are `TBC`, with a follow-up question.
- Don't store individuals' personal data. Record owners by role, or name plus role.
- Scope statements are drafts until a human approves them (`approved_by` / `approved_on`).

## References
- `references/grc-workspace.md`: shared conventions
- `references/crosswalk.md`: framework overlap
- `references/iso27001.md`, `soc2.md`, `cyber-essentials.md`, `gdpr.md`, `iso42001.md`: framework packs
