from app.models import db


class Student(db.Model):

    __tablename__ = "student"

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    address = db.Column(db.String(10))
    teacher_id = db.Column(db.Integer)

    def __init__(self, name, age, address, teacher_id):
        self.name = name
        self.age = age
        self.address = address
        self.teacher_id = teacher_id