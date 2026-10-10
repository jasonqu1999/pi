---
source_file: "packages/agent/src/agent-loop.ts"
type: "rationale"
community: "Agent 控制循环 85"
location: "executeToolCalls, prepareToolCall, executePreparedToolCall, finalizeExecutedToolCall"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Agent_控制循环_85
---

# E13 工具执行按配置/工具executionMode选并行或顺序；查找/准备/校验/前钩子/执行/后钩子

## Connections
- [[executePreparedToolCall()]] - `references` [EXTRACTED]
- [[executeToolCalls()]] - `references` [EXTRACTED]
- [[finalizeExecutedToolCall()]] - `references` [EXTRACTED]
- [[prepareToolCall()]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Agent_控制循环_85

## 源码入口

[packages/agent/src/agent-loop.ts](../../../packages/agent/src/agent-loop.ts)
