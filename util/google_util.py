import gspread, pickle, os
# from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
from requests_oauthlib import OAuth2Session
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def get_daily_scrum_lucky_winner():
  # use creds to create a client to interact with the Google Drive API
  # client_id = os.environ.get('CLIENT_ID')
  # client_secret = os.environ.get('CLIENT_SECRET')
  # redirect_uri = os.environ.get('REDIRECT_URI')
  # authorization_base_url = "https://accounts.google.com/o/oauth2/auth"
  # token_url = os.environ.get('TOKEN_URI')
  spreadsheet_id = os.environ.get('SPREADSHEET_ID')
  spreadsheet_range = os.environ.get('SPREADSHEET_RANGE')
  scope = ['https://www.googleapis.com/auth/drive']

  # Old way using oauth2client:
  # creds = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json', scope)
  # client = gspread.authorize(creds)
    # Find a workbook by name and open the first sheet
  # Make sure you use the right name here.
  # sheet = client.open('Copy of Demo & Scrum Schedule').worksheet('Daily Scrum')

  creds = None
  if os.path.exists('token.pickle'):
      with open('token.pickle', 'rb') as token:
          creds = pickle.load(token)
  if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
          creds.refresh(Request())
      else:
          flow = InstalledAppFlow.from_client_secrets_file(
              os.environ.get('GOOGLE_CREDENTIALS'), scope)
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

  # today = date.today().strftime("%b %-d, %Y")
  # cell = sheet.find(today)

  # return sheet.cell(cell.row, cell.col + 1).value
