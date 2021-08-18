from flask import Flask

from app.models import metadata, engine
from app.student import student_api, student_blueprint
from app.student.student_manage import student_ns
from app.teacher import teacher_api, teacher_blueprint
from app.teacher.teacher_manage import teacher_ns
from app.user import user_api, user_blueprint
from app.user.user_manage import user_ns
from app.views import api, student_add
from app.views.stu_add import student_add_ns
from app.views.stu_del import student_delete_ns
from app.views.stu_update import student_update_ns
from app.views.stu_qry import student_query_ns


def create_app():
	my_app = Flask(__name__)
	# 创建数据库表 有则忽略 无则创建
	metadata.create_all(engine)

	# 使用1个蓝图绑定多个namespace示例
	api.add_namespace(student_add_ns)
	api.add_namespace(student_delete_ns)
	api.add_namespace(student_update_ns)
	api.add_namespace(student_query_ns)

	my_app.register_blueprint(student_add)

	# 使用多个蓝图绑定多个namespace示例
	# student_api.add_namespace(student_ns)
	# teacher_api.add_namespace(teacher_ns)
	# user_api.add_namespace(user_ns)
	#
	# my_app.register_blueprint(student_blueprint)
	# my_app.register_blueprint(teacher_blueprint)
	# my_app.register_blueprint(user_blueprint)

	return my_app
