from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    about=TextAreaField("Tell other people about you.",validators=[Required()])
    submit=SubmitField("Submit")


class WritePitch(FlaskForm):
    title=StringField("Title of your Idea",validators=[Required()])
    pitch=TextAreaField("In about 200 words Write your Idea",validators=[Required()])
    submit=SubmitField("Submit")
