"""Entry point: scrape Kakao Channel, OCR menu, update history, post to Slack."""

from __future__ import annotations

import os
import sys
from datetime import date, timezone, timedelta

from lib.scraper import fetch_latest_post
from lib.ocr import ocr_menu_image
from lib.parser import parse_menu
from lib import history, slack


def _kst_today() -> date:
    return (
        (__import__("datetime").datetime.now(tz=timezone.utc) + timedelta(hours=9))
        .date()
    )


def main() -> int:
    today = _kst_today()
    print(f"[info] KST today = {today}", flush=True)

    post = fetch_latest_post(today=today)
    print(f"[info] latest post: date={post.post_date} image={post.image_url}", flush=True)

    ocr_lines = ocr_menu_image(post.image_url)
    print("[info] OCR lines:", flush=True)
    for ln in ocr_lines:
        print(f"  | {ln}", flush=True)

    items = parse_menu(ocr_lines)
    print("[info] parsed items:", flush=True)
    for it in items:
        print(f"  - [{it.category:7}] {it.name}", flush=True)

    if not items:
        print("[warn] no items parsed; aborting before history write", flush=True)
        return 2

    if post.post_date == today:
        history.upsert_today(post.post_date, items)
        print(f"[info] history updated for {post.post_date}", flush=True)
    else:
        print(
            f"[info] latest post date ({post.post_date}) != today ({today}); "
            "not writing history",
            flush=True,
        )

    main_names = [it.name for it in items if it.category == "main"]
    inline = history.lookup_inline(today=post.post_date, today_main_names=main_names)
    monthly = history.summarize_month(today=post.post_date)

    text = slack.build_message(
        today=today,
        post_date=post.post_date,
        items=items,
        inline_lookup=inline,
        month_summary=monthly,
    )
    print("[info] slack message:\n" + text, flush=True)

    if os.environ.get("DRY_RUN"):
        print("[info] DRY_RUN set; skipping Slack post", flush=True)
        return 0

    slack.send(text)
    print("[info] slack posted", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
