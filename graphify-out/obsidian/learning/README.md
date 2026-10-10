<!-- Derived from graphify-out/README.md; edit the Markdown source and re-export. -->

# Pi 1.0.2：从一个请求读懂架构

本资料对应提交 `cd32f7725fdbddbaecdff5b1e68491563394e0ca`。本轮仅做静态提取、源码阅读及产物校验；没有运行 Pi、测试、模型替身或真实模型。交付完成不表示学习者已掌握。

执行结果：1,818 个纳入文件、19,848 个图节点、67,046 条导出关系、492 个社区，38 项关键证据。全部约定静态产物已生成，链接、来源和版本校验通过，结果见 `validation.json`。原始提取仍有悬空端点、自环和简单图关系折叠警告；215 个代码文件被提取器报告无符号，一个测试文件部分解析；token成本未知。HTML采用社区聚合视图，浏览器安全策略阻止本地file预览，视觉/交互核验未完成。

## 先做一个预测

新会话里输入「请总结 notes.md」，没有使用 `@文件`、没有附加图片或扩展注入。假设模型第一次返回 `read({path:"notes.md"})`，第二次返回总结。

**文件内容第一次出现在什么数据里？第二次请求为什么能看见它？**

先写出自己的消息序列，再进入 [问题 Q1 与源码导航](learning-questions.md#q1)。只需要定位 `AgentSession.prompt`、`streamAssistantResponse`、`createToolResultMessage`，先不要读完整解释。

预测后对照 [完整走读](core-flow.md)。整体方向见 [架构地图](architecture.md)，要找一个修改点见 [源码导航](source-navigation.md)。缺席文件与正常路径放在同一份走读里，方便比较。

## 如何使用

| 要做的事 | 入口 |
|---|---|
| 看包的职责、接口和边界 | [architecture.md](architecture.md) |
| 串起输入、上下文、流响应、工具、状态与出口 | [core-flow.md](core-flow.md) |
| 先预测，再亲自沿符号跳转 | [learning-questions.md](learning-questions.md) → [source-navigation.md](source-navigation.md) |
| 在图中查关系 | [graph.html](../../graph.html)；精确关系用 `graph.json` |
| 核对一个论断的依据 | [evidence.md](evidence.md) / `evidence-index.json` |
| 判断覆盖深度与缺口 | `coverage.json` / [GRAPH_REPORT.md](GRAPH_REPORT.md) |
| 后续运行、修改和支线学习 | [expansion-backlog.md](expansion-backlog.md) |
| 在 Obsidian 中导航 | 打开 `obsidian/` 为 vault，从 [学习入口](../%E5%AD%A6%E4%B9%A0%E5%85%A5%E5%8F%A3.md) 开始 |

## 给后续 AI

先读取本文件、`provenance.json` 与 `coverage.json`，按 `question-index.json` 找问题和证据，再读取相关源文件。`graph.json` 是有方向的结构图，`extraction.json` 保留原始关系、来源及健康诊断所需信息；`evidence-index.json` 与 `learning-overlay.json` 保存人工核对的主链及状态归属。

图谱中的导入、静态调用、相似关系不证明运行顺序。带 `EXTRACTED` 的 AST 边也可能来自静态解析局限；关键行为以证据索引里的源码确认项为准。测试项表示作者写下的预期，本轮未执行。文档语义片段可覆盖正文主题，但超长规范和 changelog 不做逐条审计，详见逐文件覆盖。`graph.json` 保留端点已解析的多关系；未解析的原始关系保存在 `extraction.json`，详见 `graph-health.json`。

## 查询与重建

在 Pi 仓库根目录执行 `graphify query "streamAssistantResponse createToolResultMessage read"`。先使用源码符号扩展中文问题词汇；查询只给静态关联，不把搜到的邻居自动解释为调用链。工具解释器保存在 `.graphify_python`。主链也可按 `learning-overlay.json` 的顺序查询，避免大图噪声。

静态重建步骤与适配说明见 [rebuild.md](rebuild.md)。中文 Markdown 是维护来源；Obsidian 学习页由 `export-learning.py` 派生，图谱由结构提取和语义片段构建。不要分别修改导出视图。

保留原 [PLAN.md](../../PLAN.md)，本文件和 `validation.json` 记录执行结果。
