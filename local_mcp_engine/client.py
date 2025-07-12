import asyncio
from typing import Any

from authlib.jose.rfc7518.jws_algs import NoneAlgorithm
from fastmcp import Client

client = Client("http://localhost:8000/mcp")


async def greet(name: str) -> None:
    async with client:
        result = await client.call_tool(
            "greet",
            {
                "name": name,
            },
        )
        print("Server Responded:", (result.structured_content or {}).get("result"))


async def add_person(name: str, age: int, profession: str) -> None:
    async with client:
        result = await client.call_tool(
            "add_person",
            {
                "name": name,
                "age": age,
                "profession": profession,
            },
        )
        print("Server Responded:", (result.structured_content or {}).get("result"))


async def list_people() -> None:
    async with client:
        result = await client.call_tool_mcp("list_people", {})
        people: list | None = (result.structuredContent or {}).get("result")
        print("People in DB: ")
        if people:
            for item in people:
                print(item)


async def main():
    await greet("Parth")
    # await add_person("John", 22, "Singer")
    # await add_person("Jane", 23, "Guitarist")
    await list_people()


asyncio.run(main())
