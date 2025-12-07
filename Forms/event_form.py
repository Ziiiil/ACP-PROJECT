# ---------------- IMPORTS ----------------
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


# ---------------- EVENT FORM ----------------
class EventForm(FlaskForm):
    title = StringField("Event Title", validators=[DataRequired()])
    description = TextAreaField("Description")
    event_date = StringField("Event Date (YYYY-MM-DD)", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    submit = SubmitField("Add Event")
