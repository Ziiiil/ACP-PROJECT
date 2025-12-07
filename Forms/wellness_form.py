# ---------------- IMPORTS ----------------
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange


# ---------------- WELLNESS FORM ----------------
class WellnessForm(FlaskForm):
    date = StringField("Date (YYYY-MM-DD)", validators=[DataRequired()])
    mood = SelectField(
        "Mood",
        choices=[("Happy","Happy"),("Neutral","Neutral"),("Sad","Sad"),("Stressed","Stressed")],
        validators=[DataRequired()]
    )
    steps = IntegerField("Steps", validators=[NumberRange(min=0)])
    notes = TextAreaField("Notes")
    submit = SubmitField("Save Entry")
