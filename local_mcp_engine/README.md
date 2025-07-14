# Local MCP Engine

A lightweight Model Context Protocol (MCP) server built with FastMCP that interacts with an embedded SQLite database. You can perform operations via defined tools, and orchestrate them using a React-based LangChain agent (supported by both OpenAI and local Ollama models).


## Acknowledgements

 - [MCP Blog](https://www.projectpro.io/article/mcp-projects/1142)
 - [MCP Git Repo](https://github.com/patchy631/ai-engineering-hub)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`


## Run Locally

Clone the project

```bash
  git clone https://github.com/that-rookie-parth/mcp_explore.git
```

Go to the project directory

```bash
  cd mcp_explore/local_mcp_engine/

```

Install dependencies

```bash
  uv sync
```

Start the server

```bash
  uv run uvicorn server:app --reload --no-access-log
```


## Ollama

Follow [these instructions](https://github.com/ollama/ollama?tab=readme-ov-file#ollama) to set up and run a local Ollama instance.

**IMPORTANT**: Choose the model which supports the tool and agent calls.


## Features

* Local MCP server built with **FastMCP**, run via **Uvicorn** for hot-reload development.
* **SQLite database** managed in a standalone module, fully encapsulated within a cleanly designed class.
* **SQL queries** stored in separate `.sql` files to maintain a clear and organized project structure.
* MCP tools implemented in the server to seamlessly **add and fetch data** from the database.
* **React-based agent frontend** powered by **LangGraph**, capable of invoking both **OpenAI** and **Ollama** models.


## Authors

- [@Parth Kulshreshtha](https://github.com/that-rookie-parth)
