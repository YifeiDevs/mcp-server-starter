from pathlib import Path
from main import TOOL_NAME

DIR = str(Path(__file__).parent.resolve()).replace("\\", "\\\\")

open("mcp_setting.json", "w").write(f"""\
{{
  "mcpServers": {{
    "{TOOL_NAME}": {{
      "timeout": 60,
      "type": "stdio",
      "command": "uv",
      "args": ["--directory", "{DIR}", "run", "main.py"]
    }}
  }}
}}""")

print("Done: mcp_setting.json")