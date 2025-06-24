# Elastic MCP

A Minimal Command Protocol (MCP) server with tools for interacting with Elasticsearch, including searching, listing indices, retrieving mappings, and bulk data upload.

---

## 1. Setup

### Prerequisites

- Python 3.8+
- [Elasticsearch](https://www.elastic.co/downloads/elasticsearch) running and accessible
- [uv](https://github.com/astral-sh/uv) or `pip` for dependency management

### Install dependencies

Using `uv` (recommended):
```sh
uv pip install -r requirements.txt
```
Or, if you use `pyproject.toml`:
```sh
uv venv
uv pip install -r requirements.txt
```

Or with pip:
```sh
pip install -r requirements.txt
```

### Set environment variables

Set your Elasticsearch connection details:
```sh
export ELASTIC_URL="http://localhost:9200"
export ELASTIC_USERNAME="your_username"
export ELASTIC_PASSWORD="your_password"
```

## 2. Running the MCP Server

```sh
fastmcp dev tools/elastic_tool.py ELASTIC_URL="http://localhost:9200" ELASTIC_USERNAME="your_username" ELASTIC_PASSWORD="your_password"
```
or Add to the Claude Desktop
```sh
fastmcp install tools/elastic_tool.py

or edit the config.json


```

## 3. Tools Provided

- **search_index**: Search an index with a query string.
- **list_indices**: List all indices (excluding system indices).
- **get_index_mappings**: Get mappings for a specific index.

## 4. Development

- Add new tools to `tools/elastic_tool.py` using the `@mcp.tool()` decorator.
- Use environment variables for configuration.
- See `.gitignore` for ignored files.

---

## 5. License

MIT License

---

## 6. Notes

- For production, do **not** hardcode credentials.
- For more info on MCP, see [FastMCP documentation](https://github.com/ai-llm/fastmcp).