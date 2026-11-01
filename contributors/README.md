# Contributors

Each folder here is an **opt-in** public profile shown on [grcskills.io/contributors](https://grcskills.io). Add yours in the same pull request as your first contribution.

```
contributors/
  <your-github-handle>/
    README.md      your profile (required)
    avatar.png     your picture (optional; or avatar.jpg / avatar.jpeg)
```

## 1. Your profile

1. Copy `harrywestuk/README.md` to `<your-github-handle>/README.md`. The folder name is your GitHub handle in lowercase.
2. Fill in the frontmatter. Only these fields are accepted:

   | Field | Notes |
   |---|---|
   | `name` | Required. Your display name. |
   | `github` | Required. Must match the folder name. Your GitHub link is added for you. |
   | `kind` | `person` (default) or `organisation`. |
   | `role` | 80 characters max. |
   | `website` | Any `https://` URL. |
   | `linkedin` | `https://www.linkedin.com/in/…` (or `linkedin.com`) |
   | `x` | `https://x.com/…` (or `twitter.com`) |
   | `youtube` | `https://www.youtube.com/@…` |
   | `medium` | `https://medium.com/@…` or `https://<name>.medium.com/` |
   | `tiktok` | `https://www.tiktok.com/@…` |
   | `facebook` | `https://www.facebook.com/…` |

   Every link is optional and must be a full `https://` URL on that platform's own domain, with no port, login details or spaces, and at most 300 characters. Country and mobile domains (`uk.linkedin.com`, `m.facebook.com`) and short links (`youtu.be`, `fb.com`) are rejected, so use the main domain. Links that don't fit a platform, such as a Medium publication on its own domain, go under `website`.

   There is deliberately no field for email, location or employer.
3. Write a short bio below the frontmatter: 20–300 words, plain Markdown, no HTML.
4. To be credited as a skill author, add your handle to `metadata.author` in that skill's `SKILL.md` (comma-separated, e.g. `author: grcmana, your-handle`).

## 2. Your picture (optional)

Without one, the site uses your public GitHub avatar. To use your own, add **one** file named `avatar.png`, `avatar.jpg` or `avatar.jpeg` to your folder. CI checks that it is:

- a real PNG or JPEG (not just renamed), not animated, and not SVG
- square, and at least 256×256 pixels (512×512 is ideal)
- 500 KB or smaller
- **free of embedded metadata** (EXIF, XMP or IPTC). Photos from a phone or camera often record where they were taken. Remove it before you commit, for example:
  - `exiftool -all= avatar.jpg`
  - macOS Preview: Tools › Show Inspector, then remove location info, or export as PNG
  - GIMP: File › Export As, then untick "Save Exif data" and "Save XMP data"

The site picks up a new picture at the next release.

## Removing your profile

Open a PR deleting your folder, or ask a maintainer and we will do it for you. The site drops it at the next release. Earlier releases and the repository's git history still contain it, because that is how git works, so only add a picture you are happy to stay public. If that becomes a problem, contact a maintainer.
