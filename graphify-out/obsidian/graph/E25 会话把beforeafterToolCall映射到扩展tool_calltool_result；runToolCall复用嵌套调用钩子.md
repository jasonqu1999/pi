---
source_file: "packages/coding-agent/src/core/agent-session.ts"
type: "rationale"
community: "Coding Agent 会话工具 29"
location: "_installAgentToolHooks, _beforeToolCall, _afterToolCall, _executeNestedToolCall"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Coding_Agent_会话工具_29
---

# E25 会话把before/afterToolCall映射到扩展tool_call/tool_result；runToolCall复用嵌套调用钩子

## Connections
- [[dot-_afterToolCall()]] - `references` [EXTRACTED]
- [[dot-_beforeToolCall()]] - `references` [EXTRACTED]
- [[dot-_executeNestedToolCall()]] - `references` [EXTRACTED]
- [[dot-_installAgentToolHooks()]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Coding_Agent_会话工具_29

## 源码入口

[packages/coding-agent/src/core/agent-session.ts](../../../packages/coding-agent/src/core/agent-session.ts)
