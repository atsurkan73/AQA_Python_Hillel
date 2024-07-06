# homework_06.1

# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()

task = input('Input string: ')

task = task.lower()

task_list = [x for x in task]

print(f'all symbols: ', task_list)

uniq_list = []

[uniq_list.append(x) for x in task_list if x not in uniq_list]

uniq_length = len(uniq_list)

print(f'unique symbols: ', uniq_list)
print(f'unique list length: ', uniq_length)

if uniq_length > 10:
  print(True)
else:
  print(False)