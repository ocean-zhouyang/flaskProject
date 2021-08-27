from flask_restplus import Namespace, Resource

stu_ns = Namespace(name='stu_ns', description='学生模块')


@stu_ns.route('/addStudent')
class AddStudent(Resource):
    def post(self):
        """
        创建
        """
        return "add_student"


@stu_ns.route('/addStudent1')
class AddStudent1(Resource):
    def get(self):
        """
        """
        return "add_student"

@stu_ns.route('/addStudent2')
class AddStudent2(Resource):
    def head(self):
        """
        """
        return "add_student"


@stu_ns.route('/delStudent')
class StudentDelete(Resource):
    def delete(self):
        """
        删除
        """
        return "del_student"


@stu_ns.route('/updateStudent')
class Create(Resource):
    def put(self):
        """
        更新
        """
        return "update_student"