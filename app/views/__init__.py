from flask import Blueprint
from flask_restplus import Api

first_blueprint = Blueprint("first_blueprint", __name__, url_prefix='/api/v1')
api = Api(first_blueprint)