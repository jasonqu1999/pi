<!-- Derived from graphify-out/source-navigation.md; edit the Markdown source and re-export. -->

# 按问题回到源码

先看 [预测问题](learning-questions.md)，然后使用 WebStorm 的 **Go to Symbol、Go to Declaration、Find Usages、Call Hierarchy**。IdeaVim 的 leader 可绑定这些动作；此表按意图组织，不要求记键位或固定行号。路径相对 Pi 仓库，可在 IDE 的文件搜索粘贴。

本轮先使用了 WebStorm MCP 的符号查找/读取/调用层级；调用层级实际选中了 `node_modules/@earendil-works/pi-agent-core` 的映射路径，而且未列出全部调用者，因此不把该树当完整主链证据。随后用同版本工作区源码读取补全，所有结论指向 `packages/`。图谱也用于定位；回调注入与动态调度需要核对实际代码，不能仅凭静态入边得出运行顺序。

| 问题 | 文件与符号 | IDE动作与要观察的连接 | 证据 |
|---|---|---|---|
| Q1 文件正文在哪里首次出现？ | `packages/coding-agent/src/core/tools/read.ts`：`createReadToolDefinition`；`packages/agent/src/agent-loop.ts`：`createToolResultMessage` | Go to Symbol找到read；沿execute看 `ops.access/readFile`；再看content如何变成toolResult | E14、E18 |
| Q2 下一请求怎么含结果？ | `packages/agent/src/agent-loop.ts`：`runLoop`、`streamAssistantResponse`；`packages/coding-agent/src/core/agent-session.ts`：`_installAgentRequestProjection` | 搜result回填；看prepareRequest返回context，随后transform/convert/normalize；不要跳过投影 | E08、E09、E15 |
| Q3 输入如何到Agent？ | `packages/coding-agent/src/modes/interactive/interactive-mode.ts`：`run`、`setupEditorSubmitHandler`；`packages/coding-agent/src/core/agent-session.ts`：`prompt`；`packages/agent/src/agent.ts`：`prompt`、`runPromptMessages` | 先区分编辑器提交与await getUserInput；从实际调用处进入不同类的prompt | E03、E05、E10 |
| Q4 工具什么时候才执行？ | `packages/agent/src/agent-loop.ts`：`executeToolCalls`、`prepareToolCall`、`executePreparedToolCall` | 看工具name查找、校验、before钩子；找kind=immediate和prepared两支 | E13、E16 |
| Q5 谁保存状态，何时保存记录？ | `packages/agent/src/agent.ts`：`processEvents`；`packages/coding-agent/src/core/agent-session.ts`：`_handleAgentEvent`；`packages/coding-agent/src/core/session-manager.ts`：`appendMessage`、`_persist` | Find Usages找到订阅注册；比较流partial、message_end、原始条目、文件写入条件 | E06、E07、E17、E23 |
| Q6 循环什么时候结束？ | `packages/agent/src/agent-loop.ts`：`runLoop`；`packages/agent/src/agent.ts`：`runWithLifecycle`、`finishRun`；`packages/coding-agent/src/core/agent-session.ts`：`_runAgentPrompt` | 从分支条件解释turn_end、agent_end、idle、agent_settled；在会话层找continue调用 | E15、E20、E21 |
| Q7 初始system和工具如何声明？ | `packages/coding-agent/src/core/agent-session.ts`：`_preparePromptAndToolLoadout`；`packages/agent/src/agent-loop.ts`：`declareToolChanges`；`packages/ai/src/utils/transcript.ts`：`getCurrentTools`、`normalizeContext` | 对照声明delta与可执行函数对象；看何时合并system，何时新插入 | E04、E09、E11 |
| Q8 模型异常和取消在哪里分层？ | `packages/agent/src/agent.ts`：`handleRunFailure`；`packages/coding-agent/src/core/agent-session.ts`：`_handlePostAgentRun`、`abort`、`_prepareRetry` | 对照response error和工具error；追signal传播、记录投影省略与重试continue | E18、E20、E22、E24 |
| Q9 包边界在哪里？ | `packages/coding-agent/src/main.ts`：`main`；`src/core/agent-session-services.ts`：`createAgentSessionFromServices`；`src/core/sdk.ts`：`createAgentSession`（后二路径属于coding-agent） | Call Hierarchy只能提供候选；读取runtime factory和注入的streamFn/subscribe补齐回调 | E01、E02、E04、E05 |
| Q10 接近审批功能的钩子在哪里？ | `packages/coding-agent/src/core/agent-session.ts`：`_installAgentToolHooks`、`_beforeToolCall`；`packages/agent/src/agent-loop.ts`：`runToolCall` | 从beforeToolCall映射到tool_call；比较block、terminate与嵌套工具入口 | E13、E25 |

完整证据见 [evidence.md](evidence.md)。机器索引 `question-index.json` 对每个问题保存文件、符号和图节点ID；`learning-overlay.json` 给出经核对的主链步骤、状态所有者和事件连接。

## 避免误跳转

同名 `prompt` 分别属于 AgentSession、Agent 或扩展接口。先看所在文件和类，再跳声明。`read` 既可能是文件工具，也可能是协议/流读取；检索 `createReadToolDefinition` 更准确。`streamSimple` 在ModelRuntime、provider和API中均可能出现，SDK实际调用的是注入的 `modelRuntime.streamSimple`。

供应商入口：`packages/coding-agent/src/core/model-runtime.ts` 的 `streamSimple` → `prepared.provider.streamSimple`；`packages/ai/src/providers/` 的provider定义 → `packages/ai/src/api/` 的API实现。Anthropic可从 `anthropicProvider → anthropicMessagesApi` 进入；OpenAI/Codex等协议与缓存/continuation细节留待后续，不能用通用循环猜测载荷。[E26](evidence.md#e26)
