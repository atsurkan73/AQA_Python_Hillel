import unittest
import data

class MyTest(unittest.TestCase):

# homework_03.10
# Родина зібралася в автомобільну подорож із Харкова в Буда-
# пешт. Відстань між цими містами становить 1600 км. Відомо,
# що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
# становить 48 літрів.
# 1) Скільки літрів бензину знадобиться для такої подорожі?
# 2) Скільки щонайменше разів родині необхідно заїхати на зап-
# равку під час цієї подорожі, кожного разу заправляючи пов-
# ний бак?
    def test_trip_consumption_check(self):
        distance_all = 1600
        fuel_per_100_km = 9
        fuel_tank_volume = 48

        fuel_for_jorney = (distance_all / 100) * fuel_per_100_km  # fuel volume for all jorney
        tank_filling_number = fuel_for_jorney / fuel_tank_volume
        if tank_filling_number - int(tank_filling_number) != 0:
            tank_filling_number += 1                              # minimal number of fillings of full tank

        distance_for_all_fuel = int((tank_filling_number * fuel_tank_volume) / fuel_per_100_km) * 100
        distance_for_one_tank_fuel = int(fuel_tank_volume / fuel_per_100_km) * 100

        # verification that all fuel volume is enough to cover the distance and
        # not more than all distance plus distance for one full tank
        self.assertIn(distance_for_all_fuel, range(distance_all, (distance_all + distance_for_one_tank_fuel)))


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
# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
    def test_people_add_to_list (self, index = 0):
        people_records = data.people_records

        added_object = ('Harry', 'Nickolson', 39, 'Product Owner', 'Miami')

        people_records.insert(index, added_object)

        self.assertEqual (people_records[index], added_object)

# homework_05.2 #2
# Given list of tuples (name, surname, age, profession, City location)
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
    def test_swap_items_in_list(self, index1 = 2, index2 = 4):
        people_records = data.people_records

        obj1_before_swap = people_records[index1]
        obj2_before_swap = people_records[index2]

        people_records[index1], people_records[index2] = people_records[index2], people_records[index1]

        self.assertEqual(obj1_before_swap, people_records[index2], 'Swap is not correct')
        self.assertEqual(obj2_before_swap, people_records[index1], 'Swap is not correct')

# homework_05.2 #3
# Given list of tuples (name, surname, age, profession, City location)
# 3 - check that all people in modified list with records indexes 6, 10, 13 have age >=30.
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
# Є list з даними. Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Данні в лісті можуть бути будь якими
    def test_new_list_only_string(self):

        list_origin = data.lst1

        new_list1 = []
        for item in list_origin:  # new list creation by method 1 with cycle for
            if type(item) is str:
                new_list1.append(item)

        new_list2 = [x for x in list_origin if type(x) is str]  # new list creation by method 2 with list comprehension

        self.assertEqual(new_list1, new_list2, 'Different lists made with Method1 and Method2')

# homework_06.4
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
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


# homework_06.1
# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
    def test_sum_of_even_numbers_in_list (self):

        string_to_count_uniq_charecters = data.adwentures_of_tom_sawer_formatted.lower()

        task_list = [x for x in string_to_count_uniq_charecters]

        uniq_list = []
        [uniq_list.append(x) for x in task_list if x not in uniq_list]

        uniq_length = len(uniq_list)

        set_of_charecters = set(string_to_count_uniq_charecters) # second method
        set_uniq_length = len(set_of_charecters)

        self.assertEqual(uniq_length, set_uniq_length)
        self.assertEqual(uniq_length, 30)

# homework_07.4
# Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
    def test_revert_string(self):

        string_to_revert = data.adwentures_of_tom_sawer_formatted

        some_list = list(string_to_revert)
        length = len(some_list)
        j = length - 1

        for i in range(int(length / 2)):    # first revert method
            temp = some_list[i]
            some_list[i] = some_list[j]
            some_list[j] = temp
            j -= 1

        reversed_string_1 = ''.join(map(str, some_list))

        reversed_string_2 = string_to_revert[::-1]  # second revert method

        self.assertEqual(reversed_string_1, reversed_string_2, 'Bad reverse of the string')


# homework_07.5
#Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
    def test_longest_word_in_list (self):
        some_list = ['France', 'Portugal', 'Spain', 'Germany', 'Netherlands', 'Argentina', 'Philippines', 'China']

        word_max = ''
        for word in some_list:              # first method
            if len(word) > len(word_max):
                word_max = word

        max_len = len(word_max)

        word_max_list = []
        for word in some_list:
            if len(word) == max_len:
                word_max_list.append(word)
        word_max_length = len(word_max)

        word_max_length_2 = len(max(some_list, key=len))     # second method

        word_max_list_2 = []
        [word_max_list_2.append(x) for x in some_list if len(x) == word_max_length_2]

        self.assertEqual(word_max_list, word_max_list_2)
        self.assertEqual(word_max_length, word_max_length_2)


# homework_07.10
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
    def test_count_even_numbers (self):

        lst_origin = data.lst2
        lst_of_even = [x for x in lst_origin if isinstance(x, (int, float)) and x % 2 == 0]
        lst_of_even_sum = sum(lst_of_even)

        lst_of_even_2 = []
        lst_of_even_sum_2 = 0
        for num in lst_origin:
            if isinstance(num, (int, float)) and num % 2 == 0:
                lst_of_even_2.append(num)
                lst_of_even_sum_2 += num

        self.assertEqual(lst_of_even, lst_of_even_2)
        self.assertEqual(lst_of_even_sum, lst_of_even_sum_2)


    # def test_count_even_numbers_negative (self):
    #     lst_origin = data.lst2
    #     with self.assertRaises(TypeError):
    #         lst_of_even = [x for x in lst_origin if x % 2 == 0]
    #         print(lst_of_even)


if __name__ == '__main__':
    unittest.main()