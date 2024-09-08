from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lesson_22 import homework_22_classes as c
from lesson_22.homework_22_classes import  Base

# З'єднання з базою даних PostgreSQL
DATABASE_URL = 'postgresql+psycopg2://postgres:31031976@localhost/postgres'
engine = create_engine(DATABASE_URL)

# Створення таблиць у базі даних
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Завдання 2. Виконання базових операцій: програмa, яка додає нового студента (#21) до бази даних та додає його до певного курсу
new_student = c.Student(sid=21, name='Sherill Crawl', email='SerrilCrawl234@yahoo.com', year_of_entry=2021)
session.add(new_student)
session.commit()

# Завдання 2. та додає студента(#21) до певного курсу(#3)

new_attendant = c.Attendant(aid=41, student_id=21, course_id=3)
session.add(new_attendant)
session.commit()

# Завдання 4. Оновлення та видалення даних: Реалізуйте можливість оновлення даних
# про студентів або курси, а також видалення студентів з бази даних.

session.query(c.Student).filter_by(sid=21).update({c.Student.email:'new_email@yahoo.com'}, synchronize_session = False)
session.commit()

# Завдання 4. Видалення студента (№21) з бази даних.

session.query(c.Attendant).filter_by(student_id=21).delete()
session.query(c.Student).filter_by(sid=21).delete()
session.commit()

# 3. запити до бази даних, які повертають інформацію про курси, на які зареєстрований певний студент (№3)
student_3_details = session.query(c.Student).filter_by(sid=3).first()
student_3_courses = session.query(c.Course).join(c.Attendant).filter_by(student_id=3).all()
# print(f'Student name {}, id: {student_3_courses[0].attendants.})

print(f'student name {student_3_details.name} , id: {student_3_details.sid} takes part in the following courses: ')
for obj in student_3_courses:
    print(obj.title)
print(f'Total number of courses:  {len(student_3_courses)}')

#  3. запити до бази даних, які повертають інформацію про студентів, зареєстрованих на певний курс (№5)
courses_5_details = session.query(c.Course).filter_by(cid=3).first()
courses_5_students = session.query(c.Attendant).join(c.Student).join(c.Course).filter_by(cid=5).all()
print(f'course name {courses_5_details.title} , id: {courses_5_details.cid} attends the following students: ')
for obj in courses_5_students:
    print(f'Name: {obj.student.name}, Id: {obj.student.sid}')
print(f'Total number of students:  {len(courses_5_students)}')





