---
source_file: "packages/agent/src/agent-loop.ts"
type: "rationale"
community: "Agent 控制循环 85"
location: "streamAssistantResponse, case \"start\", case \"done\", message_end"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Agent_控制循环_85
---

# E12 stream start/delta/final在循环上下文形成partial和最终assistant，发消息事件

## Connections
- [[streamAssistantResponse()]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Agent_控制循环_85

## 源码入口

[packages/agent/src/agent-loop.ts](../../../packages/agent/src/agent-loop.ts)
