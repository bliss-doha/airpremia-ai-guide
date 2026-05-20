# Form: [M365] 공용 계정 생성 신청서

> 공통 입력 블록 [00-common-block.md](00-common-block.md) + 카테고리 default = `계정생성`.

## M365 공용 계정 전용 섹션

| Form Question | Type | Required | Conditional |
|---|---|---|---|
| 공용 계정 종류 | Single select: Shared Mailbox / Distribution List / Microsoft 365 Group / 공용 사용자 계정 | ✓ | always |
| 계정명 (alias) | Short text | ✓ | always |
| 표시 이름 (Display name) | Short text | ✓ | always |
| 도메인 | Single select: @company.com / @company.co.kr / 기타 | ✓ | always |
| 용도 / 사용 시나리오 | Long text | ✓ | always |
| 1차 Owner | User picker | ✓ | always |
| 2차 Owner (백업) | User picker | △ | always |
| 필요 라이선스 | Multi-select: E3 / E5 / Exchange Online Plan 1 / Plan 2 / 없음 | ✓ | always |
| 멤버 초기 멤버 (선택) | User picker (multi) | △ | always |
| 외부 송수신 허용 여부 | Yes/No | ✓ | show if `공용 계정 종류 ∈ {Shared Mailbox, Distribution List}` |

## 검증 규칙
- `계정명` 은 영문 소문자/숫자/`-`/`_` 만 허용
- 외부 송수신 허용 시 자동 코멘트로 정보보안실 검토 강조
