from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
import gspread
from util.forms import AddUserForm
from util import google_util
from datetime import date


F1_USERS = ['alan', 'dave', 'dilip', 'ellen', 'jeff', 'landon', 'matt', 'prem', 'senai', 'seth', 'xavier']


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
  today = date.today().strftime("%b %-d, %Y")
  lucky_winner = google_util.get_daily_scrum_lucky_winner()
  return render_template('index.html', today=today, lucky_winner=lucky_winner)


@app.route('/users')
def users():
  return render_template('users.html', users=F1_USERS)


@app.route('/users/add', methods=['POST'])
def add_user(request):
  print('done')
  form = AddUserForm(request.POST)
  if request.method == 'POST' and form.validate():
    F1_USERS.append(form.name.data)
    return redirect('/users')
  return render_template('users', form=form)


@app.route('/schedule')
def schedule():
  return render_template('schedule.html')


if __name__ == '__main__':
  app.run(debug=True)
