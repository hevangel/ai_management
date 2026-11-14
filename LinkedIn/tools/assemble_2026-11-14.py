#!/usr/bin/env python3
"""Assemble 2026-11-14 daily-run per-post JSONs (4 posts).

Mirrors LinkedIn/tools/assemble_round4.py conventions: relative hints are
converted to approximate ISO dates anchored at scraped_at and flagged
posted_at_approx; a leading "(edited)" in a hint is stripped for date
derivation only (stored hint stays verbatim); is_author_reply is recomputed
from the profile URL; image-only comments get "(image-only comment)".

Safety: refuses to overwrite an existing post file.
Run from the repo root.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assemble import approx_posted_at, parse_iso, OWNER_URL  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"
SRC = Path.home() / "workspace" / "linkedin-archive-daily"

SCRAPED_AT = "2026-11-14T15:54:55Z"  # feed pull ~15:50 UTC, comments ~15:53 UTC
AUTHOR = {
    "name": "Horace Chan",
    "profile_url": OWNER_URL,
    "headline": "Expert in applying AI in verification",
}

_LEADING_EDITED = re.compile(r"^\(edited\)\s*", re.IGNORECASE)


def clean_hint(hint):
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


def main():
    raw_posts = json.loads(
        (SRC / "2026-11-14_posts.json").read_text(encoding="utf-8"), strict=False)
    comments_by_id = {}
    cpath = SRC / "2026-11-14_comments.json"
    if cpath.exists():
        for entry in json.loads(cpath.read_text(encoding="utf-8")):
            comments_by_id[str(entry["activity_id"])] = entry["comments"]

    anchor = parse_iso(SCRAPED_AT)
    written, warnings = 0, []
    total_comments = total_replies = 0
    for p in raw_posts:
        aid = str(p["activity_id"])
        out_path = POSTS_DIR / f"post_{aid}.json"
        if out_path.exists():
            raise SystemExit(f"REFUSING to overwrite existing {out_path}")

        comments = [norm_comment(c, anchor)
                    for c in comments_by_id.get(aid, [])]
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

        shared = p.get("shared_article")
        if isinstance(shared, dict):
            shared = {"title": shared.get("title"), "url": shared.get("url")}
        else:
            shared = None

        post = {
            "activity_id": aid,
            "url": p.get("url"),
            "author": dict(AUTHOR),
            "posted_at": posted_at.isoformat() if posted_at else None,
            "posted_at_hint": p.get("posted_at_hint"),
            "posted_at_approx": True,
            "text": p.get("text") or "",
            "post_type": post_type,
            "shared_article": shared,
            "reshared_post": p.get("reshared_post"),
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
