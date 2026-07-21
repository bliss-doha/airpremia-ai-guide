---
title: "09. Opt-out 설정"
nav_order: 10
---

# 09. 개인 AI Opt-out 설정 가이드

개인 계정으로 상용 AI를 사용할 때 적용해야 할 최소 안전 설정입니다. **공개된 정보 작업에 한정해** 사용합니다.

**공통 원칙 3가지**

1. 회사명·직함·조직 정보를 프로필에 작성하지 않습니다
2. 회사 계정 및 회사 자산(M365·Slack·GitHub 등)은 연결하지 않습니다
3. AI 학습 차단(Opt-out) 설정 후 사용합니다
{: .note }

## LLM별 Opt-out 설정 방법

### ChatGPT
*OPENAI · Opt-out 설정*

**Settings → Data Controls**

| 설정 | 값 | 필수/권장 |
|---|---|---|
| "Improve the model for everyone" | OFF | 필수 |
| Chat History & Training | OFF | 필수 |

**Settings → Personalization**

| 설정 | 값 | 필수/권장 |
|---|---|---|
| Reference Saved Memories | OFF | 권장 |
| Reference Chat History | OFF | 권장 |

※ Temporary Chat 사용 시 기록·학습 모두 OFF로 처리됩니다.

### Claude
*ANTHROPIC · Opt-out 설정*

**Settings → Privacy**

| 설정 | 값 | 필수/권장 |
|---|---|---|
| "Help improve Claude" | OFF | 필수 |
| Location Data | OFF | 필수 |

**Settings → Features**

| 설정 | 값 | 필수/권장 |
|---|---|---|
| Search and reference chats | OFF | 권장 |
| Generate memory from chat history | OFF | 권장 |
| Network access | OFF | 권장 |

※ 회사 Claude Team과 개인 Claude는 별도 워크스페이스입니다. 혼동에 주의하세요.

### Gemini
*GOOGLE · Opt-out 설정*

**Settings → Activity**

| 설정 | 값 | 필수/권장 |
|---|---|---|
| Gemini Apps Activity | OFF | 필수 |

**Settings → Personal Intelligence**

| 설정 | 값 | 필수/권장 |
|---|---|---|
| Memory | OFF | 권장 |

※ 회사 Google Workspace 계정으로는 사용하지 않습니다.
※ 일부 UI에서는 "Keep Activity"로 표시될 수 있습니다.

### Copilot
*MICROSOFT · Opt-out 설정*

**Settings → Personal Settings**

| 설정 | 값 | 필수/권장 |
|---|---|---|
| Saved Memory | OFF | 필수 |
| Chat History (Frontier) | OFF | 필수 |
| Custom Instructions | OFF | 권고 |

※ 회사 Microsoft 계정으로는 사용하지 않습니다. 회사 업무는 M365 Copilot에서 진행합니다.
