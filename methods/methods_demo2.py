"""
Naming convention: letters, numbers, underscore
ex: sum_num, find_car
Docstring: see example below
"""


def sum_nums1(n1, n2):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


sum1 = sum_nums1(6, 9)
print(sum1)

string_add = sum_nums1('one', 'two')
print(string_add)


def is_metro(city):
    l = ['sfo', 'city', 'cluj']

    if city in l:
        return True
    else:
        return False


x = is_metro('boston')
print(x)
