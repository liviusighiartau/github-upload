def exception_handling1():
    try:
        a = 10
        b = 30
        c = 0

        d = (a + b) / c
        print(d)
    except ZeroDivisionError:
        print("The division by 0 is not possible.")
        # raise Exception("This is an exception.")
    else:
        print("Because there was no exception, else it's executed.")
    finally:
        print("Finally, always executed.")


exception_handling1()