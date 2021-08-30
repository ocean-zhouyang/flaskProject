from flask_restplus import fields

from app.student import student_api

create_student_form_model = student_api.model('createStudentFormModel', {
    'id': fields.Integer(required=False, description='id'),
    'name': fields.String(required=True, description='姓名'),
    'age': fields.Integer(required=True, description='年龄'),
    'address': fields.String(required=True, description='地址'),
    'teacher_id': fields.Integer(required=False, description='关联教师id')
})