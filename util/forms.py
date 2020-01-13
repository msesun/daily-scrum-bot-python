from wtforms import Form, BooleanField, StringField, validators

class AddUserForm(Form):
    name = StringField('Name', [validators.InputRequired()])
