from wtforms import Form, HiddenField, StringField, validators

class AddUserForm(Form):
    name = StringField('New Member\'s Name', [validators.InputRequired()])
    team = HiddenField('Team')
