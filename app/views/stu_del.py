from flask_restplus import Namespace, Resource

student_delete_ns = Namespace(name='student_delete', description='删除学生')


@student_delete_ns.route('/delStudent')
class Create(Resource):
    def post(self):
        """
        创建
        """
        return "del_student"