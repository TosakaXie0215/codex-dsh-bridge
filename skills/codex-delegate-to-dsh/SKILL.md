---
name: codex-delegate-to-dsh
description: Consider DeepSeek Harness (DSH) for a bounded, independently verifiable second review or auxiliary task using public, synthetic, or explicitly approved text. Covers code review and exploration, log and format checks, draft docs, and test ideas. Use also when the user explicitly asks for DSH or DeepSeek Harness.
---

# Codex delegation to DeepSeek Harness

Codex owns the task and its final verification. Handle quick questions directly. For larger tasks, prefer one DSH call when an independent review or bounded workstream is worth the extra latency and inference cost. Keep core algorithms, numerical correctness, architecture, multi-module refactors, scientific interpretation, and final testing and merging with Codex.

1. Decide what can be sent before calling. Send the minimum public or synthetic material or excerpts the user explicitly approved for DeepSeek. Never send patient data, private medical images, credentials, sensitive research, or confidential code without authorization. Strip personal identifiers, local paths, tokens, and irrelevant context. If the data boundary is unclear, handle the work locally.
2. Use the `dsh` MCP server. Call `dsh_health` when diagnosing availability. Send one self-contained task with `dsh_delegate`, omit `cwd`, and normally set `timeout_ms` to 90000. Include only the approved text, the desired output, and the criteria Codex can use to check it. For repository exploration, Codex can extract approved excerpts locally. DSH receives text in an isolated empty workspace with file and command tools disabled. Ask for suggested patches or tests as text. Any future write-capable DSH setup requires explicit authorization and an isolated worktree or separate checkout.
3. Review claims against the input, code or tests before relying on them. Apply and verify any changes in Codex. Limit concurrency to independent tasks with a clear benefit. If DSH is missing, unresponsive or unauthorized, continue locally. Retry once only if a transient error warrants it. Keep this workflow on MCP so the delegated request uses the restricted profile.
