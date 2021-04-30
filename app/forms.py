from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email
# from wtforms.widgets import PasswordInput

class PasswordInput():
    """
    Render a password input.

    For security purposes, this field will not reproduce the value on a form
    submit by default. To have the value filled in, set `hide_value` to
    `False`.
    """
    input_type = 'password'

    def __init__(self, hide_value=True):
        self.hide_value = hide_value

    def __call__(self, field, **kwargs):
        if self.hide_value:
            kwargs['value'] = ''
        return super(PasswordInput, self).__call__(field, **kwargs)

class UserInfoForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    email = StringField('Email', [DataRequired(),Email()])
    password = PasswordField('Password', [DataRequired()]) 
    confirm_pass = PasswordField('Confirm Password', [DataRequired(),EqualTo('password')])
    submit = SubmitField()
    

class PostForm(FlaskForm):
    title = StringField('Title', [DataRequired()])
    content = TextAreaField('Content', [DataRequired()])
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired(),Email()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField()