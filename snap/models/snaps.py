from snap.utils.database import db

class Snap(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    content=db.Column(db.Text,nullable=False)
    description=db.Column(db.Text,nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()

        