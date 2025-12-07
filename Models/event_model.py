# ---------------- IMPORTS ----------------
from models import db
from datetime import datetime


# ---------------- EVENT TABLE ----------------
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    event_date = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(100), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
