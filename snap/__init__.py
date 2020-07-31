from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from snap.users.views import user_bp
from .config import DevConfig
from snap.utils.database import db
from snap.utils.logins import login_manager

app=Flask(__name__)

app.config.from_object(DevConfig)


login_manager.init_app(app)


app.register_blueprint(user_bp,url_prefix='/users')