# ---------------- IMPORTS ----------------
from models import db
from datetime import datetime


# ---------------- FORUM POST TABLE ----------------
class ForumPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
