"""
Parent class Car
Children class BMW
Children class inherits the methods from the parent class
Overriding completely drive method in BMW class, by simply adding the
drive method in it
Overriding but still use the functionality of the method from the parent
class, by simply using super().name_of_the_method()
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

    def drive(self):
        super(BMW, self).drive()
        print("You are driving a BMW.")

    def head_up_display(self):
        print("This is a unique feature")


c = Car()
c.drive()
c.stop()

b = BMW()
b.drive()
b.stop()
b.head_up_display()
