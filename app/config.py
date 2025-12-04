import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_key_change_me")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'users.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "healthcare_db")

    WTF_CSRF_ENABLED = True

    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    # In production, also:
    # SESSION_COOKIE_SECURE = True
