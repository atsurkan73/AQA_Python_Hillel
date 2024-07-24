import unittest

from utils.assertatin_utils import compare_numbers_with_delta
import data

class MyTest(unittest.TestCase):


# homework_04, task 1 - 3
    def test_search_by_criteria(self):
        text = data.adwentures_of_tom_sawer
        text = text.replace("\n", " ")
        text = text.replace("....", " ")

        while "  " in text:
            text = text.replace("  ", " ")

        self.assertEqual(text, data.adwentures_of_tom_sawer_formatted, 'Text formatting is not correct')

# homework_05.1
    def test_search_by_criteria(self):

        cars = data.car_data
        criteria = (2017, 1.6, 36000)

        car_data_sorted = sorted(cars.items(), key=lambda car: car[1][4])
        search_list = []
        for car in car_data_sorted:
            if car[1][1] >= criteria[0] and car[1][2] >= criteria[1] and car[1][4] <= criteria[2]:
                search_list.append(car)

        for car in search_list:
            self.assertGreaterEqual(car[1][1], criteria[0], f'Year is less than {criteria[0]}') #year>= , engine_volume >= , price<=
            self.assertGreaterEqual(car[1][2], criteria[1], f'Engine volume is less than {criteria[1]}')
            self.assertLessEqual(car[1][4], criteria[2], f'Price is Greater or Equal than {criteria[2]}')

# homework_05.2 #1
    def test_people_add_to_list (self, index = 0):
        people_records = data.people_records

        added_object = ('Harry', 'Nickolson', 39, 'Product Owner', 'Miami')

        people_records.insert(index, added_object)

        self.assertEqual (people_records[index], added_object)

# homework_05.2 #2
    def test_swap_items_in_list(self, index1 = 2, index2 = 4):
        people_records = data.people_records

        obj1_before_swap = people_records[index1]
        obj2_before_swap = people_records[index2]

        people_records[index1], people_records[index2] = people_records[index2], people_records[index1]

        self.assertEqual(obj1_before_swap, people_records[index2], 'Swap is not correct')
        self.assertEqual(obj2_before_swap, people_records[index1], 'Swap is not correct')

# homework_05.2 #3
    def test_check_age_more_or_equal (self):
        people_records = data.people_records

        age = 30
        i1 = 6
        i2 = 10
        i3 = 13

        people_records.insert(i1, ('Nora', 'Star', 31, 'Doctor', 'Michigan'))
        people_records.insert(i2, ('Ben', 'Berg', 30, 'Merchandiser', 'Denver'))
        people_records.insert(i3, ('Toni', 'Pew', 45, 'Sheff', 'Solt Lake City'))

        check = True

        for i in range(len(people_records)):
            if i == i1 or i == i2 or i == i3:
                if int(people_records[i][2]) < age:
                    check = False
                    break
        self.assertTrue(check, f'Someone from verified persons has age less than {age} year')

# homework_06.3
    def test_new_list_only_string (self):

        list_origin = data.lst1

        new_list1 = []
        for item in list_origin:  # method 1 with cycle for
            if type(item) is str:
                new_list1.append(item)

        new_list2 = [x for x in list_origin if type(x) is str]  # method 2 with list comprehension

        self.assertEqual(new_list1, new_list2, 'Different lists made with Method1 and Method2')

# homework_06.4
    def test_sum_of_even_numbers_in_list (self):

        lst = data.lst2

        sum1 = 0               # method 1 with cycle for
        lst1 = []
        for num in lst:
            if num % 2 == 0:
                sum1 += num

        lst2 = list(filter(lambda x: (x % 2 == 0), lst))   # method 2 with lambda function
        sum2 = sum(x for x in lst2)

        lst3 = [x for x in lst if x % 2 == 0]      # method 3 with list comprehension
        sum3 = sum(lst3)

        self.assertEqual(sum1, sum2, 'Different sum of even numbers counted with Method1 and Method2')
        self.assertEqual(sum1, sum3, 'Different sum of even numbers counted with Method1 and Method3')
        self.assertEqual(sum2, sum3, 'Different sum of even numbers counted with Method2 and Method3')


