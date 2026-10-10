---
source_file: "packages/coding-agent/src/core/agent-session.ts"
type: "rationale"
community: "Coding Agent 会话工具 29"
location: "_installAgentNextTurnRefresh, _compactBeforeNextAssistantResponse, _preparePromptAndToolLoadout"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Coding_Agent_会话工具_29
---

# E19 轮间刷新先压缩/投影，再更新工具装载与system sections；请求前还可重建canonical投影

## Connections
- [[dot-_compactBeforeNextAssistantResponse()]] - `references` [EXTRACTED]
- [[dot-_installAgentNextTurnRefresh()]] - `references` [EXTRACTED]
- [[dot-_preparePromptAndToolLoadout()]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Coding_Agent_会话工具_29

## 源码入口

[packages/coding-agent/src/core/agent-session.ts](../../../packages/coding-agent/src/core/agent-session.ts)
