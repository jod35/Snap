from snap import db,login_manager
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(25),nullable=False)
    email=db.Column(db.String(80),nullable=False)
    password=db.Column(db.Text())

    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.password=password

    def __repr__(self):
        return f"{self.username}'s password"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
