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

    quantity = Order.query.count()
    id = model.id
    return jsonify({
        'id': id,
        'cafe_id': cafe_id,
        'dish_id': dish_id,
        'type_id': type_id,
        'user_id': user_id,
        'date': date,
        'quantity': quantity
    })

@mod_order.route('/order/<int:order_id>/<int:type_id>/<int:cafe_id>/<int:dish_id>', method=['POST'])
def remove_order(order_id, type1_id, cafe1_id, dish1_id):
    query = Order.query.filter_by(id=order_id, type_id=type1_id, cafe_id=cafe1_id, dish_id=dish1_id).first()
    db.session.delete(query)
    db.session.commit()
    quantity = Order.query.count()
    data = [{
        'id': order1_id,
        'cafe_id': cafe_id,
        'dish_id': dish_id,
        'type_id': type_id,
        'user_id': user_id,
        'date': date
    } for order1 in Order.query.all()]
    return jsonify(data), quantity

@mod_order.route('/order/<int:order_id>/<int:type_id>', method=['POST'])
def check_order(order_id, type1_id):
    query = Order.query.filter_by(id=order_id, type_id=type1_id).first()
    if query:
        return jsonify({
            'success': False
        })
    else:
        return jsonify({
            'success': True
    })
