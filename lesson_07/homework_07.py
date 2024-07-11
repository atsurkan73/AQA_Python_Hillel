# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

print('=========================================task 1================================================')

def multiplication_table(number:int):
    # Initialize the appropriate variable
    multiplier = 1
    max_result = 25
    result = 0
    print(f'Таблиця множення числа {number}')
    # Complete the while loop condition.
    while result <= max_result:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > max_result:
            print(f'Kалькуляція зупинена, тому що результат наступного множення перевищуе допустиме значення: {max_result}')
            return
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(number = 3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

print('=========================================task 2================================================')

def summ_2_int_numbers():
    print('Це функція суми двох цілих чисел')
    a = int(input('Введіть перше число: '))
    b = int(input('Введіть друге число: '))
    sum = int(a) + int(b)
    print(f'Cума складає: {sum}')

summ_2_int_numbers()

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print('=========================================task 3================================================')

def arithmetical_mean():
    print('Це функція середньоарифметичного значення списку чисел')
    n = int(input('Введіть число елементів: '))
    print(f'Введіть послідовно {n} елементів:')
    input_list = []
    sum_elements = 0
    num_elements = 0
    for i in range(n):
        input_element = float(input())
        sum_elements += input_element
        num_elements += 1
    avr_mean = sum_elements / num_elements
    print(f'Середньоарифметичне значення: {avr_mean}')

arithmetical_mean()

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print('=========================================task 4================================================')

def revert_string(some_string):
    some_list = list(some_string)
    length = len(some_list)
    j = length - 1

    for i in range(int(length / 2)):
        temp = some_list[i]
        some_list[i] = some_list[j]
        some_list[j] = temp
        j -= 1

    listToStr = ' '.join(map(str, some_list))
    print(listToStr)

    return (listToStr)

print('Це функція, що приймає рядок та  повертає його у зворотньому порядку')
some_string = input('Введіть строку: ')
revert_string(some_string)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

print('=========================================task 5================================================')

def revert_string(list_of_words):
    word_max = ''
    for word in list_of_words:
        if len(word) > len(word_max):
            word_max = word
    return (word_max)

some_list = ['facebook', 'tweeter', 'instagram', 'tiktok', 'snapchat']

print('Це функція, яка приймає список слів та повертає найдовше слово у списку')
print(f'Заданий список: {some_list}')
print(f'Найдовше слово: {revert_string(some_list)}')

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

print('=========================================task 6================================================')

print('Це функція, яка приймає два рядки та повертає індекс першого входження другого рядка\
 у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок\
не є підрядком першого рядка')

def find_substring(str1, str2):

    return_num = -1
    if str2 in str1:
        return_num = str1.find(str2)
    return return_num

str1 = "Hello, world!"
str2 = "world"
print('Аналіз прикладу 1.')
print(f'Return number: {find_substring(str1, str2)}') # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print('Аналіз прикладу 2.')
print(f'Return number: {find_substring(str1, str2)}') # поверне -1


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
#reworked #3 from homework_05.2
# check that all people in list have age >=30. Print condition check result

print('=========================================task 7================================================')

def find_substring(arg):
    age = 30
    check = True
    for i in range(len(people_records)):
        if int(people_records[i][2]) < age:
            check = False
            break
    if check:
        print(f'All verified persons have age more or equal to {age} year')
    else:
        print(f'Someone from verified persons has age less than {age} year')

    return arg

people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
]

print('Це функція, яка перевіряє, чи є в списку люди молодші ніж 30 років')
find_substring(people_records)

# task 8
# reworked task 10 from homework_03
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

print('=========================================task 8================================================')

def petrol_filling(distanse:int, fuel_per_100_km:float, tank_volume:float):

    fuel_for_jorney = (distanse / 100) * Fuel_per_100_km
    tank_filling_number = fuel_for_jorney / 48
    if tank_filling_number - int(tank_filling_number) != 0:
        tank_filling_number += 1

    return [fuel_for_jorney, tank_filling_number]

Distance_all = 1600
Fuel_per_100_km = 9.0
Fuel_tank_volume = 48.0

print('Це функція, яка рахує деталі заправки для подорожі.')
petrol_fillings = petrol_filling(Distance_all, Fuel_per_100_km, Fuel_tank_volume)
print('1. Для подорожі знадобиться', petrol_fillings[0], 'літрів бензину\n2. Необхідно заїхати на заправку щонайменше', int(petrol_fillings[1]), 'разів')

# task 9
# reworked homework_06.1
# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()

print('=========================================task 9================================================')

def uniq_chars_in_string(chars_num):

    input_str = input('Input string: ')
    input_str_low = input_str.lower()

    task_list = [x for x in input_str_low]

    uniq_list = []
    [uniq_list.append(x) for x in task_list if x not in uniq_list]
    uniq_length = len(uniq_list)

    if uniq_length > 10:
        check = True
    else:
        check = False

    return check

print('This function is for calculation the number of unique characters in the string and comparison with a given number')

char_number = int(input('Input number of characters to compare with: '))

more_than = uniq_chars_in_string(char_number)

if more_than:
    print (f'This line contains more than {char_number} unique characters')
else:
    print(f'This line contains less than or equal to {char_number} unique characters')

# task 10
#reworked homework_06.4
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

print('=========================================task 10================================================')

def count_even_numbers (list_of_int):
    lst_of_even = [x for x in list_of_int if x % 2 == 0]      # method 3 with list comprehension
    sum_of_even = sum(lst_of_even)
    return lst_of_even, sum_of_even

lst_origin = [1, 2, 3, 3, 4, 5, 6, 66, 7, 8, 9, 10, 90, 0, 11, 2, 2, 3, 4, -3, -100, 2.99, -4.0]

print ('Підрахунок суми ПАРНИХ чисел в листі')
print (f'Початковий список: {lst_origin}')
print (f'Список парних чисел: {count_even_numbers(lst_origin)[0]}')
print (f'Сума парних чисел: {count_even_numbers(lst_origin)[1]}')


