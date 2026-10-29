# Policy Catalogue — Minimum Viable Policy Set

✅ = typically required or expected · ◐ = supports / commonly requested · — = not needed for this framework

Under about 50 staff, merge the rows marked **(IS)** into one **Information Security Policy** with topic sections.

| Policy | ISO 27001 | SOC 2 | CE | GDPR | ISO 42001 | Notes |
|---|---|---|---|---|---|---|
| Information Security Policy (top-level) | ✅ 5.2, A.5.1 | ✅ CC1, CC2, CC5.3 | ◐ | ◐ Art. 24, 32 | ◐ | Leadership commitment, objectives, roles |
| Acceptable Use Policy | ✅ A.5.10 | ✅ CC1.4, CC2.2 | ◐ | ◐ | ◐ A.9 | Staff-facing; signed or acknowledged |
| Access Control & Identity **(IS)** | ✅ A.5.15–A.5.18, A.8.5 | ✅ CC6.1–CC6.3 | ✅ User access control | ◐ Art. 32 | — | MFA, least privilege, JML, access reviews |
| Asset Management **(IS)** | ✅ A.5.9–A.5.12 | ◐ CC6.1 | ✅ (scope) | ◐ Art. 30 | ◐ A.4 | Inventory, ownership, classification |
| Endpoint & Secure Configuration **(IS)** | ✅ A.8.1, A.8.9 | ✅ CC6.8 | ✅ Secure config, Malware | ◐ | — | MDM, encryption, screen lock, AV/EDR, BYOD |
| Vulnerability & Patch Management **(IS)** | ✅ A.8.8 | ✅ CC7.1 | ✅ 14-day rule | ◐ | — | SLAs by severity |
| Network Security **(IS)** | ✅ A.8.20–A.8.22 | ✅ CC6.6 | ✅ Firewalls | — | — | |
| Cryptography **(IS)** | ✅ A.8.24 | ✅ CC6.1, CC6.7 | — | ◐ Art. 32 | — | Encryption at rest and in transit, key management |
| Logging & Monitoring **(IS)** | ✅ A.8.15, A.8.16 | ✅ CC7.2 | — | ◐ | ◐ A.6.2.8 | |
| Incident Response Policy (+ plan) | ✅ A.5.24–A.5.28 | ✅ CC7.3–CC7.5 | — | ✅ Arts. 33–34 | ◐ A.8.4 | Must include personal data breach handling (72h) |
| Business Continuity & Backup | ✅ A.5.29, A.5.30, A.8.13 | ✅ CC9.1, A1 | — | ◐ Art. 32(1)(c) | — | Include restore testing |
| Supplier Security / Third-Party Risk | ✅ A.5.19–A.5.23 | ✅ CC9.2 | ◐ cloud | ✅ Art. 28 | ✅ A.10 | Include cloud and AI vendors |
| Secure Development & Change Management | ✅ A.8.25–A.8.32 | ✅ CC8.1 | — | ✅ Art. 25 | ✅ A.6 | PR review, separation of duties, testing |
| HR Security (screening, onboarding, exit, discipline) | ✅ A.6.1–A.6.5 | ✅ CC1.4 | ◐ | ◐ | ◐ | |
| Risk Management Policy / Methodology | ✅ 6.1.2, 6.1.3 | ✅ CC3 | — | ◐ Art. 35 | ✅ 6.1.2–6.1.4 | Can reference grc/context/risk-methodology.md |
| Data Protection / Privacy Policy (internal) | ◐ A.5.34 | ◐ Privacy (optional) | — | ✅ Art. 5(2), 24 | ◐ A.7 | Plus RoPA, retention schedule, DSAR procedure |
| Data Classification & Handling | ✅ A.5.12, A.5.13 | ✅ C1 (if selected) | — | ◐ | ◐ A.7 | |
| Data Retention & Disposal | ✅ A.8.10 | ✅ C1.2 (if selected) | — | ✅ Art. 5(1)(e) | ◐ | |
| AI Policy | — | — | — | ◐ | ✅ 5.2, A.2 | Organisational commitments on AI |
| AI Acceptable Use (staff use of AI tools) | ◐ A.5.10 | ◐ | — | ◐ | ✅ A.9 | Approved tools, data rules, human review |

## Priority guide
- **P1**: needed for Stage 1 / Type I / CE submission: the Information Security Policy, Acceptable Use, Access Control, Incident Response, Risk Management, and (if GDPR) Data Protection, plus (if ISO 42001) the AI Policy.
- **P2**: needed before Stage 2 / Type II period start: Supplier, Secure Development & Change, Business Continuity, HR Security, Data Classification & Retention.
- **P3**: maturity improvements and topic-specific standards.
