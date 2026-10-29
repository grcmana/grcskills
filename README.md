# GRC Skills

**Open-source agent skills for Governance, Risk & Compliance practitioners.**
Built by [GRCMANA](https://grcmana.com) · browse at **[grcskills.io](https://grcskills.io)** · MIT licensed · v0.1.0

GRC Skills are expert-written skills that teach AI agents how to do real GRC work: risk assessments, policies, audit readiness, evidence, DPIAs, Cyber Essentials scoping and AI impact assessments. They cover **ISO 27001, SOC 2, Cyber Essentials, GDPR and ISO 42001**.

They work in Claude Code, Codex, Cursor and other agents that support the open [Agent Skills](https://agentskills.io) format.

> ⚠️ Skills produce **drafts for review by a competent person**. They don't certify compliance or give legal advice. See [Disclaimer](#disclaimer).

## Install

```bash
# All GRC skills
npx skills add grcmana/grcskills

# A single skill
npx skills add grcmana/grcskills@risk-register
```

Then just ask your agent, e.g. *"Build our risk register"*, *"Are we ready for ISO 27001 Stage 1?"* or *"Do we need a DPIA for this feature?"*. In Claude Code you can also invoke a skill directly, e.g. `/company-context`.

**Start with `company-context`.** Every other skill reads the company profile it creates, so its output is specific to your organisation rather than generic.

Want the full operating system, with guardrails, a private workspace, run logs and a worked example? Use **[GRC OS](https://github.com/grcmana/grc-os)**.

## Skills

| Skill | Collection | What it does |
|---|---|---|
| [`company-context`](skills/company-context/SKILL.md) | Foundations | Builds the company GRC profile, scope and framework selection |
| [`grc-status`](skills/grc-status/SKILL.md) | Foundations | One-page programme status, board report or management review inputs |
| [`risk-register`](skills/risk-register/SKILL.md) | Risk management | Identify, score (5×5), treat and review risks, with control mapping |
| [`ai-impact-assessment`](skills/ai-impact-assessment/SKILL.md) | Risk management | AI inventory, AI risk and impact assessments (ISO 42001) |
| [`policy-writer`](skills/policy-writer/SKILL.md) | Policy management | Minimum viable policy set and tailored, testable policy drafts |
| [`policy-gap-review`](skills/policy-gap-review/SKILL.md) | Policy management | Auditor-style review of existing policies |
| [`audit-readiness`](skills/audit-readiness/SKILL.md) | Audit & evidence | Readiness/gap assessment and a remediation roadmap to audit |
| [`evidence-request-list`](skills/evidence-request-list/SKILL.md) | Audit & evidence | Deduplicated, control-mapped evidence plan and tracker |
| [`evidence-review`](skills/evidence-review/SKILL.md) | Audit & evidence | Pre-audit QA of collected evidence |
| [`cyber-essentials-scoping`](skills/cyber-essentials-scoping/SKILL.md) | Frameworks | CE / CE+ scope, inventory and fail-risk pre-check (v3.3 / Danzell) |
| [`dpia`](skills/dpia/SKILL.md) | Frameworks | GDPR DPIA screening and drafting |

## How skills work together

All skills share one convention (see [`knowledge/methodology/grc-workspace.md`](knowledge/methodology/grc-workspace.md)): your GRC data lives in a `grc/` folder in your project.

```
grc/
├── context/    company profile, scope
├── risks/      risk register, treatment plan, AI assessments
├── policies/   policy drafts, gap reviews
├── evidence/   evidence tracker, request lists, reviews
├── audits/     readiness reports, CE scope, DPIAs
└── runs/       AI run log (audit trail of AI-assisted work)
```

- **Private by default.** `grc/` contains sensitive governance data. Add it to `.gitignore`, or keep it in a private repo.
- **Human in the loop.** Approval fields (`approved_by`, `approved_on`) are never filled in by the agent.
- **Auditable AI.** Every run writes a log to `grc/runs/`, which is useful evidence when your auditor asks how AI was used.

## Repo structure

```
grcskills/
├── skills/<name>/
│   ├── SKILL.md          # the skill
│   ├── references/       # framework + methodology knowledge (synced from knowledge/)
│   └── assets/           # templates the skill fills in
├── knowledge/            # single source of truth for shared knowledge
│   ├── frameworks/       # ISO 27001, SOC 2, CE, GDPR, ISO 42001, crosswalk
│   └── methodology/      # workspace convention, risk, evidence, writing standards
└── scripts/sync_references.py
```

Framework packs are **own-words summaries** that reference clause and control IDs. They don't reproduce standard text. Each carries an `as_of` date.

## Contributing

GRC practitioners are very welcome: new skills, framework corrections, and real-world feedback. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Roadmap

- **v0.2:** `asset-inventory`, `supplier-risk`, `incident-response`, `statement-of-applicability`, `security-questionnaire`
- **v0.3:** NIS2, DORA and EU AI Act packs, plus evidence automation via MCP connectors
- Community skills, contributor profiles and collections on [grcskills.io](https://grcskills.io)

## Disclaimer

Provided "as is" under the MIT licence. GRC Skills are **not** legal, regulatory or audit advice and do not certify compliance. AI output can be wrong, so all outputs must be reviewed by a competent person. Framework summaries reflect our understanding as of each pack's `as_of` date, so check official sources. ISO/IEC standards are © ISO/IEC, the SOC 2 Trust Services Criteria are © AICPA, and Cyber Essentials is a UK Government scheme delivered by IASME for the NCSC. This project isn't affiliated with or endorsed by any of these bodies, or by Anthropic.

---

Built by **Harry West** ([GRCMANA](https://grcmana.com)): ~20 years in cyber, former Global CISO, ISO 27001 / 42001 / 9001 and Cyber Essentials certified.
⭐ Star the repo if it saves you time.
