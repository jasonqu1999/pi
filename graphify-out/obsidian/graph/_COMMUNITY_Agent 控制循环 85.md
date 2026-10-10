---
type: community
cohesion: 0.06
members: 63
---

# Agent 控制循环 85

**Cohesion:** 0.06 - loosely connected
**Members:** 63 nodes

## Members
- [[AgentEventSink]] - code - packages/agent/src/agent-loop.ts
- [[E09 transformContext→convertToLlm→normalizeContext→streamFunction构成模型边界]] - rationale - packages/agent/src/agent-loop.ts
- [[E11 declareToolChanges比较transcript声明与可执行tools，合并pending system或插入delta]] - rationale - packages/agent/src/agent-loop.ts
- [[E12 stream startdeltafinal在循环上下文形成partial和最终assistant，发消息事件]] - rationale - packages/agent/src/agent-loop.ts
- [[E13 工具执行按配置工具executionMode选并行或顺序；查找准备校验前钩子执行后钩子]] - rationale - packages/agent/src/agent-loop.ts
- [[E15 runLoop回填工具结果，finishTurn及队列决定内外循环继续或agent_end]] - rationale - packages/agent/src/agent-loop.ts
- [[E16 length响应的所有toolCall不执行而生成错误结果，erroraborted响应直接结束低层]] - rationale - packages/agent/src/agent-loop.ts
- [[E18 执行错误catch→错误结果；后钩子可改结果；toolResult携带调用id、content与isError]] - rationale - packages/agent/src/agent-loop.ts
- [[ExecutedToolCallBatch]] - code - packages/agent/src/agent-loop.ts
- [[ExecutedToolCallOutcome]] - code - packages/agent/src/agent-loop.ts
- [[FinalizedToolCallEntry]] - code - packages/agent/src/agent-loop.ts
- [[FinalizedToolCallOutcome]] - code - packages/agent/src/agent-loop.ts
- [[ImmediateToolCallOutcome]] - code - packages/agent/src/agent-loop.ts
- [[JsonSchemaObject_1]] - code - packages/ai/src/utils/validation.ts
- [[NO_CHANGES]] - code - packages/agent/src/agent-loop.ts
- [[PreparedToolCall]] - code - packages/agent/src/agent-loop.ts
- [[RunToolCallOptions]] - code - packages/agent/src/agent-loop.ts
- [[TYPEBOX_KIND]] - code - packages/ai/src/utils/validation.ts
- [[ToolCallHooks]] - code - packages/agent/src/agent-loop.ts
- [[ToolUpdateSink]] - code - packages/agent/src/agent-loop.ts
- [[agent-loop.ts]] - code - packages/agent/src/agent-loop.ts
- [[agentLoop()]] - code - packages/agent/src/agent-loop.ts
- [[agentLoopContinue()]] - code - packages/agent/src/agent-loop.ts
- [[applySchemaArrayCoercion()]] - code - packages/ai/src/utils/validation.ts
- [[applySchemaObjectCoercion()]] - code - packages/ai/src/utils/validation.ts
- [[coercePrimitiveByType()]] - code - packages/ai/src/utils/validation.ts
- [[coerceWithJsonSchema()]] - code - packages/ai/src/utils/validation.ts
- [[coerceWithUnionSchema()]] - code - packages/ai/src/utils/validation.ts
- [[createAgentStream()]] - code - packages/agent/src/agent-loop.ts
- [[createErrorToolResult()]] - code - packages/agent/src/agent-loop.ts
- [[createToolResultMessage()]] - code - packages/agent/src/agent-loop.ts
- [[declareToolChanges()]] - code - packages/agent/src/agent-loop.ts
- [[emitToolExecutionEnd()]] - code - packages/agent/src/agent-loop.ts
- [[emitToolExecutionUpdate()]] - code - packages/agent/src/agent-loop.ts
- [[emitToolResultMessage()]] - code - packages/agent/src/agent-loop.ts
- [[executePreparedToolCall()]] - code - packages/agent/src/agent-loop.ts
- [[executeToolCalls()]] - code - packages/agent/src/agent-loop.ts
- [[executeToolCallsParallel()]] - code - packages/agent/src/agent-loop.ts
- [[executeToolCallsSequential()]] - code - packages/agent/src/agent-loop.ts
- [[failToolCallsFromTruncatedMessage()]] - code - packages/agent/src/agent-loop.ts
- [[finalizeExecutedToolCall()]] - code - packages/agent/src/agent-loop.ts
- [[formatValidationPath()]] - code - packages/ai/src/utils/validation.ts
- [[getSchemaTypes()]] - code - packages/ai/src/utils/validation.ts
- [[getSubSchemaValidator()]] - code - packages/ai/src/utils/validation.ts
- [[getValidator()]] - code - packages/ai/src/utils/validation.ts
- [[matchesJsonType()]] - code - packages/ai/src/utils/validation.ts
- [[normalizeOptionalNulls()]] - code - packages/ai/src/utils/validation.ts
- [[packages_ai_src_index_gettoolstatechanges]] - concept
- [[packages_ai_src_index_toolstatechanges]] - concept
- [[packages_ai_src_index_totooldeclaration]] - concept
- [[packages_ai_src_index_validatetoolarguments]] - concept
- [[prepareToolCall()]] - code - packages/agent/src/agent-loop.ts
- [[prepareToolCallArguments()]] - code - packages/agent/src/agent-loop.ts
- [[ref_typebox_error]] - concept
- [[runLoop()]] - code - packages/agent/src/agent-loop.ts
- [[runToolCall()]] - code - packages/agent/src/agent-loop.ts
- [[shouldTerminateToolBatch()]] - code - packages/agent/src/agent-loop.ts
- [[streamAssistantResponse()]] - code - packages/agent/src/agent-loop.ts
- [[validateToolArguments()]] - code - packages/ai/src/utils/validation.ts
- [[validateToolCall()]] - code - packages/ai/src/utils/validation.ts
- [[validation.ts]] - code - packages/ai/src/utils/validation.ts
- [[validatorCache]] - code - packages/ai/src/utils/validation.ts
- [[withToolChanges()]] - code - packages/agent/src/agent-loop.ts

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Agent_控制循环_85
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_Coding Agent 会话工具 27]]
- 10 edges to [[_COMMUNITY_Coding Agent 会话工具 7]]
- 9 edges to [[_COMMUNITY_AI 模型协议 44]]
- 6 edges to [[_COMMUNITY_Agent 控制循环 82]]
- 4 edges to [[_COMMUNITY_Durable 持久任务 0]]
- 4 edges to [[_COMMUNITY_AI 模型协议 1]]
- 3 edges to [[_COMMUNITY_Coding Agent 会话工具 15]]
- 3 edges to [[_COMMUNITY_Durable 持久任务 21]]
- 1 edge to [[_COMMUNITY_MCP 远端工具 96]]
- 1 edge to [[_COMMUNITY_AI 模型协议 25]]
- 1 edge to [[_COMMUNITY_Coding Agent 会话工具 33]]
- 1 edge to [[_COMMUNITY_Coding Agent 会话工具 19]]
- 1 edge to [[_COMMUNITY_Coding Agent 会话工具 29]]
- 1 edge to [[_COMMUNITY_Coding Agent 会话工具 43]]
- 1 edge to [[_COMMUNITY_AI 模型协议 22]]

## Top bridge nodes
- [[agent-loop.ts]] - degree 73, connects to 7 communities
- [[validation.ts]] - degree 26, connects to 4 communities
- [[RunToolCallOptions]] - degree 5, connects to 3 communities
- [[declareToolChanges()]] - degree 8, connects to 1 community
- [[streamAssistantResponse()]] - degree 5, connects to 1 community