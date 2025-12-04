from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField,
    IntegerField, FloatField, SelectField
)
from wtforms.validators import DataRequired, Email, Length, EqualTo


# -------------------------
# USER AUTH FORMS
# -------------------------

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirm = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


# -------------------------
# PATIENT FORM
# -------------------------

class PatientForm(FlaskForm):
    patient_id = IntegerField("Patient ID")
    age = FloatField("Age", validators=[DataRequired()])
    gender = SelectField("Gender", choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    hypertension = SelectField("Hypertension", choices=[("0", "No"), ("1", "Yes")])
    heart_disease = SelectField("Heart Disease", choices=[("0", "No"), ("1", "Yes")])
    ever_married = SelectField("Ever Married", choices=[("No", "No"), ("Yes", "Yes")])
    work_type = StringField("Work Type", validators=[DataRequired()])
    residence_type = SelectField("Residence Type", choices=[("Urban", "Urban"), ("Rural", "Rural")])
    avg_glucose_level = FloatField("Average Glucose Level", validators=[DataRequired()])
    bmi = FloatField("BMI", validators=[DataRequired()])
    smoking_status = StringField("Smoking Status", validators=[DataRequired()])
    submit = SubmitField("Save")
