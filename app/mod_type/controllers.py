import json
from flask import Blueprint, jsonify, request

from app import db
from app.mod_cafe.controllers import mod_cafe
from app.utils import object_as_dict
from app.mod_type.models import TypeOfDish
from app.mod_dish.models import Dish

mod_type = Blueprint('type', __name__, url_prefix='/type')

@mod_cafe.route('/type_', methods=['GET'])
def get_types():
    data = [{
        'id': type_.id,
        'name': type_.name,
        'cafe_id': type_.cafe_id,
    } for type_ in TypeOfDish.query.all()]
    return jsonify(data)

@mod_type.route('/type', methods=['POST'])
def create_type():
    data = json.loads(request.data)

    name = data.get('name')
    cafe_id = data.get('cafe_id')

    model = TypeOfDish()
    model.name = name
    model.cafe_id = cafe_id

    db.session.add(model)
    db.session.commit()

    id = model.id
    return jsonify({
        'id': id,
        'cafe_id': cafe_id,
        'name': name
    })

@mod_type.route('/type/<int:type_id>', methods=['GET'])
def get_type(type_id):
    query = TypeOfDish.query.filter_by(id=type_id).first()
    return object_as_dict(query)

@mod_cafe.route('/type/<int:type_id>/dishes', methods=['GET'])
def get_dishes_of_type(type_id):
    query = Dish.query.filter_by(type_id=type_id).all()

    data = [{
        'id': dish.id,
        'name': dish.name,
        'price': dish.price,
        'picture': dish.picture,
    } for dish in query]
    return jsonify(data)