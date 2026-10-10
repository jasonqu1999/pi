---
source_file: "packages/agent/src/agent-loop.ts"
type: "rationale"
community: "Agent 控制循环 85"
location: "runLoop, currentContext.messages.push(result), getFollowUpMessages, shouldTerminateToolBatch"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Agent_控制循环_85
---

# E15 runLoop回填工具结果，finishTurn及队列决定内外循环继续或agent_end

## Connections
- [[runLoop()]] - `references` [EXTRACTED]
- [[shouldTerminateToolBatch()]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Agent_控制循环_85

## 源码入口

[packages/agent/src/agent-loop.ts](../../../packages/agent/src/agent-loop.ts)
