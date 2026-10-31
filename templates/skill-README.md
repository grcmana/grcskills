# Skill name in plain English (e.g. DPIA: data protection impact assessments)

_Lead paragraph, 2–4 sentences. Say what the skill produces and for whom, in plain English. The website uses this as the page introduction and as a fallback meta description, so make the first sentence work on its own._

_This file is the human-facing skill page shown on grcskills.io and on GitHub. `SKILL.md` is for the agent; this is for people deciding whether to use the skill. Copy this template to `skills/<name>/README.md`, keep the ten `##` headings exactly as they are and in this order, and replace every italic instruction. CI checks the headings, a length of 800–1,500 words (code blocks don't count), at least three FAQ questions, related-skill links, and no raw HTML._

## What it does

_The job to be done, the outcome, and why it matters. 100–200 words. Name the main modes (e.g. screen / draft / review) if the skill has them._

## Who it's for

_Write for both audiences. One short paragraph each:_

- **GRC practitioners and engineers:** _what it automates for them and what they still own._
- **Accidental owners** (founders, CTOs, ops leads): _what they get without needing to know the framework first._

## When to use it

_Triggers and moments in a programme, as a short bullet list. Include the phrases people actually type. Also say when **not** to use it, and which skill to use instead._

## How it works

_The workflow as numbered steps, in plain English. Say what the skill reads (e.g. `grc/context/company-profile.md`), what it asks you (at most five questions if the profile is missing), and where a human must decide. 150–300 words._

## What you get

_Every output file under `grc/`, and what each is for. Always include the run log in `grc/runs/`. A short code block showing the file tree is fine (it doesn't count towards the word limit)._

## Worked example

_A fictional scenario only, never a real company or real personal data. Show the prompt someone would type, what the skill did, and an excerpt of the output. 200–400 words. Prefer the Acme Analytics example from GRC OS where it fits._

## Frameworks covered

_Clause, article and control IDs with own-words summaries. Never paste standard text. Mention the `as_of` date of the framework pack and that the reader should check the official source for anything that may have changed._

## Guardrails

_What the skill will not do: fill in approval fields, claim an organisation meets a standard or holds a certificate, give legal advice, store secrets or individuals' personal data. Add anything specific to this skill._

## FAQ

_At least three questions, each as a `###` heading with a 1–3 sentence answer. Use questions people really ask; the site marks these up for search and answer engines._

### Question one?

_Answer._

### Question two?

_Answer._

### Question three?

_Answer._

## Related skills

_Bullets linking to other skills with relative links, so they work on GitHub and the site can rewrite them:_

- [`company-context`](../company-context/): _why you'd use it with this skill._
