---
source_file: "packages/coding-agent/test/suite/regressions/6363-agent-settled-event.test.ts"
type: "rationale"
community: "Coding Agent 会话工具 7"
location: "emits one agent_settled event after automatic retry finishes, settles only after follow-ups queued by agent_end handlers run"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Coding_Agent_会话工具_7
---

# T06 回归测试表达重试/agent_end新followUp可有多个agent_end且一个agent_settled的预期

## Connections
- [[6363-agent-settled-event.test.ts]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Coding_Agent_会话工具_7

## 源码入口

[packages/coding-agent/test/suite/regressions/6363-agent-settled-event.test.ts](../../../packages/coding-agent/test/suite/regressions/6363-agent-settled-event.test.ts)
