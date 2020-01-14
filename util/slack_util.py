from slack import WebClient
import os
from datetime import date


def slack_message(message, channel, username, icon):
    token = os.environ.get('SLACK_API_TOKEN')
    client = WebClient(token)
    client.chat_postMessage(channel=channel, text=message, username=username, icon_emoji=icon)


if __name__ == '__main__':
  today = date.today().strftime("%b %-d, %Y")
  user = 'Me'
  slack_message(f'_{today}_ - *{user}*, you are today\'s lucky winner!', '#test-zapier', 'Daily Scrum Bot', ':alarm_clock:')
