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
        'date': model.date,
        'quantity': quantity
    })


@mod_order.route('/order/remove_order', methods=['POST'])
def remove_order():
    data = json.loads(request.data)
    orders = data['orders']
    order = data['order']

    found_order = None
    for item in orders:
        if (item['id'] == order['id'] and
                item['typeId'] == order['typeId'] and
                item['institutionID'] == order['institutionID'] and
                item['typeOfInstitution'] == order['typeOfInstitution']):
            found_order = item
            break

    if found_order:
        if order['quantity'] == 1:
            orders.remove(found_order)
        else:
            found_order['quantity'] -= 1
        return jsonify({'orders': orders})
    else:
        return jsonify({'message': 'Order not found'})


@mod_order.route('/order/add_order', methods=['POST'])
def add_order():
    data = json.loads(request.data)
    print(data)
    orders = data['orders']
    order = data['order']

    found_order = None
    for item in orders:
        if (item['id'] == order['id'] and
                item['typeId'] == order['typeId'] and
                item['institutionID'] == order['institutionID'] and
                item['typeOfInstitution'] == order['typeOfInstitution']):
            found_order = item
            break

    if found_order:
        found_order['quantity'] += 1
    else:
        orders.append(order)

    return jsonify({'orders': orders})