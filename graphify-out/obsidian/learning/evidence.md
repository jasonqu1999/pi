<!-- Derived from graphify-out/evidence.md; edit the Markdown source and re-export. -->

# 论断与证据

版本 `cd32f7725fdbddbaecdff5b1e68491563394e0ca`。源码确认是局部静态阅读；测试只表达作者预期，全部未运行。源码导航使用文件/符号，不依赖行号。

## E01

包职责和workspace直接运行依赖由各包manifest记录；包版本均1.0.2

- 类别：`structure_extracted`；条件：各包manifest；运行依赖不含开发依赖
- 源码：[packages/coding-agent/package.json](../../../packages/coding-agent/package.json)
- 符号：`name`, `dependencies`
- 图节点：`packages_coding_agent_package_dependencies`, `packages_coding_agent_package_name`

## E02

CLI组合cwd服务、SessionManager和会话runtime，再按模式分派

- 类别：`source_confirmed`；条件：普通CLI interactive模式；auth/help/package命令可提前返回
- 源码：[packages/coding-agent/src/main.ts](../../../packages/coding-agent/src/main.ts)
- 符号：`main`, `createAgentSessionRuntime`, `createAgentSessionFromServices`
- 图节点：`packages_coding_agent_src_main_main`

## E03

普通编辑器输入经getUserInput进入session.prompt；UI通过会话subscribe消费事件

- 类别：`source_confirmed`；条件：普通文本；命令/streaming/compaction分流另有条件
- 源码：[packages/coding-agent/src/modes/interactive/interactive-mode.ts](../../../packages/coding-agent/src/modes/interactive/interactive-mode.ts)
- 符号：`setupEditorSubmitHandler`, `getUserInput`, `subscribeToAgent`, `handleEvent`
- 图节点：`packages_coding_agent_src_modes_interactive_interactive_mode_interactivemode_getuserinput`, `packages_coding_agent_src_modes_interactive_interactive_mode_interactivemode_handleevent`, `packages_coding_agent_src_modes_interactive_interactive_mode_interactivemode_setupeditorsubmithandler`, `packages_coding_agent_src_modes_interactive_interactive_mode_interactivemode_subscribetoagent`

## E04

SDK用已有投影创建Agent并注入转换/streamFn，然后创建AgentSession

- 类别：`source_confirmed`；条件：SDK路径；初始tools为空，后由会话装载
- 源码：[packages/coding-agent/src/core/sdk.ts](../../../packages/coding-agent/src/core/sdk.ts)
- 符号：`createAgentSession`, `convertToLlmWithBlockImages`, `new Agent`, `new AgentSession`
- 图节点：`packages_coding_agent_src_core_sdk_createagentsession`

## E05

Agent.prompt创建运行生命周期、上下文快照与loop配置并调用runAgentLoop

- 类别：`source_confirmed`；条件：非activeRun；消息规范化后执行
- 源码：[packages/agent/src/agent.ts](../../../packages/agent/src/agent.ts)
- 符号：`prompt`, `runPromptMessages`, `createContextSnapshot`, `createLoopConfig`
- 图节点：`packages_agent_src_agent_agent_createcontextsnapshot`, `packages_agent_src_agent_agent_createloopconfig`, `packages_agent_src_agent_agent_prompt`, `packages_agent_src_agent_agent_runpromptmessages`

## E06

loop工作消息数组与Agent顶层数组分离，消息对象可共享

- 类别：`source_confirmed`；条件：浅拷贝不是深拷贝；低层loop也复制初始数组
- 源码：[packages/agent/src/agent.ts](../../../packages/agent/src/agent.ts)
- 符号：`createContextSnapshot`, `messages.slice`
- 图节点：`packages_agent_src_agent_agent_createcontextsnapshot`

## E07

Agent.processEvents先归约完成消息/partial/待执行调用状态，再顺序await订阅者

- 类别：`source_confirmed`；条件：Agent订阅者与会话公开_emit不同
- 源码：[packages/agent/src/agent.ts](../../../packages/agent/src/agent.ts)
- 符号：`processEvents`, `case "message_end"`, `await listener`
- 图节点：`packages_agent_src_agent_agent_processevents`

## E08

请求前从SessionManager投影构建canonicalContext；投影按leaf/压缩/context_edit生成

- 类别：`source_confirmed`；条件：默认应用投影；previousPrepareRequest还能返回替换
- 源码：[packages/coding-agent/src/core/agent-session.ts](../../../packages/coding-agent/src/core/agent-session.ts)
- 符号：`_installAgentRequestProjection`, `buildSessionProjection`, `canonicalContext`
- 图节点：`packages_coding_agent_src_core_agent_session_agentsession_installagentrequestprojection`

## E09

transformContext→convertToLlm→normalizeContext→streamFunction构成模型边界

- 类别：`source_confirmed`；条件：normalize只给messages时不另加leading system；协议随后仍可转换
- 源码：[packages/agent/src/agent-loop.ts](../../../packages/agent/src/agent-loop.ts)
- 符号：`streamAssistantResponse`, `transformContext`, `convertToLlm`, `normalizeContext`
- 图节点：`packages_agent_src_agent_loop_streamassistantresponse`

## E10

会话prompt处理输入/模板/认证与消息构造，应用工具及system sections后进入_runAgentPrompt

- 类别：`source_confirmed`；条件：非streaming普通输入；扩展可handled/transform
- 源码：[packages/coding-agent/src/core/agent-session.ts](../../../packages/coding-agent/src/core/agent-session.ts)
- 符号：`prompt`, `_runInputHandlers`, `_preparePromptAndToolLoadout`, `_runAgentPrompt`
- 图节点：`packages_coding_agent_src_core_agent_session_agentsession_preparepromptandtoolloadout`, `packages_coding_agent_src_core_agent_session_agentsession_prompt`, `packages_coding_agent_src_core_agent_session_agentsession_runagentprompt`, `packages_coding_agent_src_core_agent_session_agentsession_runinputhandlers`

## E11

declareToolChanges比较transcript声明与可执行tools，合并pending system或插入delta

- 类别：`source_confirmed`；条件：变化为空不添加声明；工具定义剥离execute字段
- 源码：[packages/agent/src/agent-loop.ts](../../../packages/agent/src/agent-loop.ts)
- 符号：`declareToolChanges`, `getToolStateChanges`, `withToolChanges`
- 图节点：`packages_agent_src_agent_loop_declaretoolchanges`, `packages_agent_src_agent_loop_withtoolchanges`

## E12

stream start/delta/final在循环上下文形成partial和最终assistant，发消息事件

- 类别：`source_confirmed`；条件：provider stream遵循事件/result契约；结束没有start也会补message_start
- 源码：[packages/agent/src/agent-loop.ts](../../../packages/agent/src/agent-loop.ts)
- 符号：`streamAssistantResponse`, `case "start"`, `case "done"`, `message_end`
- 图节点：`packages_agent_src_agent_loop_streamassistantresponse`

## E13

工具执行按配置/工具executionMode选并行或顺序；查找/准备/校验/前钩子/执行/后钩子

- 类别：`source_confirmed`；条件：unknown/invalid/block走immediate；并行结果按源调用序提交
- 源码：[packages/agent/src/agent-loop.ts](../../../packages/agent/src/agent-loop.ts)
- 符号：`executeToolCalls`, `prepareToolCall`, `executePreparedToolCall`, `finalizeExecutedToolCall`
- 图节点：`packages_agent_src_agent_loop_executepreparedtoolcall`, `packages_agent_src_agent_loop_executetoolcalls`, `packages_agent_src_agent_loop_finalizeexecutedtoolcall`, `packages_agent_src_agent_loop_preparetoolcall`

## E14

read解析cwd路径、检查可读性、读Buffer转UTF8并应用offset/limit/截断；默认ops为本地fs

- 类别：`source_confirmed`；条件：小Markdown文本、非图片；自定义ReadOperations可替换
- 源码：[packages/coding-agent/src/core/tools/read.ts](../../../packages/coding-agent/src/core/tools/read.ts)
- 符号：`createReadToolDefinition`, `defaultReadOperations`, `ops.access`, `ops.readFile`
- 图节点：`packages_coding_agent_src_core_tools_read_createreadtooldefinition`, `packages_coding_agent_src_core_tools_read_defaultreadoperations`

## E15

runLoop回填工具结果，finishTurn及队列决定内外循环继续或agent_end

- 类别：`source_confirmed`；条件：工具批次全部terminate影响自然续轮，finishTurn:end提前退出
- 源码：[packages/agent/src/agent-loop.ts](../../../packages/agent/src/agent-loop.ts)
- 符号：`runLoop`, `currentContext.messages.push(result)`, `getFollowUpMessages`, `shouldTerminateToolBatch`
- 图节点：`packages_agent_src_agent_loop_runloop`, `packages_agent_src_agent_loop_shouldterminatetoolbatch`

## E16

length响应的所有toolCall不执行而生成错误结果，error/aborted响应直接结束低层

- 类别：`source_confirmed`；条件：错误结果仍可引发下一轮；模型error出口不执行工具
- 源码：[packages/agent/src/agent-loop.ts](../../../packages/agent/src/agent-loop.ts)
- 符号：`failToolCallsFromTruncatedMessage`, `message.stopReason === "length"`, `message.stopReason === "error"`
- 图节点：`packages_agent_src_agent_loop_failtoolcallsfromtruncatedmessage`

## E17

会话先扩展/公开通知，再于message_end追加普通消息条目；turn_end刷新pending自定义消息

- 类别：`source_confirmed`；条件：普通system/user/assistant/toolResult；其他role有单独持久化路径
- 源码：[packages/coding-agent/src/core/agent-session.ts](../../../packages/coding-agent/src/core/agent-session.ts)
- 符号：`_handleAgentEvent`, `appendMessage(event.message)`, `_emit(event`
- 图节点：`packages_coding_agent_src_core_agent_session_agentsession_handleagentevent`

## E18

执行错误catch→错误结果；后钩子可改结果；toolResult携带调用id、content与isError

- 类别：`source_confirmed`；条件：after钩子未改写时保留错误；undefined content正规化为[]
- 源码：[packages/agent/src/agent-loop.ts](../../../packages/agent/src/agent-loop.ts)
- 符号：`executePreparedToolCall`, `createErrorToolResult`, `createToolResultMessage`
- 图节点：`packages_agent_src_agent_loop_createerrortoolresult`, `packages_agent_src_agent_loop_createtoolresultmessage`, `packages_agent_src_agent_loop_executepreparedtoolcall`

## E19

轮间刷新先压缩/投影，再更新工具装载与system sections；请求前还可重建canonical投影

- 类别：`source_confirmed`；条件：主链只核对接入点；压缩算法未完整审计
- 源码：[packages/coding-agent/src/core/agent-session.ts](../../../packages/coding-agent/src/core/agent-session.ts)
- 符号：`_installAgentNextTurnRefresh`, `_compactBeforeNextAssistantResponse`, `_preparePromptAndToolLoadout`
- 图节点：`packages_coding_agent_src_core_agent_session_agentsession_compactbeforenextassistantresponse`, `packages_coding_agent_src_core_agent_session_agentsession_installagentnextturnrefresh`, `packages_coding_agent_src_core_agent_session_agentsession_preparepromptandtoolloadout`

## E20

agent_end监听者结算后finishRun才清activeRun；run异常有合成失败消息兜底

- 类别：`source_confirmed`；条件：监听者再次抛错的复杂恢复未展开
- 源码：[packages/agent/src/agent.ts](../../../packages/agent/src/agent.ts)
- 符号：`runWithLifecycle`, `handleRunFailure`, `finishRun`, `waitForIdle`
- 图节点：`packages_agent_src_agent_agent_finishrun`, `packages_agent_src_agent_agent_handlerunfailure`, `packages_agent_src_agent_agent_runwithlifecycle`, `packages_agent_src_agent_agent_waitforidle`

## E21

_runAgentPrompt可在低层结束后重试/恢复/消费新队列/收束钩子再continue，finally发agent_settled

- 类别：`source_confirmed`；条件：一次会话活动可能含多个低层run；交互进程仍可等待新输入
- 源码：[packages/coding-agent/src/core/agent-session.ts](../../../packages/coding-agent/src/core/agent-session.ts)
- 符号：`_runAgentPrompt`, `_handlePostAgentRun`, `_runBeforeSettleBoundary`, `_emitAgentSettled`
- 图节点：`packages_coding_agent_src_core_agent_session_agentsession_emitagentsettled`, `packages_coding_agent_src_core_agent_session_agentsession_handlepostagentrun`, `packages_coding_agent_src_core_agent_session_agentsession_runagentprompt`, `packages_coding_agent_src_core_agent_session_agentsession_runbeforesettleboundary`

## E22

自动重试按可重试模型错误/预算决定，保留原始失败尝试但省略其模型投影

- 类别：`source_confirmed`；条件：非toolResult错误；overflow由压缩恢复处理；未运行验证
- 源码：[packages/coding-agent/src/core/agent-session.ts](../../../packages/coding-agent/src/core/agent-session.ts)
- 符号：`_prepareRetry`, `_isRetryableError`, `_omitRecoveryAttempt`
- 图节点：`packages_coding_agent_src_core_agent_session_agentsession_isretryableerror`, `packages_coding_agent_src_core_agent_session_agentsession_omitrecoveryattempt`, `packages_coding_agent_src_core_agent_session_agentsession_prepareretry`

## E23

appendMessage推进树leaf，persist开启且有sessionFile时按会话首次user/assistant触发创建/追加

- 类别：`source_confirmed`；条件：in-memory不写；setup条目不单独触发文件创建；未观测磁盘行为
- 源码：[packages/coding-agent/src/core/session-manager.ts](../../../packages/coding-agent/src/core/session-manager.ts)
- 符号：`appendMessage`, `_appendEntry`, `_hasConversation`, `_persist`
- 图节点：`packages_coding_agent_src_core_session_manager_sessionmanager_appendentry`, `packages_coding_agent_src_core_session_manager_sessionmanager_appendmessage`, `packages_coding_agent_src_core_session_manager_sessionmanager_hasconversation`, `packages_coding_agent_src_core_session_manager_sessionmanager_persist`

## E24

会话abort取消重试/压缩/摘要并发Agent signal，等待会话idle

- 类别：`source_confirmed`；条件：协作取消；不保证撤销底层I/O副作用
- 源码：[packages/coding-agent/src/core/agent-session.ts](../../../packages/coding-agent/src/core/agent-session.ts)
- 符号：`abort`, `abortRetry`, `abortCompaction`, `waitForIdle`
- 图节点：`packages_coding_agent_src_core_agent_session_agentsession_abort`, `packages_coding_agent_src_core_agent_session_agentsession_abortcompaction`, `packages_coding_agent_src_core_agent_session_agentsession_abortretry`, `packages_coding_agent_src_core_agent_session_agentsession_waitforidle`

## E25

会话把before/afterToolCall映射到扩展tool_call/tool_result；runToolCall复用嵌套调用钩子

- 类别：`source_confirmed`；条件：只说明候选审批接缝；没有实现审批策略
- 源码：[packages/coding-agent/src/core/agent-session.ts](../../../packages/coding-agent/src/core/agent-session.ts)
- 符号：`_installAgentToolHooks`, `_beforeToolCall`, `_afterToolCall`, `_executeNestedToolCall`
- 图节点：`packages_coding_agent_src_core_agent_session_agentsession_aftertoolcall`, `packages_coding_agent_src_core_agent_session_agentsession_beforetoolcall`, `packages_coding_agent_src_core_agent_session_agentsession_executenestedtoolcall`, `packages_coding_agent_src_core_agent_session_agentsession_installagenttoolhooks`

## E26

SDK注入ModelRuntime.streamSimple，runtime分派到provider API，transcript由协议适配继续转换

- 类别：`source_confirmed`；条件：具体provider协议/网络载荷未验证；认证、payload钩子可继续变换
- 源码：[packages/coding-agent/src/core/model-runtime.ts](../../../packages/coding-agent/src/core/model-runtime.ts)
- 符号：`streamSimple`, `prepared.provider.streamSimple`, `normalizeContext`
- 图节点：`packages_coding_agent_src_core_model_runtime_modelruntime_streamsimple`

## E27

SessionManager从原始树、compaction与context_edit生成保留sourceEntry的投影

- 类别：`source_confirmed`；条件：当前leaf；原始记录和模型投影不同
- 源码：[packages/coding-agent/src/core/session-manager.ts](../../../packages/coding-agent/src/core/session-manager.ts)
- 符号：`buildSessionProjection`, `buildContextEntries`, `projectContextEntry`
- 图节点：`packages_coding_agent_src_core_session_manager_buildcontextentries`, `packages_coding_agent_src_core_session_manager_buildsessionprojection`, `packages_coding_agent_src_core_session_manager_projectcontextentry`, `packages_coding_agent_src_core_session_manager_sessionmanager_buildcontextentries`, `packages_coding_agent_src_core_session_manager_sessionmanager_buildsessionprojection`

## E28

工具声明可重放增删delta，normalizeContext仅在外部systemPrompt/tools非空时添加leading message

- 类别：`source_confirmed`；条件：此主链transcript已带声明，传入仅messages
- 源码：[packages/ai/src/utils/transcript.ts](../../../packages/ai/src/utils/transcript.ts)
- 符号：`getCurrentTools`, `normalizeContext`, `toToolDeclaration`
- 图节点：`packages_ai_src_utils_transcript_getcurrenttools`, `packages_ai_src_utils_transcript_normalizecontext`, `packages_ai_src_utils_transcript_totooldeclaration`

## E29

ToolDefinition包装为AgentTool保留参数/执行模式，execute转发到定义并提供工具context

- 类别：`source_confirmed`；条件：ReadOperations可注入；渲染器字段不进入模型声明
- 源码：[packages/coding-agent/src/core/tools/tool-definition-wrapper.ts](../../../packages/coding-agent/src/core/tools/tool-definition-wrapper.ts)
- 符号：`wrapToolDefinition`, `definition.execute`
- 图节点：`packages_coding_agent_src_core_tools_tool_definition_wrapper_wraptooldefinition`

## T01

测试表达tool call→执行→toolResult→第二响应的预期

- 类别：`test_expected`；条件：只读未运行；测试使用echo与mock stream
- 源码：[packages/agent/test/agent-loop.test.ts](../../../packages/agent/test/agent-loop.test.ts)
- 符号：`should handle tool calls and results`
- 图节点：未获精确符号节点；使用文件/证据节点导航

## T02

read单元测试表达不存在文件execute拒绝ENOENT/not found的预期

- 类别：`test_expected`；条件：只读未运行
- 源码：[packages/coding-agent/test/tools.test.ts](../../../packages/coding-agent/test/tools.test.ts)
- 符号：`should handle non-existent files`
- 图节点：未获精确符号节点；使用文件/证据节点导航

## T03

测试表达并行执行结束按完成序、结果消息按源调用序的预期

- 类别：`test_expected`；条件：只读未运行
- 源码：[packages/agent/test/agent-loop.test.ts](../../../packages/agent/test/agent-loop.test.ts)
- 符号：`should emit tool_execution_end in completion order but persist tool results in source order`
- 图节点：未获精确符号节点；使用文件/证据节点导航

## T04

测试表达未知工具、非法参数、block返回isError的预期

- 类别：`test_expected`；条件：只读未运行
- 源码：[packages/agent/test/agent-loop.test.ts](../../../packages/agent/test/agent-loop.test.ts)
- 符号：`validates, runs the hooks, and reports failures as error outcomes`
- 图节点：未获精确符号节点；使用文件/证据节点导航

## T05

测试表达prompt/waitForIdle等待异步订阅者的预期

- 类别：`test_expected`；条件：只读未运行
- 源码：[packages/agent/test/agent.test.ts](../../../packages/agent/test/agent.test.ts)
- 符号：`should await async subscribers before prompt resolves`, `waitForIdle should wait for async subscribers`
- 图节点：未获精确符号节点；使用文件/证据节点导航

## T06

回归测试表达重试/agent_end新followUp可有多个agent_end且一个agent_settled的预期

- 类别：`test_expected`；条件：只读未运行
- 源码：[packages/coding-agent/test/suite/regressions/6363-agent-settled-event.test.ts](../../../packages/coding-agent/test/suite/regressions/6363-agent-settled-event.test.ts)
- 符号：`emits one agent_settled event after automatic retry finishes`, `settles only after follow-ups queued by agent_end handlers run`
- 图节点：未获精确符号节点；使用文件/证据节点导航

## T07

测试表达length截断调用不执行且产生下一请求的预期

- 类别：`test_expected`；条件：只读未运行
- 源码：[packages/agent/test/agent-loop.test.ts](../../../packages/agent/test/agent-loop.test.ts)
- 符号：`should not execute tool calls from a length-truncated assistant message`
- 图节点：未获精确符号节点；使用文件/证据节点导航

## I01

streamFn注入为独立嵌入和可控测试提供接缝，代价是应用需保持上下文与生命周期契约

- 类别：`semantic_inference`；条件：根据包边界、SDK注入与测试写法分析，设计动机未获作者确认
- 源码：[packages/coding-agent/src/core/sdk.ts](../../../packages/coding-agent/src/core/sdk.ts)
- 符号：`createAgentSession`, `streamFn`
- 图节点：`packages_coding_agent_src_core_sdk_createagentsession`

## I02

原始记录和请求投影分离有利于保留审计历史，同时需要维护者识别修改层级

- 类别：`semantic_inference`；条件：根据projection及retry省略失败记录推断，非作者动机陈述
- 源码：[packages/coding-agent/src/core/session-manager.ts](../../../packages/coding-agent/src/core/session-manager.ts)
- 符号：`buildSessionProjection`, `sourceEntry`
- 图节点：`packages_coding_agent_src_core_session_manager_buildsessionprojection`, `packages_coding_agent_src_core_session_manager_sessionmanager_buildsessionprojection`
