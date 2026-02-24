## Tech Stack
- `uv` — package management
- `mcp[cli]` / `FastMCP` — MCP framework
- `Annotated` + `Field` — parameter schema
- `stdio` — communication method

## Adding New Tools
```python
@mcp.tool()
def my_tool(
    param: Annotated[str, Field(description="parameter description")], # description is exposed to the LLM
) -> str:
    """Briefly describe the tool's purpose and use case""" # LLM relies solely on this to decide whether to call it — must be accurate
    ...
    return result
```
## Returning Images
```python
from mcp.server.fastmcp.utilities.types import Image

@mcp.tool()
def read_image(image_path: Annotated[str, Field(description="image path")]) -> Image:
    """Read an image"""
    return Image(path=image_path)
```