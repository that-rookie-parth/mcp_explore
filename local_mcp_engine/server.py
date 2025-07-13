import logging
from typing import Any, Dict, List

from fastmcp import FastMCP

from db import Database

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fastmcp_server")

mcp = FastMCP("My MCP Server")
db: Database = Database()


@mcp.tool
def greet(name: str) -> str:
    """
    Returns a personalized greeting for the given name.
    """
    logger.info("greet() tool called")
    return f"Hello {name}!!"


@mcp.tool
def add_person(name: str, age: int, profession: str) -> str:
    """
    Add a record of the person to the database.
    """
    logger.info("Adding a new record to db")
    db.insert_person(name, age, profession)
    return f"Record of {name} added successfully to the db."


@mcp.tool
def list_people() -> list[Any]:
    """
    Retrun the details about all the people stored in the db.
    """
    logger.info("Fetching the details of all the people from the db")
    people: list[Any] = db.get_all_people()
    return people


@mcp.tool
def remove_person(id: int) -> str:
    """
    Remove the information about person from the db based on the id.
    """
    logger.info("Removing the information about a person from the db.")
    db.remove_person(id)
    return f"Record of {id} removed successfully from the db."


app = mcp.http_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )
