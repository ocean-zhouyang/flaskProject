from flask import Blueprint
from flask_restplus import Api

teacher_blueprint = Blueprint("teacher_blueprint", __name__, url_prefix='/api/teacher')
teacher_api = Api(teacher_blueprint)
