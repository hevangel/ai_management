#!/usr/bin/env python3
"""Assemble per-post JSONs from the raw batch extractions.

Reads batch_01.json .. batch_10.json (from /tmp/linkedin/, falling back to
~/workspace/linkedin-archive-backup/), normalizes the slightly different
shapes each extraction batch arrived in, converts LinkedIn's relative
timestamps ("2w", "Jun 2", "Yesterday", "4mo", ...) into approximate ISO
dates anchored at each post's scraped_at, and writes
LinkedIn/posts/post_<activity_id>.json — one JSON per post, the canonical
schema consumed by tools/build.py.

LinkedIn never exposes an absolute timestamp in the post DOM (no
<time datetime>), so posted_at is always derived: the field
"posted_at_approx" is true whenever posted_at was computed from a hint.
The original relative text is kept in "posted_at_hint".

Usage:  python3 LinkedIn/tools/assemble.py
Run from the repo root.
"""
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

OWNER_URL = "https://www.linkedin.com/in/horacechan"

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"

TMP_DIRS = [
    Path("/tmp/linkedin"),
    Path.home() / "workspace" / "linkedin-archive-backup",
]

MONTHS = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12,
}

_HINT_CLEAN = re.compile(r"\s*(?:•\s*edited|\(edited\))\s*$", re.IGNORECASE)
_REL = re.compile(r"^(\d+)\s*(m|min|mins|h|hr|hrs|d|w|mo)\s*$", re.IGNORECASE)
_MONTH_DAY = re.compile(r"^([A-Za-z]+)\s+(\d{1,2})$")


def parse_iso(s):
    if not s:
        return None
    try:
        d = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def approx_posted_at(hint, anchor):
    """Convert a LinkedIn relative timestamp to an approximate datetime.

    Returns (datetime|None, was_approximated: bool). Only called when
    posted_at is null; an already-absolute posted_at is never touched.
    """
    if not hint or not anchor:
        return None, False
    h = _HINT_CLEAN.sub("", hint).strip()
    m = _REL.match(h)
    if m:
        n, unit = int(m.group(1)), m.group(2).lower()
        delta = {
            "m": timedelta(minutes=n), "min": timedelta(minutes=n),
            "mins": timedelta(minutes=n), "h": timedelta(hours=n),
            "hr": timedelta(hours=n), "hrs": timedelta(hours=n),
            "d": timedelta(days=n), "w": timedelta(weeks=n),
            "mo": timedelta(days=30 * n),
        }[unit]
        return anchor - delta, True
    if h.lower() == "yesterday":
        return anchor - timedelta(days=1), True
    m = _MONTH_DAY.match(h)
    if m:
        month = MONTHS.get(m.group(1).lower())
        day = int(m.group(2))
        if month:
            dt = anchor.replace(month=month, day=day,
                                hour=12, minute=0, second=0, microsecond=0)
            if dt > anchor:  # must be last year, not next
                dt = dt.replace(year=dt.year - 1)
            return dt, True
    return None, False


def norm_author(raw):
    """Normalize the three comment/post author shapes seen across batches:
    nested {"author": {...}}, flat {name, profile_url, headline},
    and batch-6 {author_name, author_headline, profile_url}."""
    if isinstance(raw, dict) and isinstance(raw.get("author"), dict):
        raw = raw["author"]
    if isinstance(raw, dict):
        return {
            "name": raw.get("name") or raw.get("author_name"),
            "profile_url": raw.get("profile_url"),
            "headline": raw.get("headline") or raw.get("author_headline"),
        }
    return {"name": None, "profile_url": None, "headline": None}


def norm_comment(c, anchor):
    author = norm_author(c)
    is_reply = author.get("profile_url") == OWNER_URL
    posted_at, approx = approx_posted_at(c.get("posted_at_hint"), anchor)
    replies = [norm_comment(r, anchor) for r in c.get("replies") or []]
    # Replies are second level; their own replies list stays empty.
    for r in replies:
        r["replies"] = []
    return {
        "comment_id": c.get("comment_id"),
        "author": author,
        "is_author_reply": is_reply,
        "posted_at": posted_at.isoformat() if posted_at else c.get("posted_at"),
        "posted_at_hint": c.get("posted_at_hint"),
        "posted_at_approx": approx or c.get("posted_at") is None,
        "text": c.get("text") or "",
        "likes": c.get("likes", c.get("like_count", 0)) or 0,
        "replies": replies,
    }


def norm_post(p):
    author = norm_author(p.get("author") or {
        "author_name": p.get("author_name"),
        "profile_url": OWNER_URL,
        "author_headline": p.get("author_headline"),
    })
    anchor = parse_iso(p.get("scraped_at"))
    posted_at, approx = approx_posted_at(p.get("posted_at_hint"), anchor)
    return {
        "activity_id": p["activity_id"],
        "url": p.get("url"),
        "author": author,
        "posted_at": posted_at.isoformat() if posted_at else p.get("posted_at"),
        "posted_at_hint": p.get("posted_at_hint"),
        "posted_at_approx": approx or p.get("posted_at") is None,
        "text": p.get("text") or "",
        "post_type": p.get("post_type") or "original",
        "shared_article": p.get("shared_article"),
        "reshared_post": p.get("reshared_post"),
        "likes": p.get("likes", p.get("like_count", 0)) or 0,
        "reposts": p.get("reposts", p.get("repost_count", 0)) or 0,
        "comment_count": p.get("comment_count", 0) or 0,
        "comments": [norm_comment(c, anchor) for c in p.get("comments") or []],
        "scraped_at": p.get("scraped_at"),
    }


def main():
    src = next((d for d in TMP_DIRS if (d / "batch_01.json").exists()), None)
    if src is None:
        raise SystemExit("No batch files found in /tmp/linkedin or the workspace backup")

    batch_files = sorted(src.glob("batch_*.json"))
    posts, seen = [], set()
    for f in batch_files:
        for p in json.loads(f.read_text(encoding="utf-8")):
            if "error" in p or not p.get("activity_id"):
                print(f"SKIP {f.name}: {p.get('activity_id')} ({p.get('error')})")
                continue
            if p["activity_id"] in seen:
                raise SystemExit(f"Duplicate activity_id {p['activity_id']} in {f.name}")
            seen.add(p["activity_id"])
            posts.append(norm_post(p))

    POSTS_DIR.mkdir(exist_ok=True)
    for p in posts:
        (POSTS_DIR / f"post_{p['activity_id']}.json").write_text(
            json.dumps(p, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    n_hint = sum(1 for p in posts if p.get("posted_at_approx"))
    print(f"Assembled {len(posts)} posts from {len(batch_files)} batch files "
          f"({n_hint} with approximate posted_at).")
    print(f"Wrote {POSTS_DIR.relative_to(ROOT.parent)}/post_<activity_id>.json")


if __name__ == "__main__":
    main()
