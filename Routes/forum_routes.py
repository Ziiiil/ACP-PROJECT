from flask import Blueprint, render_template, redirect
from models.forum_model import ForumPost
from models import db
from forms.forum_form import ForumForm

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
