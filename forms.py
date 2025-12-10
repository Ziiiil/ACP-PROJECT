"""
Forms for the ACP Community Platform
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.csrf import CSRFProtect

# Initialize CSRF protection
csrf = CSRFProtect()


# ==================== EVENT FORM ====================
class EventForm(FlaskForm):
    title = StringField("Event Title", validators=[DataRequired()])
    description = TextAreaField("Description")
    event_date = StringField("Event Date (YYYY-MM-DD)", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    submit = SubmitField("Add Event")


# ==================== FORUM POST FORM ====================
class ForumForm(FlaskForm):
    username = StringField("Your Name", validators=[DataRequired()])
    title = StringField("Post Title", validators=[DataRequired()])
    content = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Post")


# ==================== WELLNESS FORM ====================
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
