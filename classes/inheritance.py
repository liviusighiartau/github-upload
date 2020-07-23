"""
Parent class Car
Children class BMW
Children class inherits the methods from the parent class
"""


class Car(object):

    def __init__(self):
        print("You just created this instance.")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("The car just stopped...")


class BMW(Car):

    def __init__(self):
        Car.__init__(self)
        print("You just created the instance BMW")


c = Car()
c.drive()
c.stop()

b = BMW()
b.drive()
b.stop()