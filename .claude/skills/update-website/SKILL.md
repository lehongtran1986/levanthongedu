---
name: update-website
description: Use whenever the user wants to edit, add, or fix content/pages on the levanthongedu.com website (LêVănThông Education) — text changes, images, new subject/program pages, form/backend integration, or deployment. Also use when asked to preview the site locally or explain how it's built.
---

# Editing the LêVănThông Education website

This is a **static HTML site generated from a single Python script** — it is
NOT hand-written HTML and NOT a framework (no React/Next/build step). Tailwind
is loaded via CDN `<script>` tag, no npm/node involved.

## The one rule that matters

**Never hand-edit the `.html` files directly.** They are all generated from
`scripts/gen_site.py`. Any manual edit to an `.html` file will be silently
overwritten the next time the script runs, and worse, will drift out of sync
with the shared header/footer/nav baked into every page.

Edit `scripts/gen_site.py`, then regenerate:

```bash
cd "/Users/lehongtran/Desktop/Website_Trung tam luyen thi"
python3 scripts/gen_site.py
```

This rewrites every `.html` file at the repo root and under `programs/`.
`css/styles.css` and `js/main.js` are hand-maintained static files (not
generated) — edit those directly.

## How the generator is organized

Read `scripts/gen_site.py` top to bottom before editing — it's ~600 lines,
plain and linear, no imports beyond `os`. Key parts:

- **Global constants** (top of file): `CENTER_NAME`, `TAGLINE`, `PHONE_DISPLAY`/`PHONE_TEL`,
  `ZALO_LINK`, `ADDRESS`, `FORM_ENDPOINT`, `MAP_LAT`/`MAP_LNG`/`MAP_IFRAME`,
  `GRADES`, `CLASS_SIZE`. Change these once, they propagate everywhere
  they're referenced (header phone button, footer, meta tags, etc).
- **`header()` / `footer()` / `page()`**: shared chrome rendered identically
  on every page. `NAV_ITEMS` list controls the nav menu — add/remove a page
  from navigation here.
- **`SUBJECTS` dict**: one entry per course page (`toan`, `vatly`, `anhvan`,
  `ielts`). Each entry configures title, summary, instructor, audience,
  eligibility text, optional `subject_image`, optional `teacher_bio`. The
  `subject_page(slug)` function renders `programs/<slug>.html` generically
  from this config — **to add a new course/subject page, add a new dict
  entry here**, don't write a new HTML template.
- Each other page (`index.html`, `about.html`, `method.html`,
  `assessment.html`, `results.html`, `public-info.html`, `contact.html`) is
  built as an f-string body (`index_body`, `about_body`, etc.) then passed to
  `write("<file>.html", page(title, description, current, body))`.

## Workflow for a content change

1. Read the relevant section of `scripts/gen_site.py` (grep for the Vietnamese
   text being changed — it's plain text in f-strings, easy to find).
2. Edit it there.
3. Run `python3 scripts/gen_site.py` from the repo root.
4. Preview locally (see below) and visually confirm the change.
5. `git add -A && git commit -m "..." && git push` — Netlify auto-deploys
   from GitHub `main` within about a minute (see Deployment below).

## Previewing locally

```bash
cd "/Users/lehongtran/Desktop/Website_Trung tam luyen thi"
python3 -m http.server 8123
# open http://localhost:8123
```

**Known gotcha:** browsers aggressively cache `js/main.js` and `.html` files
served by Python's bare `http.server` (no cache-control headers sent). If you
edit `js/main.js` and a reload doesn't seem to pick up the change, don't
trust it — kill the server and restart on a **fresh port number**, or open a
brand new browser tab, rather than assuming the fix didn't work. This bit us
once already (see git log "Kết nối form đăng ký tư vấn tới Google Apps
Script" commit) — the code was correct but stale cache made it look broken.

## Images

- Live in `assets/images/`, referenced as `/assets/images/<file>.jpg`.
- Naming: lowercase, hyphens, no spaces/accents, descriptive
  (`thay-thong-lop-vatly-01.jpg`, not `IMG_0762.jpg`).
- Compress before committing — target under ~300KB. Use macOS `sips`
  (no extra install needed):
  ```bash
  sips -Z 1200 -s formatOptions 70 path/to/image.jpg
  ```
  (`-Z 1200` caps the longer edge at 1200px, formatOptions 70 = JPEG quality.)
- HEIC photos (iPhone default) need converting first:
  ```bash
  sips -s format jpeg -Z 900 -s formatOptions 75 input.HEIC --out output.jpg
  ```
- Only use real photos the user confirms ownership of. Never scrape/reuse
  images found on the web for this commercial site without the user's
  explicit go-ahead (see prior session: Google Business Profile photos were
  used only after the user confirmed they were the center's own).

## Registration form → email (Google Apps Script)

`assessment.html`'s form POSTs JSON to the URL in `FORM_ENDPOINT`
(`scripts/gen_site.py`), which is a deployed Google Apps Script Web App. The
script itself lives in the user's Google account (Extensions → Apps Script
on their Google Sheet), **not in this repo** — if it ever needs updating,
you have to walk the user through pasting new code into the Apps Script
editor and redeploying (Deploy → Manage deployments → edit → New version).
There's a copy of the current script logic in git history (see commit "Kết
nối form đăng ký tư vấn tới Google Apps Script") if you need to reconstruct
it.

The frontend handler is in `js/main.js` (`initPage()`). It intercepts
`submit`, builds a JSON payload, and does:

```js
fetch(endpoint, { method: 'POST', mode: 'no-cors', body: JSON.stringify(payload) })
```

`mode: 'no-cors'` is required — Apps Script Web Apps don't return proper CORS
headers, so the response can't be read; we just treat any non-throwing fetch
as success and show the thank-you block (`#assessment-success`).

`js/main.js` initializes via a `document.readyState` check rather than a
bare `DOMContentLoaded` listener — this avoids a real race condition we hit
where the event had already fired by the time the listener attached,
silently breaking form submission (it fell back to a native GET submit that
reloaded the page and sent nothing to Apps Script). Keep that pattern if you
touch `main.js`.

## Deployment pipeline (already set up, don't recreate)

- **Git**: local repo → `github.com/lehongtran1986/levanthongedu` (`main` branch).
  `gh` CLI is authenticated on this machine (`gh auth status` to check).
- **Hosting**: Netlify, auto-deploys on every push to `main`. No build
  command, publish directory is repo root.
- **Domain**: `levanthongedu.com`, registered and DNS-managed at Cloudflare.
  DNS records: `A` record `@` → `75.2.60.5` (Netlify's IP), `CNAME` `www` →
  `<netlify-site-name>.netlify.app`, both set to **DNS only** (grey cloud,
  not proxied) — proxying through Cloudflare breaks Netlify's SSL.
- Pushing to `main` is the entire deploy step. No manual Netlify action
  needed for routine content changes.

## Content/brand facts worth knowing before writing new copy

- Brand: "Lê Văn Thông Education" (with spaces — not "LêVănThông").
- Positioning: luyện thi đại học đánh giá năng lực (Toán – Vật lý – Tiếng
  Anh), phục vụ học sinh lớp 6–12, nhấn mạnh định hướng đánh giá năng lực.
- No entrance test / no "Yêu cầu đầu vào" framing anywhere — the center
  explicitly dropped that positioning; don't reintroduce "kiểm tra đầu vào"
  as a requirement.
- Terminology: "học sinh", not "học viên" (site-wide rename already done).
- Tuition/schedule detail cards and the whole FAQ block were deliberately
  removed from course pages per the user's request — don't re-add without
  being asked.
- IELTS course levels are Band 5.0/5.5/6.0/6.5, not grade-based like the
  other three subjects — see how `SUBJECTS["ielts"]` differs from the
  grade-based entries if adding another non-grade-based course.
