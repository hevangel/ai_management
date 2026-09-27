#!/usr/bin/env python3
"""Repair null posted_at values using LinkedIn's relative timestamp hints.

Some posts/comments came through extraction batches without a scraped_at
anchor, so assemble.py left posted_at null -- and the viewer's fdate()
rendered those as 12/31/1969 (Unix epoch). This script re-runs the same
approx_posted_at() conversion from assemble.py with a sensible anchor:

- posts: the post's own scraped_at, else 2026-09-27 (round-2/3 scrape window;
  neighbor activity-ID ordering verified all 12 null-dated posts are 2026).
- comments/replies: the parent post's scraped_at, else the post's posted_at.

Hints that can't be parsed (None, "not shown on page") stay null; the viewer
now falls back to the hint text / "date unknown" instead of 1969.

Usage: python3 LinkedIn/tools/repair_dates.py (run from the repo root).
Only rewrites files that actually change.
"""
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assemble import approx_posted_at, parse_iso

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"

FALLBACK_ANCHOR = datetime(2026, 9, 27, tzinfo=timezone.utc)
_LEAD_EDITED = re.compile(r"^\(edited\)\s*", re.IGNORECASE)


def clean_hint(hint):
    if not hint:
        return hint
    return _LEAD_EDITED.sub("", hint).strip()


def convert(hint, anchor):
    dt, approx = approx_posted_at(clean_hint(hint), anchor)
    if dt is None:
        return None, False
    return dt.isoformat(), approx


def main():
    n_posts = n_comments = 0
    changed_files = []
    for f in sorted(POSTS_DIR.glob("post_*.json")):
        d = json.loads(f.read_text())
        changed = False

        post_anchor = parse_iso(d.get("scraped_at")) or FALLBACK_ANCHOR
        if not d.get("posted_at") and d.get("posted_at_hint"):
            iso, approx = convert(d["posted_at_hint"], post_anchor)
            if iso:
                d["posted_at"] = iso
                d["posted_at_approx"] = True
                n_posts += 1
                changed = True

        anchor = (parse_iso(d.get("scraped_at"))
                  or parse_iso(d.get("posted_at"))
                  or FALLBACK_ANCHOR)

        def fix_comments(comments):
            nonlocal n_comments, changed
            for c in comments or []:
                if not c.get("posted_at") and c.get("posted_at_hint"):
                    iso, approx = convert(c["posted_at_hint"], anchor)
                    if iso:
                        c["posted_at"] = iso
                        c["posted_at_approx"] = True
                        n_comments += 1
                        changed = True
                fix_comments(c.get("replies"))

        fix_comments(d.get("comments"))

        if changed:
            f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
            changed_files.append(f.name)

    print(f"repaired {n_posts} posts, {n_comments} comments/replies "
          f"across {len(changed_files)} files")


if __name__ == "__main__":
    main()
