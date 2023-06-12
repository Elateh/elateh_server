from app import db

class Cafe(db.Model):
    __tablename__ = 'cafes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, unique=False, nullable=False)
    picture = db.Column(db.Text, unique=False, nullable=True)
