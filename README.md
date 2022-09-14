# Daily Scrum Bot
### A simple application to randomize daily scrum presenter.
### Currently pulls data from a Google Sheets
---
- Uses Python 3.10.7
- Deployed to Heroku [https://daily-scrum-bot.herokuapp.com/](https://daily-scrum-bot.herokuapp.com/)
- Uses Flask for UI
- Uses Google API to grab Google Sheets data
- Uses `slackclient` to post messages to Slack

## Run Locally
Set environment variables:
- SPREADSHEET_ID (Google Sheets ID found in your Sheets URL)
- SPREADSHEET_RANGE (Google Sheets range ie: `Sheet 1!A1:D`)
- REDIRECT_URI (Google app redirect_uri)
- GOOGLE_CREDENTIALS (.json file that you downloaded when creating a new API credential. More info [here](https://medium.com/@osanda.deshan/getting-google-oauth-access-token-using-google-apis-18b2ba11a11a))
- SLACK_API_TOKEN (token generated from [here](https://slack.com/help/articles/215770388))

Install dependencies:
```
pip3 install -r requirements.txt
```
Start application:
```
FLASK_APP=app.py FLASK_ENV=development flask run
```
---
*Using [https://github.com/Vetronus/heroku-flask-template](https://github.com/Vetronus/heroku-flask-template) as a starting point*
