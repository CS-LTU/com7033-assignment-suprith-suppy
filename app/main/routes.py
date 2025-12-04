from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.mongo import get_mongo_db

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("main/index.html")


@main_bp.route("/dashboard")
@login_required
def dashboard():
    db = get_mongo_db()
    patients = list(db.patients.find())

    # SAFE field extraction
    ages = [p.get("age", 0) for p in patients]
    genders = [p.get("gender", "Unknown") for p in patients]

    import statistics
    avg_age = statistics.mean(ages) if ages else 0

    from collections import Counter
    gender_counts = Counter(genders)

    hypertension = sum(1 for p in patients if str(p.get("hypertension", "0")) == "1")
    heart_disease = sum(1 for p in patients if str(p.get("heart_disease", "0")) == "1")

    return render_template(
        "main/dashboard.html",
        total=len(patients),
        avg_age=avg_age,
        gender_counts=gender_counts,
        hypertension=hypertension,
        heart_disease=heart_disease
    )
