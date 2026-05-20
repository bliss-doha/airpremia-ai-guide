# Request Types - 9개

JSM Project settings → Request types. Group: `📂 계정 관리 (생성, 제거, 수정, Role)`.

모든 Request Type 공통:
- Issue Type: `Service Request with Approvals`
- Workflow: `ACCT Approval Workflow Scheme`
- Permission: Customer Portal 노출 (전사)
- 공통 필드 7개 (`01-custom-fields.csv`) 모두 포함
- 시스템별 추가 필드: `forms/{system}.md` 의 Form 1개 첨부

---

## 1. [HIWARE] 계정 및 권한 신청서

| 항목 | 값 |
|---|---|
| Icon | 🔑 (또는 HIWARE 로고 업로드) |
| 시스템 필드 default | `HIWARE` (read-only) |
| Form | [forms/01-hiware.md](forms/01-hiware.md) |
| Description | HIWARE 계정 생성, 수정, 삭제, 권한(그룹) 부여를 신청합니다. |

## 2. [M365] 공용 계정 생성 신청서

| 항목 | 값 |
|---|---|
| Icon | 📨 |
| 시스템 필드 default | `M365` |
| 카테고리 default | `계정생성` (read-only on portal) |
| Form | [forms/02-m365-shared-account.md](forms/02-m365-shared-account.md) |
| Description | 팀/프로젝트용 M365 공용 메일박스 또는 공용 계정 생성을 신청합니다. |

## 3. [M365] 권한 신청서

| 항목 | 값 |
|---|---|
| Icon | 📁 |
| 시스템 필드 default | `M365` |
| Form | [forms/03-m365-permission.md](forms/03-m365-permission.md) |
| Description | M365 그룹/라이선스, SharePoint/Teams 리소스 권한 변경을 신청합니다. |

## 4. [OKTA] 공용 계정 생성 신청서

| 항목 | 값 |
|---|---|
| Icon | 🛂 |
| 시스템 필드 default | `OKTA` |
| 카테고리 default | `계정생성` |
| Form | [forms/04-okta-shared-account.md](forms/04-okta-shared-account.md) |
| Description | OKTA 공용 계정(서비스 계정 등) 생성을 신청합니다. |

## 5. [OKTA] 권한 신청서

| 항목 | 값 |
|---|---|
| Icon | 🛂 |
| 시스템 필드 default | `OKTA` |
| Form | [forms/05-okta-permission.md](forms/05-okta-permission.md) |
| Description | OKTA 사용자 App/Group 할당 변경을 신청합니다. |

## 6. [Slack] 권한 신청서

| 항목 | 값 |
|---|---|
| Icon | 💬 |
| 시스템 필드 default | `Slack` |
| Form | [forms/06-slack-permission.md](forms/06-slack-permission.md) |
| Description | Slack Workspace/Private Channel 초대, Owner/Admin 권한 부여를 신청합니다. |

## 7. [CrowdStrike] 계정 및 권한 신청서

| 항목 | 값 |
|---|---|
| Icon | 🛡️ |
| 시스템 필드 default | `CrowdStrike` |
| Form | [forms/07-crowdstrike.md](forms/07-crowdstrike.md) |
| Description | CrowdStrike Falcon 콘솔 계정 및 Role 부여를 신청합니다. |

## 8. [Cloudflare] 계정 및 권한 신청서

| 항목 | 값 |
|---|---|
| Icon | ☁️ |
| 시스템 필드 default | `Cloudflare` |
| Form | [forms/08-cloudflare.md](forms/08-cloudflare.md) |
| Description | Cloudflare Account 멤버십 및 Role 변경을 신청합니다. |

## 9. [Datadog] 계정 및 권한 신청서

| 항목 | 값 |
|---|---|
| Icon | 🐶 |
| 시스템 필드 default | `Datadog` |
| Form | [forms/09-datadog.md](forms/09-datadog.md) |
| Description | Datadog Org 사용자 및 Role 부여를 신청합니다. |

---

## Customer Portal 표시 순서

Group `📂 계정 관리 (생성, 제거, 수정, Role)` 안에서 위 1~9 순서 그대로 노출.
