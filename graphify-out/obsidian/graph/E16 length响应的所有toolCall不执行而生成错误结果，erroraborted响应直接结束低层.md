---
source_file: "packages/agent/src/agent-loop.ts"
type: "rationale"
community: "Agent 控制循环 85"
location: "failToolCallsFromTruncatedMessage, message.stopReason === \"length\", message.stopReason === \"error\""
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Agent_控制循环_85
---

# E16 length响应的所有toolCall不执行而生成错误结果，error/aborted响应直接结束低层

## Connections
- [[failToolCallsFromTruncatedMessage()]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Agent_控制循环_85

## 源码入口

[packages/agent/src/agent-loop.ts](../../../packages/agent/src/agent-loop.ts)
