import unittest


def compare_numbers_with_delta(num1, num2, delta, msg=None):
    """
    :param num1: int | float
    :param num2: int | float
    :param delta: int
    """
    if not msg:
        msg = f'Expected {num2} between {num1 - delta} and {num1 + delta}'
    assert num1 - delta <= num2 <= num1 + delta, msg


# compare_numbers_with_delta(1, 4, 1, '1 +- 5')

# print('Only for this file')

if __name__ == '__main__':  # this file will be run if started by execution
    print('This test message')
    unittest.main() # this command will be collect and run all tests
