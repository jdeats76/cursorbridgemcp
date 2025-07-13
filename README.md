[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/jdeats76-cursorbridgemcp-badge.png)](https://mseep.ai/app/jdeats76-cursorbridgemcp)

# cursorbridgemcp
Leverage Cursor’s powerful new MCP feature with this lightweight Python FastMCP server with a Google Docs agent.
You can easily add additioanl agents 

# What Else Can You Expose?
The power of this setup lies in its flexibility. Beyond Google Docs, the same pattern applies to virtually any API. By dropping new files into your tools/ folder, you can instantly extend your MCP server to support other services - like Airtable, Slack, Jira, etc… or even internal systems. The beauty of the Model Context Protocol (MCP) is that it standardizes how large language models discover and interact with tools. It tells the LLM what functions exist, what parameters they expect, and what kind of output to anticipate - all without hardcoding behavior into the model itself.


# installation notes
You'll need to create a mcp.json file with the JSON code below. Path information formatted for MacOS 
You'll need to adapt for Windows, replace with location of your code and your_user_name

```
mcp.json

{
  "mcpServers": {
    "gdocs": {
      "command": "/Users/[your_user_name]/Code/Python/Projects/CursorBridgeMCP/.venv/bin/python",
      "args": ["/Users/[your_user_name]/Code/Python/Projects/CursorBridgeMCP/mcpserver.py"],
      "type": "command"
    }
  }
}
```

on MacOS this file will go in /[your_user_name]/~/.cursor/mcp.json on windows it's in the user's profile \.cursor folder
these are hidden folders on both OSs

# generating a credentials.json file - 
## NOTE: you must do this!!! without credentials.json gdoc agent will have no way to authenticate with Google. 

1. If you do not have a Google Cloud Account you can create one for free
https://cloud.google.com/gcp

2. Navigate to the Google Cloud Welcome Page and create a new project
https://console.cloud.google.com/welcome

3. With your new project selected, navigate to
 https://console.cloud.google.com/apis/credentials

4. Enable APIs: Google Drive & Google Docs
5. Create OAuth 2.0 Client ID → Desktop app
6. Download credentials.json to tools/gdocs/


# Testing for successful install

1. Launch Cursor and go to Cursor > Settings -> Cursor Settings
2. Click on the MCP Tools tab 
3. You should see an entry for "gdocs" with a little green circle.

If you see a yellow or red circle that means there is some issue

4. If setup is successful you can now include Google Doc request in your prompts from within cursor.
For example after a detailed explanation given to a prompt request, you might follow up with 
"Please create a new google doc called 'dev notes' and summarize your findings" 

Cursor can now use Google Docs!






 

