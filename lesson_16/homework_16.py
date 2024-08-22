# Завдання 1
#
# Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer,
# які успадковуються від Employee. Клас Manager повинен мати додатковий атрибут department,
# а клас Developer - атрибут programming_language.
#
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі атрибути
# як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує на кількість розробників
# у команді, якою керує керівник.
#
# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead


class Employer:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employer):
    def __init__(self, name, salary, department):
        Employer.__init__(self, name=name, salary=salary)
        self.department = department

class Developer(Employer):
    def __init__(self, name, salary, language):
        Employer.__init__(self, name=name, salary=salary)
        self.language = language

class TeamLeader(Manager, Developer):  # Ромбовидне наслідування

    def __init__(self, name, salary, department, team_size):
        Manager.__init__(self, name=name, salary=salary, department=department)
        self.team_size = team_size

# Створення об'єкту класу Te
teamleader = TeamLeader("John Snow", 5000, 'Update Verification', 10)

# Виведення атрибутів об'єкту
print("name:", teamleader.name)
print("salary:", teamleader.salary)
print("department:", teamleader.department)
print("team size:", teamleader.team_size)
print(TeamLeader.mro())
