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

@mod_dish.route('dish/choose_dish', method=['POST'])
def choose_dish():
    all_dishes = json.loads(request.data)
    my_dishes = all_dishes['objects']
    chosen_dishes = Dish.query.filter(Dish.id.in_([dish['id'] for dish in my_dishes])).all()
    matching_dishes = [dish for dish in my_dishes if dish['id'] in [db_dish.id for db_dish in chosen_dishes]]
    data = [{
        'id': dish.id,
        'name': dish.name,
        'price': dish.price,
        'picture': dish.picture,
        'cafe_id': cafe_id,
        'type_id': type_id,
        'is_chosen': True
    } for dish in matching_dishes]
    return jsonify(data)
