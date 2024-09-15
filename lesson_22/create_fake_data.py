from faker import Faker
from sqlalchemy import create_engine, column, Integer, String, func
from sqlalchemy.orm import sessionmaker
from lesson_22 import homework_22_classes as c
from lesson_22.homework_22_classes import  Base
from random import randint

# Завлання 1. Створення моделі даних: Створіть просту модель даних для системи управління студентами.
# Модель може містити таблиці для студентів, курсів та їх відношень. Кожен студент може бути
# зареєстрований на декілька курсів. Наприклад, створити 5 курсів, та розподілити рандомно 20 студентів.



# З'єднання з базою даних PostgreSQL
DATABASE_URL = 'postgresql+psycopg2://postgres:31031976@localhost/postgres'
engine = create_engine(DATABASE_URL)

# Створення таблиць у базі даних
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# INSERT STUDENTS
Faker.seed(123)
fake = Faker()

students = []
for x in range(20):
    name = fake.name()
    email = fake.email()
    students.append((name, email))
    print('students name: ', students[x][0]) #check names

for x in range(0, 20):
    new_student = c.Student(sid=x+1, name=students[x][0], email=students[x][1], year_of_entry=randint(2021,2025), ) #date_of_birth = students[x][2],
    session.add(new_student)

session.commit()


# INSERT COURSES
courses = ['Chemistry', 'Food Science and Technology', 'Biology', 'Mathematics', 'Sports Science']

new_course_list = []
for x in range(0, 5):
    new_course = c.Course(cid=x+1, title=courses[x], semester=randint(1,5), fee=randint(200,400))
    new_course_list.append(new_course)
    session.add(new_course)
session.commit()

# INSERT ATTENDANTS
new_attendants_list = []
for x in range(0, 40):
    if x < 20:
        new_attendant = c.Attendant(aid=x+1, student_id=x+1, course_id=randint(1,5))
    else:
        new_attendant = c.Attendant(aid=x+1, student_id=randint(1,20), course_id=randint(1,5))
    new_attendants_list.append(new_attendant)
    session.add(new_attendant)
session.commit()

session.close()




