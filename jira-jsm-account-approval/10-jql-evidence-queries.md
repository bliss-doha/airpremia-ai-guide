# ISMS 감사용 JQL & Filter

> 모두 Saved Filter 로 등록 + Dashboard 위젯으로 시각화. 권장 위치: `Filters → Group: ACCT-감사`.

---

## F1. 분기별 전체 신청 - Evidence Export 마스터

```jql
project = ACCT
AND created >= startOfQuarter()
AND created <= endOfQuarter()
ORDER BY created DESC
```

**Export columns**: Key, Created, Reporter, "부서", "직속 리더", "시스템", "카테고리", "신청 사유", "적용 희망일", "회수 예정일", Status, Resolution, Assignee, Resolved.

> 분기별 1회 CSV export → Confluence "ISMS 증빙 자료실" 페이지 첨부.

---

## F2. 자기결재 케이스 (감사 핵심 모니터링)

```jql
project = ACCT
AND comment ~ "자기결재 케이스"
AND created >= startOfYear()
ORDER BY created DESC
```

> 운영 정책: 분기당 5건 초과 시 정보보안실에서 정책 재검토.

---

## F3. 임시 권한 - 회수 미완료

```jql
project = ACCT
AND "회수 예정일" is not EMPTY
AND "회수 예정일" <= now()
AND "권한 회수 처리됨" is EMPTY
ORDER BY "회수 예정일" ASC
```

> 즉시 0건 유지가 목표. 1건이라도 잡히면 보안실 daily standup 안건.

---

## F4. 최상위 권한 부여 (Super Admin / Admin Role)

```jql
project = ACCT
AND (
    summary ~ "Super Admin*"
    OR comment ~ "최상위 권한"
)
AND created >= "-90d"
ORDER BY created DESC
```

> 분기별 보안실장 보고 자료.

---

## F5. SLA Breach (1차 결재자 응답 지연)

```jql
project = ACCT
AND "Time to lead approval" = breached()
AND created >= "-90d"
ORDER BY created DESC
```

> 결재자 단위 집계 → 분기 SLA 리포트.

---

## F6. SLA Breach (정보보안실 응답 지연)

```jql
project = ACCT
AND "Time to InfoSec approval" = breached()
AND created >= "-90d"
ORDER BY created DESC
```

> 보안실 내부 KPI.

---

## F7. 거절 사유 통계 (정성 분석용)

```jql
project = ACCT
AND resolution = "Rejected"
AND created >= startOfQuarter()
ORDER BY created DESC
```

> Export 후 거절 코멘트 keyword 분석 → 신청 가이드 개선.

---

## F8. 시스템별 신청 분포 (대시보드 파이 차트)

```jql
project = ACCT
AND created >= startOfQuarter()
```

차트 설정: Group by `시스템`, Count.

---

## F9. 카테고리별 분포

```jql
project = ACCT
AND created >= startOfQuarter()
```

차트 설정: Group by `카테고리`, Count.

---

## 대시보드 - `ACCT - ISMS 감사`

권장 구성:
- 상단 row: F8 (시스템별 파이) + F9 (카테고리별 파이)
- 중단 row: F2 (자기결재 카운트) + F3 (회수 미완료 카운트, 빨간 강조)
- 하단 row: F5/F6 SLA breach 리스트
- 사이드바: F4 최상위 권한 부여 최근 10건

> 보안실장 + ISMS 외부 심사원에게 read-only 공유.
