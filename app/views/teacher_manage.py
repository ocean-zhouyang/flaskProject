from flask_restplus import Namespace, Resource

teacher_ns = Namespace(name='teacher_ns', description='教师模块')


@teacher_ns.route('/addTeacher')
class AddTeacher(Resource):
    def post(self):
        """
        创建
        """
        return "add_Teacher"


@teacher_ns.route('/addTeacher1')
class AddTeacher1(Resource):
    def get(self):
        """
        """
        return "add_Teacher"


@teacher_ns.route('/delTeacher')
class TeacherDelete(Resource):
    def delete(self):
        """
        删除
        """
        return "del_Teacher"


@teacher_ns.route('/updateTeacher')
class TeacherUpdate(Resource):
    def put(self):
        """
        更新
        """
        return "update_Teacher"