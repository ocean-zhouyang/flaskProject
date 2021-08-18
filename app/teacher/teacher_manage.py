from flask_restplus import Namespace, Resource

teacher_ns = Namespace(name='teacher_ns', description='教师管理模块')


@teacher_ns.route('/addTeacher')
class Create(Resource):
    def post(self):
        """
        创建
        """
        return "add_teacher"