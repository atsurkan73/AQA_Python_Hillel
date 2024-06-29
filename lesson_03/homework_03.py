#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = """\'"Would you tell me, please, which way I ought to go from here?"\n"That depends 
a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then
it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an 
explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."\'"""

print ('Задача 03')
print(alice_in_wonderland)

"""
    # Задачі 04 - 10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
Black_sea = 436402
Azov_sea = 37800
Total_area = Black_sea + Azov_sea

print ('Задача 04')
print(f'Загальна площа Чоного та Азовського морей складає: {Total_area} км2')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
All_stocks = 375291
Stock_1_and_2 = 250449
Stock_2_and_3 = 222950
Stock_1 = All_stocks - Stock_2_and_3
Stock_2 = Stock_1_and_2 - Stock_1
Stock_3 = Stock_2_and_3 - Stock_2

print ('Задача 05')
print(f'На складі 1: {Stock_1} товарів; На складі 2: {Stock_2} товарів; На складі 3: {Stock_3} товарів.')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
Duration_in_month = 18
Payment_per_month = 1179
All_payment = Duration_in_month * Payment_per_month

print ('Задача 06')
print('Вартість комп’ютера складає ' + str(All_payment) + ' грн.')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print ('Задача 07')
print(f'Остаток від ділення:\n'
      f'8019 : 8 = {a} | 9907 : 9 = {b} | 2789 : 5 = {c} | 7248 : 6 = {d} | 7128 : 5 = {e} | 19224  9 = {f}')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
Pizza_big_num = 4
Pizza_big_price = 274
Pizza_mid_num = 2
Pizza_mid_price = 218
Juice_num = 4
Juice_price = 35
Cake_num = 1
Cake_price = 350
Water_num = 3
Water_price = 21
All_order_price = Pizza_big_num * Pizza_big_price + Pizza_mid_num * Pizza_mid_price + Juice_num * Juice_price + Cake_num * Cake_price + Water_num * Water_price
print ('Задача 08')
print('Усе замовлення Іринки коштує ' + str(All_order_price) + ' грн.')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
Photo_all = 232
Photo_on_one_page = 8
Page_all = Photo_all / Photo_on_one_page
if Page_all - int(Page_all) != 0:
    Page_all += 1
print ('Задача 09')
print('Ігорю знадобиться', int(Page_all), 'сторінок альбома')


# task 10
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
Distance_all = 1600
Fuel_per_100_km = 9
Fuel_tank_volume = 48

Fuel_for_jorney = (Distance_all / 100) * Fuel_per_100_km
Tank_filling_number = Fuel_for_jorney / 48
if Tank_filling_number - int(Tank_filling_number) != 0:
    Tank_filling_number += 1
print('Задача 10')
print('1. Для подорожі знадобиться', Fuel_for_jorney, 'літрів бензину\n2. Необхідно заїхати на заправку щонайменше', int(Tank_filling_number), 'разів')
