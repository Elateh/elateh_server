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
    dish_types1={'Лаваші': dish_list1, 'Хот-доги': dish_list2, 'Напої': dish_list3}
    dish_list1=[Dishes(name='Шаурма ВЕГАН - фалафель з овочами гриль (370 г)', price=80, image='шаурма1.jpeg'),
                Dishes(name='Шаурма курка з шинкою в кисло-солодкому соусі (420 г)', price=100, image='шаурма2.jpeg')]
    dish_list2=[Dishes()]
    dish_list3=[Dishes()]
    group = Group(name='Group 1', dishes=dish_types1)
    db.session.add(group)
    db.session.commit()
    group = Group.query.first()
    dises = group.dishes