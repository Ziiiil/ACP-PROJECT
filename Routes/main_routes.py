from flask import Blueprint, render_template

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
