##🏥 Healthcare Flask App
Healthcare Patient Management System

Secure Flask Web Application | MongoDB + SQLite | Authentication | Dashboard Analytics | Unit Testing

📌 Overview

This project is a secure, full-stack healthcare data management system built using Flask, integrating both MongoDB (for patient data) and SQLite (for user authentication).

The system allows healthcare professionals to log in, manage patients, analyze trends, and ensure secure handling of sensitive medical data.

This application supports:

🔐 Secure user authentication (SQLite + Flask-Login)

🗄️ Patient record management (MongoDB)

✏️ Full CRUD operations (Create, Read, Update, Delete)

📊 Analytics dashboard (age averages, gender distribution, hypertension & heart disease stats)

⚡ Secure coding practices (CSRF protection, bcrypt hashing, safe data handling)

🧪 Automated Unit Testing (pytest)

🛡 Ethical handling of health data following best practices

🚀 Features
👤 User Authentication (SQLite)

User Registration

Secure Login / Logout

Password hashing using Flask-Bcrypt

CSRF Protection (Flask-WTF)

Session management with Flask-Login

🩺 Patient Management (MongoDB)

Add New Patient

Edit Patient

View Patient Details

Delete Patient

Search & Pagination

Import patient dataset from CSV → MongoDB

Clean and accessible UI

📊 Dashboard & Analytics

The dashboard displays:

👥 Total number of patients

📈 Average patient age

🚻 Gender distribution (Male / Female / Other / Unknown)

❤️ Hypertension count

💓 Heart disease count

Displayed using responsive cards and modern UI styling.

📁 Project Structure
project/
│── app/
│   ├── auth/              # Authentication (login, register)
│   ├── patients/          # CRUD patient management
│   ├── main/              # Dashboard, homepage
│   ├── templates/         # Jinja2 HTML templates
│   ├── static/            # CSS, JS, images
│   ├── mongo.py           # MongoDB connection handler
│   ├── __init__.py        # App factory
│
│── import_patients.py     # CSV → MongoDB import script
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
│── tests/                 # Unit tests (pytest)

🧪 Unit Testing 

Unit tests are implemented using pytest.

Included Tests:

✔ Register page loads
✔ Login page loads
✔ Valid login test
✔ Invalid login test


🛡 Security Practices Implemented

❗ No plain-text passwords (bcrypt hashing)

🛡 CSRF protection for all form submissions

🔐 Session cookies secured

🧹 Input validation + safe rendering

✔ Ethical handling: No unnecessary patient data exposure

👤 Author

SUPRITH PATLOLLA
LEEDS TRINITY UNIVERSITY
MODULE — COM7033: SECURE SOFTWARE DEVELOPMENT



