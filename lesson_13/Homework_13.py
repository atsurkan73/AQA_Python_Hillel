# Завдання 1:
# Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
# Результат запишіть у файл result_<your_second_name>.csv

import csv
import pathlib
from pathlib import Path

def compare_csv_files(path_to_csv1: Path, path_to_csv2: Path, path_to_output_csv_file: Path):

    with open(path_to_csv1, newline='') as f1, open(path_to_csv2, 'r') as f2:

        reader1 = csv.reader(f1, delimiter=';')
        reader2 = csv.reader(f2)
        diff = []
        equal = []

        for str1, str2 in zip(reader1, reader2):
            if str1 != str2:
                diff.append(str1)
                diff.append(str2)
            else:
                if str1 not in equal:
                    equal.append(str1)

        final_list = equal + diff

    with open(path_to_output_csv_file, 'w+', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(final_list)
        csv_file.close()

file_1 = 'C:\\Users\\ATsurkan\\PycharmProjects\\AQA_Python_Hillel\\Lesson_13\\Ideas_for_tests\\Work_with_csv\\rmc.csv'
file_2 = 'C:\\Users\\ATsurkan\\PycharmProjects\\AQA_Python_Hillel\\Lesson_13\\Ideas_for_tests\\Work_with_csv\\r-m-c.csv'
file_result = 'C:\\Users\\ATsurkan\\PycharmProjects\\AQA_Python_Hillel\\Lesson_13\\result_Tsurkan.csv'

compare_csv_files(file_1, file_2, file_result)


# Завдання 2:
# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. результат для невалідного файлу виведіть
# через логер на рівні еррор у файл json__<your_second_name>.log

import os
import json
import logging
from pathlib import Path

def json_files_analyzer(parent_dir_path: str):

    # Шлях до батьківської директорії
    parent_dir = Path(parent_dir_path)

    files = [f for f in parent_dir.iterdir() if f.is_file()]

    for file in files:
        try:
            with open(file, 'r') as _file:
                data = json.load(_file)
        except json.JSONDecodeError as e:
            path_to_log = 'json_Tsurkan.log'
            logging.basicConfig(level=logging.ERROR, filename=path_to_log, filemode="w+")
            logger = logging.getLogger("log_event")
            logger.error(f'file {file} has UnicodeDecodeError error: {e}')

        except UnicodeDecodeError as e:
            path_to_log = 'json_Tsurkan.log'
            logging.basicConfig(level=logging.ERROR, filename=path_to_log, filemode="w+")
            logger = logging.getLogger("log_event")
            logger.error(f'file {file} has UnicodeDecodeError error: {e}')

        else:
            print(f'\nfile {file} does not have json deserialization error')

json_files_analyzer('C:\\Users\\ATsurkan\\PycharmProjects\\AQA_Python_Hillel\\Lesson_13\\Ideas_for_tests')

# Завдання 3:
## Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення значення timingExbytes/incoming
# результат виведіть у консоль через логер на рівні інфо

import logging
import xml.etree.ElementTree as ET

# Завантаження XML-файлу
def find_xml_papameter(Group_number: int):

    tree = ET.parse('C:\\Users\\ATsurkan\\PycharmProjects\\AQA_Python_Hillel\\Lesson_13\\Ideas_for_tests\\Work_with_xml\\groups.xml')
    root = tree.getroot()
    checked = False
    # Пошук елементу timing_exbytes/incoming у для заданої групи
    for group in root.findall('group'):
        timing_exbytes = group.find('timingExbytes')
        if timing_exbytes is not None:
            incoming = timing_exbytes.find('incoming')
            if incoming is not None and group.find('number').text == f'{Group_number}':
                if group.find('number').text == f'{Group_number}':
                    log_message = f"Group/number: {Group_number}, timing_exbytes/incoming: {incoming.text}"
                    checked = True


    # Створення та налаштування логера
    logging.basicConfig(
        level=logging.INFO,
        force=True
    )
    console_handler = logging.StreamHandler()
    logging.getLogger('').addHandler(console_handler)
    if checked:
        logging.info(log_message)
    else:
        print(f'Group/number \'{Group_number}\' not found!')

find_xml_papameter(8)
