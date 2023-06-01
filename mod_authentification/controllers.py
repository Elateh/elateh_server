import json

from flask import Blueprint, jsonify, request

from app.mod_authentification.models import Users

mod_healthcheck = Blueprint('authentification', __name__, url_prefix='/authentification')
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Method', 'GET, POST, OPTIONS')
    return response

@mod_authentification.route('/authentification', methods=['POST'])
@mod_authentification.route('/', methods=['POST'])
def add_user():
    data = json.loads(request.data)
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    model = Users(email=email, username=username, password=password)
    db.session.add(model)
    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'You have been registered successfully'
    })

@mod_authentification.route('/login', methods=['POST'])
def log_in():
    data = json.loads(request.data)
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    model = Users(email=email, username=username, password=password)
    if db.session.query(exists().where(Users == model)):
        return jsonify({
            'username': username,
            'password': password,
            'success': True,
            'message': 'You have been logged in successfully'
        })
