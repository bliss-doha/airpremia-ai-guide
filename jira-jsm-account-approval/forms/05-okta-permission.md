# Form: [OKTA] 권한 신청서

> 공통 입력 블록 [00-common-block.md](00-common-block.md).

## OKTA 권한 전용 섹션

| Form Question | Type | Required | Conditional |
|---|---|---|---|
| 대상자 | User picker | ✓ | always |
| 대상 OKTA 계정 ID/이메일 | Short text | △ | show if 대상자 외부 협력사인 경우 |
| 변경 유형 | Multi-select: App 할당 / App 회수 / Group 할당 / Group 회수 / Admin Role 부여 / Admin Role 회수 | ✓ | always |
| 대상 App (할당/회수) | Multi-select (lookup) | △ | show if `변경 유형 contains (App 할당 OR App 회수)` |
| 대상 Group (할당/회수) | Multi-select (lookup) | △ | show if `변경 유형 contains (Group 할당 OR Group 회수)` |
| Admin Role 종류 | Single select: Super Admin / Org Admin / App Admin / Help Desk Admin / Read Only Admin / Group Membership Admin | △ | show if `변경 유형 contains Admin Role 부여` |
| Admin Role Scope (Group 또는 App 한정) | Long text | △ | show if `Admin Role 종류 ∈ {App Admin, Group Membership Admin}` |
| 동일 권한 보유 동료 (참고) | User picker | △ | always |

## 검증 규칙
- `Super Admin` 또는 `Org Admin` 부여 신청 시 자동 코멘트 "최상위 권한 - 정보보안실 사전 협의 필수"
- 자동화로 정보보안실 채널에 즉시 thread 생성
