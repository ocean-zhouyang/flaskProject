from flask_restplus import Namespace, Resource

tea_ns = Namespace(name='tea_ns', description='教师模块')


@tea_ns.route('/addTeacher')
class AddTeacher(Resource):
    def post(self):
        """
        创建
        """
        return "add_Teacher"


@tea_ns.route('/addTeacher1')
class AddTeacher1(Resource):
    def get(self):
        """
        """
        return "add_Teacher"


@tea_ns.route('/delTeacher')
class TeacherDelete(Resource):
    def delete(self):
        """
        删除
        """
        return "del_Teacher"


@tea_ns.route('/updateTeacher')
class TeacherUpdate(Resource):
    def put(self):
        """
        更新
        """
        return "update_Teacher"