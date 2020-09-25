from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, EqualTo
from ..models import User
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')