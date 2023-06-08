from app import db
from mod_dish.models import Dishes


class Cafes(db.Model):
    __tablename__ = 'cafes'
    id = db.Column(db.Integer, autoincrement=True)
    picture = db.Column(db.File)
    name = db.Column(db.String(255), unique=True, nullable=False)
    dishes = db.relationship('Dishes', backref='group', lazy=True)
