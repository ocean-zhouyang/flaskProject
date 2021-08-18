from flask import Blueprint
from flask_restplus import Api

student_blueprint = Blueprint("student_blueprint", __name__, url_prefix='/api/student')
student_api = Api(student_blueprint)
