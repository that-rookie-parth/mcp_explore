import logging

from fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fastmcp_server")

mcp = FastMCP("My MCP Server")


@mcp.tool
def greet(name: str) -> str:
    logger.info("greet() tool called")
    return f"Hello {name}!!"


app = mcp.http_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )
