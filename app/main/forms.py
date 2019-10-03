from . import main
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,TextAreaField,SelectField
from wtforms.validators import Required
from ..models import Pitch,Comment

class PitchUploadForm(FlaskForm):
    pitch = TextAreaField('Pitch',validators=[Required()])
    category = SelectField('Category',choices=[('Interview','Interview'),('Pick-up','Pick-up'),('Product','Product'),('Promotion','Promotion')])
    submit = SubmitField('Add Pitch')

class CommentsForm(FlaskForm):
    comment = TextAreaField('comment on the post',validators=[Required()])
    submit = SubmitField('Add Comment')

class UpdateProfile(FlaskForm):
    bio = StringField('About You',validators=[Required()])
    submit = SubmitField('Add Bio')