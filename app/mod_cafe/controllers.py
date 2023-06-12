import json
from flask import Blueprint, jsonify, request

from app import db
from app.mod_cafe.models import Cafe

mod_cafe = Blueprint('cafe', __name__, url_prefix='/cafe')

@mod_cafe.route('/cafe', methods=['GET'])
def get_cafes():
    data = [{
        'id': collaborator.id,
        'name': collaborator.name,
        'picture': collaborator.picture,
    } for collaborator in Cafe.query.all()]
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