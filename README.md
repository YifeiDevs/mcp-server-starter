# Math MCP Server
A simple MCP demo built with FastMCP, demonstrating how to set up an MCP server. Provides basic math operations — add, subtract, multiply, divide — and an image reading tool.

## Install dependencies
In project directory, press Ctrl+` to open a terminal:
```bash
uv init .
uv add "mcp[cli]"
```

## Configure your client
On Windows, run `win_gen_setting.bat` to auto-generate `mcp_setting.json`, or configure manually:
```json
{
  "mcpServers": {
    "math": {
      "type": "stdio",
      "command": "uv",
      "args": ["--directory", "/path/to/project", "run", "main.py"]
    }
  }
}
```

## Test the configuration
```bash
npx @srbhptl39/mcp-superassistant-proxy@latest --config ./mcp_setting.json
```