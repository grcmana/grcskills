# catalog.json schema 2: skill, category and contributor pages

_Status: **proposed**, for agreement between the grcskills maintainers and the grcskills.io owner. Proposed 2026-10-31._

## Why

grcskills.io is a single page today. We want three new page types:

| Page | Route (suggested) | Source in this repo |
|---|---|---|
| Skill page (800–1,500 words) | `/skills/<name>` | `skills/<name>/README.md` |
| Categories index and category page | `/categories`, `/categories/<slug>` | `collections/<slug>.md` |
| Contributors index and contributor page | `/contributors`, `/contributors/<handle>` | `contributors/<handle>.md` plus `metadata.author` in each `SKILL.md` |

All of this content stays in the public repo, is reviewed in the same PRs as the skills, and reaches the site only through `catalog.json` on a pinned release. **No CMS.** Decision D6 (the website consumes only a released `catalog.json`) is unchanged.

## Compatibility

Schema 2 is a **strict superset** of schema 1. Every schema-1 field keeps its name, type and meaning. A consumer that reads schema 1 fields keeps working, provided it doesn't reject `schema: 2` outright.

## New fields

### Top level

| Field | Type | Notes |
|---|---|---|
| `schema` | `2` | |
| `collection_pages` | array of collection objects | Ordered by `order`. `collections` (strings) is kept for schema 1. |
| `contributors` | array of contributor objects | Sorted by number of skills authored, then name. |

### Collection object

| Field | Type | Notes |
|---|---|---|
| `slug` | string | Matches `skills[].collection_slug`. Use in the URL. |
| `title` | string | Same string as in `collections` and `skills[].collection`. |
| `order` | integer | Display order. |
| `intro_markdown` | string | 100–400 words. **Untrusted Markdown**: see Rendering. |
| `skills` | string[] | Skill names, alphabetical. |

### Skill object: added fields

| Field | Type | Notes |
|---|---|---|
| `collection_slug` | string | |
| `authors` | string[] | GitHub handles, lowercase. Each has a contributor object. |
| `readme` | object or `null` | `null` until the skill has a page. |
| `readme.markdown` | string | Full page Markdown, including the `#` title. **Untrusted.** |
| `readme.words` | integer | 800–1,500, code blocks excluded. |
| `readme.faq` | string[] | FAQ question headings, in order (at least 3). |
| `readme.related` | string[] | Skill names linked under "Related skills". |

The README always has these `##` sections, in this order (enforced by CI): What it does · Who it's for · When to use it · How it works · What you get · Worked example · Frameworks covered · Guardrails · FAQ · Related skills. FAQ questions are `###` headings under `## FAQ`.

### Contributor object

| Field | Type | Notes |
|---|---|---|
| `handle` | string | GitHub handle, lowercase. Use in the URL. |
| `name` | string | Display name. |
| `kind` | `"person"` or `"organisation"` | |
| `role` | string | 80 characters max, may be empty. |
| `links` | object | Optional `website`, `linkedin`. Always `https://`. |
| `github_url` | string | |
| `avatar` | string | `https://github.com/<handle>.png` |
| `bio_markdown` | string | 20–300 words. **Untrusted.** |
| `skills` | string[] | Skills this contributor authored. |

Profiles are opt-in. The repo rejects any field outside the list above, so there is no email, location or employer to leak.

## Rendering requirements for the site

Community-written Markdown now reaches the site. HTML-escaping string fields is no longer enough on its own.

1. **Render Markdown with raw HTML disabled, then sanitise** with an allowlist (for example `rehype-sanitize` with its default schema). CI also rejects raw HTML, but the site must not rely on that.
2. **Links:**
   - `../<name>/` → `/skills/<name>`.
   - Other relative links → `https://github.com/grcmana/grcskills/blob/<release>/skills/<name>/<path>`.
   - External links get `rel="nofollow ugc noopener"`.
   - Allow only `https:` and `mailto:` schemes.
3. **Images:** none are expected in v1. Strip them, or allow only images served from the release.
4. **Avatars:** prefer downloading them at build time and self-hosting, so visitors don't make third-party requests to GitHub. Fall back to initials.
5. **Skills without a page** (`readme: null`): render a short page from `summary`, `description`, frameworks and install command, and mark it `noindex` until the README lands.
6. **SEO:**
   - Meta description: `summary`.
   - `FAQPage` JSON-LD built from the FAQ section.
   - Canonical URL on the site, not GitHub.
   - Add all new routes to the sitemap.

## Release flow (unchanged)

Merge to `main`, then a maintainer cuts `vX.Y.Z`, then `release.yml` builds and attaches `catalog.json`, then the deploy hook rebuilds the site. Copy fixes ship in patch releases (`v0.1.x`).

## Open questions for the site owner

1. Does the site check `schema === 1` strictly? If so, it needs a one-line change before the first schema-2 release.
2. Are the route names right? We used `collection` in the repo and "categories" on the site.
3. Should the site add git-derived contributor stats (commits and PRs) at build time through the GitHub API? This is out of scope for the catalogue, which only records authorship.
