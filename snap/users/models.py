from datetime import datetime
from snap import db

#the user model

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(25),nullable=False)
    email=db.Column(db.String(80),nullable=False)
    password=db.Column(db.Text,nullable=False)
    created_on=db.Column(db.DateTime,default=datetime.utcnow)

    def __init__(self,username,email,password,created_on):
        self.username=username
        self.email=email
        self.password=password
        self.created_on=created_on


    def __repr__(self):
        return f"{self.username}'s Account"


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id