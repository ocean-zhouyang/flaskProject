from flask import request

from app.models.request_params import create_student_form_model
from app.models.student import Student
from flask_restplus import Namespace, Resource

from app.dao.StudentDao import ProcessStudentDao

student_ns = Namespace(name='student_ns', description='学生管理模块')


@student_ns.route('/addStudent')
class CreateStudent(Resource):
    @student_ns.expect(create_student_form_model, validate=False)
    def post(self):
        """
        新增学生
        """
        param = request.json
        # student = {'name': param.get('name', None),
        #            'age': int(param.get('age', None)),
        #            'address': param.get('address', None),
        #            'teacher_id': int(param.get('teacher_id', None))}

        student = Student(param.get('name', None), int(param.get('age', None)), param.get('address', None), int(param.get('teacher_id', None)))

        ProcessStudentDao.insertStudent(student)
        return "add_student"