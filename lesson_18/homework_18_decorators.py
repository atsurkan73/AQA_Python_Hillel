import logging

# Декоратори:
# 1. Напишіть декоратор, який логує аргументи та результати викликаної функції.

def decorator_1(func):
    def wrapper(*args):
        result = arg1 + arg2
        func(*args)
        return func
    return wrapper

@decorator_1
def log_event_1(arg1, arg2):

    result = arg1 + arg2
    log_message = f"Argument_1: {arg1}, Argument_2: {arg2} Sum: {result}"

    # Створення та налаштування логера
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        force=True
        )
    logger = logging.getLogger("log_event")

    logger.info(log_message)

    return logger


arg1 = int(input('Input Argument_1: '))
arg2 = int(input('Input Argument_2: '))

decorator_1(log_event_1(arg1,arg2))



# Декоратори:
# 2. Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

def decorator_2(func):
    def wrapper(*args):
        try:
            func(arg1, arg2)
        except ZeroDivisionError:
            print("Wrong divider. forbidden to divide by zero")
    return wrapper


@decorator_2
def divide(b, l):
    print(f'Dividing {b} / {l} = {b / l}')

print('')
arg1 = int(input('Input Divisor: '))
arg2 = int(input('Input Divider: '))

decorator_2(divide(arg1,arg2))

