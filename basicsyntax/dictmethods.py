"""
Dictionary methods
"""

car = {'make': 'bmw', 'model': '325i', 'year': 2020}
cars = {'bmw': {'model': '235i', 'year': 2020}, 'vw': {'model': 'Golf', 'year': 2020}}

print(car.keys())
print(cars.keys())
print(car.values())
print(cars.values())
print(car.items())

car_copy = car.copy()
print(car_copy)
# car.clear()
print(car)

print(car.pop('model'))
print(car)