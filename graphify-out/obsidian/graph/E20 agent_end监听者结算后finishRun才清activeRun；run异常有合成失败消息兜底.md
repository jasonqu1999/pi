---
source_file: "packages/agent/src/agent.ts"
type: "rationale"
community: "Coding Agent 会话工具 15"
location: "runWithLifecycle, handleRunFailure, finishRun, waitForIdle"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Coding_Agent_会话工具_15
---

# E20 agent_end监听者结算后finishRun才清activeRun；run异常有合成失败消息兜底

## Connections
- [[dot-finishRun()]] - `references` [EXTRACTED]
- [[dot-handleRunFailure()]] - `references` [EXTRACTED]
- [[dot-runWithLifecycle()]] - `references` [EXTRACTED]
- [[dot-waitForIdle()]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Coding_Agent_会话工具_15

## 源码入口

[packages/agent/src/agent.ts](../../../packages/agent/src/agent.ts)
