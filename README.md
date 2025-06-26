# Demo



https://github.com/user-attachments/assets/907c3f6f-807c-4805-879a-649c74804c29



# Elastic MCP

Connect to your Elasticsearch cluster from any MCP-compatible client (such as Claude Desktop) using the Model Context Protocol (MCP).
This server exposes your Elasticsearch data and operations via the MCP interface, enabling agents and applications to query, manage, and analyze your data through natural language interactions.

---

## 1. Setup

### Prerequisites

- Python 3.8+
- [Elasticsearch](https://www.elastic.co/downloads/elasticsearch) running and accessible
- [uv](https://github.com/astral-sh/uv) or `pip` for dependency management

### Install dependencies

Using `uv` package manager:
```sh
uv pip install -r requirements.txt
```

## 2. Running the MCP Server

Test using MCP Inspector

```sh
ELASTIC_URL="http://localhost:9200" ELASTIC_USERNAME="your_username" ELASTIC_PASSWORD="your_password" fastmcp dev tools/elastic_tool.py
```
or Add to the Claude Desktop by editing the claude_desktop_config.json and add the following code snippet

```sh

{
  "mcpServers": {
    "Elastic MCP Server": {
      "command": "uv",
      "args": [
        "run",
        "--with-requirements",
        "<absolute path to requirements.txt>",
        "fastmcp",
        "run",
        "<absolute path to elastic_tool.py>"
      ],
      "env": {
        "ELASTIC_URL": "http://localhost:9200",
        "ELASTIC_USERNAME": "your_username",
        "ELASTIC_PASSWORD": "your_password"
      }
    }
  }
}


```

## 3. Tools Provided

- **search_index**: Search an index with a query string.
- **list_indices**: List all indices (excluding system indices).
- **get_index_mappings**: Get mappings for a specific index.

---

## 4. License

MIT License

---

## 5. Notes

- For production, do **not** hardcode credentials.
- For more info on MCP, see [FastMCP documentation](https://github.com/ai-llm/fastmcp).
