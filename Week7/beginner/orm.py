from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


# A class that maps to a table, inherits from Base
Base = declarative_base()


# Our class will be mapped to a table with name student
# Each field is a Column with the given type and constraints
class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __str__(self):
        return "{} - {}".format(self.id, self.name)

    def __repr__(self):
        return self.__str__()


engine = create_engine("sqlite:///university.db")
# will create all tables
Base.metadata.create_all(engine)


# Session is our Data Mapper
session = Session(bind=engine)

print("Adding new student to the database via the session object")
student1 = Student(name="Tedi", age=22)
session.add_all([
    Student(name="Rado", age=23),
    Student(name="Ivo", age=21),
    Student(name="Ivan", age=23)]
)
session.commit()

# SELECT * FROM student;
all_students = session.query(Student).all()
# list of Student objects
print(all_students)


# SELECT * FROM student WHERE name = "Rado";
rado = session.query(Student).filter(Student.name == "Rado").all()
print(rado)


# SELECT name, age FROM student WHERE age = 23
twenty_three = session.query(Student.name, Student.age).\
    filter(Student.age == 23).all()

for student in twenty_three:
    print("Name {} with age {}".format(student.name, student.age))
