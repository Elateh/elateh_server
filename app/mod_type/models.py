from sqlalchemy import ForeignKey
from app import db

class TypeOfDish(db.Model):
    __tablename__ = 'types'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, unique=False, nullable=False)
    cafe_id = db.Column(db.Integer, ForeignKey('cafes.id'))