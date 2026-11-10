# Codex DSH Bridge

通过本地 MCP 把独立任务交给 DeepSeek Harness（DSH），再由 Codex 核对结果。提供 `dsh_health` 和 `dsh_delegate`，并附带一份供 Codex 选择委派任务的 Skill。

## 安装

当前配置面向 macOS。已验证 Node.js 24、npm 安装的 DSH 0.2.2-rc.1，以及通过 DSH 桌面端登录的 DeepSeek 账号。运行配置命令前，确保终端的 `PATH` 能找到 `node` 和 `dsh`。

1. 将仓库克隆到固定目录。在仓库内运行 `python3 configure.py`。
2. 备份 `~/.codex/config.toml`，把命令输出合并进去。如果已有 `[mcp_servers.dsh]`，先比较两份配置，保留一套 DSH 配置。
3. 把 `skills/codex-delegate-to-dsh` 复制到 `~/.agents/skills/`。如需主动考虑委派，可在 Codex 全局 `AGENTS.md` 加一句「对可外发、值得独立复核的任务，主动考虑 `codex-delegate-to-dsh` Skill」。
4. 重启 Codex。运行 `codex mcp list` 或在桌面端输入 `/mcp` 检查连接。

## 使用

手动测试可以说「用 DSH 独立复核下面这段合成代码，把结果和你自己的验证一起给我」。简单任务由 Codex 直接处理，适合委派的是有独立复核价值、输入可以外发、结论容易验证的任务。两项 DSH 工具的配置允许自动调用。每次委派会增加 DeepSeek 账号用量和等待时间。

DSH 在仓库下的 `.runtime/workspace` 中执行，文件、命令、联网搜索和 DSH 工作流工具在该配置中禁用。发给 DSH 的任务文本会提交给 DeepSeek。只传公开、合成或已获准外发的最小文本。会话写入 `.runtime/dsh-home`，因此这类 headless 委派在 DSH 桌面端的默认历史里看不到。首次运行前，`dsh_health` 可能显示 headless profile 尚未创建。

## 上游来源

`server/dsh-mcp.mjs` 沿用 [jeremy9682/dsh-cursor-codex](https://github.com/jeremy9682/dsh-cursor-codex/tree/81def5abbc01bd5b461710ed11a595bb4355f5f7) 的 MCP 实现。Skill 根据同一版本中的示例调整。许可见 [LICENSE](LICENSE)。
