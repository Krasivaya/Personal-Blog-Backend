from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, TextField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User
from flask_login import current_user


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    category = SelectField('Categories', choices=[('Ideas Pitch', 'Ideas Pitch'), ('Life', 'Life Pitch'), ('Business Pitch', 'Business Pitch'), ('Interview Pitch', 'Interview Pitch')], validators=[DataRequired()])
    submit = SubmitField('Post it!')
    
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Submit')