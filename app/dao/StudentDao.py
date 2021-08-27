from app import db


class ProcessStudentDao:

	def insertStudent(student):
		db.session.add(student)
		db.session.commit()
