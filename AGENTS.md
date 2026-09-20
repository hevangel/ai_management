# AGENTS.md

Instructions for AI coding agents working in this repository.

## What this repo is

An AI-agent-maintained static website of business, management, and consulting articles —
polished HBR / MIT Sloan Management Review style writing on the impact of AI in business
(see `README.md`). Published on GitHub Pages at https://hevangel.github.io/ai_management/
(repo: `hevangel/ai_management`, branch `main`). No build step, no package manager — the
site is plain files pushed to GitHub.

This repo is the sibling of `B:\ai_philosophy` (`hevangel/ai_philosophy`): same single-page
app architecture, same content pipeline, different subject matter. When a convention is not
covered here, **read `B:\ai_philosophy\AGENTS.md`** — it is the reference implementation.

Status: the site exists — `index.html` + `content.json` at the repo root, ported from the
philosophy repo and extended with the case-study reader. The first case study (VIBEITDA) is
published at `articles/case-studies/vibeitda/`: one business problem (AI decouples growth
from headcount) attacked through five publication-style essays drafted in the owner's
ChatGPT conversation and refined from the transcript at
`sratchpad/vibeitda_chatgpt_transcript.md`. Nothing is pushed/committed beyond the initial
commit yet, and GitHub Pages may still need enabling in the repo settings.

## The five-styles skill

`.agents/skills/five-styles/SKILL.md` transforms raw material — conversation transcript,
brainstorming notes, rough draft — into **five structurally different articles** in the
editorial logics of: 1. MIT Sloan Management Review, 2. Harvard Business Review,
3. McKinsey & Company, 4. BCG, 5. Bain & Company. It is implemented faithfully from the
spec at the end of the ChatGPT conversation "Explain Vibeitda"
(https://chatgpt.com/share/6aa621ef-59d0-83e8-9cb4-0083364b9f6b); the scraped transcript is
at `sratchpad/vibeitda_chatgpt_transcript.md` (strip chat-export artifacts — favicon
citation images, `utm_source=chatgpt.com` links, `citeturn` tokens — when quoting from it).

Core pipeline:

- **Stage 0 — Source Synthesis Memo**: a one-page memo written before anything else and
  the canonical source of truth for every later output — thesis, causal chain, evidence,
  counterarguments, unresolved questions, authorial position (section spec in the skill's
  `references/source-synthesis-memo.md`). When the author's thinking changes, revise the
  memo first, then regenerate only the affected versions.
- **Stage 1 — extract the intellectual core** before writing anything: central thesis,
  conventional view being challenged, new observation, causal mechanism, key tension,
  evidence (separating empirical / example / analogy / speculation), original terminology,
  managerial implications. When the source is a conversation, use the most developed version
  of the argument and note which early ideas the author rejected or refined.
- **Stage 2 — verify** current facts via research (original research, filings, government
  statistics first; a consulting firm's claim is never proof just because the article is in
  consulting style). Never invent data, examples, or personal experiences. Label speculation.
- **Stage 3 — write five independent articles**: different structures, different section
  logic — never one article with synonym-swapped headings. Sloan = strongest conceptual
  model (equations and new terminology allowed); HBR = clearest managerial actions; McKinsey
  = clearest operating model; BCG = strongest competitive-strategy argument; Bain =
  strongest economic decision framework.
- **Cover-art briefs**: one per publication, each visualizing that version's argument —
  never one image recolored, never masthead imitation (briefs + required output format in
  the skill's `references/cover-art.md`).
- **Final quality check**: same underlying insight in all five, factual claims supported,
  no invented experience, author's strongest ideas not diluted, five structures and five
  cover concepts materially different.
- Optional invocation parameters: length, audience, evidence rigor, editorial voice,
  anecdote handling, provocativeness, cover-art output (briefs only / prompts only /
  generated images / none); sensible defaults are in the spec.

## Site architecture

Port the SPA from `B:\ai_philosophy` (single `index.html` + `content.json` at repo root)
and extend it with the case-study reader. Inherited rules that must be preserved:

- GitHub Pages serves under the subpath `/ai_management/` — **every URL must be relative**,
  no leading `/`.
- `content.json` drives the whole UI (menu, sections, item metadata). Nothing is
  auto-scanned; a page only exists if registered there.
- Markdown rendered client-side by `marked` + `DOMPurify` (jsDelivr CDN). Routing uses the
  History API with clean paths: `/ai_management/`, `/section/<id>`, `/read/<section>/<slug>`,
  `/case/<slug>[/<publication>]` (a case study's title page, or one of its five publication
  essays), `/md/<path>`. The app derives its base path from `location.pathname` (`APP_BASE` —
  `/ai_management/` on both live hosts, `/` for a local server rooted at the repo) and prefixes
  every app-relative resource/link with it. A document-level click interceptor routes in-app
  links via `pushState`; `popstate` re-routes; legacy `#/…` URLs are upgraded to clean paths in
  place (never re-introduce hash-only links). Deep links rely on server fallback: Apache
  `RewriteRule . index.html [L]` in the horace.org `.htaccess`, and the repo's `404.html` shim
  on GitHub Pages (which has no fallback) — keep `404.html` in sync if the base path changes.
  The SPA strips the first
  `H1` of rendered markdown (titles come from `content.json`) and resolves relative
  `img src` against the markdown file's own folder.
- Google Analytics 4 (`G-QQXX5SHEHH`, shared with the philosophy repo's property) is wired
  into `index.html`: the gtag config sets `send_page_view: false` and the router's
  `setTitle()` sends `page_view` manually (via `trackPageView`) so every hash-route change
  counts, with the final document title and full hash URL. Don't bypass `setTitle()` in
  route code, or pages stop being tracked.
- Bilingual (English / Hong Kong Traditional Chinese) and themeable (light / dark), with
  `EN / 中` and 🌙/☀️ switches persisting in `localStorage` (use fresh keys, e.g.
  `aimgmt-lang` / `aimgmt-theme`, not the philosophy repo's), applied pre-paint by an inline
  head script. Chinese documents are the `chinese_`-prefixed sibling of the registered
  `path` (`articles/x/index.md` → `chinese_index.md`); display fields fall back from
  `<field>_zh` to English. Write Chinese at a business-reader register (HK Traditional
  Chinese, 「」 quotes, 《》 for works), not the philosophy repo's academic register.
- Cover images: AI-generated via the glm-image API — recipe, prompt style formula, and the
  current API-balance failure mode are documented in `B:\ai_philosophy\AGENTS.md`
  (Content conventions + Gotchas). Same `cover.png` / `chinese_cover.png` / `cover_zh_text`
  fallback conventions apply.

### The case-study page

A series of articles attacking **the same business problem from five publication angles**
is NOT listed as five separate items. The index page links to a single landing page — the
**Case Study** (section `case-studies`, route `#/case/<slug>`).

Implemented shape (keep new case studies consistent with it; everything registered in
`content.json`): a case folder under `articles/case-studies/<slug>/` holds:

- `problem.md` — the title page (problem statement + plain-language findings), plus
  `chinese_problem.md`;
- one markdown file per publication — `sloan.md`, `hbr.md`, `mckinsey.md`, `bcg.md`,
  `bain.md` — each with a `chinese_` sibling;
- one logo file per publication (`<pub>_logo.svg`) plus `cover.png` (AI-generated or
  supplied art);

and the `content.json` item carries a `case.publications` array, each entry with `id`,
`name` (+ `name_zh`), `logo`, `title` (+ `title_zh`), `path`. The page renders the title
page by default; the five tabs (publication logo + name, localized) swap in each essay.
A "Read each angle" guide — localized links to all five essays plus the cover image — is
rendered by the SPA below the content on every tab (including the title page), so readers
can move between essays; the current essay is highlighted rather than linked.
The tab labels and headings come from `content.json` — never hardcode publication names in
`index.html`. Publication logos are trademarks — committed image files in the case-study
folder (SVG wordmarks from official/Wikimedia sources), never hotlinked; the SPA inverts
them to white in dark theme.

## Content conventions

- One folder per document: `<folder>/<slug>/index.md`, images in the same folder, cover
  image `cover.png`, first line `# Title`. For case studies see the structure above.
- Publishing = create the folder + markdown (promoted out of `sratchpad/` if drafted
  there), then register an entry in `content.json` with `slug`, `title`, `summary`,
  `path`, `cover`, `date` (ISO) plus the `_zh` fields; missing `_zh` falls back to English
  and must never break the site.
- Writing register: polished HBR / MIT Sloan management prose. Claims must be supported or
  labeled as speculation; preserve the author's strongest original ideas and terminology
  (e.g. VIBEITDA).
- Strip chat-export artifacts (`citeturn…` tokens, favicon citation images,
  `utm_source=chatgpt.com` links) when promoting anything from a chat transcript.

## Verifying changes

- `fetch()` does not work from `file://`. Serve locally and open the printed URL:
  `py -3 -m http.server 8123` → http://localhost:8123/ (port 8000 is blocked on this
  machine — see Gotchas).
- Check: home renders all sections from `content.json`; every registered entry opens and
  renders; images resolve (covers, thumbnails, logos); `content.json` is still valid JSON;
  on a case-study page the title page renders by default and all five tabs switch content
  with name + logo visible.
- Check both languages and both themes on the home page, one article, and one case study;
  missing Chinese text or covers must fall back to English silently.

## Gotchas

- Relative paths only (GitHub Pages project site = subpath hosting).
- CDN scripts need network access during local preview; if the libs fail to load, markdown
  will not render — check the browser console.
- Port 8000 sits in a Windows reserved-port range on this machine (`WinError 10013`) — use
  e.g. 8123. Local preview servers are ephemeral; the live site is GitHub Pages.
- If the live site 404s after a push, check GitHub Pages is enabled for `hevangel/ai_management`
  (deploy from branch `main`, root) in the repo settings — the repo is new.
- `.mimosa/` is security-scanner state, not site content — leave it alone, never register it.
- `sratchpad/` (note the spelling) is scratch space: working files, drafts, downloads,
  transcripts. **Never displayed by the site; never reference it from `content.json`.**
- `.firecrawl/` scrape outputs are disposable working data — move anything worth keeping
  into `sratchpad/` (the VIBEITDA transcript lives at
  `sratchpad/vibeitda_chatgpt_transcript.md`).
- `linkedin/` is the owner's working data for LinkedIn posts — not site content, never
  register it in `content.json`.
- Logo files must have truthful extensions: an SVG saved as `.png` (or a failed download
  saved as an image) renders as a broken tab icon because the dev server sends the
  MIME type by extension.
