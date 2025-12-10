from flask import Flask, Blueprint, render_template, redirect
from config import Config
from models import db, Event, WellnessEntry, ForumPost
from forms import csrf, EventForm, WellnessForm, ForumForm


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


# ==================== MAIN BLUEPRINT ====================
main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/health")
def health():
    return render_template("health.html")

@main_bp.route("/livelihood")
def livelihood():
    return render_template("livelihood.html")


# ==================== WELLNESS BLUEPRINT ====================
wellness_bp = Blueprint("wellness", __name__)

@wellness_bp.route("/")
def list_entries():
    entries = WellnessEntry.query.all()
    return render_template("wellness_list.html", entries=entries)

@wellness_bp.route("/add", methods=["GET", "POST"])
def add_entry():
    form = WellnessForm()
    if form.validate_on_submit():
        entry = WellnessEntry(
            date=form.date.data,
            mood=form.mood.data,
            steps=form.steps.data,
            notes=form.notes.data
        )
        db.session.add(entry)
        db.session.commit()
        return redirect("/wellness")
    return render_template("wellness_add.html", form=form)


# ==================== EVENTS BLUEPRINT ====================
event_bp = Blueprint("events", __name__)

@event_bp.route("/")
def events():
    events = Event.query.all()
    return render_template("events.html", events=events)

@event_bp.route("/add", methods=["GET", "POST"])
def add_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(
            title=form.title.data,
            description=form.description.data,
            event_date=form.event_date.data,
            location=form.location.data
        )
        db.session.add(event)
        db.session.commit()
        return redirect("/events")
    return render_template("events_add.html", form=form)


# ==================== FORUM BLUEPRINT ====================
forum_bp = Blueprint("forum", __name__)

@forum_bp.route("/")
def forum():
    posts = ForumPost.query.all()
    return render_template("forum.html", posts=posts)

@forum_bp.route("/add", methods=["GET", "POST"])
def add_post():
    form = ForumForm()
    if form.validate_on_submit():
        post = ForumPost(
            username=form.username.data,
            title=form.title.data,
            content=form.content.data
        )
        db.session.add(post)
        db.session.commit()
        return redirect("/forum")
    return render_template("forum_add.html", form=form)


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
