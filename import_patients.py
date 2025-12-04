import csv
from app import create_app
from app.mongo import get_mongo_db

app = create_app()

CSV_FILE = "stroke-data.csv"

with app.app_context():
    db = get_mongo_db()

    with open(CSV_FILE, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        patients = []

        for row in reader:
            # Convert numeric fields to correct types
            row["age"] = float(row["age"])
            row["avg_glucose_level"] = float(row["avg_glucose_level"])
            bmi_value = row["bmi"].strip()
            row["bmi"] = float(bmi_value) if bmi_value not in ("", "N/A", "NA", "n/a") else None


            # Convert hypertension & heart_disease to int
            row["hypertension"] = int(row["hypertension"])
            row["heart_disease"] = int(row["heart_disease"])

            patients.append(row)

        if patients:
            db.patients.insert_many(patients)
            print(f"Inserted {len(patients)} patients!")
        else:
            print("No patients found in CSV.")
