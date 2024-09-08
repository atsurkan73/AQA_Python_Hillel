from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Завдання 1. Створення моделі даних: Створіть просту модель даних для системи управління студентами.
# Модель може містити таблиці для студентів, курсів та їх відношень. Кожен студент може бути
# зареєстрований на декілька курсів. Наприклад, створити 5 курсів, та розподілити рандомно 20 студентів.

# Базовий клас для визначення моделей даних
Base = declarative_base()

# Визначення моделі даних (таблиць) за допомогою класів
class Student(Base):
  __tablename__ = 'students'

  sid = Column(Integer, primary_key=True)
  name = Column(String)
  email = Column(String)
  # date_of_birth = Column(String)
  year_of_entry = Column(Integer)

  # Встановлення відношення "один до багатьох" з таблицею attendants
  attendants = relationship("Attendant", back_populates="student")

class Course(Base):
  __tablename__ = 'courses'

  cid = Column(Integer, primary_key=True)
  title = Column(String)
  semester = Column(Integer)
  fee = Column(Integer)

  # Встановлення відношення "багато до багатьох" з таблицею attendants
  attendants = relationship("Attendant", back_populates="courses")


class Attendant(Base):
  __tablename__ = 'attendants'

  aid = Column(Integer, primary_key=True)
  student_id = Column(Integer, ForeignKey('students.sid'))
  course_id = Column(Integer, ForeignKey('courses.cid'))

  # Встановлення відношення "багато до багатьох" з таблицею courses
  courses = relationship("Course", back_populates="attendants")
  # Встановлення відношення "багато до одного" з таблицею students
  student = relationship("Student", back_populates="attendants")

