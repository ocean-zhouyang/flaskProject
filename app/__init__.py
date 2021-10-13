from flask import Flask

from app.models import metadata, engine, db
from app.student import student_api, student_blueprint
from app.student.student_manage import student_ns
from app.teacher import teacher_api, teacher_blueprint
from app.teacher.teacher_manage import teacher_ns
from app.user import user_api, user_blueprint
from app.user.user_manage import user_ns
from app.views import api, first_blueprint
from app.views.stu_manage import stu_ns
from app.views.user_manage import u_ns
from app.views.teacher_manage import tea_ns



def create_app():
	my_app = Flask(__name__)

	# 创建数据库表 有则忽略 无则创建
	my_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/mytest?charset=utf8'
	# 禁用事件跟踪系统，防止消耗系统资源
	my_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	metadata.create_all(engine)
	db.init_app(my_app)

	# 使用1个蓝图绑定多个namespace示例
	# api.add_namespace(stu_ns)
	# api.add_namespace(u_ns)
	# api.add_namespace(tea_ns)
	#
	# my_app.register_blueprint(first_blueprint)

	# 使用多个蓝图绑定多个namespace示例
	student_api.add_namespace(student_ns)
	teacher_api.add_namespace(teacher_ns)
	user_api.add_namespace(user_ns)

	my_app.register_blueprint(student_blueprint)
	my_app.register_blueprint(teacher_blueprint)
	my_app.register_blueprint(user_blueprint)

	return my_app
