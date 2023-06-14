import json

from flask import Blueprint, jsonify, request

from app.mod_dish.models import Dish
from app import db

mod_dish = Blueprint('dish', __name__, url_prefix='/dish')
@mod_dish.route('/dish', methods=['POST'])
def create_dish():
    data = json.loads(request.data)

    name = data.get('name')
    picture = data.get('picture')
    price = data.get('price')
    cafe_id = data.get('cafe_id')
    type_id = data.get('types_id')

    model = Dish()
    model.price = price
    model.name = name
    model.picture = picture
    model.cafe_id = cafe_id
    model.type_id = type_id
    model.is_chosen = False

    db.session.add(model)
    db.session.commit()

    id = model.id
    return jsonify({
        'id': id,
        'picture': picture,
        'name': name,
        'price': price,
        'cafe_id': cafe_id,
        'type_id': type_id,
        'is_chosen': is_chosen
    })
