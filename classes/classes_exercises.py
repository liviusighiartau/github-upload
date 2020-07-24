

class Fruit(object):

    def __init__(self, fruit_name, nutrition_value, fruit_shape):
        self.nutrition_value = nutrition_value
        self.fruit_shape = fruit_shape
        self.fruit_name = fruit_name

    def nutrition(self):
        print("The nutrition value for " + str(self.fruit_name) + " is: " + str(self.nutrition_value))

    def shape(self):
        print("It is a " + str(self.fruit_shape) + " fruit.")


class Apple(Fruit):

    def __init__(self, fruit_name, nutrition_value, fruit_shape, fruit_color):
        Fruit.__init__(self, fruit_name, nutrition_value, fruit_shape)
        self.fruit_color = fruit_color

    def nutrition(self):
        print("This is an Apple. Enjoy it!")

    def color(self):
        print("The colour of it is: " + str(self.fruit_color) + " .")


fruit1 = Fruit('Apple', '100 kcal', 'round')
fruit1.nutrition()
fruit1.shape()
print(fruit1.fruit_name)
print(fruit1.nutrition_value)
print(fruit1.fruit_shape)

fruit2 = Apple('Apple', '57 kcal', 'rectangular', 'red')
fruit2.nutrition()
fruit2.color()