"""Fetch latest post metadata from a Kakao Channel feed using Playwright."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date, datetime

from playwright.sync_api import sync_playwright


CHANNEL_URL = "https://pf.kakao.com/_VAaRX/posts"


@dataclass
class LatestPost:
    post_date: date
    image_url: str
    post_id: str | None


def _parse_korean_date(text: str, today: date) -> date:
    """Parse strings like '5월 21일', '2026.5.21', 'YYYY-MM-DD', or '오늘' / 'N분 전'."""
    text = text.strip()
    if not text:
        return today
    if "오늘" in text or "분 전" in text or "시간 전" in text or "방금" in text:
        return today
    m = re.search(r"(20\d{2})[.\-/](\d{1,2})[.\-/](\d{1,2})", text)
    if m:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    m = re.search(r"(\d{1,2})\s*월\s*(\d{1,2})\s*일", text)
    if m:
        month, day = int(m.group(1)), int(m.group(2))
        year = today.year
        candidate = date(year, month, day)
        if candidate > today:
            candidate = date(year - 1, month, day)
        return candidate
    return today


def fetch_latest_post(today: date | None = None) -> LatestPost:
    today = today or date.today()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 2000},
        )
        page = ctx.new_page()
        page.goto(CHANNEL_URL, wait_until="domcontentloaded", timeout=30000)
        try:
            page.wait_for_selector("img[src*='kakaocdn.net/dn/']", timeout=15000)
        except Exception:
            pass
        page.wait_for_timeout(2500)

        data = page.evaluate(
            """
            () => {
              const imgs = Array.from(document.querySelectorAll('img'))
                .map(i => ({src: i.currentSrc || i.src || '', w: i.naturalWidth, h: i.naturalHeight}))
                .filter(i => i.src.includes('kakaocdn.net/dn/'));
              const text = document.body ? document.body.innerText : '';
              return { imgs, text };
            }
            """
        )
        browser.close()

    imgs = data.get("imgs") or []
    body_text = data.get("text") or ""

    candidates = [i for i in imgs if "profile" not in i["src"].lower()]
    if not candidates:
        candidates = imgs
    if not candidates:
        raise RuntimeError("no menu image found on channel page")

    candidates.sort(key=lambda i: (i["w"] or 0) * (i["h"] or 0), reverse=True)
    image_url = candidates[0]["src"]

    date_match = re.search(r"\d{1,2}\s*월\s*\d{1,2}\s*일", body_text)
    post_date = _parse_korean_date(date_match.group(0) if date_match else "", today)

    post_id = None
    m = re.search(r"/_VAaRX/(\d+)", body_text)
    if m:
        post_id = m.group(1)

    return LatestPost(post_date=post_date, image_url=image_url, post_id=post_id)


if __name__ == "__main__":
    print(fetch_latest_post())
