import asyncio
import logging

from fastmcp import Client

from server import mcp


async def call_tool(name: str) -> None:
    logging.info("Tool Called!!")
    async with Client(mcp) as client:
        result = await client.call_tool(
            "greet",
            {
                "name": name,
            },
        )
        print("Server Responded:", (result.structured_content or {}).get("result"))


asyncio.run(call_tool("Parth"))
