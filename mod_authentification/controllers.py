from flask import Blueprint, jsonify, request

from app.mod_authentification.models import Users

mod_healthcheck = Blueprint('authentification', __name__, url_prefix='/authentification')

@mod_authentification.route('/authentification', methods=['POST'])
@mod_hauthentification.route('/', methods=['POST'])
def addUser():
    data = [{
        'email': request.email,
        'username': request.username,
        'password': request.password
    } for authentification in Users.query.all()]
    authentification_data = data[0]

    return  jsonify(authentification_data)