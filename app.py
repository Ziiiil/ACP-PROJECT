from flask import Flask, Blueprint, render_template, redirect, flash, request
from models import db, Event, WellnessEntry, ForumPost, Comment
from flask_wtf.csrf import CSRFProtect
from forms import EventForm, WellnessForm, ForumForm  
import os

# ==================== CONFIG ====================
class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'final_project_db.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "supersecretkey123"

# Initialize CSRF
csrf = CSRFProtect()

# ==================== BLUEPRINTS ====================
main_bp = Blueprint("main", __name__)
wellness_bp = Blueprint("wellness", __name__)
event_bp = Blueprint("events", __name__)
forum_bp = Blueprint("forum", __name__)

# ==================== CREATE APP ====================
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        db.create_all()

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(wellness_bp, url_prefix="/wellness")
    app.register_blueprint(event_bp, url_prefix="/events")
    app.register_blueprint(forum_bp, url_prefix="/forum")

    return app

# ==================== MAIN ROUTES ====================
@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/health")
def health():
    return render_template("health.html")

@main_bp.route("/livelihood")
def livelihood():
    return render_template("livelihood.html")

# ==================== WELLNESS ROUTES ====================
@wellness_bp.route("/")
def list_entries():
    entries = WellnessEntry.query.all()
    return render_template("wellness_list.html", entries=entries)

@wellness_bp.route("/add", methods=["GET", "POST"])
def add_entry():
    form = WellnessForm()
    if form.validate_on_submit():
        # Create a new WellnessEntry object from the form data
        entry = WellnessEntry(
            date=form.date.data,
            mood=form.mood.data,
            steps=form.steps.data,
            notes=form.notes.data
        )
        # Add to session and commit to save in the database
        db.session.add(entry)
        db.session.commit()
        flash("Wellness entry added!", "success")
        return redirect("/wellness")
    return render_template("wellness_add.html", form=form)

# ==================== EVENTS ROUTES ====================
@event_bp.route("/")
def events():
    events = Event.query.all()
    return render_template("events.html", events=events)

@event_bp.route("/add", methods=["GET", "POST"])
def add_event():
    form = EventForm()
    if form.validate_on_submit():
        # Create a new Event object from the form data
        event = Event(
            title=form.title.data,
            description=form.description.data,
            event_date=form.event_date.data,
            location=form.location.data
        )
        # Add to session and commit to save in the database
        db.session.add(event)
        db.session.commit()
        flash("Event added successfully!", "success")   
        return redirect("/events")
    return render_template("events_add.html", form=form)

# ==================== FORUM ROUTES ====================
@forum_bp.route("/")
def forum():
    posts = ForumPost.query.all()
    return render_template("forum.html", posts=posts)

@forum_bp.route("/add", methods=["GET", "POST"])
def add_post():
    form = ForumForm()
    if form.validate_on_submit():
        # Create a new ForumPost object from the form data
        post = ForumPost(
            username=form.username.data,
            title=form.title.data,
            content=form.content.data
        )
        db.session.add(post)
        db.session.commit()
        flash("Post created successfully!", "success")
        return redirect("/forum")
    return render_template("forum_add.html", form=form)

# Inline add comment route
@forum_bp.route("/<int:post_id>/comment", methods=["POST"], endpoint="add_comment_inline")
def add_comment(post_id):
    post = ForumPost.query.get_or_404(post_id)
    username = request.form.get("username")
    content = request.form.get("content")
    if username and content:
        comment = Comment(forum_post_id=post.id, username=username, content=content)
        db.session.add(comment)
        db.session.commit()
        flash("Comment added!", "success")
    else:
        flash("All fields are required!", "danger")
    return redirect("/forum")

# ==================== RUN APP ====================
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

