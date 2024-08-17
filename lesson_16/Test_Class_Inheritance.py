# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
import random
import unittest
import string
from lesson_16_lesson import homework_16

# 'C:\\Users\\ATsurkan\\PycharmProjects\\AQA_Python_Hillel\\lesson_16_lesson\\homework_16'

class MyTest(unittest.TestCase):

    def test_check_teamleader_positive(self):

        name = ''.join(random.choices(string.ascii_letters, k=random.randrange(2,20)))
        salary = random.randrange(1000,10000)
        department = random.choice(['Data Verification', 'Data Collection'])
        team_size = random.randint(2,100)

        team_leader_ = homework_16.TeamLeader(name, salary, department, team_size)
        print(f'+++team_leader_1 name+++: {name}')
        self.assertTrue(self, name == team_leader_.name)
        self.assertTrue(self, salary == team_leader_.salary)
        self.assertTrue(self, department == team_leader_.department)
        self.assertTrue(self, team_size == team_leader_.team_size)

    def test_check_teamleader_negative(self):
        name = ''.join(random.choices(string.ascii_letters, k=random.randrange(2,20)))
        salary = random.randrange(1000,10000)
        department = random.choice(['Data Verification', 'Data Collection'])
        team_size = random.randint(2,100)

        team_leader_1 = homework_16.TeamLeader(name, salary, department, team_size)
        self.assertFalse(hasattr(team_leader_1, 'language'))

if __name__ == '__main__':
    unittest.main()