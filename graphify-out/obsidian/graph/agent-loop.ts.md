---
source_file: "packages/agent/src/agent-loop.ts"
type: "code"
community: "Agent 控制循环 85"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Agent_控制循环_85
---

# agent-loop.ts

## Connections
- [[AgentContext]] - `imports` [EXTRACTED]
- [[AgentEvent]] - `imports` [EXTRACTED]
- [[AgentEventSink]] - `contains` [EXTRACTED]
- [[AgentLoopConfig]] - `imports` [EXTRACTED]
- [[AgentMessage]] - `imports` [EXTRACTED]
- [[AgentTool]] - `imports` [EXTRACTED]
- [[AgentToolCall]] - `imports` [EXTRACTED]
- [[AgentToolCallOutcome]] - `imports` [EXTRACTED]
- [[AgentToolResult]] - `imports` [EXTRACTED]
- [[AssistantMessage]] - `imports` [EXTRACTED]
- [[EventStream]] - `imports` [EXTRACTED]
- [[ExecutedToolCallBatch]] - `contains` [EXTRACTED]
- [[ExecutedToolCallOutcome]] - `contains` [EXTRACTED]
- [[FinalizedToolCallEntry]] - `contains` [EXTRACTED]
- [[FinalizedToolCallOutcome]] - `contains` [EXTRACTED]
- [[ImmediateToolCallOutcome]] - `contains` [EXTRACTED]
- [[NO_CHANGES]] - `contains` [EXTRACTED]
- [[PrepareNextTurnContext]] - `imports` [EXTRACTED]
- [[PreparedToolCall]] - `contains` [EXTRACTED]
- [[RunToolCallOptions]] - `contains` [EXTRACTED]
- [[StreamFn]] - `imports` [EXTRACTED]
- [[SystemMessage]] - `imports` [EXTRACTED]
- [[ToolCallHooks]] - `contains` [EXTRACTED]
- [[ToolResultMessage]] - `imports` [EXTRACTED]
- [[ToolStateChanges]] - `imports` [EXTRACTED]
- [[ToolUpdateSink]] - `contains` [EXTRACTED]
- [[agentsrctypes.ts]] - `imports_from` [EXTRACTED]
- [[agentLoop()]] - `contains` [EXTRACTED]
- [[agentLoopContinue()]] - `contains` [EXTRACTED]
- [[aisrcindex.ts]] - `imports_from` [EXTRACTED]
- [[createAgentStream()]] - `contains` [EXTRACTED]
- [[createErrorToolResult()]] - `contains` [EXTRACTED]
- [[createToolResultMessage()]] - `contains` [EXTRACTED]
- [[declareToolChanges()]] - `contains` [EXTRACTED]
- [[emitToolExecutionEnd()]] - `contains` [EXTRACTED]
- [[emitToolExecutionUpdate()]] - `contains` [EXTRACTED]
- [[emitToolResultMessage()]] - `contains` [EXTRACTED]
- [[executePreparedToolCall()]] - `contains` [EXTRACTED]
- [[executeToolCalls()]] - `contains` [EXTRACTED]
- [[executeToolCallsParallel()]] - `contains` [EXTRACTED]
- [[executeToolCallsSequential()]] - `contains` [EXTRACTED]
- [[failToolCallsFromTruncatedMessage()]] - `contains` [EXTRACTED]
- [[finalizeExecutedToolCall()]] - `contains` [EXTRACTED]
- [[getCurrentTools()]] - `imports` [EXTRACTED]
- [[getDefaultStreamFn()]] - `imports` [EXTRACTED]
- [[getToolStateChanges()]] - `imports` [EXTRACTED]
- [[normalizeContext()]] - `imports` [EXTRACTED]
- [[packages_ai_src_index_assistantmessage]] - `imports` [EXTRACTED]
- [[packages_ai_src_index_eventstream]] - `imports` [EXTRACTED]
- [[packages_ai_src_index_getcurrenttools]] - `imports` [EXTRACTED]
- [[packages_ai_src_index_gettoolstatechanges]] - `imports` [EXTRACTED]
- [[packages_ai_src_index_normalizecontext]] - `imports` [EXTRACTED]
- [[packages_ai_src_index_systemmessage]] - `imports` [EXTRACTED]
- [[packages_ai_src_index_toolresultmessage]] - `imports` [EXTRACTED]
- [[packages_ai_src_index_toolstatechanges]] - `imports` [EXTRACTED]
- [[packages_ai_src_index_totooldeclaration]] - `imports` [EXTRACTED]
- [[packages_ai_src_index_validatetoolarguments]] - `imports` [EXTRACTED]
- [[prepareToolCall()]] - `contains` [EXTRACTED]
- [[prepareToolCallArguments()]] - `contains` [EXTRACTED]
- [[runAgentLoop()]] - `contains` [EXTRACTED]
- [[runAgentLoopContinue()]] - `contains` [EXTRACTED]
- [[runLoop()]] - `contains` [EXTRACTED]
- [[runToolCall()]] - `contains` [EXTRACTED]
- [[shouldTerminateToolBatch()]] - `contains` [EXTRACTED]
- [[stream-fn.ts]] - `imports_from` [EXTRACTED]
- [[streamAssistantResponse()]] - `contains` [EXTRACTED]
- [[toToolDeclaration()]] - `imports` [EXTRACTED]
- [[validateToolArguments()]] - `imports` [EXTRACTED]
- [[withToolChanges()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Agent_控制循环_85

## 源码入口

[packages/agent/src/agent-loop.ts](../../../packages/agent/src/agent-loop.ts)
