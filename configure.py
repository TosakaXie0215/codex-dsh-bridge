"""Print a Codex MCP configuration fragment for this checkout."""

import json
import shutil
from pathlib import Path


def quote(path):
    return json.dumps(str(path), ensure_ascii=False)


def executable(name):
    path = shutil.which(name)
    if path is None:
        raise SystemExit(f"Required executable not found on PATH: {name}")
    return quote(Path(path).resolve())


root = Path(__file__).resolve().parent
credentials = Path.home() / ".dsh" / ".credentials.yaml"
if not credentials.is_file():
    raise SystemExit("Sign in to DeepSeek Harness on this Mac first.")

node = executable("node")
dsh = executable("dsh")

print(f"""[mcp_servers.dsh]
command = {node}
args = [{quote(root / 'server/dsh-mcp.mjs')}]
cwd = {quote(root)}
startup_timeout_sec = 10
tool_timeout_sec = 135

[mcp_servers.dsh.env]
DSH_HOME = {quote(root / '.runtime/dsh-home')}
DSH_BRIDGE_NODE = {node}
DSH_BRIDGE_CLI = {dsh}
DSH_BRIDGE_CREDENTIALS = {quote(credentials)}
PATH = {quote(str(root / 'bin') + ':/usr/bin:/bin')}

[mcp_servers.dsh.tools.dsh_health]
approval_mode = "approve"

[mcp_servers.dsh.tools.dsh_delegate]
approval_mode = "approve"
""", end="")
