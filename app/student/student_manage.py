from flask import request, g, current_app

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
        student_forms = request.json
        # student = {'name': param.get('name', None),
        #            'age': int(param.get('age', None)),
        #            'address': param.get('address', None),
        #            'teacher_id': int(param.get('teacher_id', None))}
        for param in student_forms:
            student = Student(param.get('name', None), int(param.get('age', None)), param.get('address', None), int(param.get('teacher_id', None)))
            ProcessStudentDao.insertStudent(student)

        return "add_student"


@student_ns.route('/qryStudent')
class QueryStudent(Resource):
    def post(self):
        """
        学生查询
        :return:
        """
        # return ProcessStudentDao.qryStudent()
        g.username = 'yyy'
        g.ip = '192.168.1.2'
        # print(current_app)
        return ProcessStudentDao.qryStudent2()


@student_ns.route('/delStudent/<id>')
class DeleteStudent(Resource):
    def post(self, id):
        """
        删除学生
        :return:
        """
        return ProcessStudentDao.delStudent(id)

@student_ns.route('/updStudent')
class UpdateStudent(Resource):
    @student_ns.expect(create_student_form_model, validate=False)
    def post(self):
        """
        更新学生信息
        :return:
        """
        data = request.json
        return ProcessStudentDao.updStudent(data)