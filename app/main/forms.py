from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class BlogForm(FlaskForm):

    title = StringField("Review title", validators=[Required()])
    content = TextAreaField("Blog Content")
    submit = SubmitField("Submit")


class CommentForm(FlaskForm):
    description = TextAreaField("Add comment", validators=[Required()])
