# Form: [Slack] 권한 신청서

> 공통 입력 블록 [00-common-block.md](00-common-block.md).

## Slack 권한 전용 섹션

| Form Question | Type | Required | Conditional |
|---|---|---|---|
| 대상자 | User picker | ✓ | always |
| Workspace | Single select: Primary Workspace / Enterprise Grid (해당 시) | ✓ | always |
| 변경 유형 | Multi-select: Workspace 초대 / Private Channel 초대 / Channel 추방 / Workspace Owner 부여 / Workspace Admin 부여 / Multi-Channel Guest / Single-Channel Guest | ✓ | always |
| 대상 Channel(s) | Long text (채널명, 콤마 구분) | △ | show if `변경 유형 contains (Private Channel 초대 OR Channel 추방 OR Single-Channel Guest)` |
| Guest 회사명 | Short text | △ | show if `변경 유형 contains (Multi-Channel Guest OR Single-Channel Guest)` |
| Guest 연락처 (이메일) | Email | △ | show if `변경 유형 contains (Multi-Channel Guest OR Single-Channel Guest)` |
| Guest 계약 종료일 | Date | △ | show if `변경 유형 contains (Multi-Channel Guest OR Single-Channel Guest)` → 회수 예정일 자동 동기화 |
| 부여 사유 (Owner/Admin 인 경우 상세 사유) | Long text | △ | show if `변경 유형 contains (Workspace Owner 부여 OR Workspace Admin 부여)` |

## 검증 규칙
- `Workspace Owner` 또는 `Admin` 부여 시 자동 코멘트 "관리자 권한 - 정보보안실 사전 협의 권장"
- Guest 신청 시 `회수 예정일` 필수 자동 강제
