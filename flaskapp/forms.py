from flask_wtf import FlaskForm, csrf
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, length, Email, EqualTo, Optional

class RegistrationForm(FlaskForm):
    username = StringField('Username',
         validators=[DataRequired(), length(min=6,max=20)])
    email = StringField('Email',
         validators=[DataRequired(),Email()])
    password = PasswordField('Password',
         validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
         validators=[DataRequired(), EqualTo('password')])

class LoginForm(FlaskForm):
    username = StringField('Username',
         validators=[DataRequired(), length(min=6,max=20)])
    email = StringField('Email',
         validators=[DataRequired(),Email()])
    password = PasswordField('Password',
         validators=[DataRequired()])