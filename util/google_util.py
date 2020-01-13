import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date

def get_daily_scrum_lucky_winner():
  # use creds to create a client to interact with the Google Drive API
  scope = ['https://www.googleapis.com/auth/drive']
  creds = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json', scope)
  client = gspread.authorize(creds)

  # Find a workbook by name and open the first sheet
  # Make sure you use the right name here.
  sheet = client.open('Copy of Demo & Scrum Schedule').worksheet('Daily Scrum')

  # Extract and print all of the values
  # list_of_hashes = sheet.get_all_records()
  # print(list_of_hashes)

  # Find and extract cell matching value
  today = date.today().strftime("%b %-d, %Y")
  cell = sheet.find(today)
  # print(cell.row, cell.col)
  # print(sheet.cell(cell.row, cell.col + 1).value)

  return sheet.cell(cell.row, cell.col + 1).value
