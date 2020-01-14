import gspread, pickle, os, json
from datetime import date
from requests_oauthlib import OAuth2Session
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def get_daily_scrum_lucky_winner():
  spreadsheet_id = os.environ.get('SPREADSHEET_ID')
  spreadsheet_range = os.environ.get('SPREADSHEET_RANGE')
  scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/spreadsheets.readonly'
  ]

  creds = None
  # google_credentials = json.loads(os.environ.get('GOOGLE_CREDENTIALS'))
  # with open('client_creds.json', 'w') as file:
  #   json.dump(google_credentials, file)
  if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
      creds = pickle.load(token)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file('client_creds.json', scope)
      creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token:
      pickle.dump(creds, token)

  service = build('sheets', 'v4', credentials=creds)

  # Call the Sheets API
  sheet = service.spreadsheets()
  result = sheet.values().get(spreadsheetId=spreadsheet_id,
                              range=spreadsheet_range).execute()
  values = result.get('values', [])

  if not values:
      print('No data found.')
  else:
      for row in values:
        today = date.today().strftime("%b %-d, %Y")
        if row[0] == today:
          # row: ['Feb 11, 2020', 'Alan']
          return row[1]


# if __name__ == '__main__':
#   todays_user = get_daily_scrum_lucky_winner()

