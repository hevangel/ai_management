#!/usr/bin/env python3
"""Assemble daily per-post JSONs for the 2026-11-22 run (4 new posts).

Input: ~/workspace/linkedin-archive-daily/2026-11-22_posts.json
       (browser extraction; keys likes_count/reposts_count/full_text)
       ~/workspace/linkedin-archive-daily/2026-11-22_comments.json
       (2 posts with comment_count 1 each; both extracted totals match)
Normalization mirrors LinkedIn/tools/assemble_round4.py: relative hints
converted to approximate ISO dates anchored at scraped_at, flagged
posted_at_approx; author fixed to the archive owner; refuses to
overwrite an existing post file; comment counts validated.

Usage: python3 LinkedIn/tools/assemble_2026-11-22.py  (run from repo root)
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assemble import approx_posted_at, parse_iso, OWNER_URL  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"
WORK = Path.home() / "workspace" / "linkedin-archive-daily"
SRC = WORK / "2026-11-22_posts.json"
COMMENTS_SRC = WORK / "2026-11-22_comments.json"

SCRAPED_AT = "2026-11-22T14:58:00Z"  # feed pull 14:45-14:55 UTC, comments 14:56-14:58 UTC
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
    posted_at, _ = approx_posted_at(clean_hint(c.get("posted_at_hint")), anchor)
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
    raw_posts = json.loads(SRC.read_text(encoding="utf-8"), strict=False)
    comments_by_id = {}
    if COMMENTS_SRC.exists():
        cdata = json.loads(COMMENTS_SRC.read_text(encoding="utf-8"))
        if isinstance(cdata, dict):
            cdata = [cdata]
        for entry in cdata:
            comments_by_id[str(entry["activity_id"])] = entry["comments"]
    anchor = parse_iso(SCRAPED_AT)
    written, n_comments, n_replies, warnings = 0, 0, 0, []
    for p in raw_posts:
        aid = str(p["activity_id"])
        out_path = POSTS_DIR / f"post_{aid}.json"
        if out_path.exists():
            raise SystemExit(f"REFUSING to overwrite existing {out_path}")

        comments = [norm_comment(c, anchor) for c in comments_by_id.get(aid, [])]
        n_top = len(comments)
        n_rep = sum(len(c["replies"]) for c in comments)
        n_comments += n_top
        n_replies += n_rep
        comment_count = int(p.get("comment_count") or 0)
        if comment_count != n_top + n_rep:
            warnings.append(f"{aid}: comment_count={comment_count} but extracted "
                            f"{n_top}+{n_rep}={n_top + n_rep}")

        posted_at, _ = approx_posted_at(clean_hint(p.get("posted_at_hint")), anchor)
        if posted_at is None:
            warnings.append(f"{aid}: could not derive posted_at from "
                            f"hint {p.get('posted_at_hint')!r}")

        post = {
            "activity_id": aid,
            "url": p.get("url") or p.get("canonical_post_url"),
            "author": dict(AUTHOR),
            "posted_at": posted_at.isoformat() if posted_at else None,
            "posted_at_hint": p.get("posted_at_hint"),
            "posted_at_approx": True,
            "text": p.get("text") or p.get("full_text") or "",
            "post_type": p.get("post_type") or "original",
            "shared_article": p.get("shared_article"),
            "reshared_post": p.get("reshared_post"),
            "likes": int(p.get("likes") or p.get("likes_count") or 0),
            "reposts": int(p.get("reposts") or p.get("reposts_count") or 0),
            "comment_count": comment_count,
            "comments": comments,
            "scraped_at": SCRAPED_AT,
        }
        out_path.write_text(
            json.dumps(post, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8")
        written += 1

    print(f"Wrote {written} posts ({n_comments} comments, {n_replies} replies).")
    for w in warnings:
        print("WARN:", w)


if __name__ == "__main__":
    main()
