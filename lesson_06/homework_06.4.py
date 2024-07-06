#homework_06.4

# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

lst1 = [1, 2, 3, 3, 4, 5, 6, 66, 7, 8, 9, 10, 90, 0, 11, 2, 2, 3, 4, -3, -100, 2.99, -4.0]

lst2 = []               # method 1 with cycle for
for num in lst1:
    if num % 2 == 0:
        lst2.append(num)
print('method 1 with cycle for')
print(f'Список парних чисел: {lst2}')
print (f'Сума парних чисел: {len(lst2)}')

lst3 = [x for x in lst1 if x % 2 == 0] # method 2 with list comprehension

print('method 2 with list comprehension')
print(f'Список парних чисел: {lst3}')
print (f'Сума парних чисел: {len(lst3)}')

