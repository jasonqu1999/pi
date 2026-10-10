---
source_file: "packages/coding-agent/src/modes/interactive/interactive-mode.ts"
type: "rationale"
community: "Coding Agent 会话工具 143"
location: "setupEditorSubmitHandler, getUserInput, subscribeToAgent, handleEvent"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Coding_Agent_会话工具_143
---

# E03 普通编辑器输入经getUserInput进入session.prompt；UI通过会话subscribe消费事件

## Connections
- [[dot-getUserInput()]] - `references` [EXTRACTED]
- [[dot-handleEvent()]] - `references` [EXTRACTED]
- [[dot-setupEditorSubmitHandler()]] - `references` [EXTRACTED]
- [[dot-subscribeToAgent()]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Coding_Agent_会话工具_143

## 源码入口

[packages/coding-agent/src/modes/interactive/interactive-mode.ts](../../../packages/coding-agent/src/modes/interactive/interactive-mode.ts)
