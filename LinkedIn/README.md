# LinkedIn Posts Archive

A complete archive of Horace Chan's LinkedIn posts — full text, timestamps,
like/comment counts, and the full comment threads (who commented, their profile
links, comment text, timestamps, nested replies, and Horace's own replies).

## Coverage

- **201 posts**, 2026-04-05 → 2026-09-26 (newest first in `index.json`)
- 80 top-level comments, 63 nested replies, all threads fully expanded
- LinkedIn renders only relative timestamps ("2w", "Jun 2"), never an
  absolute `<time datetime>` — so `posted_at` is approximated from the
  relative hint anchored at each post's `scraped_at`
  (`posted_at_approx: true`; the original hint is kept in `posted_at_hint`)
- Scope note: the activity feed holds 600+ posts; this archive covers the
  201 most recent verified post IDs. Older posts are not yet included.

## Layout

| Path | What it is |
|---|---|
| `index.json` | Index of every post JSON (newest first) with titles, dates, counts |
| `index.html` | Static viewer page — all posts + comment threads, searchable, sortable, light/dark. Data is inlined, so it works from `file://` and from GitHub Pages with zero network calls |
| `posts/post_<activity_id>.json` | One JSON per post (schema below) |
| `tools/extract_posts.js` | Browser page-eval helper: scrape the post list from the activity feed |
| `tools/extract_comments.js` | Browser page-eval helper: expand + serialize comment threads on a post page |
| `tools/build.py` | Validates `posts/*.json`, regenerates `index.json` and `index.html` |

This folder is working data, not site content — it is intentionally **not**
registered in the repo's `content.json` (per `AGENTS.md`).

## Refreshing the archive

The workflow is documented as the `linkedin-archive` skill at
`.agents/skills/linkedin-archive/SKILL.md`. In short:

1. **Recon** — open LinkedIn in the live browser, confirm signed in as
   `linkedin.com/in/horacechan`, estimate the post count from
   `…/recent-activity/all/`.
2. **Extract posts** — scroll the activity feed to the bottom, run
   `tools/extract_posts.js`, save each result as
   `posts/post_<activity_id>.json` (fill in `author`, `scraped_at`, and an
   empty `comments: []` array at this stage).
3. **Extract comments** — open each post URL, run
   `tools/extract_comments.js` with the owner's profile URL, merge the returned
   `comments` array into the post's JSON.
4. **Rebuild** — `python3 LinkedIn/tools/build.py` (run from the repo root).
5. **Commit & push** — `git add LinkedIn`, commit, push.

Read-only throughout: never like, comment, share, follow, or message while
scraping. Pause if LinkedIn throttles.

## Per-post JSON schema

```json
{
  "activity_id": "7505886375943000065",
  "url": "https://www.linkedin.com/posts/...-activity-7505886375943000065-xxxx",
  "author": {"name": "Horace Chan", "profile_url": "https://www.linkedin.com/in/horacechan", "headline": "..."},
  "posted_at": "2026-09-16T07:12:44Z",
  "text": "full post text",
  "post_type": "original",
  "shared_article": null,
  "likes": 0, "reposts": 0, "comment_count": 0,
  "comments": [
    {
      "comment_id": "...",
      "author": {"name": "...", "profile_url": "...", "headline": "..."},
      "is_author_reply": false,
      "posted_at": "...",
      "text": "...",
      "likes": 0,
      "replies": []
    }
  ],
  "scraped_at": "2026-09-26T..."
}
```

`is_author_reply` marks comments written by the archive owner ("my replies").
