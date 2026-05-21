"""Parse OCR lines into categorized menu items."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path


CONFIG_DIR = Path(__file__).resolve().parent.parent / "config"

HEADER_PATTERNS = [
    re.compile(r"점심\s*메뉴"),
    re.compile(r"정심\s*메뉴"),
    re.compile(r"오늘\s*메뉴"),
    re.compile(r"올데이"),
    re.compile(r"^\W+$"),
    re.compile(r"^\d{1,2}\s*월\s*\d{1,2}\s*일"),
    re.compile(r"(월|화|수|목|금|토|일)\s*요일"),
]


@dataclass(frozen=True)
class MenuItem:
    name: str
    category: str  # "rice" | "banchan" | "main"


def _load_keywords(filename: str) -> list[str]:
    path = CONFIG_DIR / filename
    if not path.exists():
        return []
    out: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.append(line)
    return out


def normalize(name: str) -> str:
    name = unicodedata.normalize("NFC", name)
    name = re.sub(r"\(\s*feat[^)]*\)", "", name, flags=re.IGNORECASE)
    name = re.sub(r"\(.*?\)", "", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name


def _is_header(line: str) -> bool:
    return any(p.search(line) for p in HEADER_PATTERNS)


def _split_line(line: str) -> list[str]:
    parts = re.split(r"[,/·•・∙]+", line)
    return [p.strip(" -·•※*") for p in parts if p.strip(" -·•※*")]


def _classify(name: str, rice_kw: list[str], banchan_kw: list[str]) -> str:
    if any(k in name for k in rice_kw):
        return "rice"
    if any(k in name for k in banchan_kw):
        return "banchan"
    return "main"


def parse_menu(ocr_lines: list[str]) -> list[MenuItem]:
    rice_kw = _load_keywords("rice_keywords.txt")
    banchan_kw = _load_keywords("banchan_keywords.txt")

    items: list[MenuItem] = []
    seen: set[str] = set()
    for raw in ocr_lines:
        if _is_header(raw):
            continue
        for piece in _split_line(raw):
            name = normalize(piece)
            if len(name) < 2:
                continue
            if name in seen:
                continue
            seen.add(name)
            items.append(MenuItem(name=name, category=_classify(name, rice_kw, banchan_kw)))
    return items


if __name__ == "__main__":
    import sys

    sample = [ln.strip() for ln in sys.stdin if ln.strip()]
    for it in parse_menu(sample):
        print(f"[{it.category:7}] {it.name}")
