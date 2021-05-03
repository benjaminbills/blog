from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required, Email
from ..models import Subscriber
from wtforms import ValidationError


class BlogForm(FlaskForm):

    title = StringField("Review title", validators=[Required()])
    description = StringField("Description", validators=[Required()])
    urlToImage = StringField("Image Path", validators=[Required()])
    content = TextAreaField("Blog Content")
    submit = SubmitField("Submit")


class CommentForm(FlaskForm):
    description = TextAreaField("Add comment", validators=[Required()])


class SubscriberForm(FlaskForm):
    email = StringField("Enter Email", validators=[Required(), Email()])
    submit = SubmitField("Submit")

    def validate_email(self, data_field):
        if Subscriber.query.filter_by(email=data_field.data).first():
            raise ValidationError("You've already subscribe with that email")


class UpdateProfile(FlaskForm):
    bio = TextAreaField("Tell us about you.", validators=[Required()])
    profile_pic_path = StringField("Enter Image Url", validators=[Required()])
    submit = SubmitField("Submit")
