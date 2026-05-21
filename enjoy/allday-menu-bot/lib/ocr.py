"""Download a menu image and OCR it with Tesseract (Korean)."""

from __future__ import annotations

import io

import pytesseract
import requests
from PIL import Image, ImageOps


def _download(url: str) -> Image.Image:
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return Image.open(io.BytesIO(resp.content))


def _preprocess(img: Image.Image) -> Image.Image:
    img = img.convert("L")
    img = ImageOps.autocontrast(img)
    w, h = img.size
    if w < 1200:
        scale = 1200 / w
        img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
    img = img.point(lambda px: 0 if px < 160 else 255, mode="1")
    return img


def ocr_menu_image(url: str) -> list[str]:
    """Return non-empty OCR lines extracted from the menu image."""
    img = _download(url)
    img = _preprocess(img)
    text = pytesseract.image_to_string(img, lang="kor", config="--psm 6")
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    return lines


if __name__ == "__main__":
    import sys

    for ln in ocr_menu_image(sys.argv[1]):
        print(ln)
