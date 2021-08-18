from flask_restplus import Namespace, Resource

student_query_ns = Namespace(name='student_query', description='学生信息查询')


@student_query_ns.route('/getStudent')
class Create(Resource):
    def post(self):
        """
        创建
        """
        return "get_student"