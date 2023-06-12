import json

from flask import Blueprint, jsonify, request

from app import db
from app.mod_auth.models import Users

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

@mod_auth.route('/auth/sign-up', methods=['POST'])
def add_user():
    data = json.loads(request.data)
    email = data.get('email')
    password = data.get('password')

    model = Users()
    model.email=email
    model.password=password

    db.session.add(model)
    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'You have been registered successfully'
    })

@mod_auth.route('/auth/login', methods=['POST'])
def log_in():
    data = json.loads(request.data)
    email = data.get('email')
    password = data.get('password')
    user = db.session.query(Users).filter_by(email=email, password=password).first()
    if user:
        return jsonify({
            'email': email,
            'success': True,
            'message': 'You have been logged in successfully'
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Wrong email or password'
        })
