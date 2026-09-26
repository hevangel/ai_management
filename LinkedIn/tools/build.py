#!/usr/bin/env python3
"""Build the LinkedIn archive: validate posts/*.json, write index.json,
and generate a self-contained index.html viewer (data inlined, no fetch,
no CDN, no build step — works from file:// and GitHub Pages).

Usage:  python3 LinkedIn/tools/build.py
Run from the repo root.
"""
import json
import html
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"
INDEX_JSON = ROOT / "index.json"
INDEX_HTML = ROOT / "index.html"

REQUIRED_POST_FIELDS = [
    "activity_id", "url", "author", "posted_at", "text",
    "post_type", "likes", "comment_count", "comments", "scraped_at",
]


def parse_dt(s):
    if not s:
        return datetime.min.replace(tzinfo=timezone.utc)
    try:
        d = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
    except ValueError:
        return datetime.min.replace(tzinfo=timezone.utc)


def validate(post, path):
    for f in REQUIRED_POST_FIELDS:
        if f not in post:
            raise ValueError(f"{path}: missing field {f!r}")
    if not isinstance(post["comments"], list):
        raise ValueError(f"{path}: comments must be a list")
    for c in post["comments"]:
        for f in ("author", "text", "replies"):
            if f not in c:
                raise ValueError(f"{path}: comment missing {f!r}")
        if not isinstance(c["replies"], list):
            raise ValueError(f"{path}: replies must be a list")


def title_of(text, limit=80):
    t = " ".join(text.split())
    return t if len(t) <= limit else t[:limit].rstrip() + "…"


def main():
    files = sorted(POSTS_DIR.glob("post_*.json"))
    if not files:
        raise SystemExit(f"No post JSON files found in {POSTS_DIR}")

    posts = []
    for f in files:
        post = json.loads(f.read_text(encoding="utf-8"))
        validate(post, f.name)
        posts.append(post)

    posts.sort(key=lambda p: parse_dt(p.get("posted_at")), reverse=True)

    # Map activity_id -> actual file name (files are post_<activity_id>.json).
    file_of = {}
    for f in files:
        for p in posts:
            if f.name == f"post_{p['activity_id']}.json":
                file_of[p["activity_id"]] = f.name
                break

    owner = posts[0].get("author", {}) if posts else {}
    total_comments = sum(len(p["comments"]) for p in posts)
    total_replies = sum(len(c.get("replies", [])) for p in posts for c in p["comments"])

    index = {
        "profile": {
            "name": owner.get("name"),
            "url": owner.get("profile_url"),
        },
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_posts": len(posts),
        "total_comments": total_comments,
        "total_replies": total_replies,
        "posts": [
            {
                "activity_id": p["activity_id"],
                "file": f"posts/{file_of.get(p['activity_id'], f'post_{p['activity_id']}.json')}",
                "url": p["url"],
                "posted_at": p.get("posted_at"),
                "title": title_of(p.get("text", "")),
                "likes": p.get("likes", 0),
                "comment_count": len(p.get("comments", [])),
            }
            for p in posts
        ],
    }
    INDEX_JSON.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")

    data_blob = json.dumps(
        {"profile": index["profile"], "posts": posts},
        ensure_ascii=False,
    ).replace("</", "<\\/")

    INDEX_HTML.write_text(render_html(data_blob, index), encoding="utf-8")
    print(f"Validated {len(posts)} posts "
          f"({total_comments} comments, {total_replies} replies).")
    print(f"Wrote {INDEX_JSON.relative_to(ROOT.parent)} and {INDEX_HTML.relative_to(ROOT.parent)}")


def render_html(data_blob, index):
    pname = html.escape(index["profile"].get("name") or "LinkedIn")
    purl = html.escape(index["profile"].get("url") or "#")
    gen = html.escape(index["generated_at"])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{pname} — LinkedIn Posts Archive</title>
<style>
  :root {{ --bg:#ffffff; --fg:#1a1a1a; --muted:#666; --card:#f6f7f9; --border:#e2e5ea;
           --accent:#0a66c2; --reply:#eef6ff; --own:#fff7e6; }}
  [data-theme="dark"] {{ --bg:#121212; --fg:#e8e8e8; --muted:#9a9a9a; --card:#1c1e21;
           --border:#2c2f34; --accent:#5aa9ff; --reply:#16202c; --own:#2a2416; }}
  * {{ box-sizing:border-box; }}
  body {{ font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
          background:var(--bg); color:var(--fg); margin:0; line-height:1.55; }}
  header {{ padding:28px 20px 18px; border-bottom:1px solid var(--border); max-width:860px; margin:0 auto; }}
  header h1 {{ margin:0 0 6px; font-size:1.6rem; }}
  header p {{ margin:4px 0; color:var(--muted); font-size:.92rem; }}
  header a {{ color:var(--accent); }}
  .toolbar {{ max-width:860px; margin:0 auto; padding:14px 20px; display:flex; gap:10px; flex-wrap:wrap;
              position:sticky; top:0; background:var(--bg); border-bottom:1px solid var(--border); z-index:5; }}
  .toolbar input[type=search] {{ flex:1; min-width:200px; padding:9px 12px; font-size:.95rem;
              border:1px solid var(--border); border-radius:8px; background:var(--bg); color:var(--fg); }}
  .toolbar select, .toolbar button {{ padding:9px 12px; font-size:.9rem; border:1px solid var(--border);
              border-radius:8px; background:var(--card); color:var(--fg); cursor:pointer; }}
  main {{ max-width:860px; margin:0 auto; padding:18px 20px 60px; }}
  .post {{ background:var(--card); border:1px solid var(--border); border-radius:12px;
           padding:18px 20px; margin:0 0 18px; }}
  .post .meta {{ color:var(--muted); font-size:.83rem; margin-bottom:8px; }}
  .post .meta a {{ color:var(--accent); text-decoration:none; }}
  .post .text {{ white-space:pre-wrap; word-wrap:break-word; margin:8px 0 10px; }}
  .post .text a {{ color:var(--accent); }}
  .post .stats {{ color:var(--muted); font-size:.85rem; display:flex; gap:14px; align-items:center; }}
  .post .stats button {{ background:none; border:1px solid var(--border); border-radius:7px;
           color:var(--fg); padding:5px 12px; font-size:.85rem; cursor:pointer; }}
  .post .stats button:hover {{ border-color:var(--accent); color:var(--accent); }}
  .badge {{ display:inline-block; font-size:.72rem; font-weight:600; padding:2px 8px; border-radius:20px;
            background:var(--accent); color:#fff; margin-left:8px; vertical-align:middle; }}
  .comments {{ margin-top:12px; border-top:1px solid var(--border); padding-top:10px; display:none; }}
  .comments.open {{ display:block; }}
  .comment {{ padding:10px 12px; border-radius:9px; margin:0 0 10px; background:var(--bg);
              border:1px solid var(--border); }}
  .comment.own {{ background:var(--own); }}
  .comment .who {{ font-size:.85rem; margin-bottom:4px; }}
  .comment .who a {{ color:var(--accent); font-weight:600; text-decoration:none; }}
  .comment .who .headline {{ color:var(--muted); font-weight:400; }}
  .comment .when {{ color:var(--muted); font-size:.78rem; margin-left:8px; }}
  .comment .ctext {{ white-space:pre-wrap; word-wrap:break-word; font-size:.93rem; margin:4px 0; }}
  .comment .ctext a {{ color:var(--accent); }}
  .comment .clikes {{ color:var(--muted); font-size:.78rem; }}
  .replies {{ margin:8px 0 0 14px; padding-left:12px; border-left:2px solid var(--border); }}
  .empty {{ color:var(--muted); text-align:center; padding:40px 0; }}
  footer {{ max-width:860px; margin:0 auto; padding:20px; color:var(--muted); font-size:.8rem;
            border-top:1px solid var(--border); }}
</style>
</head>
<body>
<header>
  <h1>{pname} <span style="font-weight:400;font-size:1rem;color:var(--muted)">LinkedIn posts archive</span></h1>
  <p><a href="{purl}">{purl}</a></p>
  <p>{index["total_posts"]} posts · {index["total_comments"]} comments · {index["total_replies"]} replies · generated {gen}</p>
</header>
<div class="toolbar">
  <input type="search" id="q" placeholder="Search posts and comments…" aria-label="Search">
  <select id="sort" aria-label="Sort order">
    <option value="new">Newest first</option>
    <option value="old">Oldest first</option>
    <option value="liked">Most liked</option>
    <option value="discussed">Most discussed</option>
  </select>
  <button id="theme" title="Toggle light/dark">🌙</button>
</div>
<main id="list"></main>
<footer>Static archive generated by <code>LinkedIn/tools/build.py</code> — no tracking, no network calls.</footer>
<script type="application/json" id="archive-data">{data_blob}</script>
<script>
(function() {{
  const DATA = JSON.parse(document.getElementById('archive-data').textContent);
  const posts = DATA.posts;
  const list = document.getElementById('list');
  const q = document.getElementById('q');
  const sortSel = document.getElementById('sort');

  const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({{
    '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]));
  const linkify = s => esc(s).replace(/(https?:\\/\\/[^\\s<]+)/g, '<a href="$1" target="_blank" rel="noopener">$1</a>');
  const fdate = s => {{ try {{ return new Date(s).toLocaleString(); }} catch(e) {{ return s || ''; }} }};

  function commentHTML(c) {{
    const own = c.is_author_reply ? ' own' : '';
    const badge = c.is_author_reply ? '<span class="badge">author</span>' : '';
    const who = c.author.profile_url
      ? `<a href="${{esc(c.author.profile_url)}}" target="_blank" rel="noopener">${{esc(c.author.name || 'Unknown')}}</a>`
      : esc(c.author.name || 'Unknown');
    const replies = (c.replies || []).map(r =>
      `<div class="replies">${{commentHTML(r)}}</div>`).join('');
    return `<div class="comment${{own}}"><div class="who">${{who}}${{badge}}
      ${{c.author.headline ? `<span class="headline"> · ${{esc(c.author.headline)}}</span>` : ''}}
      <span class="when">${{esc(fdate(c.posted_at))}}</span></div>
      <div class="ctext">${{linkify(c.text)}}</div>
      ${{c.likes ? `<div class="clikes">👍 ${{c.likes}}</div>` : ''}}${{replies}}</div>`;
  }}

  function render() {{
    const term = q.value.trim().toLowerCase();
    let items = posts.filter(p => {{
      if (!term) return true;
      const hay = (p.text + ' ' + p.comments.map(c =>
        c.text + ' ' + c.author.name + ' ' + (c.replies||[]).map(r => r.text + ' ' + r.author.name).join(' ')
      ).join(' ')).toLowerCase();
      return hay.includes(term);
    }});
    const by = sortSel.value;
    items = items.slice().sort((a,b) => {{
      if (by === 'old') return new Date(a.posted_at) - new Date(b.posted_at);
      if (by === 'liked') return (b.likes||0) - (a.likes||0);
      if (by === 'discussed') return (b.comments.length + (b.comments.reduce((n,c)=>n+(c.replies||[]).length,0)))
                                   - (a.comments.length + (a.comments.reduce((n,c)=>n+(c.replies||[]).length,0)));
      return new Date(b.posted_at) - new Date(a.posted_at);
    }});
    if (!items.length) {{ list.innerHTML = '<div class="empty">No posts match.</div>'; return; }}
    list.innerHTML = items.map((p, i) => {{
      const n = p.comments.length + p.comments.reduce((n,c)=>n+((c.replies||[]).length),0);
      const comments = p.comments.length
        ? p.comments.map(commentHTML).join('')
        : '<div class="empty">No comments.</div>';
      return `<article class="post" data-i="${{i}}">
        <div class="meta">${{esc(fdate(p.posted_at))}} · <a href="${{esc(p.url)}}" target="_blank" rel="noopener">View on LinkedIn</a>
        ${{p.post_type !== 'original' ? ` · ${{esc(p.post_type)}}` : ''}}</div>
        <div class="text">${{linkify(p.text)}}</div>
        ${{p.shared_article && p.shared_article.url ? `<div class="meta">🔗 <a href="${{esc(p.shared_article.url)}}" target="_blank" rel="noopener">${{esc(p.shared_article.title || p.shared_article.url)}}</a></div>` : ''}}
        <div class="stats"><span>👍 ${{p.likes||0}}</span><span>💬 ${{n}}</span><span>🔁 ${{p.reposts||0}}</span>
        ${{p.comments.length ? `<button data-toggle="${{i}}">Show comments (${{n}})</button>` : ''}}</div>
        <div class="comments" id="c-${{i}}">${{comments}}</div>
      </article>`;
    }}).join('');
    list.querySelectorAll('[data-toggle]').forEach(btn => btn.addEventListener('click', () => {{
      const box = document.getElementById('c-' + btn.getAttribute('data-toggle'));
      const open = box.classList.toggle('open');
      btn.textContent = (open ? 'Hide' : 'Show') + ' comments (' + btn.textContent.match(/\\d+/)[0] + ')';
    }}));
  }}

  q.addEventListener('input', render);
  sortSel.addEventListener('change', render);

  const themeBtn = document.getElementById('theme');
  const setTheme = t => {{ document.documentElement.setAttribute('data-theme', t);
    themeBtn.textContent = t === 'dark' ? '☀️' : '🌙'; try {{ localStorage.setItem('li-arch-theme', t); }} catch(e) {{}} }};
  let saved = 'light';
  try {{ saved = localStorage.getItem('li-arch-theme') || 'light'; }} catch(e) {{}}
  setTheme(saved);
  themeBtn.addEventListener('click', () =>
    setTheme(document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark'));

  render();
}})();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    main()
