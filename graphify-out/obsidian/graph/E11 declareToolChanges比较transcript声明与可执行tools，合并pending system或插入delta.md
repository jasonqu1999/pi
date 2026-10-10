---
source_file: "packages/agent/src/agent-loop.ts"
type: "rationale"
community: "Agent 控制循环 85"
location: "declareToolChanges, getToolStateChanges, withToolChanges"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Agent_控制循环_85
---

# E11 declareToolChanges比较transcript声明与可执行tools，合并pending system或插入delta

## Connections
- [[declareToolChanges()]] - `references` [EXTRACTED]
- [[withToolChanges()]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Agent_控制循环_85

## 源码入口

[packages/agent/src/agent-loop.ts](../../../packages/agent/src/agent-loop.ts)
