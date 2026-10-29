---
title: Domain-level crosswalk — ISO 27001 · SOC 2 · Cyber Essentials · GDPR · ISO 42001
as_of: 2026-10-29
status: indicative — verify mappings before relying on them in an audit
---

# Framework Crosswalk (domain level)

Use this to **build once, comply many**. Each row is a control domain. Cells show where each framework addresses it. "—" means not directly addressed. Mappings are indicative and many-to-many, so always confirm against the framework itself.

| # | Domain | ISO 27001:2022 | SOC 2 TSC | Cyber Essentials v3.3 | GDPR | ISO 42001:2023 |
|---|---|---|---|---|---|---|
| 1 | Governance, policy & roles | 5.1–5.3, A.5.1–A.5.4 | CC1.1–CC1.5, CC2.1, CC5.3 | — (board-level declaration) | Arts. 5(2), 24, 37–39 | 5.1–5.3, A.2, A.3 |
| 2 | Risk management | 6.1.2, 6.1.3, 8.2, 8.3 | CC3.1–CC3.4, CC9.1 | — | Arts. 24, 32, 35 | 6.1.2–6.1.4, 8.2–8.4, A.5 |
| 3 | Asset & data inventory | A.5.9–A.5.12 | CC6.1 | Scope + device/cloud inventory | Art. 30 (RoPA) | A.4 (resources), AI system inventory |
| 4 | Identity & access control | A.5.15–A.5.18, A.8.2, A.8.5 | CC6.1–CC6.3 | User access control (MFA) | Art. 32 | — |
| 5 | Secure configuration | A.8.1, A.8.9, A.8.19 | CC6.8, CC7.1 | Secure configuration | Art. 32 | — |
| 6 | Vulnerability & patch management | A.8.8 | CC7.1 | Security update management (14 days) | Art. 32 | — |
| 7 | Malware protection | A.8.7 | CC6.8 | Malware protection | Art. 32 | — |
| 8 | Network security & firewalls | A.8.20–A.8.22 | CC6.6 | Firewalls | Art. 32 | — |
| 9 | Cryptography | A.8.24 | CC6.1, CC6.7 | — | Art. 32(1)(a) | — |
| 10 | Logging & monitoring | A.8.15, A.8.16 | CC7.2, CC7.3 | — | Arts. 32, 33 | A.6.2.6, A.6.2.8 |
| 11 | Incident management | A.5.24–A.5.28, A.6.8 | CC7.3–CC7.5 | — | Arts. 33–34 | A.8.4 |
| 12 | Continuity, backup & resilience | A.5.29, A.5.30, A.8.13, A.8.14 | CC9.1, A1.1–A1.3 | — | Art. 32(1)(b)–(c) | — |
| 13 | Supplier & cloud risk | A.5.19–A.5.23 | CC9.2 | Cloud services in scope | Art. 28 | A.10 |
| 14 | Secure development & change | A.8.25–A.8.29, A.8.32 | CC8.1 | — | Art. 25 | A.6 |
| 15 | People: screening, awareness, discipline | A.6.1–A.6.5, 7.2–7.3 | CC1.4, CC2.2 | — | Arts. 29, 32(4) | 7.2–7.3 |
| 16 | Privacy & data protection | A.5.33, A.5.34, A.8.10–A.8.12 | C1, P1–P8 (optional) | — | Arts. 5–49 | A.7 |
| 17 | Monitoring, audit & review | 9.1–9.3, 10.1–10.2 | CC4.1, CC4.2 | Annual recertification | Art. 5(2) | 9.1–9.3, 10 |
| 18 | AI governance & impact | — (A.5.23 for AI SaaS) | — (via CC3/CC9 risk) | — | Arts. 22 (EU) / 22A–22D (UK), 35 | 6.1.4, A.2–A.10 |

## How skills use this
- **audit-readiness** maps the user's existing controls to domains, then shows coverage per selected framework.
- **evidence-request-list** dedupes requests across frameworks by domain, so one artefact can serve several frameworks.
- **policy-writer** uses the domains to decide which policy covers which requirement.
