---
type: community
cohesion: 0.04
members: 67
---

# Agent 控制循环 82

**Cohesion:** 0.04 - loosely connected
**Members:** 67 nodes

## Members
- [[dot-constructor()_2]] - code - packages/agent/src/proxy.ts
- [[dot-constructor()_3]] - code - packages/agent/test/agent-loop.test.ts
- [[@earendil-workspi-agent-core_6]] - concept - packages/agent/package.json
- [[CLIENT_ID_2]] - code - packages/coding-agent/examples/extensions/custom-provider-anthropic/index.ts
- [[CalculateParams]] - code - packages/agent/test/utils/calculate.ts
- [[CalculateResult]] - code - packages/agent/test/utils/calculate.ts
- [[CustomMessage]] - code - packages/agent/test/agent-loop.test.ts
- [[CustomNotification]] - code - packages/agent/test/agent-loop.test.ts
- [[MockAssistantStream]] - code - packages/agent/test/agent-loop.test.ts
- [[ProxyAssistantMessageEvent]] - code - packages/agent/src/proxy.ts
- [[ProxyMessageEventStream]] - code - packages/agent/src/proxy.ts
- [[ProxySerializableStreamOptions]] - code - packages/agent/src/proxy.ts
- [[ProxyStreamOptions]] - code - packages/agent/src/proxy.ts
- [[T01 测试表达tool call→执行→toolResult→第二响应的预期]] - rationale - packages/agent/test/agent-loop.test.ts
- [[T03 测试表达并行执行结束按完成序、结果消息按源调用序的预期]] - rationale - packages/agent/test/agent-loop.test.ts
- [[T04 测试表达未知工具、非法参数、block返回isError的预期]] - rationale - packages/agent/test/agent-loop.test.ts
- [[T07 测试表达length截断调用不执行且产生下一请求的预期]] - rationale - packages/agent/test/agent-loop.test.ts
- [[agent-loop.test.ts]] - code - packages/agent/test/agent-loop.test.ts
- [[agentvitest.config.ts]] - code - packages/agent/vitest.config.ts
- [[agentSrcIndex]] - code - packages/agent/vitest.config.ts
- [[aiSrcCompat]] - code - packages/agent/vitest.config.ts
- [[aiSrcIndex]] - code - packages/agent/vitest.config.ts
- [[buildProxyRequestOptions()]] - code - packages/agent/src/proxy.ts
- [[calculate()]] - code - packages/agent/test/utils/calculate.ts
- [[calculate.ts]] - code - packages/agent/test/utils/calculate.ts
- [[calculateSchema]] - code - packages/agent/test/utils/calculate.ts
- [[calculateTool]] - code - packages/agent/test/utils/calculate.ts
- [[ccToolLookup_1]] - code - packages/coding-agent/examples/extensions/custom-provider-anthropic/index.ts
- [[claudeCodeTools_1]] - code - packages/coding-agent/examples/extensions/custom-provider-anthropic/index.ts
- [[convertContentBlocks()_1]] - code - packages/coding-agent/examples/extensions/custom-provider-anthropic/index.ts
- [[convertMessages()_4]] - code - packages/coding-agent/examples/extensions/custom-provider-anthropic/index.ts
- [[convertTools()_3]] - code - packages/coding-agent/examples/extensions/custom-provider-anthropic/index.ts
- [[createAssistantMessage()]] - code - packages/agent/test/agent-loop.test.ts
- [[createCalculateToolWithUsage()]] - code - packages/agent/test/utils/calculate.ts
- [[createModel()]] - code - packages/agent/test/agent-loop.test.ts
- [[createUsage()]] - code - packages/agent/test/agent-loop.test.ts
- [[createUserMessage()]] - code - packages/agent/test/agent-loop.test.ts
- [[custom-provider-anthropicindex.ts]] - code - packages/coding-agent/examples/extensions/custom-provider-anthropic/index.ts
- [[decode()_2]] - code - packages/coding-agent/examples/extensions/custom-provider-anthropic/index.ts
- [[execute()]] - code - packages/agent/test/agent-loop.test.ts
- [[fromClaudeCodeName()_1]] - code - packages/coding-agent/examples/extensions/custom-provider-anthropic/index.ts
- [[identityConverter()]] - code - packages/agent/test/agent-loop.test.ts
- [[isOAuthToken()_1]] - code - packages/coding-agent/examples/extensions/custom-provider-anthropic/index.ts
- [[mapStopReason()_5]] - code - packages/coding-agent/examples/extensions/custom-provider-anthropic/index.ts
- [[model_1]] - code - packages/agent/test/proxy.test.ts
- [[packages_ai_src_index_assistantmessageevent]] - concept
- [[packages_ai_src_index_calculatecost]] - concept
- [[packages_ai_src_index_collapsesystemmessages]] - concept
- [[packages_ai_src_index_eventstream]] - concept
- [[packages_ai_src_index_oauthcredentials]] - concept
- [[packages_ai_src_index_parsestreamingjson]] - concept
- [[packages_ai_src_index_stopreason]] - concept
- [[packages_ai_src_index_thinkingcontent]] - concept
- [[prepareArguments()]] - code - packages/agent/test/agent-loop.test.ts
- [[processProxyEvent()]] - code - packages/agent/src/proxy.ts
- [[proxy.test.ts]] - code - packages/agent/test/proxy.test.ts
- [[proxy.ts]] - code - packages/agent/src/proxy.ts
- [[refreshAnthropicToken()_1]] - code - packages/coding-agent/examples/extensions/custom-provider-anthropic/index.ts
- [[sanitizeSurrogates()_1]] - code - packages/coding-agent/examples/extensions/custom-provider-anthropic/index.ts
- [[setDefaultStreamFn()]] - code - packages/agent/src/stream-fn.ts
- [[streamCustomAnthropic()]] - code - packages/coding-agent/examples/extensions/custom-provider-anthropic/index.ts
- [[streamProxy()]] - code - packages/agent/src/proxy.ts
- [[telemetrySrcIndex]] - code - packages/agent/vitest.config.ts
- [[toClaudeCodeName()_1]] - code - packages/coding-agent/examples/extensions/custom-provider-anthropic/index.ts
- [[usage]] - code - packages/agent/test/proxy.test.ts
- [[wait-for-tick.ts]] - code - packages/agent/test/utils/wait-for-tick.ts
- [[waitForTick()]] - code - packages/agent/test/utils/wait-for-tick.ts

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Agent_控制循环_82
SORT file.name ASC
```

## Connections to other communities
- 26 edges to [[_COMMUNITY_Coding Agent 会话工具 7]]
- 26 edges to [[_COMMUNITY_Coding Agent 会话工具 15]]
- 20 edges to [[_COMMUNITY_Coding Agent 会话工具 27]]
- 10 edges to [[_COMMUNITY_AI 模型协议 44]]
- 8 edges to [[_COMMUNITY_Durable 持久任务 0]]
- 6 edges to [[_COMMUNITY_Agent 控制循环 85]]
- 6 edges to [[_COMMUNITY_AI 模型协议 1]]
- 5 edges to [[_COMMUNITY_Coding Agent 会话工具 12]]
- 4 edges to [[_COMMUNITY_AI 模型协议 54]]
- 4 edges to [[_COMMUNITY_Coding Agent 会话工具 11]]
- 4 edges to [[_COMMUNITY_Coding Agent 会话工具 2]]
- 3 edges to [[_COMMUNITY_Coding Agent 会话工具 165]]
- 3 edges to [[_COMMUNITY_Coding Agent 会话工具 40]]
- 2 edges to [[_COMMUNITY_Durable 持久任务 5]]
- 2 edges to [[_COMMUNITY_AI 模型协议 140]]
- 2 edges to [[_COMMUNITY_AI 模型协议 156]]
- 2 edges to [[_COMMUNITY_Coding Agent 会话工具 3]]
- 2 edges to [[_COMMUNITY_AI 模型协议 52]]
- 2 edges to [[_COMMUNITY_Coding Agent 会话工具 43]]
- 1 edge to [[_COMMUNITY_Coding Agent 会话工具 69]]
- 1 edge to [[_COMMUNITY_Coding Agent 会话工具 56]]
- 1 edge to [[_COMMUNITY_Coding Agent 会话工具 116]]
- 1 edge to [[_COMMUNITY_Durable 持久任务 21]]
- 1 edge to [[_COMMUNITY_Coding Agent 会话工具 24]]
- 1 edge to [[_COMMUNITY_Client 远程连接 14]]
- 1 edge to [[_COMMUNITY_Agent 控制循环 377]]
- 1 edge to [[_COMMUNITY_Agent 控制循环 277]]
- 1 edge to [[_COMMUNITY_MCP 远端工具 96]]
- 1 edge to [[_COMMUNITY_Agent 控制循环 139]]
- 1 edge to [[_COMMUNITY_Agent 控制循环 305]]
- 1 edge to [[_COMMUNITY_AI 模型协议 22]]

## Top bridge nodes
- [[custom-provider-anthropicindex.ts]] - degree 62, connects to 18 communities
- [[@earendil-workspi-agent-core_6]] - degree 22, connects to 10 communities
- [[proxy.ts]] - degree 29, connects to 9 communities
- [[agent-loop.test.ts]] - degree 44, connects to 8 communities
- [[proxy.test.ts]] - degree 17, connects to 5 communities