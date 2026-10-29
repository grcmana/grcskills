---
framework: Cyber Essentials / Cyber Essentials Plus (UK)
as_of: 2026-10-29
scheme_version: Requirements for IT Infrastructure v3.3, "Danzell" question set (for assessment accounts created from 27 April 2026)
type: UK Government-backed certification (NCSC scheme, delivered by IASME and its certification bodies)
licence_note: Own-words summary. Always check the current requirements document and question set on the IASME/NCSC websites — the scheme updates annually (usually April).
---

# Cyber Essentials — Practitioner Pack

## What it is
A UK baseline certification that proves five technical controls against common internet-borne attacks. It's often required for UK public sector contracts and increasingly by insurers and supply chains.

- **Cyber Essentials (CE)**: a verified self-assessment questionnaire. A board member or equivalent must sign the declaration. A certification body marks it.
- **Cyber Essentials Plus (CE+)**: CE **plus** a hands-on technical audit (sampled devices, vulnerability scans, tests for malware and MFA). CE must be achieved first. CE+ has to be completed within a fixed window after CE (check the current rule).
- Certification is valid for **12 months**.

## Version note (2026)
- Assessment accounts created on or after **27 April 2026** use **Requirements v3.3** and the **Danzell** question set, which replaces Willow (v3.2).
- Accounts created before that date were assessed under Willow, with six months to complete.
- Headline changes:
  - **MFA is mandatory for cloud services wherever it's available.** Not enabling it where it's technically possible is a fail.
  - Clearer scoping, especially for cloud services.
  - More emphasis on passwordless authentication options.
  - Explicit removal of unnecessary software.
  - Tighter marking.
- ⚠️ The scheme changes every year. Confirm the live version before advising.

## The five controls (own words)
| Control | The essence |
|---|---|
| **Firewalls** | Every in-scope device is protected by a correctly configured boundary or software firewall. Default admin passwords are changed. Inbound rules are approved, documented and removed when no longer needed. Admin interfaces aren't exposed to the internet unless there's a justified need, and then they're protected with MFA or an IP allow-list. |
| **Secure configuration** | Remove or disable unnecessary software, accounts and services. Change default passwords. Disable auto-run. Device unlock is required (PIN or password, biometrics allowed) with protection against brute force. |
| **Security update management** | All software is licensed and supported (unsupported software is removed or segregated out of scope). Install **critical and high-risk updates (CVSS v3 ≥ 7, or vendor "critical"/"high") within 14 days** of release, including firmware. Turn on automatic updates where possible. |
| **User access control** | Accounts are provisioned through a process and removed promptly. Least privilege applies. Separate admin accounts are used only for admin tasks. **MFA on all cloud services where available.** Password-based authentication is protected by MFA, a minimum length, or blocking of common passwords. Check the current length rules. |
| **Malware protection** | Use anti-malware (with signature updates and on-access scanning, plus web filtering) **or** application allow-listing **or** sandboxing, per device type. |

## Scoping essentials
- The default and preferred scope is the **whole organisation**. A sub-set is allowed only if it's segregated by a boundary firewall or VLAN and clearly named.
- In scope:
  - All end-user devices (desktops, laptops, tablets, mobiles) that access organisational data or services, **including BYOD**
  - Servers and network devices
  - **Cloud services**: IaaS, PaaS and SaaS
  - Home workers' devices (but not their home routers, if the device has its own software firewall)
- Thin clients, and devices used only for personal purposes, are handled under specific rules. Check the requirements document.

## Common failure points
- Unsupported operating systems or apps still in use (old Windows/macOS versions, end-of-life browsers or plugins)
- No MFA on one or more SaaS tools where it's available, which is now a hard fail
- BYOD phones accessing email with no device lock or OS updates
- Admin users browsing and emailing from admin accounts
- Patch evidence that can't demonstrate the 14-day window
- A scope that omits cloud services

## Typical effort
For a 10–100 person cloud-first company with an MDM and identity provider: 1–4 weeks of preparation. The main work is the device and cloud-service inventory and closing the MFA and patching gaps.
