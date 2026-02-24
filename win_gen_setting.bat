@echo off
set "DIR=%~dp0"
set "DIR=%DIR:~0,-1%"
set "DIR=%DIR:\=\\%"
(
echo {
echo   "mcpServers": {
echo     "math": {
echo       "timeout": 60,
echo       "type": "stdio",
echo       "command": "uv",
echo       "args": ["--directory", "%DIR%", "run", "main.py"]
echo     }
echo   }
echo }
) > mcp_setting.json
echo Done: mcp_setting.json
pause