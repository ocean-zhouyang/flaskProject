from sqlalchemy import and_, or_, text, func

from app import db
from app.models.student import Student


class ProcessStudentDao:

	def insertStudent(student):
		db.session.add(student)
		db.session.commit()
		db.session.close()

	@staticmethod
	def qryStudent():
		student_list = db.session.query(Student).all()
		ret = [{'id': x.id,
				'name': x.name} for x in student_list]
		print(ret)
		db.session.close()
		return ret

	@staticmethod
	def delStudent(id):
		res = db.session.query(Student).filter(Student.id == id).delete()
		# 删除全部
		# res = db.session.query(Student).delete()
		print(res)
		db.session.commit()
		db.session.close()
		return res

	@staticmethod
	def updStudent(data : dict):
		res = db.session.query(Student).filter(Student.id == data['id']).update(data)
		db.session.commit()
		db.session.close()
		return res

	@staticmethod
	def qryStudent2():
		# and  or
		# student_list = db.session.query(Student).filter(and_(Student.id > 0, Student.id < 20)).all()
		# student_list = db.session.query(Student).filter(or_(Student.id < 5, Student.name == '张三')).all()
		student_list = db.session.query(Student).filter(
			or_(
				Student.id < 2,
				and_(Student.name == '张三', Student.id > 3),
				Student.address != ""
			)).all()
		ret = [{'id': x.id, 'name': x.name} for x in student_list]

		# 查询数据 指定查询数据列 加入别名
		# student_list = db.session.query(Student.name.label('username'), Student.id).first()
		# ret = dict(student_list)

		# 表达式筛选条件
		# student_list = db.session.query(Student).filter(Student.name == "张三").all()
		# ret = [{'id': x.id, 'name': x.name} for x in student_list]

		# 原生SQL筛选条件
		# student_list = db.session.query(Student).filter_by(name='张三').all()
		# ret = [{'id': x.id, 'name': x.name} for x in student_list]
		# student_list = db.session.query(Student).filter_by(name='张三').first()
		# ret = [{'id': student_list.id, 'name': student_list.name}]

		# 字符串匹配方式筛选条件 并使用 order_by进行排序
		# student_list = db.session.query(Student).filter(text("id<:value and name=:name")).params(value=224, name='张三').order_by(
		# 	Student.id).all()
		# ret = [{'id': x.id, 'name': x.name} for x in student_list]

		# 原生SQL查询
		# student_list = db.session.query(Student).from_statement(text("SELECT * FROM student where name=:name")).params(
		# 	name='张三').all()
		# ret = [{'id': x.id, 'name': x.name} for x in student_list]

		# 筛选查询列
		# query的时候我们不在使用Student ORM对象,而是使用Student.name来对内容进行选取
		# student_list = db.session.query(Student.name, Student.id).all()
		# print(student_list)
		# for row in student_list:
		# 	print(row.name)

		# 别名映射  name as username
		# student_list = db.session.query(Student.name.label("username")).all()
		# print(student_list)
		# for row in student_list:
		# 	print(row.username)  # 这里要写别名了

		# between 大于1小于3的
		# student_list = db.session.query(Student).filter(Student.id.between(1, 10), Student.name == '张三').all()
		# ret = [{'id': x.id, 'name': x.name} for x in student_list]

		# in_([1,3,4]) 只查询id等于1,3,4的
		# student_list = db.session.query(Student).filter(Student.id.in_([1, 3, 4])).all()
		# ret = [{'id': x.id, 'name': x.name} for x in student_list]

		# ~xxxx.in_([1,3,4]) 查询不等于1,3,4的
		# student_list = db.session.query(Student).filter(~Student.id.in_([1, 3, 4])).all()
		# student_list = db.session.query(Student).filter(Student.id.notin_([1, 3, 4])).all()
		# ret = [{'id': x.id, 'name': x.name} for x in student_list]

		# 子查询
		# student_list = db.session.query(Student).filter(Student.id.in_(db.session.query(Student.id).filter_by(name='张三'))).all()
		# ret = [{'id': x.id, 'name': x.name} for x in student_list]

		# 通配符
		# student_list = db.session.query(Student).filter(Student.name.like('张%')).all()
		# student_list = db.session.query(Student).filter(~Student.name.like('张%')).all()
		# student_list = db.session.query(Student).filter(Student.name.notlike('张%')).all()
		# ret = [{'id': x.id, 'name': x.name} for x in student_list]

		# 切片取值法
		# student_list = db.session.query(Student)[1:3]
		# ret = [{'id': x.id, 'name': x.name} for x in student_list]

		# student_list = db.session.query(func.max(Student.id), func.sum(Student.id), func.min(Student.id)).group_by(Student.teacher_id).all()
		# student_list = db.session.query(func.max(Student.id), func.sum(Student.id), func.min(Student.id)).group_by(Student.name).having(func.min(Student.id) > 2).all()
		# print(student_list)

		return ret