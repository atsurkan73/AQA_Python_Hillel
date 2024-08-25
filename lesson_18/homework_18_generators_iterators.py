from enum import Enum

class List_type(Enum):
    FIBONACCI = 1
    EVEN_NUMBERS = 2
    REVERSE_ORDER = 3

# Генератори:
# 1. Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
# 2. Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

class Generators:
    def __init__(self):
        self.max_value = 0

    def fibonacci_generator(self): # generator method
        a, b = 0, 1
        while True:
            yield a   # return one value while requesting
            a, b = b, a+b

    def even_numbers_generator(self): # generator method
        a = 0
        while True:
            yield a   # return one value while requesting
            a += 2

    def generator_result(self, gen_type:List_type):
        match gen_type:
            case List_type.FIBONACCI:
                num = self.fibonacci_generator()
            case List_type.EVEN_NUMBERS:
                num = self.even_numbers_generator()
        list_ = []
        while True:
            fnum = next(num)
            if fnum > self.max_value:
                self.next_value = fnum
                return list_
            list_.append(fnum)

    def input_number(self, list_type:str):
        n = int(input(f'Input maximum value N for creating a list with {list_type}: '))
        return n

    def print_long_list(self, list_of_items, chars_per_line):
        for line in range(0, len(list_of_items), chars_per_line):
            print (list_of_items[line:line+chars_per_line])




generator_1 = Generators()

generator_1.max_value = generator_1.input_number('generator')
lst_fib_1 = generator_1.generator_result(List_type.FIBONACCI)
print(f'Max_value N for lists created with generator: {generator_1.max_value}')
print(f'Fibonacci list created with generator: \n{lst_fib_1}')
lst_even = generator_1.generator_result(List_type.EVEN_NUMBERS)
print('Even numbers list created with generator:')
generator_1.print_long_list(lst_even, 35)


# Ітератори:
# 1. Реалізуйте ітератор для зворотного виведення елементів списку.
# 2. Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

class Iterators(Generators):
    def __init__(self, list_type:List_type):
        self.list_type = list_type
        self.max_value = 0
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max_value:
            if self.list_type == List_type.EVEN_NUMBERS:
                self.current += 2
                return self.current
        else:
            raise StopIteration

        if self.max_value >= 0:
            if self.list_type == List_type.REVERSE_ORDER:
                    self.max_value -= 1
                    return self.max_value
        else:
            raise StopIteration

iterator_1 = Iterators(List_type.EVEN_NUMBERS)
iterator_2 = Iterators(List_type.REVERSE_ORDER)


iterator_1.max_value = iterator_1.input_number('iterator')
iterator_2.max_value = iterator_1.max_value
print(f'Max_value N for lists created with iterator: {iterator_1.max_value}')
list_even = [iterator_1.current]

list_reverse = [iterator_2.max_value]

for _ in range((iterator_1.max_value) // 2):
    list_even.append(next(iterator_1))
for _ in range(iterator_2.max_value):
    list_reverse.append(next(iterator_2))

print('Even numbers list created with iterator:')
iterator_1.print_long_list(list_even, 35)

print('Reversed list created with iterator:')
iterator_2.print_long_list(list_reverse, 35)


