from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from flask_bcrypt import Bcrypt
from .config import Config
from .mongo import close_mongo

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
bcrypt = Bcrypt()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"

    from .auth.routes import auth_bp
    from .patients.routes import patients_bp
    from .main.routes import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(patients_bp)
    app.register_blueprint(main_bp)

    app.teardown_appcontext(close_mongo)

    return app
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
