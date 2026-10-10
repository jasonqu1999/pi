# 静态重建与工具适配

所有脚本只写 `graphify-out/`，不运行 Pi、测试或模型。以 `cd32f7725fdbddbaecdff5b1e68491563394e0ca` 为证据版本；版本改变时先重查证据，不能自动给旧结论盖新版本戳。

## 已有提取结果的重建

在 Pi 仓库根目录，用 `.graphify_python` 中记录的解释器执行：

```sh
/Users/jason/.local/share/uv/tools/graphifyy/bin/python graphify-out/build-artifacts.py
/Users/jason/.local/share/uv/tools/graphifyy/bin/python graphify-out/export-learning.py
/Users/jason/.local/share/uv/tools/graphifyy/bin/python graphify-out/validate-artifacts.py
```

这会从保留的 `corpus.json`、`structural-extraction.json`、`semantic-extraction.json` 与 `evidence-seed.json` 重新合并、构图、聚类、分析和导出。原始关系保存在 `extraction.json`；简单图分析会折叠同端点关系；`graph.json` 保留端点已解析的多条关系。未解析关系及健康警告保留在原始提取和 `graph-health.json`。不强行绕过graphify的缩图保护。

执行环境是 Python 3.14、graphify 0.9.75，精确路径/版本和规格hash见 `provenance.json`。脚本使用安装包API；CLI技能示例与0.9.75的模块/参数有差异，所以使用实际签名。未升级skill或其他全局安装。

## 重新提取源码结构

依次执行 `detect-corpus.py`、`extract-structure.py`。扫描排除graphify-out、依赖和构建噪声，记录敏感/未分类/忽略项。AST显式使用 `parallel=False`；初次多进程脚本缺少入口保护触发重复启动，已终止，现不会再启动worker。缓存使用 `cache_root=仓库根`，graphify实际写入根下的 `graphify-out/cache/`。

新扫描的未缓存文档和图片由 `semantic-batches.json` 列出。语义提取须通过graphify skill，在当前会话/子代理中读取 `references/extraction-spec.md` 后完成；这里**没有**离线脚本能替代语义提取。每批片段需有效JSON、完整端点、来源与置信度；超长文档的阅读粒度记录到semantic-coverage。新增/修改文档不能仅复用旧semantic-extraction冒充重提取。

此次147个非代码文件按22个文档或单图像分13批，3工作槽分配；全部返回有效片段。图像实际经视觉读取。工作用片段转存 `semantic-fragments/`，正式合并数据保留供重建。代码结构提取不使用模型；语义提取使用当前会话和子代理，没有发起Gemini等供应商请求，token用量不可得，记为unknown。

## 校验边界

`validate-artifacts.py` 检查必需产物、JSON结构、图边端点、证据文件hash/符号、问题映射、Markdown目标/标题锚点、Obsidian节点和wiki链接、HTML嵌入数据及版本/工作区约束。它不是Pi行为测试，也不能替代人工源码核对。浏览器预览检查另记在validation中；如果未观察到实际浏览器渲染，不称视觉交互验证通过。

社区命名来自主要包职责，带编号避免重名。HTML按5000节点阈值聚合为社区图；Obsidian保留完整节点笔记，另有预测→导航→解释的学习入口。`graph.html` 是导出视图，不单独维护中文解释。

graphify benchmark只是按词数和子图文本估算token压缩，结果在 `benchmark.json`，不代表实际会话消耗或查询正确率。

## 增量支线

补支线先更新论断/条件/证据，再修改维护来源Markdown和 `evidence-seed.json`，最后导出与校验。不要在该版本审计上直接运行会改变主链行为的脚本；后续实际观测与修改按 [expansion-backlog](expansion-backlog.md) 单独开展。
