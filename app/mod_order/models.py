from app import db
from sqlalchemy import ForeignKey

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cafe_id = db.Column(db.Integer, ForeignKey('cafes.id'))
    dish_id = db.Column(db.JSON)
    type_id = db.Column(db.JSON)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    date = db.Column(db.Datetime)