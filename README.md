# Healthcare Flask App
# 🏥 Healthcare Patient Management System  
### Secure Flask Web Application | MongoDB + SQLite | Authentication | Dashboard Analytics

## 📌 Overview
This project is a **secure healthcare data management system** built using **Flask**, supporting:
- 🔐 Secure user authentication (SQLite)
- 🗄️ Patient record management (MongoDB)
- ✏️ CRUD operations for patient data
- 📊 Analytics dashboard with gender distribution, hypertension, heart disease stats
- ⚡ Secure coding practices (CSRF protection, password hashing, input validation)
- 🧪 Unit testing structure
- 🛡 Ethical handling of sensitive health data

This system follows **professional software engineering practices**, including:
- Modular architecture  
- Proper session handling  
- Separation of concerns (auth vs patient management)  
- Version control (GitHub)  

---

# 🚀 Features

### 👤 User Authentication (SQLite)
- Registration & Login
- Password hashing using **Flask-Bcrypt**
- CSRF protection with **Flask-WTF**
- Secure session handling

### 🩺 Patient Management (MongoDB)
- Import patient dataset (CSV → MongoDB)
- Add, edit, view, delete patient records
- Pagination & improved UI
- Data validation

### 📊 Dashboard & Analytics
The dashboard displays:
- Total patients
- Average age
- Gender distribution (Male/Female/Other/Unknown)
- Hypertension count
- Heart disease count

 ### Project Structure Section
 project/
│── app/
│   ├── auth/
│   ├── patients/
│   ├── main/
│   ├── templates/
│   ├── static/
│   ├── mongo.py
│   ├── __init__.py
│── import_patients.py
│── requirements.txt
│── README.md


---




