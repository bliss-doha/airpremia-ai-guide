"""Persist daily menus and compute duplication views over a 30-day window."""

from __future__ import annotations

import json
from collections import Counter
from dataclasses import asdict
from datetime import date, timedelta
from pathlib import Path

from .parser import MenuItem, normalize


WINDOW_DAYS = 30
HISTORY_PATH = Path(__file__).resolve().parent.parent / "data" / "history.json"


def _load() -> dict[str, list[dict]]:
    if not HISTORY_PATH.exists():
        return {}
    return json.loads(HISTORY_PATH.read_text(encoding="utf-8") or "{}")


def _save(data: dict[str, list[dict]]) -> None:
    HISTORY_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def upsert_today(today: date, items: list[MenuItem]) -> None:
    data = _load()
    data[today.isoformat()] = [asdict(it) for it in items]
    _save(data)


def _window_entries(today: date) -> list[tuple[date, str]]:
    """Return (date, normalized_name) for every main-category entry in the last 30 days."""
    data = _load()
    cutoff = today - timedelta(days=WINDOW_DAYS - 1)
    out: list[tuple[date, str]] = []
    for day_str, entries in data.items():
        try:
            d = date.fromisoformat(day_str)
        except ValueError:
            continue
        if d < cutoff or d > today:
            continue
        for entry in entries:
            if entry.get("category") != "main":
                continue
            out.append((d, normalize(entry["name"])))
    return out


def lookup_inline(today: date, today_main_names: list[str]) -> dict[str, list[int]]:
    """For each main menu today, return days-ago counts for past occurrences (excluding today)."""
    entries = _window_entries(today)
    by_name: dict[str, list[date]] = {}
    for d, name in entries:
        if d == today:
            continue
        by_name.setdefault(name, []).append(d)

    result: dict[str, list[int]] = {}
    for raw_name in today_main_names:
        n = normalize(raw_name)
        dates = sorted(by_name.get(n, []), reverse=True)
        if dates:
            result[raw_name] = [(today - d).days for d in dates]
    return result


def summarize_month(today: date) -> list[tuple[str, int, list[date]]]:
    """Return main menus appearing >=2 times in the 30-day window, sorted by count desc, name asc."""
    entries = _window_entries(today)
    by_name: dict[str, list[date]] = {}
    for d, name in entries:
        by_name.setdefault(name, []).append(d)

    summary = []
    for name, dates in by_name.items():
        if len(dates) >= 2:
            summary.append((name, len(dates), sorted(dates)))
    summary.sort(key=lambda x: (-x[1], x[0]))
    return summary
