adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

print('task 01')
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

print('task 02')
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
while "  " in adwentures_of_tom_sawer:
    adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("  ", " ")

print('task 03')
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

words = adwentures_of_tom_sawer.split(' ')
h_number = 0
for word in words:
    for letter in word:
        if letter == 'h':
            h_number += 1
print('task 04')
print(f'Літера "h" зустрічається у тексті {h_number} разів.')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

Title_number = 0
for word in words:
    if word.istitle():
        Title_number += 1

print('task 05')
print('Кількість слів, що починаються з Великої литери:', Title_number)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
# adwentures_of_tom_sawer1 = adwentures_of_tom_sawer.replace('Tom', 'Sawer')
index_first = adwentures_of_tom_sawer.find('Tom')
print('task 06')
if index_first != -1:
    index_second = adwentures_of_tom_sawer.find('Tom', index_first + 3)
    if index_second != -1:
        print(f'Прзиція слова \'Tom\', яке зустрічається вдруге: {index_second}')
    else:
        print('Слово \'Tom\' зустрічається в тексті тільки один раз')
else:
    print('Слово \'Tom\' в тексті не зустрічається')

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
for x in adwentures_of_tom_sawer_sentences:
    if x == '':
        adwentures_of_tom_sawer_sentences.remove('')

print('task 07')
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print('task 08')
print(adwentures_of_tom_sawer_sentences[3].lower().lstrip())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print('task 09')
startswith = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.lstrip().startswith('By the time'):
        startswith = True
        print('В тексті є речення, що починається з \"By the time\"')
        break
if not startswith:
    print('В тексті нема речення, що починається з \"By the time\"')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

print('task 10')
print('Кількість слів останнього речення:', len(adwentures_of_tom_sawer_sentences[-1].split()))
