from flask import Blueprint
from flask_restplus import Api

student_add = Blueprint("student_add", __name__, url_prefix='/api/v1')
api = Api(student_add)