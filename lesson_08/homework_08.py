"""
Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
[”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
Використовуйте блок try\\except, щоб уникнути інших символів, окрім чисел у списку.
Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”
"""

example = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']
new_num_array = ['1, 3, 5', '10, 12, 14, 16', '2, 0, 7, 0, 8, 10, 113', '#1, 4, $5, 4, 1s, 5', '12, 3erter', '6, 9, 12, 20, 20, 1, 101']

def exeption_first_version (args=[]):
    lst_sort = []
    i = 0
    list_sum = []

    for item in args:
        sum = 0
        check = True
        item_sort = [x for x in item.split(',')]
        lst_sort.append(item_sort)
        try:
            for elem in lst_sort[i]:
                sum += int(elem)
        except Exception:
            print(f'Exception on element #{i}: "{item}" | Can\'t sum up')
            check = False
        if check:
            print(f'sum of element #{i}: {sum}')
            list_sum.append(sum)
        else:
            list_sum.append('Error')
        i += 1
    return list_sum

print('\n=========================list #1==========================')
exeption_first_version(example)
print('\n=========================list #2==========================')
list_with_sum = exeption_first_version(new_num_array)
print(f'List of summed elements {list_with_sum}')
