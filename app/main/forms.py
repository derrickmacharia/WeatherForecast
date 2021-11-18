from flask_wtf import FlaskForm 
from wtforms import SelectField,StringField,SubmitField,TextAreaField,PasswordField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

# class ReviewForm(FlaskForm):
#     title = StringField('Review title',validators=[Required()])
#     review = TextAreaField('Weather Forecast review',validators=[Required()])
#     submit = SubmitField('Add a review')