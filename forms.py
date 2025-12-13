from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.csrf import CSRFProtect


csrf = CSRFProtect()



class EventForm(FlaskForm):
    title = StringField("Event Title", validators=[DataRequired()])
    description = TextAreaField("Description")
    event_date = StringField("Event Date (YYYY-MM-DD)", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    submit = SubmitField("Add Event")



class ForumForm(FlaskForm):
    username = StringField("Your Name", validators=[DataRequired()])
    title = StringField("Post Title", validators=[DataRequired()])
    content = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Post")



class WellnessForm(FlaskForm):
    date = StringField("Date (YYYY-MM-DD)", validators=[DataRequired()])
    mood = SelectField(
        "Mood",
        choices=[("Happy", "Happy"), ("Neutral", "Neutral"), ("Sad", "Sad"), ("Stressed", "Stressed")],
        validators=[DataRequired()]
    )
    steps = IntegerField("Steps", validators=[NumberRange(min=0)])
    notes = TextAreaField("Notes")
    submit = SubmitField("Save Entry")


class CommentForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Add Comment')
