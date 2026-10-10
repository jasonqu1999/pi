# 先预测，再核对

每题先用一两句话或几条消息写预测，再用指定导航核对。下面不附答案；完整解释单独放在 [core-flow](core-flow.md) 和 [architecture](architecture.md)。本轮不要求运行代码，预测结果不自动记为能力证据。

## Q1

普通文本里写「总结 notes.md」，文件正文第一次会出现在user、assistant还是toolResult中？如果工具根本没有执行，模型依据什么回答？

最小导航：`createReadToolDefinition → createToolResultMessage`。核对点：真正读取者是谁、content来源、id匹配。[导航表](source-navigation.md) · 预测后查 [完整解释](core-flow.md#两次请求的数据变化)。

## Q2

工具结果已经追加到循环数组，为什么会话还要在下一次请求前重建投影？如果一条原始条目被context_edit省略，下次模型还能看到它吗？

最小导航：`runLoop → _installAgentRequestProjection → buildSessionProjection`。核对点：工作数组、原始记录、请求投影的所有者。[导航](source-navigation.md) · [解释](architecture.md#三份容易混淆的数据)。

## Q3

按下提交键后，是编辑器直接调用Agent，还是经过输入队列和会话层？当Agent正在回答时，同样文本如何进入下一轮？

最小导航：`InteractiveMode.run`、`setupEditorSubmitHandler`、`AgentSession.prompt`。核对点：普通输入与streamingBehavior的分支。[导航](source-navigation.md) · [解释](core-flow.md#正常例子总结-notesmd)。

## Q4

模型输出完整read调用、未知工具名、非法参数、被前钩子阻止、输出被length截断：这五种情况下哪些会进入execute？阻止一个调用是否必然结束全部请求？

最小导航：`prepareToolCall`、`failToolCallsFromTruncatedMessage`、`shouldTerminateToolBatch`。核对点：条件先后、immediate结果、整批terminate。[导航](source-navigation.md) · [解释](core-flow.md#各种出口)。

## Q5

文件读取完成时，会话里已有哪几条完成消息？流式delta是否每次落盘？第一次user消息出现前，setup条目是否一定创建会话文件？

最小导航：`processEvents → _handleAgentEvent → appendMessage → _persist`。核对点：message_end、streamingMessage、persist条件。[导航](source-navigation.md) · [解释](core-flow.md#记录更新在哪里发生)。

## Q6

UI看到agent_end后，Agent一定已经idle吗？一次自动重试能产生几个agent_end和几个agent_settled？最终回答后终端程序会退出吗？

最小导航：`finishRun`、`_runAgentPrompt`、`_emitAgentSettled`、`InteractiveMode.run`。核对点：低层/会话/交互进程三个边界。[导航](source-navigation.md) · [解释](core-flow.md#控制流循环和事件是两条连接)。

## Q7

`context.tools` 包含execute函数，而模型只需要声明。两者如何一致？新会话一定有两条system消息吗？normalizeContext会无条件添加system吗？

最小导航：`declareToolChanges`、`toToolDeclaration`、`normalizeContext`。核对点：delta合并和插入条件。[导航](source-navigation.md) · [解释](core-flow.md#两次请求的数据变化)。

## Q8

read抛ENOENT与模型response.stopReason=error对循环的影响是否相同？取消是立即杀死所有工作，还是向各层发送signal？

最小导航：`executePreparedToolCall`、`runLoop`、`AgentSession.abort`。核对点：工具结果、低层return、重试决策、协作取消。[导航](source-navigation.md) · [解释](core-flow.md#对照例子文件不存在)。

## Q9

如果把read改成远程读取，哪些接口可保持不变？如果只修改终端toolResult的显示，下次模型输入一定改变吗？

最小导航：`ReadOperations`、`streamFn`、`subscribeToAgent`。核对点：执行边界与输出消费边界。设计比较需注明推断，不把接口可能性写成已实现/已验证。[导航](source-navigation.md) · [解释](architecture.md#设计取舍事实与推断)。

## Q10

将来添加「允许/询问/拒绝」命令审批，拦截点应该在模型输出、工具执行前，还是渲染层？嵌套工具能绕过同一个钩子吗？

最小导航：`_installAgentToolHooks`、`prepareToolCall`、`runToolCall`。本轮只提出候选接缝，完整设计留在 [backlog](expansion-backlog.md)。

## 自查方式

拿一条自己写的预测，对照源码回答：输入是什么、谁执行、什么条件改变分支、输出在哪里、谁拥有状态、相邻修改影响谁。允许查看笔记；能够独立解释和迁移比背函数名有用。老师写出的答案、本轮静态校验、已有历史实验都不能替代你后续亲自运行和修改的证据。
