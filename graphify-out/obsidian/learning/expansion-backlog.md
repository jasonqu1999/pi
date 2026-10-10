<!-- Derived from graphify-out/expansion-backlog.md; edit the Markdown source and re-export. -->

# 支线接入与后续问题

以下机制已保留职责与入口，未完整审计算法，未运行验证。状态和触发条件以 v1.0.2 源码入口为准。[E19](evidence.md#e19) [E21](evidence.md#e21) [E22](evidence.md#e22) [E25](evidence.md#e25)

| 支线 | 职责、触发点 | 状态所有者 / 接入位置 | 下一次要回答什么 |
|---|---|---|---|
| 上下文压缩 | 请求前或轮间阈值判断；post-run还处理overflow/length恢复 | AgentSession的compaction/恢复标记；SessionManager的compaction条目和projection；`_compactBeforeNextAssistantResponse`、`_checkCompaction`、`_runAutoCompaction` | 哪些消息被保留？摘要失败/取消时历史和projection如何变化？ |
| steering | 回答期间的新输入，轮间注入；准备下一轮期间也可再次取队列 | Agent的steeringQueue；会话另维护显示队列；`getSteeringMessages` / `_queueSteer` / `prepareNextTurn` | 一次取一条和all模式如何影响新输入顺序？为何工具批次中间不直接插入？ |
| follow-up | Agent原本会停时继续；agent_end handler排队的消息需要新run | Agent的followUpQueue；会话显示队列及post-run标记；`getFollowUpMessages`、`_handlePostAgentRun` | 和steering同时存在时谁先被取出？ |
| 自动重试 | 可重试模型错误、有预算、未取消时延迟后continue；不是任意toolResult.isError | AgentSession的_retryAttempt、_retryAbortController、_failedResponse；`_prepareRetry`、`_isRetryableError` | 失败assistant怎样留在原始记录但退出下一请求projection？预算耗尽怎样收束？ |
| 恢复/继续会话 | 选中已有leaf后重建上下文；低层continue要求非空且不能直接以assistant结尾（Agent有队列例外） | SessionManager原始树和leaf；Agent当前messages；`buildSessionProjection`、`Agent.continue`、`runAgentLoopContinue` | 如何区分“加载历史后新prompt”和“继续未完成请求”？ |
| 扩展输入/上下文 | input可handled/transform；before_agent_start可改变工具/正文；context在模型转换前处理 | ExtensionRunner handler注册、AgentSession pending消息、transformContext；`_runInputHandlers`、SDK的transformContext | 改写是否写原始记录？forced prompt与history的差异在哪里？ |
| 扩展工具拦截 | 校验后beforeToolCall→tool_call可阻止；afterToolCall→tool_result可改结果 | 会话tool hooks、AgentLoop的Prepared/Immediate outcome；`_beforeToolCall`、`_afterToolCall`、`runToolCall` | block、terminate、嵌套executeTool如何组合？异步询问取消后会发生什么？ |
| turn/settlement边界 | finishTurn/turn_end与agent_before_settle可请求继续并提交边界draft | AgentSession的边界draft、_isBeforeSettle、_deferredSettledActions；`_installAgentBoundaryHooks`、`_runBeforeSettleBoundary` | 一个context-only继续是否有足够的provider-compatible尾消息？ |
| provider协议/缓存 | ModelRuntime分派到provider/API；具体协议将system/tool等映射到请求 | provider/API的transport状态及sessionId；`ModelRuntime.streamSimple`、`packages/ai/src/api/` | 请求构造、实际传输、缓存、provider continuation分别有哪些证据？ |
| codemode/MCP | 工具装载与受限执行连接，远端结果回到统一工具消息 | ToolsManager、MCP client连接、sandbox能力；`src/core/tools-manager.ts`、`packages/mcp/src/index.ts`、`packages/codemode/src/runtime/host.ts` | 哪些声明对模型可见？隐藏工具与嵌套调用走什么路径？ |
| durable/远程服务 | conversation/task/checkpoint与远程Session attachment架构 | durable Harness/存储、Chord service/state、protocol/client/server | 与本轮CLI AgentSession是否共享状态/生命周期？不要先假设替换关系 |
| 命令审批（未来功能） | 候选beforeToolCall / tool_call；允许/询问/拒绝需定义策略与真实交互 | 尚未设计或实现 | 路径/命令解析、规则优先级、取消、嵌套调用、结果与terminate分别如何验证？ |

## 后续运行与修改候选

1. 学习者先预测正常/缺席read，再设计一个最小可控观测。区分真实模型选择和固定响应前提；本轮没有生成该脚本。
2. 在实际输出中核对message_end、toolCallId、下一次请求和agent_settled；然后亲自定位源码证明原因。不要将旧版教师运行结果当作本版观测。
3. 修改文件内容、构造非法工具参数、输出length等相邻条件，验证分支；此阶段再运行相应测试，遵守仓库规则并单独取得任务授权。
4. 能解释正常链后，定义审批功能需求并比较扩展钩子与核心修改的取舍。

## 增量维护

`coverage.json` 区分 AST已提取、语义概览、源码核对、仅入口和未覆盖；`provenance.json` 固定版本/工具；证据索引是关键论断入口。扩展一条支线时先核对版本与工作区差异，补论断/条件/来源，再更新图中对应关系和Markdown，最后重新导出及校验。图health中的关系折叠、解析缺口应保留审计记录。
