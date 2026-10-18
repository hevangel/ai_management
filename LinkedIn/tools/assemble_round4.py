#!/usr/bin/env python3
"""Assemble round-4 per-post JSONs (posts from 2026-09-27 to 2026-10-18).

Inputs (all under ~/workspace/linkedin-archive-round4/):
  r4_posts_raw.json          — 60 posts from the activity-feed extraction
                               (saved verbatim: literal newlines inside
                               strings, counts as strings, shared_article
                               sometimes a dict-literal string)
  r4_comments_<activity_id>.json — extracted comment threads (27 posts)
  r4_reshared.json           — original-post details for the 4 reshares

Normalization mirrors tools/assemble.py (same canonical schema): relative
hints are converted to approximate ISO dates anchored at scraped_at and
flagged posted_at_approx; comment is_author_reply is recomputed from the
profile URL. One addition over assemble.py: a leading "(edited)" in a
hint is stripped for date derivation (assemble.py only strips a trailing
one); the stored hint stays verbatim.

Safety: refuses to overwrite an existing post file.

Usage:  python3 LinkedIn/tools/assemble_round4.py
Run from the repo root.
"""
import ast
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assemble import approx_posted_at, parse_iso, OWNER_URL  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"
SRC = Path.home() / "workspace" / "linkedin-archive-round4"

SCRAPED_AT = "2026-10-18T08:05:00Z"  # 01:05 PDT, feed pull time
AUTHOR = {
    "name": "Horace Chan",
    "profile_url": OWNER_URL,
    "headline": "Expert in applying AI in verification",
}

_LEADING_EDITED = re.compile(r"^\(edited\)\s*", re.IGNORECASE)


def clean_hint(hint):
    """Strip a leading '(edited)' so approx_posted_at can parse the hint."""
    if not hint:
        return hint
    return _LEADING_EDITED.sub("", hint).strip()


def norm_comment(c, anchor):
    author = c.get("author") or {}
    author = {
        "name": author.get("name"),
        "profile_url": author.get("profile_url"),
        "headline": author.get("headline"),
    }
    posted_at, approx = approx_posted_at(clean_hint(c.get("posted_at_hint")), anchor)
    replies = [norm_comment(r, anchor) for r in c.get("replies") or []]
    for r in replies:
        r["replies"] = []
    text = c.get("text")
    if not text:
        # Verified image-only comments (no text at all) get the same
        # descriptive placeholder round 1 used, so the archive does not
        # render them as blank.
        text = "(image-only comment)"
    return {
        "comment_id": c.get("comment_id"),
        "author": author,
        "is_author_reply": author.get("profile_url") == OWNER_URL,
        "posted_at": posted_at.isoformat() if posted_at else None,
        "posted_at_hint": c.get("posted_at_hint"),
        "posted_at_approx": True,
        "text": text,
        "likes": c.get("likes") or 0,
        "replies": replies,
    }


def norm_shared_article(raw):
    if raw is None or raw == "None":
        return None
    if isinstance(raw, str):
        raw = ast.literal_eval(raw)
    if isinstance(raw, dict):
        return {"title": raw.get("title"), "url": raw.get("url")}
    raise ValueError(f"Unexpected shared_article shape: {raw!r}")


def main():
    raw_posts = json.loads(
        (SRC / "r4_posts_raw.json").read_text(encoding="utf-8"), strict=False)
    reshared = {}
    rp = SRC / "r4_reshared.json"
    if rp.exists():
        reshared = {r["activity_id"]: r["reshared_post"]
                    for r in json.loads(rp.read_text(encoding="utf-8"))}

    anchor = parse_iso(SCRAPED_AT)
    written, warnings = 0, []
    total_comments = total_replies = 0
    for p in raw_posts:
        aid = str(p["activity_id"])
        out_path = POSTS_DIR / f"post_{aid}.json"
        if out_path.exists():
            raise SystemExit(f"REFUSING to overwrite existing {out_path}")

        comments = []
        cf = SRC / f"r4_comments_{aid}.json"
        if cf.exists():
            cdata = json.loads(cf.read_text(encoding="utf-8"))
            comments = [norm_comment(c, anchor) for c in cdata["comments"]]
        n_top = len(comments)
        n_rep = sum(len(c["replies"]) for c in comments)
        total_comments += n_top
        total_replies += n_rep

        comment_count = int(p.get("comment_count") or 0)
        if comment_count != n_top + n_rep:
            warnings.append(
                f"{aid}: comment_count={comment_count} but extracted "
                f"{n_top}+{n_rep}={n_top + n_rep}")

        post_type = p.get("post_type") or "original"
        if post_type == "article":
            post_type = "article_share"

        posted_at, _ = approx_posted_at(clean_hint(p.get("posted_at_hint")), anchor)
        if posted_at is None:
            warnings.append(f"{aid}: could not derive posted_at from "
                            f"hint {p.get('posted_at_hint')!r}")

        post = {
            "activity_id": aid,
            "url": p.get("url"),
            "author": dict(AUTHOR),
            "posted_at": posted_at.isoformat() if posted_at else None,
            "posted_at_hint": p.get("posted_at_hint"),
            "posted_at_approx": True,
            "text": p.get("text") or "",
            "post_type": post_type,
            "shared_article": norm_shared_article(p.get("shared_article")),
            "reshared_post": reshared.get(aid),
            "likes": int(p.get("likes") or 0),
            "reposts": int(p.get("reposts") or 0),
            "comment_count": comment_count,
            "comments": comments,
            "scraped_at": SCRAPED_AT,
        }
        if post_type == "reshare" and post["reshared_post"] is None:
            warnings.append(f"{aid}: reshare with no reshared_post data")
        out_path.write_text(
            json.dumps(post, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8")
        written += 1

    print(f"Wrote {written} posts ({total_comments} top-level comments, "
          f"{total_replies} replies).")
    for w in warnings:
        print("WARN:", w)


if __name__ == "__main__":
    main()
