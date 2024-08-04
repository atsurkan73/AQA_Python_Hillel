import pytest
import random
import re
from lesson_11.homework.homework_10 import read_lines
from lesson_11.homework.homework_10 import log_event
import lesson_11.homework.homework_10 as main_file

def test_status_success(status_list = main_file.list_status):

    path = main_file.path_to_log

    for status in status_list:
        user_name = random.choice(main_file.list_names)
        log_msg = f"Login event - Username: {user_name}, Status: {status}"
        log_event(user_name, status)

        lines = read_lines(path)

        print(lines[len(lines) - 1])

        assert log_msg in lines[len(lines) - 1]
        assert re.search(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}', lines[len(lines) - 1])