from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

db = SQLAlchemy()

engine = create_engine("mysql+pymysql://root:123456@localhost:3306/mytest?charset=utf8", echo=True, pool_size=8,
					   pool_recycle=60 * 30)
metadata = MetaData(engine)

student = Table('student', metadata,
				Column('id', Integer, primary_key=True),
				Column('name', String(50)),
				Column('age', Integer),
				Column('address', String(10)),
				Column('teacher_id', Integer),
				)

teacher = Table('teacher', metadata,
				Column('teacher_id', Integer, primary_key=True),
				Column('name', String(50)),
				Column('age', Integer),
				Column('address', String(10)),
				)
