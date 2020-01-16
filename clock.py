from apscheduler.schedulers.blocking import BlockingScheduler
from util import google_util, slack_util
from datetime import date

sched = BlockingScheduler(timezone="America/New_York")


# @sched.scheduled_job('interval', minutes=3)
# def timed_job():
#     print('This job is run every three minutes.')


# TODO: dynamic bot name, bot icon, channel name, message, hour, day_of_week?
@sched.scheduled_job('cron', day_of_week='mon-fri', hour=10)
def scheduled_job():
  lucky_winner = google_util.get_daily_scrum_lucky_winner()
  today = date.today().strftime("%b %-d, %Y")
  slack_util.slack_message(f'_{today}_ - *{lucky_winner}*, you are today\'s lucky winner!', '#test-zapier', 'Daily Scrum Bot', ':alarm_clock:')
  slack_util.slack_message(f'_{today}_ - *{lucky_winner}*, you are today\'s lucky winner!', '#drc-f1-app-team', 'Daily Scrum Bot', ':alarm_clock:')
  print('This job is run every weekday at 10am.')


sched.start()
