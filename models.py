from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class WellnessEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    mood = db.Column(db.String(20), nullable=False)
    steps = db.Column(db.Integer)
    notes = db.Column(db.Text)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    event_date = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(100), nullable=False)



class ForumPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)



class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    forum_post_id = db.Column(db.Integer, db.ForeignKey('forum_post.id'), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)


    forum_post = db.relationship('ForumPost', backref=db.backref('comments', lazy=True))






