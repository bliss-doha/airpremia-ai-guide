# Form: [HIWARE] 계정 및 권한 신청서

> 공통 입력 블록은 [00-common-block.md](00-common-block.md) 참고. 아래는 HIWARE 전용 추가 섹션.

## HIWARE 전용 섹션

| Form Question | Type | Required | Conditional |
|---|---|---|---|
| 대상자 이름 (한글) | Short text | ✓ | always show |
| 대상자 이메일 | Email | ✓ | always show |
| HIWARE 계정 ID | Short text | △ | show if `카테고리 ∈ {계정수정, 계정삭제, 권한부여}` (생성 시는 미존재) |
| 입사일 / 직책 | Short text | △ | show if `카테고리 == 계정생성` |
| 요청 권한/그룹 | Multi-select | △ | show if `카테고리 ∈ {권한부여, 계정수정}` |
| 동일 권한 보유자 (참고) | User picker | △ | show if `카테고리 == 권한부여` (감사 시 비교 기준) |

## 검증 규칙
- 이메일 형식 검증
- `대상자 == 요청자` 인 경우는 자기 권한 신청 → 별도 코멘트 자동 추가 ("본인 신청")
