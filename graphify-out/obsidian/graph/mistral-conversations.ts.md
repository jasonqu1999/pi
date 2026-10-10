---
source_file: "packages/ai/src/api/mistral-conversations.ts"
type: "code"
community: "AI 模型协议 102"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AI_模型协议_102
---

# mistral-conversations.ts

## Connections
- [[AssistantMessage]] - `imports` [EXTRACTED]
- [[AssistantMessageEventStream]] - `imports` [EXTRACTED]
- [[MISTRAL_STREAM_DONE]] - `contains` [EXTRACTED]
- [[Message]] - `imports` [EXTRACTED]
- [[MistralChatMessage]] - `contains` [EXTRACTED]
- [[MistralChatPayload]] - `contains` [EXTRACTED]
- [[MistralCompletionEvent]] - `contains` [EXTRACTED]
- [[MistralContentChunk]] - `contains` [EXTRACTED]
- [[MistralFunctionTool]] - `contains` [EXTRACTED]
- [[MistralHttpError]] - `contains` [EXTRACTED]
- [[MistralOptions]] - `contains` [EXTRACTED]
- [[MistralReasoningEffort]] - `contains` [EXTRACTED]
- [[MistralRequestToolCall]] - `contains` [EXTRACTED]
- [[MistralStreamContentChunk]] - `contains` [EXTRACTED]
- [[MistralStreamToolCall]] - `contains` [EXTRACTED]
- [[Model_2]] - `imports` [EXTRACTED]
- [[SimpleStreamOptions]] - `imports` [EXTRACTED]
- [[StopReason]] - `imports` [EXTRACTED]
- [[StreamFunction]] - `imports` [EXTRACTED]
- [[StreamOptions]] - `imports` [EXTRACTED]
- [[TextContent]] - `imports` [EXTRACTED]
- [[ThinkingContent]] - `imports` [EXTRACTED]
- [[Tool]] - `imports` [EXTRACTED]
- [[ToolCall]] - `imports` [EXTRACTED]
- [[TranscriptContext]] - `imports` [EXTRACTED]
- [[aisrctypes.ts]] - `imports_from` [EXTRACTED]
- [[aisrcutilspi-user-agent.ts]] - `imports_from` [EXTRACTED]
- [[aisrcutilstext.ts]] - `imports_from` [EXTRACTED]
- [[applyMistralHeaderOverrides()]] - `contains` [EXTRACTED]
- [[buildBaseOptions()]] - `imports` [EXTRACTED]
- [[buildChatPayload()]] - `contains` [EXTRACTED]
- [[buildMistralHeaders()]] - `contains` [EXTRACTED]
- [[buildToolResultText()]] - `contains` [EXTRACTED]
- [[calculateCost()]] - `imports` [EXTRACTED]
- [[clampThinkingLevel()]] - `imports` [EXTRACTED]
- [[constrained-sampling.ts]] - `imports_from` [EXTRACTED]
- [[consumeChatStream()]] - `contains` [EXTRACTED]
- [[createMistralToolCallIdNormalizer()]] - `contains` [EXTRACTED]
- [[createOutput()]] - `contains` [EXTRACTED]
- [[deriveMistralToolCallId()]] - `contains` [EXTRACTED]
- [[event-stream.ts]] - `imports_from` [EXTRACTED]
- [[findMistralEventBoundary()]] - `contains` [EXTRACTED]
- [[formatMistralError()]] - `contains` [EXTRACTED]
- [[getCurrentTools()]] - `imports` [EXTRACTED]
- [[getJsonSchemaToolParameters()]] - `imports` [EXTRACTED]
- [[getMistralCachedPromptTokens()]] - `contains` [EXTRACTED]
- [[getPiUserAgent()]] - `imports` [EXTRACTED]
- [[getSystemMessageText()]] - `imports` [EXTRACTED]
- [[hasMistralHeaderOverride()]] - `contains` [EXTRACTED]
- [[hash.ts]] - `imports_from` [EXTRACTED]
- [[headers.ts]] - `imports_from` [EXTRACTED]
- [[headersToRecord()]] - `imports` [EXTRACTED]
- [[isMistralRecord()]] - `contains` [EXTRACTED]
- [[json-parse.ts]] - `imports_from` [EXTRACTED]
- [[mapChatStopReason()]] - `contains` [EXTRACTED]
- [[mapToolChoice()_1]] - `contains` [EXTRACTED]
- [[parseMistralEvent()]] - `contains` [EXTRACTED]
- [[parseStreamingJson()]] - `imports` [EXTRACTED]
- [[readMistralEvents()]] - `contains` [EXTRACTED]
- [[remapMistralProperty()]] - `contains` [EXTRACTED]
- [[renderSystemMessageUpdate()]] - `imports` [EXTRACTED]
- [[requestMistralStream()]] - `contains` [EXTRACTED]
- [[resolveJsonSchemaStrictSampling()]] - `imports` [EXTRACTED]
- [[resolveTranscript()]] - `imports` [EXTRACTED]
- [[safeJsonStringify()]] - `contains` [EXTRACTED]
- [[sanitize-unicode.ts]] - `imports_from` [EXTRACTED]
- [[sanitizeSurrogates()]] - `imports` [EXTRACTED]
- [[shortHash()]] - `imports` [EXTRACTED]
- [[shouldUsePromptCaching()]] - `contains` [EXTRACTED]
- [[simple-options.ts]] - `imports_from` [EXTRACTED]
- [[srcmodels.ts]] - `imports_from` [EXTRACTED]
- [[stream()_5]] - `contains` [EXTRACTED]
- [[streamSimple()_5]] - `contains` [EXTRACTED]
- [[stripSymbolKeys()]] - `contains` [EXTRACTED]
- [[toChatMessages()]] - `contains` [EXTRACTED]
- [[toFunctionTools()]] - `contains` [EXTRACTED]
- [[toMistralWireContentChunk()]] - `contains` [EXTRACTED]
- [[toMistralWireMessage()]] - `contains` [EXTRACTED]
- [[toMistralWirePayload()]] - `contains` [EXTRACTED]
- [[transform-messages.ts]] - `imports_from` [EXTRACTED]
- [[transformMessages()]] - `imports` [EXTRACTED]
- [[truncateErrorText()]] - `contains` [EXTRACTED]
- [[utilstranscript.ts]] - `imports_from` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AI_模型协议_102

## 源码入口

[packages/ai/src/api/mistral-conversations.ts](../../../packages/ai/src/api/mistral-conversations.ts)
