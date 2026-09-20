import mcp
import logging
from mcp.server import MCPServer

mcp = MCPServer("calc-service")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@mcp.tool()
def add(a: float,b: float) -> str:
    """ Adding two numbers and returning the result"""
    logger.info(f"Adding {a} and {b}")
    return f"Result {a+b}"

@mcp.tool()
def subtract(a: float, b: float) -> str:
    """ Subtracting two numbers and returning the result"""
    logger.info(f"Substracting {a} and {b}")
    return f"Result {a-b}"

@mcp.resource("calc://formulas/geometry")
def get_geometry_formulas() -> str:
    """Provide a reference sheet of basic geometry formulas for calculating areas and volumes."""
    logger.info("AI requested geometry formulas resource")
    return (
        "Geometry Formulas Cheat Sheet:\n"
        "- Area of a Circle: area = 3.14159 * radius * radius\n"
        "- Area of a Rectangle: area = width * height\n"
        "- Perimeter of a Rectangle: perimeter = 2 * (width + height)\n"
    )

if __name__ == "__main__":
    # Run the server using Standard I/O (stdio) transport
    mcp.run(transport="stdio")

