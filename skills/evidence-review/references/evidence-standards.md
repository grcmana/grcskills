# Evidence Standards

What makes evidence acceptable to an auditor or certification body. This applies across ISO 27001, ISO 42001, SOC 2 and Cyber Essentials Plus.

## The five tests
1. **Relevant**: it shows the specific control or requirement operating, not something adjacent.
2. **Complete**: it covers the full population or the full period. An auditor samples from the whole population, e.g. *all* leavers in the period, not the ones you chose.
3. **Dated**: there's a visible date or timestamp inside the audit period, or at the point in time for Type I and Stage 1.
4. **Attributable**: you can see who performed or approved it (name or role, system user).
5. **Authentic**: it comes from the system of record, as an export or a screenshot with URL, date and user visible, not retyped.

## Evidence types
| Type | Example | Strength |
|---|---|---|
| System-generated export | IdP user list with MFA status, CSV with timestamp | Strong |
| Screenshot (with context) | Config screen showing URL, date and logged-in user | Medium. Include context |
| Ticket / workflow record | Jira change ticket with approval and linked PR | Strong |
| Signed or approved document | Policy with version history and approval | Medium |
| Meeting minutes | Management review with inputs, outputs and decisions | Medium |
| Attestation / self-declaration | "We do X" | Weak. Only acceptable where the framework permits it (e.g. CE self-assessment) |
| Interview / observation | Auditor walkthrough | Auditor-collected |

## Design vs operating effectiveness
- **Design** (ISO Stage 1, SOC 2 Type I): a policy or procedure plus configuration showing the control exists.
- **Operating** (ISO Stage 2, SOC 2 Type II): records over time showing it actually happened, e.g. 4 quarterly access reviews, not just the procedure.

## Evidence hygiene
- Name files consistently: `<control-ref>_<short-desc>_<YYYY-MM-DD>.<ext>`, e.g. `A.8.8_vuln-scan-summary_2026-09-30.pdf`.
- **Redact** secrets, tokens and unnecessary personal data before sharing.
- Store evidence in your system of record (drive, GRC platform). The tracker records the **location**, not the file content.
- One artefact can satisfy several frameworks. Map it once, in `framework_refs`.

## Evidence tracker columns
`evidence_id, request, domain, framework_refs, owner, source_system, frequency, period_or_date, location, status, quality_rating, reviewer_notes, due_date, last_collected`

Status: `requested · in-progress · collected · reviewed · accepted · rejected · not-applicable`
Quality rating: `strong · adequate · weak · insufficient`
