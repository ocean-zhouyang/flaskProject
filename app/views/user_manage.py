from flask_restplus import Namespace, Resource

user_ns = Namespace(name='user_ns', description='用户模块')


@user_ns.route('/addUser')
class AddUser(Resource):
    def post(self):
        """
        创建
        """
        return "add_User"


@user_ns.route('/addUser1')
class AddUser1(Resource):
    def get(self):
        """
        """
        return "add_User"

@user_ns.route('/addUser2')
class AddUser2(Resource):
    def head(self):
        """
        """
        return "add_User"


@user_ns.route('/delStudent')
class UserDelete(Resource):
    def delete(self):
        """
        删除
        """
        return "del_User"


@user_ns.route('/updateUser')
class Create(Resource):
    def put(self):
        """
        更新
        """
        return "update_User"