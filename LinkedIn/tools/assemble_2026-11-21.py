#!/usr/bin/env python3
"""Assemble daily per-post JSONs for the 2026-11-21 run (3 new posts).

Input: ~/workspace/linkedin-archive-daily/2026-11-21_posts.json
       (browser extraction, verbatim; all 3 posts have comment_count 0)
Normalization mirrors LinkedIn/tools/assemble_round4.py: relative hints
converted to approximate ISO dates anchored at scraped_at, flagged
posted_at_approx; author fixed to the archive owner; refuses to
overwrite an existing post file.

Usage: python3 LinkedIn/tools/assemble_2026-11-21.py  (run from repo root)
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assemble import approx_posted_at, parse_iso, OWNER_URL  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"
SRC = Path.home() / "workspace" / "linkedin-archive-daily" / "2026-11-21_posts.json"

SCRAPED_AT = "2026-11-21T14:52:00Z"  # feed pull 14:44-14:51 UTC
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


def main():
    raw_posts = json.loads(SRC.read_text(encoding="utf-8"), strict=False)
    anchor = parse_iso(SCRAPED_AT)
    written, warnings = 0, []
    for p in raw_posts:
        aid = str(p["activity_id"])
        out_path = POSTS_DIR / f"post_{aid}.json"
        if out_path.exists():
            raise SystemExit(f"REFUSING to overwrite existing {out_path}")

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
            "text": p.get("text") or "",
            "post_type": p.get("post_type") or "original",
            "shared_article": p.get("shared_article"),
            "reshared_post": p.get("reshared_post"),
            "likes": int(p.get("likes") or 0),
            "reposts": int(p.get("reposts") or 0),
            "comment_count": int(p.get("comment_count") or 0),
            "comments": [],
            "scraped_at": SCRAPED_AT,
        }
        out_path.write_text(
            json.dumps(post, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8")
        written += 1

    print(f"Wrote {written} posts (0 comments, 0 replies).")
    for w in warnings:
        print("WARN:", w)


if __name__ == "__main__":
    main()
