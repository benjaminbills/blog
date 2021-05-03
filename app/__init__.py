from flask import Flask
from flask_login import LoginManager
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_simplemde import SimpleMDE
from flask_mail import Mail


login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"
mail = Mail()
db = SQLAlchemy()

csrf = CSRFProtect()
simple = SimpleMDE()


def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing DATABASE.
    db.init_app(app)

    simple.init_app(app)

    # Intializing Login Manager
    login_manager.init_app(app)
    # Registering the blueprint
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)
    # authentication blueprint
    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    # setting config
    from .requests import configure_request

    mail.init_app(app)
    configure_request(app)
    csrf.init_app(app)
    return app
