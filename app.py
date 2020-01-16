from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
import gspread, os
from util.forms import AddUserForm
from util import google_util
from datetime import date
from util.teams_and_users import TEAMS_AND_USERS_DICT


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
  today = date.today().strftime("%b %-d, %Y")
  lucky_winner = google_util.get_daily_scrum_lucky_winner()
  return render_template('index.html', today=today, lucky_winner=lucky_winner)


@app.route('/users')
def users():
  return render_template('users.html', teams_and_users=TEAMS_AND_USERS_DICT)


@app.route('/users/add', methods=['GET', 'POST'])
def add_user():
  message = ''
  form = AddUserForm(request.form)
  print('REQUEST METHOD', request.method)
  if request.method == 'POST' and form.validate():
    user_name = form.name.data
    team_name = form.team.data
    if user_name not in TEAMS_AND_USERS_DICT[team_name]:
      TEAMS_AND_USERS_DICT[team_name].append(user_name)
      message = f'{user_name} has been added to {team_name}'
      return render_template('users.html', message=message, teams_and_users=TEAMS_AND_USERS_DICT)
    else:
      message = f'{user_name} already exists in {team_name}'
      return render_template('add_user.html', team=team_name, form=form)
  else:
    print('Form not valid')
  return render_template('add_user.html', team=team_name, form=form)


@app.route('/schedule')
def schedule():
  return render_template('schedule.html')


if __name__ == '__main__':
  app.run(debug=True)
