from flask import Blueprint
from flask_restplus import Api

user_blueprint = Blueprint("user_blueprint", __name__, url_prefix='/api/user')
user_api = Api(user_blueprint)
