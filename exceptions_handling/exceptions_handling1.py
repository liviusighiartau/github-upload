"""
Exceptions are errors
They should be handled in the code in order to make sure
that the cde is running well
Link to built-in exceptions: https://docs.python.org/3/library/exceptions.html
"""


def exception_handling1():
    try:
        a = 10
        b = 3
        c = 0

        d = (a == b) / c
        print(d)
    except ZeroDivisionError:
        print("The division by 0 is not possible.")


exception_handling1()


def exception_handling2():
    try:
        a1 = 10
        b1 = "my string"
        c1 = 3

        d1 = (a1 + b1) / c1
        print(d1)
    except TypeError:
        print("You are not using the correct data types.")


exception_handling2()
