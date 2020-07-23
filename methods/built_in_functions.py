"""
Some built-in functions
max(): Takes any number of arguments and returns the largest one.

min(): Takes any number of arguments and returns the smallest one.

abs(): Returns the absolute value of the number. It returns a positive value.
It takes a single number.

type(): Returns the type of the data it receives as argument.
"""


def largest_num(*args):    # use * to specify that the method can take multiple arguments
    return max(args)


x = largest_num(10, -10, 9, 11)
print(x)


def smallest_num(*args):    # use * to specify that the method can take multiple arguments
    return min(args)


x = smallest_num(10, -10, 9, 11)
print(x)


def abs_function(a):    # use * to specify that the method can take multiple arguments
    return abs(a)


x = abs_function(-20)
print(x)


def type_function(a):    # use * to specify that the method can take multiple arguments
    return type(a)


x = type_function(-20)
y = type_function(-99.9)
print(x)
print(y)
