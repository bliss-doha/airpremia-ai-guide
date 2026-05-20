# Workflow 스펙 - `ACCT: Account & Permission Approval`

JIRA Admin → Workflows → Create workflow.

## 1. Status (6개)

| Status 이름 | Category | 설명 |
|---|---|---|
| Open | To Do | 티켓 생성 직후. R1 automation 이 즉시 다음 status 로 전이. |
| Pending Lead Approval | In Progress | 직속 리더 승인 대기. Approvers 패널 활성화. |
| Pending InfoSec Approval | In Progress | 정보보안실 그룹 승인 대기. 1 of N 승인 정책. |
| In Progress | In Progress | 양쪽 승인 완료. IT 운영 담당자가 실제 작업 수행. |
| Done | Done | 작업 정상 완료. |
| Rejected | Done | 1차 또는 2차 단계에서 거절되어 종료. |

## 2. Transition (6개)

| # | Transition 이름 | From | To | Trigger | Post-function 비고 |
|---|---|---|---|---|---|
| T1 | Auto-Start | Open | Pending Lead Approval | Automation R1 (Issue created) | - |
| T2 | Lead Approve | Pending Lead Approval | Pending InfoSec Approval | Automation R3 (Approval approved) | - |
| T3 | Lead Reject | Pending Lead Approval | Rejected | Automation R4 (Approval declined) | Resolution = "Rejected" |
| T4 | InfoSec Approve | Pending InfoSec Approval | In Progress | Automation R6 (Approval approved) | Assignee = IT-운영 그룹 round-robin |
| T5 | InfoSec Reject | Pending InfoSec Approval | Rejected | Automation R7 (Approval declined) | Resolution = "Rejected" |
| T6 | Complete | In Progress | Done | Manual (Assignee) | Resolution = "Done", 처리 결과 코멘트 필수 |

## 3. Approvers 필드 - Status 별 매핑

JSM Project settings → Request types → Workflow → Approval 섹션에서 다음 status 에 Approval 활성화.

| Status | Approvers 출처 | 승인 정책 |
|---|---|---|
| Pending Lead Approval | `직속 리더` 필드 (단일 사용자) | 1명 승인 |
| Pending InfoSec Approval | Group: `정보보안실` | 1 of N (그룹원 중 1명) |

- Approvers 필드는 1개를 stage 별로 dynamic 하게 자동 갱신 (R2, R5 automation).
- 승인 행위 자체는 JSM 네이티브 Approve/Decline 버튼으로 수행 → 결재 이력은 자동 보존.

## 4. Workflow Scheme

- Workflow Scheme 이름: `ACCT Approval Workflow Scheme`
- 매핑: 모든 9개 Request Type (Issue Type) → 위 workflow

## 5. Resolution

| 시점 | Resolution 값 |
|---|---|
| Lead Reject (T3) | Rejected |
| InfoSec Reject (T5) | Rejected |
| Complete (T6) | Done |

## 6. 다이어그램 (텍스트)

```
                       ┌────────────────────────┐
                       │  Open                  │
                       └────────────┬───────────┘
                                    │ T1 Auto-Start
                                    ▼
                       ┌────────────────────────┐
                       │ Pending Lead Approval  │ ◀── Approvers = {직속 리더}
                       └─────┬─────────────┬────┘
                  T2 Approve │             │ T3 Reject
                             ▼             ▼
        ┌──────────────────────────┐   ┌─────────────┐
        │ Pending InfoSec Approval │   │  Rejected   │
        └─────┬─────────────┬──────┘   └─────────────┘
   T4 Approve │             │ T5 Reject
              ▼             ▼
   ┌────────────────┐   ┌─────────────┐
   │  In Progress   │   │  Rejected   │
   └────────┬───────┘   └─────────────┘
            │ T6 Complete
            ▼
   ┌────────────────┐
   │  Done          │
   └────────────────┘
```
