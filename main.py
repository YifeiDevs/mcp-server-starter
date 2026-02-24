from typing import Annotated
from pydantic import Field
from mcp.server.fastmcp import FastMCP
import logging

TOOL_NAME = "math"

mcp = FastMCP(TOOL_NAME)

file_handler = logging.FileHandler(f'{TOOL_NAME}.log', mode='a')
logger = logging.getLogger()
# logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logging.info(f"{TOOL_NAME} MCP server initialized")

@mcp.tool()
def add(
    a: Annotated[float, Field(description="The first number to add")],
    b: Annotated[float, Field(description="The second number to add")])-> float:
    """Add two numbers"""
    logging.info(f"{a}+{b}={a+b}")
    return a + b

@mcp.tool()
def subtract(
    a: Annotated[float, Field(description="The number to be subtracted from")],
    b: Annotated[float, Field(description="The number to subtract")]) -> float:
    """Subtract b from a"""
    logging.info(f"{a}-{b}={a-b}")
    return a - b

@mcp.tool()
def multiply(
    a: Annotated[float, Field(description="The multiplicand")],
    b: Annotated[float, Field(description="The multiplier")]) -> float:
    """Multiply two numbers"""
    logging.info(f"{a}*{b}={a*b}")
    return a * b

@mcp.tool()
def divide(
    a: Annotated[float, Field(description="The dividend")],
    b: Annotated[float, Field(description="The divisor")]) -> float:
    """Divide a by b."""
    result = "Error: Cannot divide by zero." if b == 0 else a / b
    logging.info(f"{a}÷{b}={result}")
    return result

from mcp.server.fastmcp.utilities.types import Image
@mcp.tool()
def read_image(image_path: Annotated[str, Field(description="Path to the image file")]) -> Image:
    """Read an image from the given path"""
    return Image(path=image_path)

if __name__ == '__main__':
    # In project directory, press Ctrl+` to open a terminal:
    # uv init .
    # uv add "mcp[cli]"
    mcp.run("stdio")