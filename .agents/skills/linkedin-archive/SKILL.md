name: linkedin-archive
description: Archive a LinkedIn user's own posts — full text, dates, like/comment counts, and the complete comment threads (commenter names, profile URLs, comment text, timestamps, nested replies, and the author's own replies) — into JSON: one file per post plus an index.json, and generate a static HTML viewer page. Use when the user asks to "download all my LinkedIn posts", archive LinkedIn content with comments, or build a LinkedIn posts viewer page. LinkedIn has no usable posts API for this; the workflow scrapes via an authenticated live-browser task (read-only), assembles the JSON with LinkedIn/tools/build.py, and commits everything to the repo.
---

# LinkedIn Archive Skill

Origin: user request 2026-09-26 — "go to my LinkedIn, download ALL my posts
and commit to this folder. Use JSON format to store the post, the comments, who
comment and my replies. One json per post, then an index JSON to list all the
post JSON. Then write a static html page to display all my post and the comment
and replies. Also commit the skill, scripts, tools, instructions that you used."

LinkedIn offers no public API for reading a user's posts with comments (the
"Download your data" export includes your posts but NOT other people's comments
on them). So this skill scrapes through a signed-in live browser task.

## Repo layout produced by this skill

```
LinkedIn/
  README.md            # human instructions for refreshing the archive
  index.json           # index of every post JSON (newest first)
  index.html           # static viewer: all posts + comment threads (data inlined)
  posts/
    post_<activity_id>.json   # one file per post
  tools/
    extract_posts.js      # page-eval helper: post list from activity feed
    extract_comments.js   # page-eval helper: expand + serialize comment threads
    build.py              # validates posts/*.json -> writes index.json + index.html
```

## Pipeline

### 0. Recon (one browser task, read-only)

- Open https://www.linkedin.com/ ; confirm signed in as the right person
  (profile https://www.linkedin.com/in/<handle>). If signed out, hand off with
  `ask_for_information` and let the user sign in — never enter credentials.
- Visit `https://www.linkedin.com/in/<handle>/recent-activity/all/`, scroll the
  feed 8–10 times, count distinct posts, estimate the total.
- Open one post page; confirm comments load and replies expand.
- Report: sign-in state, estimated post count, comments expandable yes/no, any
  CAPTCHA/rate-limit blocks. Do NOT extract data yet.

### 1. Extract the post list (one browser task)

Brief the task to, on the recent-activity page:

1. Scroll to the bottom slowly (pause ~2s per scroll) until no new posts load.
2. Run `LinkedIn/tools/extract_posts.js` (adapt selectors to the live DOM if
   needed) to collect for each post: activity_id, canonical post URL, full text,
   posted timestamp, like count, comment count, repost count, post type
   (original / article share / repost / etc.) and shared-article metadata.
3. Return the array as JSON in the handoff. If it is too large for one handoff,
   return it in 2–3 chunks via `ask_for_information` (task stays resumable).

Save the result to a working file, e.g. `/tmp/linkedin_post_list.json`
(workspace scratch — NOT committed).

### 2. Extract comment threads (browser task(s), batched)

For each post URL, in batches of ~10 posts per task:

1. Open the post URL. If a login wall or "unusual activity" challenge appears,
   stop and report — do not fight it; resume later.
2. Scroll to the comments section; run `LinkedIn/tools/extract_comments.js`:
   click every "Load more comments" / "View N replies" button until exhausted
   (bounded loop, ~1.5s pause between clicks), then serialize the thread:
   commenter display name, profile URL, headline, comment text, posted
   timestamp, like count, `is_author_reply` (commenter == profile owner), and
   nested `replies` (one level, same shape).
3. Return one JSON object per post (matching the per-post schema below).

Between batches, pause a few minutes if LinkedIn shows any throttling. Never
like, comment, share, follow, or message — strictly read-only.

### 3. Assemble (`LinkedIn/tools/build.py`)

For each post, write `LinkedIn/posts/post_<activity_id>.json`, then run:

```bash
python3 LinkedIn/tools/build.py
```

It validates every per-post JSON against the schema, writes `LinkedIn/index.json`
(newest first), and regenerates `LinkedIn/index.html` with all data inlined, so
the page works from `file://` and from GitHub Pages with no fetch and no build
step.

### 4. Commit & push

```bash
git add LinkedIn .agents/skills/linkedin-archive
git commit -m "LinkedIn archive: <N> posts with comment threads + viewer"
git push
```

Commit the skill, the tools, and the README alongside the data — the archive
must be reproducible from the repo alone.

## Per-post JSON schema (`posts/post_<activity_id>.json`)

```json
{
  "activity_id": "7505886375943000065",
  "url": "https://www.linkedin.com/posts/...-activity-7505886375943000065-xxxx",
  "author": {"name": "Horace Chan", "profile_url": "https://www.linkedin.com/in/horacechan", "headline": "..."},
  "posted_at": "2026-09-16T07:12:44Z",
  "text": "full post text",
  "post_type": "original | article_share | repost | ...",
  "shared_article": {"title": "...", "url": "..."} | null,
  "likes": 0, "reposts": 0, "comment_count": 0,
  "comments": [
    {
      "comment_id": "...",
      "author": {"name": "...", "profile_url": "...", "headline": "..."},
      "is_author_reply": false,
      "posted_at": "...",
      "text": "...",
      "likes": 0,
      "replies": [ { "...same shape, replies: []..." } ]
    }
  ],
  "scraped_at": "2026-09-26T..."
}
```

`is_author_reply` is true when the commenter's profile URL matches the archive
owner — that is how "my replies" are identified.

## index.json schema

```json
{
  "profile": {"name": "Horace Chan", "url": "https://www.linkedin.com/in/horacechan"},
  "generated_at": "2026-09-26T...",
  "total_posts": 9,
  "posts": [
    {"activity_id": "...", "file": "posts/post_<id>.json", "url": "...",
     "posted_at": "...", "title": "first ~80 chars of text",
     "likes": 0, "comment_count": 0}
  ]
}
```

## Safety & etiquette

- Read-only: no likes, comments, shares, follows, or messages, ever.
- Human pacing: ~1.5–2s pauses between scrolls/clicks; back off for minutes if
  LinkedIn throttles or challenges.
- CAPTCHA: the task pauses and asks the user; never auto-solve against policy.
- Only the signed-in user's own posts are archived. Do not scrape other
  people's profiles or feeds.
- Commenter names/headlines are public profile data shown on the post page;
  they are archived as displayed.
