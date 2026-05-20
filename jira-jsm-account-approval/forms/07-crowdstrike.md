# Form: [CrowdStrike] 계정 및 권한 신청서

> 공통 입력 블록 [00-common-block.md](00-common-block.md).

## CrowdStrike 전용 섹션

| Form Question | Type | Required | Conditional |
|---|---|---|---|
| 대상자 | User picker | ✓ | always |
| 대상 Falcon 계정 (이메일) | Email | △ | show if `카테고리 ∈ {계정수정, 계정삭제, 권한부여}` |
| Falcon Console Role | Multi-select: Falcon Administrator / Endpoint Manager / Falcon Analyst / Real Time Responder Active / Real Time Responder Read Only / Falcon Investigator / Read-Only Analyst / Custom Role | ✓ | show if `카테고리 ∈ {계정생성, 권한부여, 계정수정}` |
| Custom Role 명세 | Long text | △ | show if `Falcon Console Role contains Custom Role` |
| API Key 발급 필요 여부 | Yes/No | ✓ | show if `카테고리 ∈ {계정생성, 권한부여}` |
| API Scope (필요 시) | Multi-select: Hosts / Detections / Incidents / Real Time Response / Sensor Download / 기타 | △ | show if `API Key 발급 == Yes` |
| 사용 도구/스크립트 | Long text | △ | show if `API Key 발급 == Yes` |

## 검증 규칙
- `Falcon Administrator` 부여 시 자동 코멘트 "최상위 권한 - 정보보안실 사전 협의 필수"
- API Key 발급 시 회수 예정일 필수
