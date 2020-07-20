from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import DevConfig
from snap.users.views import user_bp

app=Flask(__name__)
app.config.from_object(DevConfig)
db=SQLAlchemy(app)


app.register_blueprint(user_bp,url_prefix='/users')