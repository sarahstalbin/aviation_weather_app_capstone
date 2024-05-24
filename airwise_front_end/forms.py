
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError, Length, EqualTo

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6, max=40)])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')