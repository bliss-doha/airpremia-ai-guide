# 공통 입력 블록 (모든 Form 의 첫 섹션에 동일하게 포함)

> JSM Forms editor 에서 9개 Form 에 동일하게 복제. Custom field 를 그대로 매핑하면 됨.

| Form Question | 매핑 Custom Field | Type | Required | Conditional |
|---|---|---|---|---|
| 부서 | `부서` | Single select | ✓ | always show |
| 직속 리더 (1차 결재자) | `직속 리더` | User picker | ✓ | always show |
| 카테고리 | `카테고리` | Single select | ✓ | always show |
| 신청 사유 | `신청 사유` | Long text | ✓ | always show |
| 적용 희망일 | `적용 희망일` | Date | ✓ | always show |
| 회수 예정일 (임시 권한일 경우만) | `회수 예정일` | Date | △ | show if `카테고리 == 권한부여` |
| 삭제 사유 | (form-only) | Single select: 퇴사 / 부서이동 / 직무변경 / 기타 | △ | show if `카테고리 == 계정삭제` |
| 효력 발생일 (계정 차단 시점) | (form-only) | Date | △ | show if `카테고리 == 계정삭제` |

> 시스템 필드(`시스템`)는 Request Type 별로 자동 셋팅이므로 Form 에서는 노출하지 않음 (read-only on issue view).
