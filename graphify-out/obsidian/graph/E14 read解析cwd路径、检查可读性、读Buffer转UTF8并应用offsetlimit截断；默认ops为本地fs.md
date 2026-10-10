---
source_file: "packages/coding-agent/src/core/tools/read.ts"
type: "rationale"
community: "Coding Agent 会话工具 10"
location: "createReadToolDefinition, defaultReadOperations, ops.access, ops.readFile"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Coding_Agent_会话工具_10
---

# E14 read解析cwd路径、检查可读性、读Buffer转UTF8并应用offset/limit/截断；默认ops为本地fs

## Connections
- [[createReadToolDefinition()]] - `references` [EXTRACTED]
- [[defaultReadOperations]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Coding_Agent_会话工具_10

## 源码入口

[packages/coding-agent/src/core/tools/read.ts](../../../packages/coding-agent/src/core/tools/read.ts)
