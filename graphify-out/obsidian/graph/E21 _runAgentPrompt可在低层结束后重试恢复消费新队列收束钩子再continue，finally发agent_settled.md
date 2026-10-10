---
source_file: "packages/coding-agent/src/core/agent-session.ts"
type: "rationale"
community: "Coding Agent 会话工具 29"
location: "_runAgentPrompt, _handlePostAgentRun, _runBeforeSettleBoundary, _emitAgentSettled"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Coding_Agent_会话工具_29
---

# E21 _runAgentPrompt可在低层结束后重试/恢复/消费新队列/收束钩子再continue，finally发agent_settled

## Connections
- [[dot-_emitAgentSettled()]] - `references` [EXTRACTED]
- [[dot-_handlePostAgentRun()]] - `references` [EXTRACTED]
- [[dot-_runAgentPrompt()]] - `references` [EXTRACTED]
- [[dot-_runBeforeSettleBoundary()]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Coding_Agent_会话工具_29

## 源码入口

[packages/coding-agent/src/core/agent-session.ts](../../../packages/coding-agent/src/core/agent-session.ts)
