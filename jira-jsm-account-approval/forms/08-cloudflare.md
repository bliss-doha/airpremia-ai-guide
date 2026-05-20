# Form: [Cloudflare] 계정 및 권한 신청서

> 공통 입력 블록 [00-common-block.md](00-common-block.md).

## Cloudflare 전용 섹션

| Form Question | Type | Required | Conditional |
|---|---|---|---|
| 대상자 | User picker | ✓ | always |
| 대상 Cloudflare 계정 (이메일) | Email | △ | show if `카테고리 ∈ {계정수정, 계정삭제, 권한부여}` |
| Cloudflare Account | Single select: Production / Staging / 기타 | ✓ | always |
| Account Role | Multi-select: Super Administrator / Administrator / Administrator Read Only / Audit Logs Viewer / Billing / DNS / SSL/TLS, Caching, Performance / Workers Admin / Custom Scoped Role | ✓ | show if `카테고리 ∈ {계정생성, 권한부여, 계정수정}` |
| 적용 대상 Zone(s) | Long text (도메인 콤마 구분, 전체이면 "ALL") | △ | show if `Account Role contains Custom Scoped Role` |
| API Token 발급 필요 여부 | Yes/No | ✓ | show if `카테고리 ∈ {계정생성, 권한부여}` |
| API Token Scope | Long text | △ | show if `API Token 발급 == Yes` |
| 사용 시스템/CI 파이프라인 | Long text | △ | show if `API Token 발급 == Yes` |

## 검증 규칙
- `Super Administrator` 부여 시 자동 코멘트 "최상위 권한 - 정보보안실 사전 협의 필수, 최소 2명 유지 정책 확인"
- API Token 발급 시 회수 예정일 필수
