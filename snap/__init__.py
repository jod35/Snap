from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from snap.users.views import user_bp
from .config import DevConfig
from snap.utils.database import db
from snap.utils.logins import login_manager
from snap.models.users import User

app=Flask(__name__)

app.config.from_object(DevConfig)

db.init_app(app)
login_manager.init_app(app)


app.register_blueprint(user_bp,url_prefix='/users')


@app.shell_context_processor
def make_shell_context():
    return {
        'db':db,
        'user_model':User,
        'app':app
    }