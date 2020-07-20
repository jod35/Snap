from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from snap.users.views import user_bp
from .config import DevConfig

app=Flask(__name__)

app.config.from_object(DevConfig)

db=SQLAlchemy(app)

login_manager=LoginManager()
login_manager.init_app(app)

from snap.users.models import User as user_model

@login_manager.user_loader
def load_user(user_id):
    return user_model.query.get(int(user_id))

app.register_blueprint(user_bp,url_prefix='/users')