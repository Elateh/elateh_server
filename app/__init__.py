from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app.app_context().push())
app.config.from_object('config')

db: SQLAlchemy = SQLAlchemy(app)

# Import a modules using its blueprint handler variable
from app.mod_healthcheck.controllers import mod_healthcheck
from app.mod_authentification.controllers import mod_authentification
from app.mod_dish.controllers import mod_dish
from app.mod_cafe.controllers import mod_cafe

# Register blueprint(s)
app.register_blueprint(mod_healthcheck, url_prefix='/api')
app.register_blueprint(mod_authentification, url_prefix='/api')
app.register_blueprint(mod_dish, url_prefix='/api')
app.register_blueprint(mod_cafe, url_prefix='/api')

if __name__ == 'main':
    try:
        db.create_all()
        print('\n----------- All models were created/updated')
    except Exception as e:
        print('\n----------- Connection failed ! ERROR : ', e)

