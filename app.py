from flask import Flask, Blueprint, render_template, redirect, flash, request, url_for
from models import db, Event, WellnessEntry, ForumPost, Comment
from flask_wtf.csrf import CSRFProtect
from forms import EventForm, WellnessForm, ForumForm, CommentForm
import os


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'final_project_db.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "supersecretkey123"


csrf = CSRFProtect()


main_bp = Blueprint("main", __name__)
wellness_bp = Blueprint("wellness", __name__)
event_bp = Blueprint("events", __name__)
forum_bp = Blueprint("forum", __name__)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        db.create_all()


    app.register_blueprint(main_bp)
    app.register_blueprint(wellness_bp, url_prefix="/wellness")
    app.register_blueprint(event_bp, url_prefix="/events")
    app.register_blueprint(forum_bp, url_prefix="/forum")

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404

    return app



@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/health")
def health():
    return render_template("health.html")

@main_bp.route("/livelihood")
def livelihood():
    return render_template("livelihood.html")



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
        flash("Wellness entry added!", "success")
        return redirect(url_for("wellness.list_entries"))
    return render_template("wellness_add.html", form=form)


@wellness_bp.route("/edit/<int:entry_id>", methods=["GET", "POST"])
def edit_wellness(entry_id):
    entry = WellnessEntry.query.get_or_404(entry_id)
    form = WellnessForm(obj=entry)
    if form.validate_on_submit():
        entry.date = form.date.data
        entry.mood = form.mood.data
        entry.steps = form.steps.data
        entry.notes = form.notes.data
        db.session.commit()
        flash("Wellness entry updated!", "success")
        return redirect(url_for("wellness.list_entries"))
    return render_template("wellness_edit.html", form=form, entry=entry)


@wellness_bp.route("/delete/<int:entry_id>", methods=["POST"])
def delete_wellness(entry_id):
    entry = WellnessEntry.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted!", "success")
    return redirect(url_for("wellness.list_entries"))



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
        flash("Event added successfully!", "success")
        return redirect(url_for("events.events"))
    return render_template("events_add.html", form=form)


@event_bp.route("/edit/<int:event_id>", methods=["GET", "POST"])
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)
    form = EventForm(obj=event)
    if form.validate_on_submit():
        event.title = form.title.data
        event.description = form.description.data
        event.event_date = form.event_date.data
        event.location = form.location.data
        db.session.commit()
        flash("Event updated!", "success")
        return redirect(url_for("events.events"))
    return render_template("events_edit.html", form=form, event=event)


@event_bp.route("/delete/<int:event_id>", methods=["POST"])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    flash("Event deleted!", "success")
    return redirect(url_for("events.events"))



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
        flash("Post created successfully!", "success")
        return redirect(url_for("forum.forum"))
    return render_template("forum_add.html", form=form)



@forum_bp.route("/<int:post_id>/comment", methods=["POST"])
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

    return redirect(url_for("forum.forum"))



@forum_bp.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit_forum(post_id):
    post = ForumPost.query.get_or_404(post_id)
    form = ForumForm(obj=post)
    if form.validate_on_submit():
        post.username = form.username.data
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Post updated!", "success")
        return redirect(url_for("forum.forum"))
    return render_template("forum_edit.html", form=form, post=post)



@forum_bp.route("/delete/<int:post_id>", methods=["POST"])
def delete_forum(post_id):
    post = ForumPost.query.get_or_404(post_id)
    Comment.query.filter_by(forum_post_id=post_id).delete()
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted!", "success")
    return redirect(url_for("forum.forum"))



@forum_bp.route("/comment/edit/<int:comment_id>", methods=["GET", "POST"])
def edit_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    form = CommentForm(obj=comment)

    if form.validate_on_submit():
        comment.username = form.username.data
        comment.content = form.content.data
        db.session.commit()
        flash("Comment updated!", "success")
        return redirect(url_for("forum.forum"))

    return render_template("comment_edit.html", form=form, comment=comment)



@forum_bp.route("/comment/delete/<int:comment_id>", methods=["POST"])
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    flash("Comment deleted!", "success")
    return redirect(url_for("forum.forum"))



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
