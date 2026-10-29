---
name: cyber-essentials-scoping
description: Scope and pre-assess a UK Cyber Essentials / Cyber Essentials Plus certification (Requirements v3.3, Danzell question set) — building the device, cloud service and network inventory, checking the five technical controls (firewalls, secure configuration, security update management, user access control incl. mandatory MFA, malware protection), and listing fail risks before submission. Use for "Cyber Essentials", "CE+", "get CE certified", "CE scope", or "will we pass Cyber Essentials".
license: MIT
metadata:
  author: GRCMANA
  version: 0.1.0
  collection: frameworks
  summary: "Scopes Cyber Essentials and finds the hard fails before you submit."
  frameworks: "Cyber Essentials"
---

# Cyber Essentials Scoping & Pre-Assessment

You get an organisation ready to submit Cyber Essentials, and optionally CE+, first time. Most failures come from scope gaps, missing MFA on a cloud service, unsupported software, and patches that miss the 14-day window.

Read `references/grc-workspace.md` and `references/cyber-essentials.md` first.

> ⚠️ The scheme updates every year (usually April). The pack reflects **Requirements v3.3 / Danzell** for assessment accounts created from 27 April 2026. Tell the user to confirm the live version, and the exact question wording, with their certification body before submitting.

## Context
Read `grc/context/company-profile.md`. If it's missing, ask: headcount; office and remote model; company vs personal devices; OS mix; MDM; identity provider; the SaaS and cloud services in use; who manages IT.

## Workflow
1. **Scope decision.** Recommend whole-organisation scope (the default). If a sub-set is proposed, check it's network-segregated and clearly named, and explain the trade-off: a narrower certificate means less customer assurance.
2. **Inventory.** Build `grc/audits/ce-scope.md` from `assets/ce-scope-template.md`:
   - **End-user devices** by OS and version (counts, not serials), company vs BYOD. Note whether each OS version is vendor-supported.
   - **Servers and VMs** (including cloud IaaS)
   - **Network devices**: firewalls and routers (office), including boundary firewall ownership
   - **Cloud services** (IaaS, PaaS, SaaS): **every** service the organisation uses for work, with MFA status. Prompt for the commonly forgotten ones: code hosting, password manager, CRM, finance and payroll, HR, design tools, AI tools, DNS and registrar.
   - **Users and admin accounts**: counts, separate admin accounts (y/n)
3. **Control pre-check.** Walk the five controls, in batches, with plain-English questions. Record each as ✅ / ⚠️ / ❌ with the reason.
   - Firewalls
   - Secure configuration
   - Security update management: the **14-day rule** for critical/high, and unsupported software
   - User access control: **MFA on all cloud services where available**, admin separation, password approach
   - Malware protection
4. **Fail-risk list.** List every ❌ and ⚠️ as a remediation item, with an owner and a fix. Mark **hard fails** clearly: any cloud service without MFA where it's available, unsupported software in scope, patching outside 14 days, default passwords, admin accounts used for email and browsing.
5. **CE+ readiness** (if targeted): note the technical audit expectations (sampled devices, authenticated vulnerability scans, MFA checks, malware tests), and check that the patch and anti-malware evidence will stand up to sampling.

## Outputs
- `grc/audits/ce-scope.md`: scope statement, inventory, control pre-check, fail-risk list
- Optionally, add material gaps to `grc/risks/risk-register.csv` (category `security`, framework ref `CE:<control>`)
- A summary in chat: ready / not-ready, hard-fail count, the top five fixes in order, and an estimated time to submission
- A run log in `grc/runs/`

## Guardrails
- Don't fill in the official questionnaire for the user, or reproduce its question text. Prepare them to answer accurately.
- The declaration is signed by a board member or equivalent, and answers must be true. Never suggest answering "yes" to something not yet in place.
- Device inventories hold counts and models, not personal data about users.

## References
- `references/grc-workspace.md`
- `references/cyber-essentials.md`
