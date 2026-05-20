# Form: [Datadog] 계정 및 권한 신청서

> 공통 입력 블록 [00-common-block.md](00-common-block.md).

## Datadog 전용 섹션

| Form Question | Type | Required | Conditional |
|---|---|---|---|
| 대상자 | User picker | ✓ | always |
| 대상 Datadog 계정 (이메일) | Email | △ | show if `카테고리 ∈ {계정수정, 계정삭제, 권한부여}` |
| Datadog Org | Single select: Production / Staging / 기타 | ✓ | always |
| Datadog Role | Multi-select: Datadog Admin Role / Datadog Standard Role / Datadog Read Only Role / Custom Role | ✓ | show if `카테고리 ∈ {계정생성, 권한부여, 계정수정}` |
| Custom Role 명세 | Long text | △ | show if `Datadog Role contains Custom Role` |
| API Key / Application Key 필요 여부 | Single select: 불필요 / API Key / Application Key / 둘 다 | ✓ | show if `카테고리 ∈ {계정생성, 권한부여}` |
| Key 사용 시스템 | Long text | △ | show if `API Key/Application Key 필요 여부 != 불필요` |
| 접근 필요 Service / Dashboard / Monitor | Long text | △ | always |

## 검증 규칙
- `Datadog Admin Role` 부여 시 자동 코멘트 "최상위 권한 - 정보보안실 사전 협의 필수"
- API/Application Key 발급 시 회수 예정일 필수
