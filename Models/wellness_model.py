# ---------------- IMPORTS ----------------
from models import db
from datetime import datetime


# ---------------- WELLNESS ENTRY TABLE ----------------
class WellnessEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date = db.Column(db.String(20), nullable=False)
    mood = db.Column(db.String(20), nullable=False)
    steps = db.Column(db.Integer)
    notes = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
