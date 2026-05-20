# 검증 시나리오 V1 ~ V8

각 시나리오 실행 후 결과 캡처 (스크린샷 + 이슈 키) 를 본 문서 하단에 첨부.

| ID | 시나리오 | 사전 조건 | 실행 단계 | 기대 결과 |
|---|---|---|---|---|
| **V1** | 정상 흐름 - Slack 권한 신청 | 테스트 계정 A(요청자), B(직속 리더), 보안실 그룹에 C 1명 | 1. A 가 `[Slack] 권한 신청서` 작성 (직속 리더=B, 카테고리=권한부여, Channel=#test-private)<br>2. B 가 Slack DM 알림 확인 후 Approve<br>3. C 가 정보보안실 채널 알림 확인 후 Approve<br>4. IT 운영 D 가 In Progress 에서 작업 후 T6 Complete | - 각 단계 알림 도달<br>- Status: Open → Pending Lead → Pending InfoSec → In Progress → Done<br>- Approval 패널에 B, C 의 결재시각·코멘트 자동 기록<br>- Done 시 Reporter, B, 보안실 모두 알림 수신 |
| **V2** | 1차 거절 | V1 과 동일 | 1~2. A 신청, B 가 Decline (사유: "권한 과다") | - Status → Rejected<br>- Resolution = Rejected<br>- 코멘트에 거절자/사유 자동 기록<br>- 2차 단계 미진입 (정보보안실에 알림 없음)<br>- A 에게 거절 사유 email 도달 |
| **V3** | 2차 거절 | V1 과 동일 | 1~2. A 신청, B Approve, C Decline (사유: "회수 일정 누락") | - Status: Pending Lead → Pending InfoSec → Rejected<br>- 1차 승인 이력은 Approval 패널에 보존<br>- A, B 모두 거절 알림 수신 |
| **V4** | 자기결재 시도 | A 가 직속 리더에 본인 지정 | 1. A 신청 (직속 리더=A) | - R8 발동: 1차 단계 자동 스킵<br>- 즉시 Pending InfoSec Approval 로 이동<br>- 코멘트에 "⚠️ 자기결재 케이스" 자동 기록<br>- `#infosec-approval` 채널에 경고 메시지<br>- 보안실 단독 승인/거절로 종결 |
| **V5** | 임시 권한 회수 알림 | 회수 예정일 = 오늘 + 7일, 카테고리=권한부여, status=Done 이슈 1개 | 1. R9 scheduled rule 트리거 시각 (다음날 09:00 KST) 대기<br>또는 수동으로 Manual trigger 실행 | - Slack `#infosec-approval` 에 회수 D-7 알림<br>- 회수용 신규 티켓 자동 생성 (카테고리=계정수정, 사유에 원본 키 기재)<br>- 원본 이슈에 회수 티켓 키 코멘트 추가 |
| **V6** | Customer Portal 노출 확인 | 일반 사용자 계정으로 로그인 | 1. Portal 접속 → `📂 계정 관리` 그룹 진입 | - 9개 Request Type 모두 노출<br>- 그룹 안 순서: HIWARE → M365 공용 → M365 권한 → OKTA 공용 → OKTA 권한 → Slack → CrowdStrike → Cloudflare → Datadog |
| **V7** | 감사용 Evidence export | V1~V5 의 종결 티켓 존재 | 1. Issue Navigator → JQL `project = ACCT AND created >= "테스트 시작일"`<br>2. Export → CSV (All fields) | - Issue Key, Reporter, 직속 리더, 시스템, 카테고리, 신청 사유, 1차 승인자/시각, 2차 승인자/시각, Assignee, Resolution, Resolved 컬럼이 모두 채워짐<br>- 비어 있는 결재 컬럼 없음 (Rejected 케이스 포함) |
| **V8** | Forms conditional 분기 | 임의 신청서 진입 | 1. 카테고리=권한부여 선택 → 회수 예정일 노출 확인<br>2. 카테고리=계정삭제 선택 → 시스템별 권한 입력 필드 숨김, 삭제 사유/효력 발생일 노출 확인<br>3. OKTA 권한 신청서에서 Admin Role 종류=Super Admin 선택 → "최상위 권한" 자동 코멘트 확인 | - Conditional 동작 정상<br>- 강제 코멘트 자동 추가 |

---

## 결과 첨부 (실행 후 채워 넣기)

| ID | 실행일 | 실행자 | 이슈 키 | 결과 (P/F) | 비고 |
|---|---|---|---|---|---|
| V1 |  |  |  |  |  |
| V2 |  |  |  |  |  |
| V3 |  |  |  |  |  |
| V4 |  |  |  |  |  |
| V5 |  |  |  |  |  |
| V6 |  |  |  |  |  |
| V7 |  |  |  |  |  |
| V8 |  |  |  |  |  |

> 모두 Pass 후 ISMS 책임자 서명 → 운영 전환 승인.
