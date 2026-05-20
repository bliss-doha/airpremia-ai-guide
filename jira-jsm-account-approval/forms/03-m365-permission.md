# Form: [M365] 권한 신청서

> 공통 입력 블록 [00-common-block.md](00-common-block.md).

## M365 권한 전용 섹션

| Form Question | Type | Required | Conditional |
|---|---|---|---|
| 대상자 (개인 or 그룹) | Single select: 개인 / 그룹 | ✓ | always |
| 대상 사용자 | User picker | ✓ | show if `대상자 == 개인` |
| 대상 그룹 | Short text | ✓ | show if `대상자 == 그룹` |
| 권한 유형 | Multi-select: 라이선스 / Security Group / Distribution Group / SharePoint 사이트 / Teams 채널 / Exchange 권한 / 기타 | ✓ | always |
| 라이선스 종류 | Multi-select: E3 / E5 / Exchange Plan 1 / Plan 2 / Power BI / 기타 | △ | show if `권한 유형 contains 라이선스` |
| 그룹/사이트/채널 명 | Short text | △ | show if `권한 유형 contains (Security Group OR Distribution Group OR SharePoint OR Teams)` |
| 부여 권한 레벨 | Single select: Owner / Edit / Read | △ | show if `권한 유형 contains (SharePoint OR Teams)` |
| Exchange 권한 종류 | Multi-select: Send As / Send on Behalf / Full Access | △ | show if `권한 유형 contains Exchange` |
| 동일 권한 보유 동료 (참고) | User picker | △ | always |

## 검증 규칙
- `대상자 == 본인` 인 경우 자동 코멘트 "본인 신청 - 정보보안실 추가 검토 필요"
