from flask import Blueprint, render_template
from .services.engine import run_security_engine
from .models.threat import Threat

main = Blueprint("main", __name__)

@main.route("/")
def dashboard():
    run_security_engine()  # Populate DB
    threats = Threat.query.all()
    return render_template("dashboard.html", threats=threats)
