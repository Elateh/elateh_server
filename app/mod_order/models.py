from app import db
from sqlalchemy import ForeignKey

class Order(db.Model):
    __tablename__ = 'cafes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cafe.id = db.Column(db.Integer, ForeignKey('cafes.id'))
    dish.id = db.Column(db.Integer, ForeignKey('dishes.id'))
    user.id = db.Column(db.Integer, ForeignKey('users.id'))
    date = db.Column(db.Datetime)
