"""
Positional parameters
They are like optional parameters
Can be assigned a default value, if no value is provide from outside
Can be interchanged
"""


def sum_nums1(n1=2, n2=4):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


sum1 = sum_nums1(6, n2=5)
print(sum1)
