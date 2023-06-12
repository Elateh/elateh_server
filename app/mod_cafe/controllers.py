import json
from flask import Blueprint, jsonify, request

from app import db
from app.utils import object_as_dict
from app.mod_cafe.models import Cafe
from app.mod_dish.models import Dish

mod_cafe = Blueprint('cafe', __name__, url_prefix='/cafe')

@mod_cafe.route('/cafe', methods=['GET'])
def get_cafes():
    data = [{
        'id': cafe.id,
        'name': cafe.name,
        'picture': cafe.picture,
    } for cafe in Cafe.query.all()]
    return jsonify(data)

@mod_cafe.route('/cafe', methods=['POST'])
def create_cafe():
    data = json.loads(request.data)

    name = data.get('name')
    picture = data.get('picture')

    model = Cafe()
    model.name = name
    model.picture = picture

    db.session.add(model)
    db.session.commit()

    id = model.id
    return jsonify({
        'id': id,
        'picture': picture,
        'name': name
    })

@mod_cafe.route('/cafe/<int:cafe_id>', methods=['GET'])
def get_cafe(cafe_id):
    query = Cafe.query.filter_by(id=cafe_id).first()

    print(query)

    # data = [{
    #     'id': cafe.id,
    #     'name': cafe.name,
    #     'picture': cafe.picture,
    # } for cafe in query]
    return object_as_dict(query)

@mod_cafe.route('/cafe/<int:cafe_id>/dishes', methods=['GET'])
def get_cafe_dishes(cafe_id):
    query = Dish.query.filter_by(cafe_id=cafe_id).all()

    data = [{
        'id': dish.id,
        'name': dish.name,
        'price': dish.price,
        'picture': dish.picture,
    } for dish in query]
    return jsonify(data)