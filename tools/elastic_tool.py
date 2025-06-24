import os
import logging
from fastmcp import FastMCP
from elasticsearch import Elasticsearch

# Create an MCP server
mcp = FastMCP("Elastic MCP Server")

# Get Elasticsearch connection details from environment variables
ELASTIC_URL = os.environ.get("ELASTIC_URL", None)
ELASTIC_USERNAME = os.environ.get("ELASTIC_USERNAME", None)
ELASTIC_PASSWORD = os.environ.get("ELASTIC_PASSWORD", None)

# Check for missing environment variables
if not all([ELASTIC_URL, ELASTIC_USERNAME, ELASTIC_PASSWORD]):
    logging.error("ELASTIC_URL, ELASTIC_USERNAME, and ELASTIC_PASSWORD environment variables must be set.")

es = Elasticsearch(
    ELASTIC_URL,
    basic_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD)
)


@mcp.tool()
def search_index(index: str, query: str) -> dict:
    """Search an Elasticsearch index with a simple query string."""
    resp = es.search(index=index, query={"query_string": {"query": query}})
    return resp

@mcp.tool()
def list_indices() -> list:
    """List all indices in the Elasticsearch cluster."""
    indices = es.indices.get_alias()
    filtered = [name for name in indices.keys() if not name.startswith('.')]
    return filtered

@mcp.tool()
def get_index_mappings(index: str) -> dict:
    """Get the mappings of a specific Elasticsearch index."""
    mappings = es.indices.get_mapping(index=index)
    return mappings.get(index, {})


if __name__ == "__main__":
    mcp.run()


