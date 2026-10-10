---
source_file: "packages/ai/src/utils/transcript.ts"
type: "rationale"
community: "AI 模型协议 44"
location: "getCurrentTools, normalizeContext, toToolDeclaration"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/AI_模型协议_44
---

# E28 工具声明可重放增删delta，normalizeContext仅在外部systemPrompt/tools非空时添加leading message

## Connections
- [[getCurrentTools()]] - `references` [EXTRACTED]
- [[normalizeContext()]] - `references` [EXTRACTED]
- [[toToolDeclaration()]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/AI_模型协议_44

## 源码入口

[packages/ai/src/utils/transcript.ts](../../../packages/ai/src/utils/transcript.ts)
