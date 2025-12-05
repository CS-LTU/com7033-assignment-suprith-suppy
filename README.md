# 🏥 Healthcare Flask App
## Healthcare Patient Management System

**Secure Flask Web Application | MongoDB + SQLite | Authentication | Dashboard Analytics | Unit Testing**

---

## 📌 Overview

This project is a **secure, full-stack healthcare data management system** built using **Flask**, integrating:

- **MongoDB** → Patient data storage  
- **SQLite** → User authentication system  

The system enables healthcare professionals to:

- Log in securely  
- Manage patient information  
- Perform CRUD operations  
- View an analytics dashboard  
- Ensure ethical and secure handling of medical records  

---

## 🚀 Features

### 🔐 Secure User Authentication (SQLite + Flask-Login)

- User Registration  
- User Login & Logout  
- Password hashing using **Flask-Bcrypt**  
- CSRF protection with **Flask-WTF**  
- Session management  

---

### 🩺 Patient Management (MongoDB)

Full CRUD functionality:

- ➕ Add new patient  
- ✏️ Edit patient details  
- 👁️ View patient  
- ❌ Delete patient  
- 🔍 Search patients  
- 📄 Pagination  
- 📥 Import CSV dataset → MongoDB  
- Responsive and accessible UI  

---

### 📊 Dashboard & Analytics

The dashboard visually displays patient trends:

- 👥 Total number of patients  
- 📈 Average age  
- 🚻 Gender distribution  
- ❤️ Hypertension count  
- 💓 Heart disease count  

---

## 📁 Project Structure

project/
│── app/
│ ├── auth/ # Login, Register, Authentication logic
│ ├── patients/ # CRUD patient management
│ ├── main/ # Dashboard, Index routes
│ ├── templates/ # Jinja2 HTML templates
│ ├── static/ # Images, CSS, JS
│ ├── mongo.py # MongoDB connection functions
│ ├── init.py # Flask app factory
│
│── import_patients.py # CSV → MongoDB import script
│── requirements.txt # Python dependencies
│── tests/ # Unit tests (pytest)
│── README.md # Project documentation


---

## 🧪 Unit Testing

Unit tests are implemented using **pytest**.

### ✔ Included Tests

- Register page loads  
- Login page loads  
- Valid login test  
- Invalid login test  

### ▶ Run tests:


All tests pass successfully.

---

## 🛡 Security Practices Implemented

### 🔒 Password Security
- Password hashing using bcrypt  
- No plain-text password storage  

### 🛡 Form & CSRF Security
- CSRF protection enabled  
- Input validation  

### 🔐 Session Security
- Secure session cookies  
- Restricted access to dashboard and patient pages  

### 📘 Ethical Data Handling
- No unnecessary exposure of patient details  
- Sensitive data minimized everywhere possible  

---

## 🛠 Technologies Used

| Component | Technology |
|----------|------------|
| Backend Framework | Flask |
| Database (Users) | SQLite |
| Database (Patients) | MongoDB |
| Authentication | Flask-Login |
| Form Security | Flask-WTF |
| Password Security | Bcrypt |
| UI Framework | Bootstrap |
| Testing | pytest |
| Version Control | Git & GitHub |

---

### 3️⃣ Open in Browser

http://127.0.0.1:5000/


---

## 📤 GitHub Submission Status

Your repository now includes:

✔ Source Code  
✔ Working Flask Application  
✔ CRUD Patient Management  
✔ MongoDB + SQLite Integration  
✔ Unit Tests (All Passed)  
✔ README Documentation  
✔ Requirements.txt  

Your project is **ready for Phase 2 assessment submission**.

---

## 👤 Author

**SUPRITH PATLOLLA**  
*Leeds Trinity University*  
**Module: COM7033 — Secure Software Development**

---







