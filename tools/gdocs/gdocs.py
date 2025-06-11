import os
import logging
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/documents"]
CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), "credentials.json")
TOKEN_PATH = os.path.join(os.path.dirname(__file__), "token.json")

logger = logging.getLogger("gdocs")
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)-8s %(message)s', datefmt='%H:%M:%S')


def get_docs_service():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, "w") as token:
            token.write(creds.to_json())
    return build("docs", "v1", credentials=creds)


def register(mcp):
    docs_service = get_docs_service()

    @mcp.tool()
    def create_doc(title: str, body: str) -> str:
        """Create a Google Doc with the given title and body text."""
        logger.info(f"[create_doc] title: {title}")
        logger.info(f"[create_doc] body: {body}")
        doc = docs_service.documents().create(body={"title": title}).execute()
        doc_id = doc.get("documentId")

        requests = [
            {
                "insertText": {
                    "location": {"index": 1},
                    "text": body
                }
            }
        ]

        docs_service.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()
        logger.info(f"[create_doc] created doc ID: {doc_id}")
        return f"Created: https://docs.google.com/document/d/{doc_id}/edit"

    @mcp.tool()
    def insert_text(doc_id: str, index: int, text: str) -> str:
        """Insert text into a document at a given index."""
        logger.info(f"[insert_text] doc_id: {doc_id}, index: {index}, text: {text}")
        requests = [
            {
                "insertText": {
                    "location": {"index": index},
                    "text": text
                }
            }
        ]
        docs_service.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()
        return "Text inserted."

    @mcp.tool()
    def delete_text(doc_id: str, start_index: int, end_index: int) -> str:
        """Delete text in a document from start to end index."""
        logger.info(f"[delete_text] doc_id: {doc_id}, start: {start_index}, end: {end_index}")
        requests = [
            {
                "deleteContentRange": {
                    "range": {
                        "startIndex": start_index,
                        "endIndex": end_index
                    }
                }
            }
        ]
        docs_service.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()
        return "Text deleted."

    @mcp.tool()
    def replace_all_text(doc_id: str, new_content: str) -> str:
        """Replace all content in a document with new content."""
        logger.info(f"[replace_all_text] doc_id: {doc_id}, new_content: {new_content}")
        requests = [
            {"deleteContentRange": {"range": {"startIndex": 1, "endIndex": 9999}}},
            {"insertText": {"location": {"index": 1}, "text": new_content}}
        ]
        docs_service.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()
        return "Document replaced."
