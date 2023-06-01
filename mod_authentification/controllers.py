from flask import Blueprint, jsonify, request

from app.mod_authentification.models import Users

mod_authentification = Blueprint('authentification', __name__, url_prefix='/authentification')

@mod_authentification.route('/authentification', methods=['POST'])
@mod_authentification.route('/', methods=['POST'])
def add_user():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    model = new Users({email, username, password})
    model.save()

    return jsonify({
        'username': username,
        'email ': email,
        'message': 'You have been registered successfully'
    })
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
    
