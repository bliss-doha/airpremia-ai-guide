# allday-menu-bot

올데이프리미엄한식뷔페 마곡본점 ([pf.kakao.com/_VAaRX](https://pf.kakao.com/_VAaRX)) 카카오톡채널의 일일 점심 메뉴를 OCR로 읽어 슬랙에 전송하고, 최근 30일 내 중복 메뉴를 함께 표시합니다.

## 작동 방식

1. Playwright headless로 채널 페이지를 렌더링하여 최상단 소식 이미지 URL 추출
2. Tesseract (한국어) OCR로 메뉴 텍스트 추출
3. `config/rice_keywords.txt`, `config/banchan_keywords.txt`로 항목을 `rice` / `banchan` / `main` 분류
4. `data/history.json`에 누적 저장. 중복 카운팅은 `main`만
5. 슬랙 Incoming Webhook으로 메시지 전송

슬랙 메시지 예:

```
🍱 *5월 21일 (목) 올데이 점심 메뉴*
• 백미 / 흑미
• 가스오부시 유부장국
• 100% 수제 치즈함박스테이크
• 크림 파스타 (feat.펜네리니)  (3일 전, 12일 전)
• 매콤 순살 닭강정
• 양배추샐러드

[올데이 중복 메뉴]
• [3회] 제육볶음 (5월 10일, 5월 14일, 5월 15일)
• [2회] 크림 파스타 (5월 5일, 5월 21일)

원문: https://pf.kakao.com/_VAaRX
```

## 로컬 실행

```bash
cd enjoy/allday-menu-bot
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
brew install tesseract tesseract-lang   # macOS

export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/..."
DRY_RUN=1 python fetch_menu.py          # 콘솔만 출력, 슬랙 전송 안 함
python fetch_menu.py                    # 실제 전송
```

## GitHub Actions 자동 실행

- 워크플로 파일: 리포 루트의 [.github/workflows/daily-menu.yml](../../.github/workflows/daily-menu.yml)
- 매일 KST 10:30 (UTC 01:30) 실행. 수동 실행은 Actions 탭의 "Run workflow"
- 필요한 사전 설정:
  1. 리포 Settings → Secrets and variables → Actions → New repository secret
     - `SLACK_WEBHOOK_URL`: Slack Incoming Webhook URL
  2. Settings → Actions → General → Workflow permissions
     - "Read and write permissions" 활성화 (history.json 자동 커밋용)

## 카테고리 키워드 튜닝

OCR 결과를 보고 분류가 어긋나면 다음 파일을 편집하세요. 부분 일치(substring)로 매칭됩니다.

- `config/rice_keywords.txt` — 밥류 (중복 카운팅에서 제외)
- `config/banchan_keywords.txt` — 반찬류 (중복 카운팅에서 제외)
- 매칭되지 않은 항목은 모두 `main`으로 분류되어 중복 추적 대상

## OCR이 부정확할 때

Tesseract 한글이 메뉴 폰트와 잘 안 맞으면 `lib/ocr.py`에서:
- `--psm` 값 변경 (4, 6, 11 등 시도)
- 전처리 이진화 임계값(`160`) 조정
- 또는 `pytesseract` 대신 Claude Vision API 호출로 교체

## 파일 구조

```
allday-menu-bot/
├── fetch_menu.py            # 진입점
├── lib/
│   ├── scraper.py           # Playwright로 최신 포스트 메타 수집
│   ├── ocr.py               # 이미지 다운로드 + Tesseract OCR
│   ├── parser.py            # 라인 파싱 + 카테고리 분류
│   ├── history.py           # 30일 윈도우 누적/조회
│   └── slack.py             # 메시지 포맷 + Webhook 전송
├── config/
│   ├── rice_keywords.txt
│   └── banchan_keywords.txt
├── data/
│   └── history.json         # GitHub Actions가 자동 커밋
└── requirements.txt
```
