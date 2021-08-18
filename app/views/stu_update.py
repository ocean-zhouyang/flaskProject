from flask_restplus import Namespace, Resource

student_update_ns = Namespace(name='student_update', description='学生信息更新')


@student_update_ns.route('/updateStudent')
class Create(Resource):
    def post(self):
        """
        创建
        """
        return "update_student"