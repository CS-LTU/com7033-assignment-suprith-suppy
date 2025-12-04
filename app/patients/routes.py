from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from bson.objectid import ObjectId
from app.mongo import get_mongo_db
from app.forms import PatientForm

patients_bp = Blueprint("patients", __name__, url_prefix="/patients")


@patients_bp.route("/")
@login_required
def list_patients():
    db = get_mongo_db()

    # --- FILTERS ---
    search = request.args.get("search", "").strip()
    gender = request.args.get("gender", "")
    hypertension = request.args.get("hypertension", "")
    sort = request.args.get("sort", "age")  # default sort by age
    order = request.args.get("order", "asc")

    query = {}

    if search:
        # search by patient id (in CSV it's called "id")
        query["id"] = {"$regex": search, "$options": "i"}

    if gender:
        query["gender"] = gender

    if hypertension in ("0", "1"):
        query["hypertension"] = int(hypertension)

    # --- SORTING ---
    direction = 1 if order == "asc" else -1

    # --- PAGINATION ---
    page = int(request.args.get("page", 1))
    per_page = 20
    skip = (page - 1) * per_page

    total = db.patients.count_documents(query)

    cursor = (
        db.patients.find(query)
        .sort(sort, direction)
        .skip(skip)
        .limit(per_page)
    )
    patients = list(cursor)

    return render_template(
        "patients/list.html",
        patients=patients,
        total=total,
        page=page,
        per_page=per_page,
        sort=sort,
        order=order,
        search=search,
        gender=gender,
        hypertension=hypertension,
    )

@patients_bp.route("/create", methods=["GET", "POST"])
@login_required
def create_patient():
    form = PatientForm()
    if form.validate_on_submit():
        db = get_mongo_db()
        patient = form.data.copy()
        patient.pop("submit", None)
        db.patients.insert_one(patient)
        flash("Patient added successfully.", "success")
        return redirect(url_for("patients.list_patients"))
    return render_template("patients/create.html", form=form)


@patients_bp.route("/<string:id>")
@login_required
def view_patient(id):
    db = get_mongo_db()
    patient = db.patients.find_one({"_id": ObjectId(id)})
    if not patient:
        flash("Patient not found.", "warning")
        return redirect(url_for("patients.list_patients"))
    return render_template("patients/detail.html", patient=patient)


@patients_bp.route("/<string:id>/edit", methods=["GET", "POST"])
@login_required
def edit_patient(id):
    db = get_mongo_db()
    patient = db.patients.find_one({"_id": ObjectId(id)})
    if not patient:
        flash("Patient not found.", "warning")
        return redirect(url_for("patients.list_patients"))

    form = PatientForm(data=patient)
    if form.validate_on_submit():
        updated = form.data.copy()
        updated.pop("submit", None)
        db.patients.update_one({"_id": ObjectId(id)}, {"$set": updated})
        flash("Patient updated successfully.", "success")
        return redirect(url_for("patients.view_patient", id=id))

    return render_template("patients/edit.html", form=form, patient=patient)


@patients_bp.route("/<string:id>/delete", methods=["POST"])
@login_required
def delete_patient(id):
    db = get_mongo_db()
    db.patients.delete_one({"_id": ObjectId(id)})
    flash("Patient deleted.", "info")
    return redirect(url_for("patients.list_patients"))
