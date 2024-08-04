import re
"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import os

list_names = ('Isaak Newton','Irene Joliet','John Rood', 'Nasty Dasty')
list_status = ['success', 'expired', 'error']
path_to_log = 'C:\\Users\\ATsurkan\\PycharmProjects\\pythonProject\\lesson_11\\homework\\login_system.log'

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename=path_to_log,
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        force=True
        )
    logger = logging.getLogger("log_event")

        # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

def read_lines (path: str):
    with open(path, 'r') as file:
        lines = file.readlines()
    file.close()
    return lines

def remove_log_file(path_to_log: str):
    if os.path.exists(path_to_log):
      os.remove(path_to_log)
    else:
      print("Log file does not exist")

