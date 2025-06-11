#!/bin/bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

mkdir -p ~/.cursor
cat > ~/.cursor/mcp.json <<EOF
{
  "mcpServers": {
    "gdocs": {
      "command": "/Users/[your_user_name]/Code/Python/Projects/CursorBridgeMCP/.venv/bin/python",
      "args": ["/Users/[your_user_name]/Code/Python/Projects/CursorBridgeMCP/mcpserver.py"],
      "type": "command"
    }
  }
}
EOF