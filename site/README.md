# grcskills.io site

A single static page, generated from `skills/*/SKILL.md`, so the catalogue never drifts from the repo.

```bash
NEWSLETTER_ACTION="https://<your-newsletter-provider>/subscribe" python3 site/build.py
# -> site/dist/index.html
```

## Deploy (Vercel)
- Import `grcmana/grcskills` in Vercel.
- **Root directory:** repo root. **Build command:** `python3 site/build.py`. **Output directory:** `site/dist`.
- Add the `NEWSLETTER_ACTION` environment variable (your Beehiiv, Kit or other provider's form endpoint).
- Add the `grcskills.io` domain.

`site/dist/` is committed too, so any static host (Netlify, Cloudflare Pages, GitHub Pages) can serve it with no build step.

Edit the copy in `site/template.html`, and the one-line skill summaries in `site/build.py` (`SUMMARY`).
