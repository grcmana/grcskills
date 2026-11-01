# Cyber Essentials scoping: find the hard fails before you submit

The `cyber-essentials-scoping` skill helps your AI agent get a UK organisation ready to submit Cyber Essentials, and optionally Cyber Essentials Plus, at the first attempt. It builds your device, cloud service and network inventory, checks the five technical controls in plain English, and gives you a prioritised list of fail risks and fixes. It prepares you to answer the official questionnaire accurately; it doesn't fill it in for you.

## What it does

Cyber Essentials is a UK government-backed baseline certification covering five technical controls, often required for public sector contracts and increasingly by insurers and customers. Most failed submissions come from predictable gaps: a scope that leaves out cloud services, a SaaS tool without multi-factor authentication (MFA), an unsupported operating system still in use, or patches that miss the 14-day window.

The skill works through it in order: a scope decision, an inventory of devices, cloud services, network devices and accounts, a pre-check of the five controls (each marked ✅, ⚠️ or ❌), and a fail-risk list with hard fails clearly marked. If you are aiming for Plus, it also checks whether your evidence will stand up to the technical audit's sampling.

## Who it's for

- **GRC practitioners and engineers:** the skill does the inventory legwork, prompts for forgotten cloud services, and produces a scope document and fail-risk list for IT. You still own the scope decision, the conversation with the certification body and the answers on the questionnaire.
- **Accidental owners** (founders, CTOs, ops leads): you get a clear "ready" or "not ready", a count of hard fails, the top five fixes in order and a realistic time to submission, without needing to read the requirements document first.

## When to use it

Use it before you open, or early in, your assessment account with a certification body. Typical triggers:

- "We need Cyber Essentials for a tender" or "get CE certified"
- "What's in scope for Cyber Essentials?" or "CE scope"
- "Will we pass Cyber Essentials?" or "CE+ readiness"
- Annual renewal, especially after the scheme's yearly update (usually in April)

Don't use it for a readiness assessment across several frameworks; use `audit-readiness`. To plan CE+ evidence alongside ISO 27001 or SOC 2, use `evidence-request-list`.

## How it works

1. **Context.** The skill reads `grc/context/company-profile.md`. If it is missing, it asks about headcount, remote working, company versus personal devices, OS mix, MDM, identity provider, cloud services and who manages IT, and suggests running `company-context`.
2. **Scope decision.** It recommends whole-organisation scope, the scheme's default. If a sub-set is proposed, it checks that it is network-segregated and clearly named, and explains that a narrower certificate gives customers less assurance.
3. **Inventory.** It builds `grc/audits/ce-scope.md` from its template: devices by OS version and support status (company versus BYOD), servers and VMs, firewalls and routers, every cloud service with its MFA status, and account counts. It prompts for commonly forgotten services such as code hosting, password manager, CRM, HR, finance, design and AI tools, and DNS and registrar.
4. **Control pre-check.** It asks plain-English questions in batches about firewalls, secure configuration, security update management, user access control and malware protection.
5. **Fail-risk list.** Every ❌ and ⚠️ becomes a remediation item with an owner and a fix. Hard fails are marked clearly.
6. **CE+ readiness.** If you are targeting Plus, it notes what the technical audit samples and tests (devices, authenticated vulnerability scans, MFA, malware) and checks your patching and anti-malware evidence.
7. **Human decisions.** The scope, the fixes and the final answers are yours. The `approved_by` and `approved_on` fields are left blank, and the board-level declaration is for a person to sign.

## What you get

```
grc/
├── audits/ce-scope.md                  # scope, inventory, pre-check, fail-risk list
├── risks/risk-register.csv             # optional rows, category "security", ref CE:<control>
└── runs/YYYY-MM-DD-cyber-essentials-scoping-<slug>.md   # AI run log
```

- **Scope and pre-assessment:** scope statement, inventory, control pre-check, fail-risk list and earliest realistic submission date.
- **Risk register rows (optional):** material gaps, category `security`.
- **Chat summary:** ready or not ready, the hard-fail count, the top five fixes in order and an estimated time to submission.
- **Run log:** files read and written, and decisions pending.

## Worked example

_This scenario is fictional. Acme Analytics is an invented 40-person UK B2B SaaS analytics company._

Acme Analytics has been asked for Cyber Essentials in a public sector tender and plans to go for CE+ afterwards. Staff use company laptops managed through MDM and their own phones for email and chat. The CTO asks the agent:

> We need Cyber Essentials for a tender, then CE+. What's in scope and what would fail us?

The skill reads the company profile, recommends whole-organisation scope and builds the inventory. Its prompts for often-missed services add a design tool, an AI assistant and the domain registrar. It then walks the five controls. The fail-risk list in `grc/audits/ce-scope.md` reads, in part:

```
## 4. Fail-risk list
| # | Item                                        | Hard fail? | Fix                                   | Owner    | Due        |
|---|---------------------------------------------|------------|---------------------------------------|----------|------------|
| 1 | Design tool: MFA available, not enforced    | Yes        | Enforce MFA for all users             | Ops lead | 2026-11-06 |
| 2 | Domain registrar: MFA not enabled           | Yes        | Enable MFA on all registrar logins    | CTO      | 2026-11-06 |
| 3 | 2 laptops on an unsupported macOS version   | Yes        | Upgrade or remove from use            | IT       | 2026-11-13 |
| 4 | Engineers use admin accounts for email      | Yes        | Create separate admin-only accounts   | CTO      | 2026-11-13 |
| 5 | BYOD phones: no OS update check             | No (⚠️)    | Require minimum OS and device lock    | Ops lead | 2026-11-20 |
|   |   via MDM                                   |            |   before email access                 |          |            |
```

In chat, the skill summarised: not ready, four hard fails, the top five fixes in the order above, and an estimate of two to three weeks to submission. For CE+, it noted that sampled devices must show critical and high updates installed within 14 days, and that the CE+ audit must be completed within three months of the basic certificate. The `approved_by` field was left blank.

## Frameworks covered

- **Cyber Essentials and Cyber Essentials Plus (UK):** the skill's pack reflects Requirements for IT Infrastructure v3.3 and the "Danzell" question set, used for assessment accounts created from 27 April 2026. It covers the five controls in its own words:
  - **Firewalls:** a correctly configured boundary or software firewall for every device, with default passwords changed and inbound rules documented.
  - **Secure configuration:** unnecessary software and accounts removed, auto-run disabled, device unlock required.
  - **Security update management:** only licensed, supported software, with critical and high-risk updates (CVSS v3 of 7 or above, or vendor-rated critical or high) installed within 14 days.
  - **User access control:** least privilege, separate admin accounts, and MFA for all users on every cloud service that offers it, which is now an automatic fail if missed.
  - **Malware protection:** up-to-date anti-malware or application allow-listing, as appropriate per device type.
- **Scheme basics:** CE is a self-assessment marked by a certification body, with the declaration signed by a board member or equivalent. CE+ adds a hands-on technical audit. Certification lasts 12 months.

The NCSC scheme is delivered by IASME and its certification bodies, and changes every year, usually in April. The pack's `as_of` date is 2026-10-29. Before you submit, confirm the live requirements version and question set with your certification body or on the IASME and NCSC websites.

## Guardrails

- **No ghost-writing the questionnaire.** The skill won't complete the official questionnaire or reproduce its question text. It prepares you to answer accurately.
- **Honest answers only.** The declaration is signed by a board member or equivalent and the answers must be true. The skill never suggests answering "yes" to something not yet in place.
- **No promises of passing.** It identifies fail risks; the certification body marks the assessment.
- **No personal data in the inventory.** Device lists hold counts and models, not serials or user details.
- **Humans approve.** The scope statement's approval fields are left blank for a person to complete, and listed as pending in the run log.

## FAQ

### Do personal phones count for Cyber Essentials?

Yes, if they access organisational data or services such as email. They need device lock, a supported OS and timely updates like any company device.

### Can we certify just part of the business?

You can, but only if that part is segregated by a boundary firewall or VLAN and clearly named. The skill recommends whole-organisation scope because a narrower certificate gives customers less assurance.

### What counts as a hard fail?

Any cloud service without MFA where it is available, unsupported software in scope, critical or high patches applied outside 14 days, default passwords, and admin accounts used for email and browsing. The skill marks each one in the fail-risk list.

### How long does preparation usually take?

For a cloud-first company of 10 to 100 people with an MDM and an identity provider, the pack estimates one to four weeks. Most of the effort goes into the inventory and closing MFA and patching gaps.

## Related skills

- [`company-context`](../company-context/): builds the profile this skill reads, including devices, identity provider and SaaS tools.
- [`audit-readiness`](../audit-readiness/): runs a wider gap assessment if Cyber Essentials sits alongside ISO 27001 or SOC 2.
- [`evidence-request-list`](../evidence-request-list/): plans the patching and anti-malware evidence a CE+ technical audit will sample.
- [`evidence-review`](../evidence-review/): checks that evidence before the CE+ assessor sees it.
- [`risk-register`](../risk-register/): carries material Cyber Essentials gaps into your main risk register.
