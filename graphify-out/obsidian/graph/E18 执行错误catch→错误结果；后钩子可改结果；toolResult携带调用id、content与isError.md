---
source_file: "packages/agent/src/agent-loop.ts"
type: "rationale"
community: "Agent 控制循环 85"
location: "executePreparedToolCall, createErrorToolResult, createToolResultMessage"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Agent_控制循环_85
---

# E18 执行错误catch→错误结果；后钩子可改结果；toolResult携带调用id、content与isError

## Connections
- [[createErrorToolResult()]] - `references` [EXTRACTED]
- [[createToolResultMessage()]] - `references` [EXTRACTED]
- [[executePreparedToolCall()]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Agent_控制循环_85

## 源码入口

[packages/agent/src/agent-loop.ts](../../../packages/agent/src/agent-loop.ts)
