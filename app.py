from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SPREADSHEET_ID = "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"
RANGE_NAME = "Sheet1!A1:E5"  # Replace with your specific range

# Load credentials from the downloaded JSON file
credentials = Credentials.from_authorized_user_file("token.json", SCOPES)(
    service_account.Credentials.from_service_account_file(
    "credentials.json",
    scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
))

# Create a Google Sheets API service
service = googleapiclient.discovery.build("sheets", "v4", credentials=credentials)

# Call the Sheets API
result = (
    service.spreadsheets()
    .values()
    .get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME)
    .execute()
)

values = result.get("values", [])

if not values:
    print("No data found.")
else:
    for row in values:
        print(row)
