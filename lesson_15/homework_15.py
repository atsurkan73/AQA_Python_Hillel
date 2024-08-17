# Створіть клас геометричної фігури "Пералелограм". Клас повинен мати наступні атрибути:
#
# сторона_а (довжина сторони a)
# сторона_б (довжина сторони b)
# кут_1 (кут між сторонами a і b)
# кут_2 (кут між сторонами b і a)
# Необхідно реалізувати наступні вимоги:
#
# Значення сторін повинні бути більше 0.
# Сума кутів повинна дорівнювати 360 градусів.
# Для встановлення значень атрибутів використовуйте метод setattr.

class Parallelogram:
    def __setattr__(self, key:str, value:int):
        if value <= 0 or not isinstance(value, int):
            raise 'The value must be a positive integer number. Try next time.'
        if key == 'angel_2':
            if (value + angel_1)*2 != 360 or not isinstance(value, int):
                raise 'The SUM of all angels (angel_1 + angel_2)*2 must be equal 360 degrees. Try next time.'
        super().__setattr__(key, value)

    def input_value (self, value_name, units):
        value = input(f'Enter integer {value_name} in {units}: ')
        if value is not None and value.isdigit():
                return int(value)
        else:
            raise 'Not correct input. The value must be an integer number. Try again.'


figure = Parallelogram()

side_a = figure.input_value('side_a', 'cm')
setattr(figure, 'side_a', side_a) #adding attributes

side_b = figure.input_value('side_b', 'cm')
setattr(figure, 'side_b', side_b)

angel_1 = figure.input_value('angle_1', 'degree')
setattr(figure, 'angel_1', angel_1)

angel_2 = figure.input_value('angle_2', 'degree')
setattr(figure, 'angel_2', angel_2)


print(f'side_a: {side_a} cm')
print(f'side_b: {side_b} cm')
print(f'angel_1: {angel_1} degree')
print(f'angel_2: {angel_2} degree')
