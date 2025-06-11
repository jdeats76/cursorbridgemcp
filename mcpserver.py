from mcp.server.fastmcp import FastMCP
from tools.gdocs import gdocs

mcp = FastMCP("mcp-utility")

# Register tool modules
gdocs.register(mcp)

if __name__ == "__main__":
    print(">>> Starting MCP server...")
    mcp.run()