from sqlalchemy import ForeignKey
from app import db

class Dish(db.Model):
    __tablename__ = 'dishes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, unique=False, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    picture = db.Column(db.Text, unique=False, nullable=False)
    cafe_id = db.Column(db.Integer, ForeignKey('cafes.id'))
