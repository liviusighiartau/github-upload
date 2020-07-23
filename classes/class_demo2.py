"""
A class is a template that defines the object, what it contains, what it does.
An object is a template of a class.
__init__ is a method required in every class which will be initialised
"""


class Car(object):

    def __init__(self, make, model="325d"):
        self.make = make
        self.model = model


c1 = Car('Honda')
print(c1.make)
print(c1.model)

c2 = Car('VW')
print(c2.make)
print(c2.model)