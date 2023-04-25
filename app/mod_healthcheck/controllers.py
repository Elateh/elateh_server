from flask import Blueprint, jsonify, request
import time

from app.mod_healthcheck.models import Healthcheck

mod_healthcheck = Blueprint('healthcheck', __name__, url_prefix='/healthcheck')

@mod_healthcheck.route('/healthcheck', methods=['GET'])
@mod_healthcheck.route('/', methods=['GET'])
def findAll():
    startTime = time.time()
    data = [{
        'version': healthcheck.version,
        'name': healthcheck.name
    } for healthcheck in Healthcheck.query.all()]
    healthcheck_data = data[0]
    healthcheck_data['uptime'] = time.time() - startTime
    healthcheck_data['status'] = 'online'

    return  jsonify(healthcheck_data)