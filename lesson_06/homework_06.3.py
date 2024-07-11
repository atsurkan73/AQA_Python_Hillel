# homework_06.3

# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

lst2 = []               # method 1 with cycle for
for item in lst1:
    if type(item) is str:
        lst2.append(item)

lst3 = [x for x in lst1 if type(x) is str] # method 2 with list comprehension

print(lst2)
print(lst3)