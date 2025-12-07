# ---------------- IMPORTS ----------------
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


# ---------------- FORUM POST FORM ----------------
class ForumForm(FlaskForm):
    username = StringField("Your Name", validators=[DataRequired()])
    title = StringField("Post Title", validators=[DataRequired()])
    content = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Post")
