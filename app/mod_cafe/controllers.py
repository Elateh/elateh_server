import json

import app
from flask import Blueprint, jsonify, request
from sqlalchemy import exists

from app.mod_cafe.models import Cafes
from app.mode_dishes.models import Dishes
from app import db

mod_authentification = Blueprint('cafe', __name__, url_prefix='/cafe')
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Method', 'GET, POST, OPTIONS')
    return response

@mod_cafe.route('/cafe', methods=['POST'])
@mod_cafe.route('/', methods=['POST'])
def return_cafe():
    return jsonify({
        'picture': picture,
        'name': name,
        'dishes': [dish for dishes in types for types in dish_types]
    })

def index():
    with app.app_context():
        dish_types1 = {'Лаваші': dish_list1, 'Хот-доги': dish_list2, 'Напої': dish_list3}
        dish_list1 = [dish111, dish112, dish113]
        dish_list2 = [Dishes()]
        dish_list3 = [Dishes()]
        group = Group(name='Group 1', dishes=dish_types)
        cafe1 = Cafes(image='фішка.jpeg',name='Фішка',dishes=dish_types1)
        db.session.add(cafe1)
        db.session.commit()
