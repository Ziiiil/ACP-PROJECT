from flask import Blueprint, render_template, redirect
from Models.event_model import Event
from Models import db
from Forms.event_form import EventForm

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
