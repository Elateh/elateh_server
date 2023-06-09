import json

from flask import Blueprint, jsonify, request
from sqlalchemy import exists

from app.mod_dish.models import Dishes
from app import db

mod_dish = Blueprint('dish', __name__, url_prefix='/dish')
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Method', 'GET, POST, OPTIONS')
    return response

def index():
    with app.app_context():
        dish111=Dishes(name='Шаурма ВЕГАН - фалафель з овочами гриль (370 г)', price=80, image='шаурма1.jpeg')
        dish112=Dishes(name='Шаурма курка з шинкою в кисло-солодкому соусі (420 г)', price=100, image='шаурма2.jpeg')
        dish113=Dishes(name='Шаурма свинина з беконом під соусом BBQ (430 г', price=100)
        db.session.add(dish111)
        db.session.add(dish112)
        db.session.commit()
