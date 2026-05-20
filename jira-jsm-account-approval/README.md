# JSM 계정·권한 신청 승인 절차 - 구현 패키지

ISMS-P **2.5.1** 사용자 계정 관리 통제(접근권한 부여 시 승인 절차) 구축용 JIRA Service Management(Cloud Premium) 설정 산출물 묶음.

> 마스터 계획서: `~/.claude/plans/jira-service-desk-parsed-pony.md`

---

## 적용 흐름 요약

```
요청자 (Customer Portal 신청)
   │
   ▼
1차: 직속 리더 (User Picker로 매번 지정)        ─── 거절 → Rejected (종료)
   │
   ▼
2차: 정보보안실 그룹 (1 of N)                    ─── 거절 → Rejected (종료)
   │
   ▼
IT 운영 처리 → Done
```

---

## 파일 구성

| # | 파일 | 용도 | 작업자 |
|---|---|---|---|
| 01 | [01-custom-fields.csv](01-custom-fields.csv) | Custom Field 7개 정의 | JIRA Admin |
| 02 | [02-workflow.md](02-workflow.md) | Workflow / Status / Transition 스펙 | JIRA Admin |
| 03 | [03-request-types.md](03-request-types.md) | Request Type 9개 정의 | JIRA Admin |
| 04 | [forms/](forms/) | 시스템별 Forms 9종 (필드 + conditional logic) | JIRA Admin |
| 05 | [05-automation-rules.md](05-automation-rules.md) | Automation Rule 9개 (R1~R9) | JIRA Admin |
| 06 | [06-permission-notification-scheme.md](06-permission-notification-scheme.md) | Permission/Notification scheme | JIRA Admin |
| 07 | [07-sla-config.md](07-sla-config.md) | SLA 정책 | JIRA Admin |
| 08 | [08-internal-guide.md](08-internal-guide.md) | Confluence/Notion 사내 안내 페이지 원고 | 정보보안실 |
| 09 | [09-test-cases.md](09-test-cases.md) | 검증 시나리오 V1~V8 | 정보보안실 + IT |
| 10 | [10-jql-evidence-queries.md](10-jql-evidence-queries.md) | ISMS 감사용 JQL/Filter | 정보보안실 |

---

## 적용 순서 (체크리스트)

- [ ] **A. 사전 준비**
  - [ ] JSM Cloud Premium 라이선스 확인
  - [ ] User Group 생성: `정보보안실`, `IT-운영`
  - [ ] Slack 채널 준비: `#infosec-approval`
- [ ] **B. 프로젝트 셋업**
  - [ ] JSM 프로젝트 신규 생성: `IT 서비스 데스크 - 계정 및 권한` (key: `ACCT`)
  - [ ] [01-custom-fields.csv](01-custom-fields.csv) 의 7개 Custom Field 생성
  - [ ] [02-workflow.md](02-workflow.md) 의 Workflow 생성 + Workflow Scheme 적용
- [ ] **C. Request Type & Form**
  - [ ] [03-request-types.md](03-request-types.md) 의 9개 Request Type 생성
  - [ ] [forms/](forms/) 의 Form 9종 생성·연결
  - [ ] 각 Request Type 의 `시스템` 필드 기본값(read-only) 셋팅
- [ ] **D. 자동화**
  - [ ] [05-automation-rules.md](05-automation-rules.md) 의 R1~R9 등록
  - [ ] Approvers 필드 활성화 (Pending Lead Approval / Pending InfoSec Approval status)
- [ ] **E. 운영 정책**
  - [ ] [06-permission-notification-scheme.md](06-permission-notification-scheme.md) 적용
  - [ ] [07-sla-config.md](07-sla-config.md) SLA 등록
- [ ] **F. 검증 & 공지**
  - [ ] [09-test-cases.md](09-test-cases.md) V1~V8 실행, 결과 캡처 첨부
  - [ ] [08-internal-guide.md](08-internal-guide.md) 를 사내 위키에 게시
  - [ ] 전사 공지 (Customer Portal URL + 사용 가이드)

---

## Out of Scope

- HR 시스템 자동 연동 (입·퇴사 트리거 자동 티켓)
- 정기 권한 검토(Access Review) 워크플로우 - ISMS 2.5.6 별도 구축
- 위 9개 외 시스템 추가 - 동일 패턴 복제로 확장
