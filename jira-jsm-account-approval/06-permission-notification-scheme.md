# Permission & Notification Scheme

## 1. Permission Scheme - `ACCT Permission Scheme`

| Permission | Grantee | 비고 |
|---|---|---|
| Browse Projects | `정보보안실`, `IT-운영`, Project Admin | Customer 는 자기 티켓만 조회 (Customer Portal 별도) |
| Create Issues | `service-desk-customers` (전사) | 포털 경유로만 |
| Edit Issues | `IT-운영`, `정보보안실`, Project Admin | 요청자/리더는 코멘트만 |
| Add Comments | Reporter, Approvers, `IT-운영`, `정보보안실` | |
| Assign Issues | `IT-운영`, Project Admin | |
| Resolve Issues | `IT-운영` | T6 Complete 권한 |
| Manage Watchers | `IT-운영`, `정보보안실` | |
| Transition Issues | Automation actor, Approvers (Approve/Decline 한정), `IT-운영` (T6 한정) | |
| View Read-Only Workflow | All logged-in users | |
| View Voters and Watchers | `정보보안실`, Project Admin | |
| Administer Project | Project Admin only (보안실 1명 + IT 리드) | |

---

## 2. Customer Permission

JSM Project settings → Customer permissions:
- Who can access the portal? → **Anyone with an account on the Atlassian instance** (사내 전 직원)
- Who can send requests to your service project? → **Customers added to this service project (자동 등록)**
- 외부 사용자 초대 비활성화 (사내 전용)

---

## 3. Notification Scheme - `ACCT Notification Scheme`

| Event | Recipients |
|---|---|
| Issue Created | Reporter, `직속 리더` (R2 trigger 가 별도 처리하므로 중복 방지) |
| Issue Assigned | Assignee, Reporter |
| Status Changed → Pending Lead Approval | (R2 가 처리, scheme 에서는 비활성) |
| Status Changed → Pending InfoSec Approval | (R5 가 처리) |
| Status Changed → In Progress | Reporter, Assignee, `직속 리더`, `정보보안실` |
| Status Changed → Done | Reporter, `직속 리더`, `정보보안실` |
| Status Changed → Rejected | Reporter, `직속 리더` |
| Issue Commented | Reporter, Assignee, Approvers, `정보보안실` |
| Issue Resolved | Reporter, `직속 리더`, `정보보안실` |

> Slack 알림은 별도 Slack-JIRA integration + Automation R2/R5 가 담당. 결재자에게는 Slack DM 우선, email 은 백업.
