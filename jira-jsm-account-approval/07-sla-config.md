# SLA 정책 - `ACCT SLA`

JSM Project settings → SLAs.

> 영업일 = 월~금, 09:00~18:00 KST (한국 공휴일 제외) - Calendar 신규 생성: `KR Business Hours`.

## SLA 1. 1차 결재자 응답 시간 (Time to lead approval)

| 항목 | 값 |
|---|---|
| Goal | **2 영업일** |
| Start condition | Status = `Pending Lead Approval` |
| Pause condition | (없음) |
| Stop condition | Status changes to `Pending InfoSec Approval` OR `Rejected` |
| Calendar | KR Business Hours |
| Breach 알림 | 1.5 영업일 경과 시 직속 리더 + 정보보안실 escalation |

## SLA 2. 정보보안실 응답 시간 (Time to InfoSec approval)

| 항목 | 값 |
|---|---|
| Goal | **1 영업일** |
| Start condition | Status = `Pending InfoSec Approval` |
| Stop condition | Status changes to `In Progress` OR `Rejected` |
| Calendar | KR Business Hours |
| Breach 알림 | 0.75 영업일 경과 시 정보보안실 채널 + 보안실장 escalation |

## SLA 3. 작업 완료 시간 (Time to resolution)

| 항목 | 값 |
|---|---|
| Goal | **3 영업일** |
| Start condition | Status = `In Progress` |
| Stop condition | Status = `Done` |
| Calendar | KR Business Hours |
| Breach 알림 | 2.5 영업일 경과 시 IT 운영 + 요청자 escalation |

## SLA 4. 전체 처리 시간 (Time to overall close)

| 항목 | 값 |
|---|---|
| Goal | **5 영업일** |
| Start condition | Issue created |
| Stop condition | Status = `Done` OR `Rejected` |
| Calendar | KR Business Hours |
| 용도 | ISMS 운영 KPI 리포트 |

---

## SLA 대시보드 (별도 구성)

- 분기별 SLA 달성률, breach 건수, breach top reason
- 결재자별 평균 응답 시간 (개인정보 노출 주의 - 보안실 내부용)
