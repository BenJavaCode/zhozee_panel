from wtforms import PasswordField, validators, StringField
from flask_wtf import FlaskForm

# LOGINFORM
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])

#Dummyfield this whole mehtod should be reconsidered
# TESTFORM POSTGRESS1
class PostgresqlTestForm(FlaskForm):
    refresh = StringField("dummyfield")