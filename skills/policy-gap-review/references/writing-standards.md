# Writing Standards for GRC Documents

## Document hierarchy
| Level | Answers | Changes | Approved by |
|---|---|---|---|
| **Policy** | *What* we commit to and *who* is accountable | Rarely (annual review) | Leadership / board |
| **Standard** | Specific mandatory requirements (e.g. "MFA on all SaaS") | Occasionally | Policy owner |
| **Procedure** | *How*, step by step | Often | Process owner |
| **Record** | Evidence it happened | Continuously | n/a |

Policies that contain procedure go stale and create audit exceptions. Keep them short.

## Policy anatomy
1. Document control: title, ID, version, owner, approver, `approved_on`, next review, classification
2. Purpose (2–3 lines)
3. Scope (who and what is in and out)
4. Policy statements: numbered, **testable**, using "must" for requirements and "should" for recommendations
5. Roles and responsibilities
6. Exceptions process
7. Compliance and enforcement
8. Related documents
9. Framework mapping (an appendix table of clause and control refs)
10. Revision history

## Testability rule
Every "must" statement should let an auditor ask "show me".
- ❌ "Access must be managed appropriately."
- ✅ "Access to production systems must be approved by the system owner before it's granted and reviewed at least quarterly."

## Proportionality
Write for the organisation that exists. A 20-person startup doesn't need a 40-page policy set. Use **the minimum viable policy set** that satisfies the selected frameworks, and merge topics where that's sensible (e.g. one "Information Security Policy" with topic sections).

## Commitments you can keep
Never commit to a frequency or SLA the team can't sustain for 12 months. Under SOC 2 Type II, every missed commitment is an exception. Prefer "at least annually" plus a real practice of more often, over "monthly" plus a real practice of annually.

## Style
- UK English unless the company profile says otherwise. ISO 8601 dates.
- Plain English. Define acronyms on first use.
- Role names, not people's names, in policy text. Named individuals belong in the document control and RACI only.
