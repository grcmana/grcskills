# Security policy

GRC Skills are instructions that AI agents follow while handling sensitive governance data. We treat weaknesses in them as security issues.

## What to report privately
- A skill that could leak data: e.g. an instruction that sends workspace content somewhere, or copies secrets or personal data into outputs.
- Prompt-injection weaknesses: a skill that would follow instructions embedded in documents, evidence files or web pages.
- A skill that bypasses human approval, or fills in approval fields.
- Malicious or suspicious content in a merged contribution.
- Vulnerabilities in the repo's scripts or workflows.

## How to report
Use **[Report a vulnerability](https://github.com/grcmana/grcskills/security/advisories/new)** (GitHub private vulnerability reporting). Please don't open a public issue.

We aim to acknowledge reports within 5 working days, and to agree a fix and disclosure timeline with you.

## Not security issues
Wrong or outdated framework guidance is important, but it isn't a security issue. Use the **Framework correction** issue form.
