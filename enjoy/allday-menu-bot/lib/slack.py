"""Format the daily menu Slack message and post it via Incoming Webhook."""

from __future__ import annotations

import os
from datetime import date

import requests

from .parser import MenuItem


CHANNEL_HOME = "https://pf.kakao.com/_VAaRX"
_WEEKDAY_KR = ["월", "화", "수", "목", "금", "토", "일"]


def _fmt_date_korean_short(d: date) -> str:
    return f"{d.month}월 {d.day}일"


def _fmt_header_date(d: date) -> str:
    return f"{d.month}월 {d.day}일 ({_WEEKDAY_KR[d.weekday()]})"


def build_message(
    today: date,
    post_date: date,
    items: list[MenuItem],
    inline_lookup: dict[str, list[int]],
    month_summary: list[tuple[str, int, list[date]]],
) -> str:
    lines: list[str] = []

    if post_date != today:
        lines.append(
            f":warning: 오늘 새 메뉴가 안 올라왔어요. 가장 최근 포스트: "
            f"{_fmt_date_korean_short(post_date)}"
        )
        lines.append("")

    lines.append(f":bento: *{_fmt_header_date(post_date)} 올데이 점심 메뉴*")
    for it in items:
        line = f"• {it.name}"
        if it.category == "main" and it.name in inline_lookup:
            ago = inline_lookup[it.name]
            parts = ", ".join(f"{d}일 전" for d in ago)
            line += f"  ({parts})"
        lines.append(line)

    if month_summary:
        lines.append("")
        lines.append("[올데이 중복 메뉴]")
        for name, count, dates in month_summary:
            date_str = ", ".join(_fmt_date_korean_short(d) for d in dates)
            lines.append(f"• [{count}회] {name} ({date_str})")

    lines.append("")
    lines.append(f"원문: {CHANNEL_HOME}")
    return "\n".join(lines)


def send(text: str, webhook_url: str | None = None) -> None:
    url = webhook_url or os.environ.get("SLACK_WEBHOOK_URL")
    if not url:
        raise RuntimeError("SLACK_WEBHOOK_URL is not set")
    resp = requests.post(url, json={"text": text}, timeout=15)
    resp.raise_for_status()
