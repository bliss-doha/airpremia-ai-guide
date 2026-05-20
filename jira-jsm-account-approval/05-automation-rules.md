# Automation Rules - R1 ~ R9

JIRA → Project settings → Automation. 모든 rule scope = `Project: ACCT`.

> 표기: `{{var}}` 는 Smart Value, `[Branch]` 는 conditional/branch action.

---

## R1. 자동 시작 (Open → Pending Lead Approval)

| 항목 | 값 |
|---|---|
| Trigger | Issue created |
| Condition | Issue Type ∈ (위 9개 Request Type 의 issue type) AND Reporter is not empty |
| Action 1 | **Validate**: `직속 리더` ≠ Reporter (자기결재 차단 → see R8) |
| Action 2 | **Transition issue**: `Auto-Start` (Open → Pending Lead Approval) |
| Action 3 | **Comment**: `요청이 접수되었습니다. 1차 결재자({{직속 리더.displayName}}) 의 승인을 기다립니다.` |

---

## R2. 1차 결재자 셋팅 (Pending Lead Approval 진입 시)

| 항목 | 값 |
|---|---|
| Trigger | Issue transitioned to `Pending Lead Approval` |
| Action 1 | **Edit issue**: `Approvers` = `{{issue.직속 리더}}` |
| Action 2 | **Send email** to `{{issue.직속 리더.emailAddress}}` - Subject: `[승인요청] {{issue.summary}}`, Body: portal link 포함 |
| Action 3 | **Send Slack DM** (Slack integration 사용) to `{{issue.직속 리더}}` |

---

## R3. 1차 승인 처리 (Approve → Pending InfoSec Approval)

| 항목 | 값 |
|---|---|
| Trigger | Approval completed |
| Condition | Approval decision = `Approved` AND status = `Pending Lead Approval` |
| Action 1 | **Transition issue**: `Lead Approve` (→ Pending InfoSec Approval) |
| Action 2 | **Comment**: `1차 승인 완료 (승인자: {{approval.approver.displayName}}, {{now}}). 정보보안실 검토를 기다립니다.` |

---

## R4. 1차 거절 처리 (Reject → Rejected)

| 항목 | 값 |
|---|---|
| Trigger | Approval completed |
| Condition | Approval decision = `Declined` AND status = `Pending Lead Approval` |
| Action 1 | **Edit issue**: Resolution = `Rejected` |
| Action 2 | **Transition issue**: `Lead Reject` (→ Rejected) |
| Action 3 | **Comment**: `1차 결재 거절 (거절자: {{approval.approver.displayName}}, 사유: {{approval.comment}}). 종료됩니다. 재신청은 신규 티켓으로 요청해 주세요.` |
| Action 4 | **Send email** to Reporter |

---

## R5. 정보보안실 결재자 셋팅 (Pending InfoSec Approval 진입 시)

| 항목 | 값 |
|---|---|
| Trigger | Issue transitioned to `Pending InfoSec Approval` |
| Action 1 | **Edit issue**: `Approvers` = members of group `정보보안실` |
| Action 2 | Approval rule: 1 of N (project setting) |
| Action 3 | **Send Slack message** to `#infosec-approval`: `🔐 신규 결재 요청 - {{issue.summary}} ({{issue.key}}) | 시스템={{issue.시스템}} | 카테고리={{issue.카테고리}} | 신청자={{issue.reporter.displayName}}` |

---

## R6. 정보보안실 승인 처리 (Approve → In Progress)

| 항목 | 값 |
|---|---|
| Trigger | Approval completed |
| Condition | Approval decision = `Approved` AND status = `Pending InfoSec Approval` |
| Action 1 | **Transition issue**: `InfoSec Approve` (→ In Progress) |
| Action 2 | **Assign issue**: round-robin within group `IT-운영` |
| Action 3 | **Comment**: `정보보안실 승인 완료 (승인자: {{approval.approver.displayName}}). IT 운영팀 작업 대기.` |
| Action 4 | **Send email** to Assignee + Reporter |

---

## R7. 정보보안실 거절 처리 (Reject → Rejected)

| 항목 | 값 |
|---|---|
| Trigger | Approval completed |
| Condition | Approval decision = `Declined` AND status = `Pending InfoSec Approval` |
| Action 1 | **Edit issue**: Resolution = `Rejected` |
| Action 2 | **Transition issue**: `InfoSec Reject` (→ Rejected) |
| Action 3 | **Comment**: `정보보안실 거절 (거절자: {{approval.approver.displayName}}, 사유: {{approval.comment}}). 1차 승인 이력은 보존됩니다.` |
| Action 4 | **Send email** to Reporter + 직속 리더 |

---

## R8. 자기결재 차단 (Reporter == 직속 리더)

| 항목 | 값 |
|---|---|
| Trigger | Issue created |
| Condition | Reporter == `직속 리더` |
| Action 1 | **Edit issue**: `Approvers` = members of group `정보보안실` (직속 리더 단계 건너뛰고 보안실로 직행) |
| Action 2 | **Transition issue**: `Auto-Start` 후 즉시 `Lead Approve` (스킵) → 결과적으로 Pending InfoSec Approval 로 이동 |
| Action 3 | **Comment**: `⚠️ 자기결재 케이스 - 1차 결재 단계 자동 스킵, 정보보안실 단독 검토. 감사 기록을 위해 본 코멘트가 자동 추가됩니다.` |
| Action 4 | **Send Slack message** to `#infosec-approval`: `⚠️ 자기결재 케이스 발생: {{issue.key}} - 정보보안실에서 단독 심사가 필요합니다.` |

> 운영 정책: 자기결재 케이스는 분기별 감사 리포트에 별도 집계.

---

## R9. 임시 권한 회수 리마인드 (회수 예정일 D-7)

| 항목 | 값 |
|---|---|
| Trigger | Scheduled - 매일 09:00 KST, JQL: `project = ACCT AND "회수 예정일" >= now() AND "회수 예정일" <= now("7d") AND status = Done AND resolution = Done AND "권한 회수 처리됨" is EMPTY` |
| Action 1 | **Send Slack message** to `#infosec-approval`: `🔁 권한 회수 D-7 알림 - {{issue.key}} ({{issue.시스템}} / {{issue.카테고리}}) | 대상자={{issue.reporter}} | 회수예정일={{issue.회수예정일}}` |
| Action 2 | **Create new issue**: type = `[{{issue.시스템}}] 계정 및 권한 신청서`, 카테고리 = `계정삭제` 또는 `계정수정`(권한 회수), 사유 = "임시 권한 회수 (원본 티켓: {{issue.key}})", 회수 예정일 = (없음), Linked Issue: `relates to` `{{issue.key}}` |
| Action 3 | **Edit original issue**: 코멘트 `회수 티켓 자동 생성: {{newIssue.key}}` |

> 별도 custom field `권한 회수 처리됨` (Yes/No) 을 신설하여 회수 완료 표시. 회수 티켓이 Done 으로 종료되면 R9.b 로 원본 이슈에 표시.

### R9.b. 회수 완료 표시 (보조)

| 항목 | 값 |
|---|---|
| Trigger | Issue transitioned to `Done` |
| Condition | Issue has linked issue with relationship `relates to` AND linked source 카테고리 == `권한부여` |
| Action 1 | **Edit linked source issue**: `권한 회수 처리됨` = `Yes` |
| Action 2 | **Comment** on source: `회수 처리 완료 - 회수 티켓 {{issue.key}}` |

---

## 참고: Smart Values 매핑

| Smart Value | JIRA Custom Field |
|---|---|
| `{{issue.직속 리더}}` | `customfield_xxxxx` (직속 리더) |
| `{{issue.시스템}}` | `customfield_xxxxx` (시스템) |
| `{{issue.카테고리}}` | `customfield_xxxxx` (카테고리) |
| `{{issue.회수예정일}}` | `customfield_xxxxx` (회수 예정일) |

> 실제 customfield ID 는 프로젝트 생성 후 JSON view 에서 확인하여 본 문서를 업데이트.
