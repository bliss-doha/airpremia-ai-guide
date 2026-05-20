# Form: [OKTA] 공용 계정 생성 신청서

> 공통 입력 블록 [00-common-block.md](00-common-block.md) + 카테고리 default = `계정생성`.

## OKTA 공용 계정 전용 섹션

| Form Question | Type | Required | Conditional |
|---|---|---|---|
| 계정 종류 | Single select: 서비스 계정 / 공용 사용자 계정 / 외부 협력사 계정 | ✓ | always |
| 계정명 | Short text | ✓ | always |
| 1차 Owner | User picker | ✓ | always |
| 2차 Owner (백업) | User picker | △ | always |
| 용도 / 사용 시나리오 | Long text | ✓ | always |
| 할당할 OKTA App | Multi-select (lookup) | ✓ | always |
| 할당할 OKTA Group | Multi-select (lookup) | △ | always |
| MFA 정책 | Single select: 기본(Push) / Hardware Key 필수 / 면제(승인 필요) | ✓ | always |
| MFA 면제 사유 | Long text | △ | show if `MFA 정책 == 면제(승인 필요)` |
| 비밀번호 회전 주기 | Single select: 90일 / 180일 / 미회전(승인 필요) | ✓ | always |
| 외부 협력사 정보 | Long text (회사명, 담당자, 계약 종료일) | △ | show if `계정 종류 == 외부 협력사 계정` |

## 검증 규칙
- `MFA 정책 == 면제` 또는 `비밀번호 회전 == 미회전` 시 자동 코멘트 "정보보안실 강제 검토 항목"
- `계정 종류 == 외부 협력사 계정` 인 경우 `회수 예정일` 필수로 자동 강제
