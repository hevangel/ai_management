---
name: linkedin-publish
description: Publish one of the site's articles as a long-form LinkedIn article (Pulse) on the owner's account — cover image, full text, then "share with a post" — via browser automation (browser-use). Use whenever the user asks to post, publish, or promote a repo article on LinkedIn. Requires the share-post text to be supplied verbatim by the user — this skill NEVER drafts, summarizes, translates, or "improves" post content.
---

# linkedin-publish — publish a site article as a LinkedIn article

Publishes `articles/<slug>/` to the owner's LinkedIn (account: Horace Chan,
linkedin.com/in/horacechan) as a **long-form LinkedIn article** (the "Write
article" / Pulse flow) with the article cover as the hero image and the full
markdown text as the body, then shares it with a post carrying the human's
words. Correct flow confirmed by the owner 2026-10-25 — do NOT post a bare
link to the site instead.

## Hard rules

- **The share-post text is 100% human-supplied. If it was not provided in the
  invocation, STOP and ask for it.** Never summarize the article, never draft,
  rewrite, fix typos, translate, or "polish" it. Post it character-for-
  character (double spaces and grammar quirks included). The article body
  itself, by contrast, is site content — copy it from `index.md` faithfully.
- **Load the `browser-use:control-browser` skill first and do the browser work
  yourself** — never delegate to a subagent. If that skill is not available,
  use the **`playwright-cli` fallback** (section below) instead.
- If the in-app browser is not logged in to LinkedIn, stop and hand the login
  to the user. Never touch credentials.
- One article per invocation; never bulk-publish or auto-retry a failed
  Publish click more than once (check recent activity first — the first click
  often succeeded).
- The Mimosa commit hook may block a push over pre-existing findings elsewhere
  in the tree; commit only this skill's own files and report any blocked
  finding to the user instead of "fixing" unrelated code silently.

## Input prep

1. Read `articles/<slug>/index.md` and take the title from the `# ` line; the
   rest is the body. For a case study, use the chosen publication essay under
   `articles/case-studies/<slug>/` and that folder's `cover.png`. Check the
   article's `title`/`summary` in `content.json`.
2. **Convert LaTeX math to plain Unicode text first.** LinkedIn cannot render
   LaTeX: `\[ ... \]` and `\( ... \)` arrive as raw source or vanish. Find them
   with a search for `\[`, `\(`, `\mathrm`, `\frac`, `\sum`. Rewrite each in a
   LinkedIn-only copy of the body, never in `index.md`: display equations as a
   bold paragraph (`**N_b = F ÷ [ (C_b + R_b) − (C_t + R_t) ]**`), inline math as
   plain text with Unicode symbols (`ℰ Δ Σ → × ÷ −`, `C_b` for subscripts —
   Unicode has no subscript letters for most). Do NOT put `*` (e.g. `N*`) inside
   bold markup — it breaks the emphasis; rename the symbol instead. Write the
   converter as a script file; shell heredocs and tool-call strings halve
   backslashes, so build patterns with `chr(92)` / `re.escape`.
3. Convert the body (title stripped) markdown → HTML with
   `py -3 -m pip install --user markdown`, then
   `markdown.markdown(body, extensions=['extra'])`. The Pulse paste keeps
   `<p>/<strong>/<em>/<h2>` rich formatting; `<hr>` section breaks may or may
   not survive — text is what must survive. Tables and code blocks may be
   flattened; check them after pasting.
4. Check for leftovers before pasting: no `\[a-zA-Z]+` and no `\(`, `\[`, `\)`
   remain in the LinkedIn copy.

## Browser mechanics (learned 2026-10-25, all confirmed live)

- **Session shape**: set the tab viewport to 1366x900 first — narrower panes
  get LinkedIn's mobile layout. Tabs are released at turn end: if
  `browser.tabs.list()` comes back empty, check `browser.user.openTabs()` and
  `claimTab` the LinkedIn page, or just open a fresh tab — the login session
  persists in the browser, not in the tab.
- **Write article, not Start a post.** Feed → "Write article" link
  (`/article/new/`) → "Publish new article" editor with a cover area, a
  `textbox "Title"`, and a `textbox "Article editor content"`. The first
  `goto` may report a navigation timeout — check URL/title before retrying;
  it loads anyway.
- **Title**: focus via `locator.evaluate((el) => el.focus())`, type via
  `locator.type(...)`. `innerText` reads back empty on this field — verify
  through `domSnapshot()` instead.
- **Cover image upload works via direct file-input injection** (the share
  composer does NOT allow this, but the article editor does):
  1. CUA-click "Upload from computer".
  2. Immediately deep-search shadow DOM for `input[type=file]` (it mounts on
     click; walk elements + `.shadowRoot` recursively).
  3. Build the File in-page: `new Image()` with `crossOrigin="anonymous"` →
     canvas → `toBlob` → `File` → `DataTransfer` → `input.files = dt.files` →
     dispatch `input` + `change` events. Source URL:
     `https://hevangel.github.io/ai_management/articles/<slug>/cover.png`
     (GitHub Pages sends open CORS; LinkedIn's patched `fetch`/XHR are blocked
     by CSP, the `img` route is not).
  4. A crop/confirm dialog appears → screenshot to aim → click its "Next".
- **Body paste**: the Pulse editor ACCEPTS synthetic `ClipboardEvent("paste")`
  with `text/html` + `text/plain` (unlike the feed share composer, which only
  accepts trusted OS input). OS-clipboard routes (`execCommand("copy")`,
  `navigator.clipboard.write`) are all permission-blocked in the IAB.
  Transport the ~40 KB HTML into the page as chunked `evaluate` arguments
  stashed on `window.__chunks[i]` (order-independent), join in order, then:
  1. **First clear the editor with a REAL CUA click into the body text**,
     then CUA `Control+a` + `Backspace` (evaluate-focus alone ignores keys).
     Verify `(el.innerText).trim().length === 0` before pasting.
  2. Dispatch one paste event carrying the full HTML + plain-text twin.
  3. Verify: `innerText` length ≈ 36 k for a 5 k-word essay, head matches the
     first sentence, tail matches the last line.
- **Draft autosave is a trap**: the editor saves continuously ("Draft - saved").
  A reload does NOT give a blank editor — it restores the last save. Escape a
  bad state inside the editor (click into the text, `Control+a`, `Backspace`,
  verify empty); never reload to "reset".
- **Publish flow**: "Next →" opens the share dialog ("Tell your network what
  your article is about...", article preview attached). Focus its textbox and
  `locator.type` the human's words verbatim — this dialog accepts locator
  typing. "Publish" publishes the article AND the share post together.

## Fallback: `playwright-cli` (when browser-use is unavailable)

Same flow, same hard rules; only the driver changes. `playwright-cli` is a
global npm CLI (`playwright-cli --help`; `-s=<name>` names a session). This
fallback is **untested on LinkedIn** — verify each step with a snapshot or
screenshot and update this section with what actually works.

- **Login**: open a visible, persistent session so the login survives between
  runs: `playwright-cli -s=li open https://www.linkedin.com/feed/ --headed
  --persistent` (add `--browser=chrome` or `msedge` if the bundled Chromium is
  missing; `install-browser` fetches one). If not logged in, stop and let the
  user log in in that window — never touch credentials. Alternative:
  `attach --extension=chrome` to reuse the user's real Chrome session.
- **Viewport**: `playwright-cli -s=li resize 1366 900` before anything else.
- **Navigate / inspect**: `goto https://www.linkedin.com/article/new/`, then
  `snapshot` to get element refs and `screenshot` to check visually. Click and
  type by ref (`click <ref>`, `fill <ref> <text>`, `type <text>`); `press
  Control+a` / `press Backspace` for real keystrokes.
- **Cover upload**: much simpler than browser-use. Download the cover locally
  (`articles/<slug>/cover.png` in the repo is the same file), click "Upload from
  computer", then `playwright-cli -s=li upload <absolute path to cover.png>`
  (answers the file chooser). If `upload` finds no chooser, fall back to
  `run-code` with `page.setInputFiles('input[type=file]', path)`. Then click the
  crop dialog's "Next". (Confirmed 2026-11-11: `upload` works.)
- **Title**: click the Title textbox by ref, `type` the title; verify with
  `snapshot`.
- **Body**: click into the editor, `press Control+a` + `press Backspace`, verify
  empty (`eval` `innerText.trim().length === 0`; Ctrl+A stays inside the body,
  the title and cover survive). Then paste the HTML via `run-code` dispatching
  a synthetic `ClipboardEvent("paste")` with `text/html` + `text/plain`.
  **`run-code` has no `require`/`fs`**, so generate a JS file that embeds the
  HTML and text as `JSON.stringify` literals and load it with
  `run-code --filename=<file>` (a 46 KB script is fine). Verify head, tail and
  `innerText` length as above (confirmed: 5.2 k words → ~38 k chars).
- **Publish**: click "Next", `click`/`type` the human's share text verbatim into
  the dialog, screenshot to confirm, then click "Publish" **only after the user
  confirms**. Verify as in Procedure step 6.
- Close with `playwright-cli -s=li close` (or `detach` for an attached browser)
  when done; the persistent profile keeps the login. **Never chain `close`
  after a command that may fail** — it kills the session you still need.
- Snapshots/console logs land in a `.playwright-cli/` folder in the current
  directory: run from the repo root or a scratch dir, and delete it afterwards
  — never commit it. Write temp files (HTML, scripts, screenshots) to the
  scratchpad, not the article folder.
- The first confirmed run (2026-11-11) used refs from `snapshot`: Title and
  "Article editor content" textboxes, the share dialog's "Text editor for
  creating content" textbox, then its "Publish" button. `type` into the Title
  and share textboxes worked; read back via `screenshot` (the Title field's
  `innerText` is empty).

## Editing an already-published article

Open `https://www.linkedin.com/article/edit/<id>/` (the id is in the edit URL
shown while drafting, and under Manage on the live article). The page shows an
**Update** button instead of Next/Publish. Clear the body, paste the corrected
HTML, verify, then click **Update** — it re-publishes in place, keeps the same
`/pulse/...` URL and does **not** create a new share post. Confirm on the live
page by searching `document.body.innerText` for expected strings.

## Feed composer — plain posts, DMs, comments (the hard way)

If the human ever wants a plain feed post, DM, or comment, the feed UI is
far more hostile than the article editor:

- "Start a post" and the composer toolbar live in **shadow DOM**: role/CSS
  locator *clicks* time out, and `evaluate(() => el.click())` is a no-op.
  Screenshot, then click **CUA coordinates**. Locator *typing* still works
  after `locator.evaluate((el) => el.focus())` — clicks are the broken path,
  not keys.
- **Attaching an image to a feed post is not automatable here**: the IAB has
  no file-chooser access, `navigator.clipboard.write` is permission-denied,
  `document.execCommand("copy")` returns false, and the composer ignores
  untrusted synthetic paste/drop events carrying files (it accepts only
  trusted OS input). Only the article editor mounts an injectable
  `input[type=file]` (see above). If a feed post must carry a custom image,
  either link a URL whose Open Graph card carries the image, or hand the one
  attach step to the human in an open composer.
- Page-level `fetch`/XMLHttpRequest to other origins are killed by LinkedIn's
  CSP and its patched fetch wrapper — move data in through `evaluate`
  arguments, or load images via the CORS `img` → `canvas` route (GitHub Pages
  serves `Access-Control-Allow-Origin: *`).
- **Verification**: the feed lags and may not show your own new post at once —
  `linkedin.com/in/horacechan/recent-activity/all/` is authoritative. Permalink
  shapes: link posts `…/feed/update/urn:li:activity:<id>/`, article shares
  `…/feed/update/urn:li:share:<id>/`, articles `…/pulse/<slug>-horace-chan-<id>/`.
  Grab the permalink from the `a[href*="/feed/update/"]` inside the matching
  post container, not from a page-wide link dump.

## Procedure

1. Convert markdown → HTML (Input prep, including LaTeX → Unicode). Load
   `browser-use:control-browser`, or use the `playwright-cli` fallback.
2. Open `https://www.linkedin.com/article/new/` (first goto may report a
   navigation timeout — check URL/title before retrying; it loads anyway).
3. Upload the cover (mechanics above), confirm with the dialog's "Next".
4. Type the title; paste the body; verify head/tail/length.
5. Type the human's share text in the "Next" dialog; screenshot the composer
   to confirm text + article preview; **stop and get the user's explicit go-ahead,
   then** click "Publish" (it posts publicly on their account).
6. Verify: the tab lands on `linkedin.com/pulse/<slug>-horace-chan-<id>/`;
   dismiss the congrats dialog; confirm the share post exists under
   `linkedin.com/in/horacechan/recent-activity/all/` (feed rendering lags) and
   capture its permalink (`a[href*="/feed/update/"]` inside the matching post
   container). Report both URLs.
- OG share pages (`articles/<slug>/index.html`) are NOT needed for this flow —
  the Pulse article carries its own cover. They remain useful only if the
  human explicitly wants to share the *site* link on social platforms (clean
  `/read/...` routes return HTTP 404 to crawlers and never unfurl). If you do
  create one: commit only that file, push, and verify the deploy with
  `gh api repos/hevangel/ai_management/pages/builds/latest --jq .status`
  until `built` — local `curl` to github.io is network-blocked on this
  machine (HTTP 000 is a proxy block, not a missing deploy).
