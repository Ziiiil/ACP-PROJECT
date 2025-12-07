from flask import Blueprint, render_template, redirect
from models.wellness_model import WellnessEntry
from models import db
from forms.wellness_form import WellnessForm

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
