from flask_restplus import Namespace, Resource

user_ns = Namespace(name='user_ns', description='用户管理模块')


@user_ns.route('/addUser')
class Create(Resource):
    def post(self):
        """
        创建
        """
        return "add_user"