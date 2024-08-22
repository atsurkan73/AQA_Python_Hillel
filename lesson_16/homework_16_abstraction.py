# Завдання 2
#
# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи
# для площі та периметру. Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
# та ініціалізуватись через конструктор. Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

import math
from abc import ABC, abstractmethod


# Абстрактний клас
class Shape(ABC):
    def __init__(self, name): #initialisation or constructor
        self.name = name

    @abstractmethod
    def calc_perimeter(self):
        pass

    @abstractmethod
    def calc_area(self):
        pass

class Square(Shape):
    def __init__(self, name, side):  #initialisation or constructor
        self.__side = side
        Shape.__init__(self, name)

    def get_side(self):
        return self.__side

    def set_side(self, side):
        self.__side = side

    def calc_perimeter(self):
        return round((self.__side * 4), 2)

    def calc_area(self):
        return round((self.__side ** 2), 2)


class Circle(Shape):
    def __init__(self, name, radius):  #initialisation or constructor
        self.name = name
        self.__radius = radius
        Shape.__init__(self, name)

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def calc_perimeter(self):
        return round((self.__radius * 2 * math.pi), 2)

    def calc_area(self):
        return round((self.__radius ** 2 * math.pi), 2)


class Parallelogram(Shape):
    def __init__(self, name, side_1, side_2, angel):  #initialisation or constructor
        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__angel = angel
        Shape.__init__(self, name)

    def get_side_1(self):
        return self.__side_1
    def set_side_1(self, side_1):
        self.__side_1 = side_1
    def get_side_2(self):
        return self.__side_2
    def set_side_2(self, side_2):
        self.__side_2 = side_2
    def get_angel(self):
        return self.__angel
    def get_angel(self, angel):
        self.__angel = angel

    def calc_perimeter(self):
        return round((self.__side_1 * 2) + (self.__side_2 * 2), 2)

    def calc_area(self):
        if self.__angel > 90:
            angel = 180 - self.__angel
        return round(abs(self.__side_1 * self.__side_2 * math.sin(self.__angel)), 2)

lst_shapes = []
square = Square('square', 5)
lst_shapes.append(square)
circle = Circle('circle', 3)
lst_shapes.append(circle)
parallelogram = Parallelogram('parallelogram',5, 10, 30)
lst_shapes.append(parallelogram)

[print(f'Area of {x.name}: {x.calc_area()}, Perimeter: {x.calc_perimeter()}') for x in lst_shapes]




