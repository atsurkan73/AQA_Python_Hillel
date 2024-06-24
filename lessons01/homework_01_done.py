# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
_storona = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = _storona + storona_2 + storona_3 + storona_4
print('Сума сторін фігури дорівнює', perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_tree = 4
pear_tree = apple_tree * 5
plum_tree = apple_tree - 2
all_trees = apple_tree+pear_tree + plum_tree
print('Всього посадили дерев: ' + str(all_trees))
# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
morning_temp = 5
day_temp = morning_temp - 10
evening_temp = day_temp + 4
if evening_temp > 0:
    if evening_temp % 10 == 1 and evening_temp != 11:
        print('Tемпература надвечір складає ' + str(evening_temp) + ' градус вище нуля') # case for positive values that end with 1 (1, 21, 31,...) exept for 11
    elif evening_temp % 10 == 0 or evening_temp % 10 in range(5, 10) or evening_temp in range(11, 15):
        print('Tемпература надвечір складає ' + str(evening_temp) + ' градусів вище нуля') # case for positive values that end with 0,5,6,7,8,9 (10, 23, 39,...), and values from 11 to 19
    else:
        print('Tемпература надвечір складає ' + str(evening_temp) + ' градуси вище нуля')  # case for positive values 2,3,4, and values that end with 2,3,4 (22, 33, 34,...) exept for 12,13,14
elif evening_temp < 0:
    if abs(evening_temp) % 10 == 1 and abs(evening_temp) not in range(11, 20):
        print('Tемпература надвечір складає ' + str(abs(evening_temp)) + ' градус нижче нуля') # case for negative value -1, values that end with 1 but not including values -11...-19 (-1, -21, -31,...)
    elif abs(evening_temp) % 10 == 0 or abs(evening_temp) % 10 in range(5, 10) or abs(evening_temp) in range(11, 20):
        print('Tемпература надвечір складає ' + str(abs(evening_temp)) + ' градусів нижче нуля') # case for negative values that end with 0,5,6,7,8,9, and values  -11 ... -19 (-10, -11, -20, -30,...)
    else:
        print('Tемпература надвечір складає ' + str(abs(evening_temp)) + ' градуси нижче нуля') # case for negative values -2,-3,-4, and values that end with 2,3,4 exept for range -11...-19 (-22, -23, -24, -32,...)
else:
    print('Tемпература надвечір складає 0 градусів') #case for zero value

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys / 2
children_today = int((boys-1) + (girls-2))
print('Загальна кількість дітей у театральному гуртку сьогодні: ' + str(children_today))

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book_1 = 8
book_2 = book_1 + 2
book_3 = (book_1 + book_2) / 2
book_all = book_1 + book_2 + book_3
book_all_2_signs_after_point = "{:.2f}".format(book_all)
print('Усі книги коштують ' + str(book_all_2_signs_after_point) + ' грн.')