import json

from flask import Blueprint, jsonify, request
from sqlalchemy import exists

from app.mod_authentification.models import Users
from app import db

mod_authentification = Blueprint('authentification', __name__, url_prefix='/authentification')
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
    password = data.get('password')
    model = Users(email=email, password=password)
    user = db.session.query(Users).filter_by(email=email, password=password).first()
    if user:
        return jsonify({
            'email': email,
            'username': user.username,
            'password': password,
            'success': True,
            'message': 'You have been logged in successfully'
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Wrong email or password'
        })
