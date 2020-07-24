class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the car: " + self.make)
        print("Model of the car: " + self.model)


c1 = Car('Honda', 'Civic')
print(c1.make)
# c1.info()

c2 = Car('VW', 'Golf')
print(c2.make)
# c2.info()

print(Car.wheels)
