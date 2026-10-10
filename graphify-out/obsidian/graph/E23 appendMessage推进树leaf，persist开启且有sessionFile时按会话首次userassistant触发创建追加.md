---
source_file: "packages/coding-agent/src/core/session-manager.ts"
type: "rationale"
community: "Coding Agent 会话工具 2"
location: "appendMessage, _appendEntry, _hasConversation, _persist"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Coding_Agent_会话工具_2
---

# E23 appendMessage推进树leaf，persist开启且有sessionFile时按会话首次user/assistant触发创建/追加

## Connections
- [[dot-_appendEntry()]] - `references` [EXTRACTED]
- [[dot-_hasConversation()]] - `references` [EXTRACTED]
- [[dot-_persist()]] - `references` [EXTRACTED]
- [[dot-appendMessage()]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Coding_Agent_会话工具_2

## 源码入口

[packages/coding-agent/src/core/session-manager.ts](../../../packages/coding-agent/src/core/session-manager.ts)
