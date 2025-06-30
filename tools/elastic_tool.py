import os
import logging
from fastmcp import FastMCP
from elasticsearch import Elasticsearch, exceptions as es_exceptions

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("elastic-mcp")

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
    try:
        resp = es.search(index=index, query={"query_string": {"query": query}})
        return resp
    except Exception as e:
        logger.error(f"Error searching index '{index}': {e}")
        return {"error": str(e)}

@mcp.tool()
def list_indices() -> list:
    """List all indices in the Elasticsearch cluster."""
    try:
        indices = es.indices.get_alias()
        filtered = [name for name in indices.keys() if not name.startswith('.')]
        return filtered
    except Exception as e:
        logger.error(f"Error listing indices: {e}")
        return []

@mcp.tool()
def get_index_mappings(index: str) -> dict:
    """Get the mappings of a specific Elasticsearch index."""
    try:
        mappings = es.indices.get_mapping(index=index)
        return mappings.get(index, {})
    except Exception as e:
        logger.error(f"Error getting mappings for index '{index}': {e}")
        return {"error": str(e)}


if __name__=="__main__":
    mcp.run(transport="streamable-http")
