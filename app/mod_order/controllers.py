import json

from flask import Blueprint, jsonify, request
from datetime import datetime

from app.mod_order.models import Order
from app import db

mod_order = Blueprint('order', __name__, url_prefix='/order')
@mod_order.route('/order', methods=['POST'])
def make_order():
    data = json.loads(request.data)

    cafe_id = data.get('cafe_id')
    dish_id = data.get('dish_id')
    type_id = data.get('type_id')
    user_id = data.get('user_id')

    model = Order()
    model.cafe_id = cafe_id
    model.dish_id = dish_id
    model.type_id = type_id
    model.user_id = user_id
    model.date = datetime.now()

    db.session.add(model)
    db.session.commit()

    id = model.id
    return jsonify({
        'id': id,
        'cafe_id': cafe_id,
        'dish_id': dish_id,
        'type_id': type_id,
        'user_id': user_id,
        'date': date
    })