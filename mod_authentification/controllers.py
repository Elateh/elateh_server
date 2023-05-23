from flask import Blueprint, jsonify, request

from app.mod_authentification.models import Users

mod_authentification = Blueprint('authentification', __name__, url_prefix='/authentification')

@mod_authentification.route('/authentification', methods=['POST'])
@mod_authentification.route('/', methods=['POST'])
def add_user():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    model = Users({email, username, password})
    model.save()

    return jsonify({
        'username': username,
        'email ': email,
        'message': 'You have been registered successfully'
    })
