#homework_06.4

# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

lst = [1, 2, 3, 3, 4, 5, 6, 66, 7, 8, 9, 10, 90, 0, 11, 2, 2, 3, 4, -3, -100, 2.99, -4.0]

sum1 = 0               # method 1 with cycle for
lst1 = []
for num in lst:
    if num % 2 == 0:
        lst1.append(num)
        sum1 += num

print('method 1 with cycle for')
print(f'Список парних чисел: {lst1}')
print (f'Сума парних чисел: {sum1}')

lst2 = list(filter(lambda x: (x % 2 == 0), lst))   # method 2 with lambda function
sum2 = sum(x for x in lst2)
print('method 2 with lambda function')
print(f'Список парних чисел: {lst2}')
print (f'Сума парних чисел: {sum2}')

lst3 = [x for x in lst if x % 2 == 0]      # method 3 with list comprehension
sum3 = sum(lst3)
print('method 3 with list comprehension')
print(f'Список парних чисел: {lst3}')
print (f'Сума парних чисел: {sum3}')

