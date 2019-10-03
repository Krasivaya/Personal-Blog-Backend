from flask_wtf import FlaskForm
from wtforms.validators import Email,Required,EqualTo,ValidationError
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from ..models import User
        

class LoginForm(FlaskForm):
    email = StringField('Please enter your Email',validators=[Required()])
    password = PasswordField('Please enter your Password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    username = StringField('Enter your Username',validators=[Required()])
    email = StringField('Please Enter Your Email',validators=[Email(),Required()])
    password = PasswordField('Please Enter Your Password',validators=[Required(),EqualTo('confirm_password',message='Passwords do not match')])
    confirm_password = PasswordField('Please Confirm Your Password',validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('Email already exists')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken, please pick another')
