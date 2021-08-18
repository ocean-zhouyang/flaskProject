from flask_restplus import Namespace, Resource

student_ns = Namespace(name='student_ns', description='学生管理模块')


@student_ns.route('/addStudent')
class Create(Resource):
    def post(self):
        """
        创建
        """
        return "add_student"