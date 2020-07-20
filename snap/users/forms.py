from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo,Length

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(max=15)])
    email=StringField('Email',validators=[DataRequired(),Length(max=80)])
    password=PasswordField('password',validators=[DataRequired(),EqualTo('confirm')])
    confirm=PasswordField('Confirm password',validators=[DataRequired()])
    submit=SubmitField('Sign Up')
#login form
class LoginForm(FlaskForm):
    username=StringField('username',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    submit=SubmitField('Login')
