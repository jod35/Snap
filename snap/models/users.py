from flask_login import UserMixin
from snap.utils.database import db
from snap.utils.logins import login_manager
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model,UserMixin):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(25),nullable=False)
    email=db.Column(db.String(80),nullable=False)
    password=db.Column(db.Text())

    # def __init__(self,username,email,password):
    #     self.username=username
    #     self.email=email
    #     self.password=password

    def __repr__(self):
        return f"{self.username}'s password"


    def create(self):
        db.session.add(self)
        db.session.commit()

    def generate_password(self,password):
        self.password=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)
    

    @classmethod
    def get_by_username(cls,username):
        return cls.query.filter_by(username=username).first()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))