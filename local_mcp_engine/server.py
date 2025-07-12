from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")


@mcp.tool
def greet(name: str) -> str:
    return f"Hello {name}!!"


app = mcp.http_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )
