# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
# який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть його середній бал.

class Student:

    grades_Peter_Pettigrew = {'math': 60, 'art': 90, 'English': 88, 'history': 67,
                              'science': 90, 'geography': 78, 'biology': 89, 'chemistry': 90,
                              'physics': 76, 'IT': 80, 'philosophy': 100, 'literature': 75}

    grades_Ron_Weasley = {'math': 60, 'art': 90, 'English': 88, 'history': 67,
                          'science': 90, 'geography': 78, 'biology': 89, 'chemistry': 90,
                          'physics': 76, 'IT': 80, 'philosophy': 68, 'literature': 75, 'algebra': 0, 'geometry': 0}

    def __init__(self, name, surname, age, average_grade):  # initialisation or constructor
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def average_grade_count (self, subj:dict):
        list_values = subj.values()
        sum_grade = 0
        num_subject = 0
        for grade in list_values:
            if grade != 0:
                sum_grade += grade
                num_subject += 1
        self.average_grade = round((sum_grade / num_subject), 1)

    def get_info(self):
        return f"Student {self.name} {self.surname} age {self.age} has average grade: {self.average_grade}"

student_Peter_Pettigrew = Student('Peter', 'Pettigrew', 13, 0)
student_Ron_Weasley = Student('Ron', 'Weasley', 12,0)

student_Peter_Pettigrew.average_grade_count(Student.grades_Peter_Pettigrew)
student_Ron_Weasley.average_grade_count(Student.grades_Ron_Weasley)

print('===================Initial grades===================')
print(student_Peter_Pettigrew.get_info())
print(student_Ron_Weasley.get_info())

print('===================Grades changing===================')
Student.grades_Peter_Pettigrew.update({'math': 95})
Student.grades_Peter_Pettigrew.update({'physics': 70})

Student.grades_Ron_Weasley.update({'biology': 60})
Student.grades_Ron_Weasley.update({'chemistry': 75})

student_Peter_Pettigrew.average_grade_count(Student.grades_Peter_Pettigrew)
student_Ron_Weasley.average_grade_count(Student.grades_Ron_Weasley)

print(student_Peter_Pettigrew.get_info())
print(student_Ron_Weasley.get_info())
