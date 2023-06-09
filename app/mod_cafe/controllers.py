import json

from flask import Blueprint, jsonify, request
from sqlalchemy import exists

from app.mod_cafe.models import Users
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
        'name': name
        'dishes': [dish for dishes in types for types in dish_types]
    })

def index():
    cafe1 = Cafes(image='фішка.jpeg',name='Фішка',dishes=dish_types1)
    })
