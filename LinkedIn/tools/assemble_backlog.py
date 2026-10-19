#!/usr/bin/env python3
"""Assemble backlog per-post JSONs from the LinkedIn data export + page grinds.

The export (Shares_498116.csv) is the ground-truth list of Horace's posts:
it gives each post's share-URN id, exact UTC date, and full commentary —
but no engagement counts and none of the comments other people left. The
grind (browser visits to each post's share-URN URL, results saved as
~/workspace/linkedin-archive-backlog/grind_batch_*.json) supplies likes,
reposts, the displayed comment count, the full comment thread, and any
embedded reshared post or shared article.

Backlog posts are keyed by their SHARE id: the share-URN URL
(https://www.linkedin.com/feed/update/urn:li:share:<id>/) opens the post
directly, and the activity URN is not exposed to the read-only browser
extraction. The id is stored in both "activity_id" (the schema's key) and
"share_id". The 377 feed-archived posts keep their activity ids.

Dates: "posted_at" is the export's exact timestamp, so
"posted_at_approx" is false and "posted_at_hint" is null. Comment
timestamps are still hint-derived (anchored at the grind's scraped_at).

Export text cleaning (verified against 376 matched archived posts):
LinkedIn's CSV exporter turns each newline into '"\\n"' and doubles
genuine double-quotes; clean_export_text() reverses both.

Safety: refuses to overwrite an existing post file; skips share ids a
previous run already assembled.

Usage:  python3 LinkedIn/tools/assemble_backlog.py
Run from the repo root.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assemble_round4 import norm_comment, AUTHOR  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"
R4 = Path.home() / "workspace" / "linkedin-archive-round4"
GRIND_DIR = Path.home() / "workspace" / "linkedin-archive-backlog"


def clean_export_text(s):
    return (s or "").replace('"\n"', "\n").replace('""', '"')


def main():
    backlog = {e["share_id"]: e
               for e in json.loads((R4 / "backlog_raw.json").read_text(encoding="utf-8"))}

    written, skipped, warnings = 0, 0, []
    total_comments = total_replies = 0
    for gf in sorted(GRIND_DIR.glob("grind_batch_*.json")):
        batch = json.loads(gf.read_text(encoding="utf-8"))
        scraped_at = batch["scraped_at"]
        anchor = datetime.fromisoformat(scraped_at.replace("Z", "+00:00"))
        for g in batch["results"]:
            sid = str(g["share_id"])
            out_path = POSTS_DIR / f"post_{sid}.json"
            if out_path.exists():
                skipped += 1
                continue
            e = backlog.get(sid)
            if e is None:
                warnings.append(f"{sid}: grind result has no export record")
                continue
            posted_at = datetime.strptime(
                e["date"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)

            comments = [norm_comment(c, anchor) for c in g.get("comments") or []]
            n_top = len(comments)
            n_rep = sum(len(c["replies"]) for c in comments)
            total_comments += n_top
            total_replies += n_rep
            if g["comment_count"] != n_top + n_rep:
                warnings.append(
                    f"{sid}: displayed comment_count={g['comment_count']} but "
                    f"extracted {n_top}+{n_rep}={n_top + n_rep}")

            if g.get("reshared_post"):
                post_type = "reshare"
            elif g.get("shared_article"):
                post_type = "article_share"
            else:
                post_type = "original"

            post = {
                "activity_id": sid,
                "share_id": sid,
                "url": g.get("final_url") or e["share_link"],
                "author": dict(AUTHOR),
                "posted_at": posted_at.isoformat(),
                "posted_at_hint": None,
                "posted_at_approx": False,
                "text": clean_export_text(e["commentary"]),
                "post_type": post_type,
                "shared_article": g.get("shared_article"),
                "reshared_post": g.get("reshared_post"),
                "likes": g.get("likes") or 0,
                "reposts": g.get("reposts") or 0,
                "comment_count": g["comment_count"],
                "comments": comments,
                "scraped_at": scraped_at,
            }
            out_path.write_text(
                json.dumps(post, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8")
            written += 1

    print(f"Wrote {written} backlog posts ({total_comments} top-level "
          f"comments, {total_replies} replies); {skipped} already assembled.")
    for w in warnings:
        print("WARN:", w)


if __name__ == "__main__":
    main()
