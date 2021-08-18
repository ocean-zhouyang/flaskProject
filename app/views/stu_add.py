from flask_restplus import Namespace, Resource

student_add_ns = Namespace(name='student_add', description='学生录入')


@student_add_ns.route('/addStudent')
class Create(Resource):
    def post(self):
        """
        创建
        """
        return "add_student"