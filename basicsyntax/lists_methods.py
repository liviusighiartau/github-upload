"""
Built-in methods to help manipulate a list
"""

cars = ["bmw", "audi", "vw"]

length = len(cars)
print(length)

cars.append("opel")
cars.append("ferrari")
print(cars)

cars.insert(1, "Jeep")
print(cars)

x = cars.index("audi")
print(x)

y = cars.pop()
print(y)
print(cars)

cars.remove("Jeep")
print(cars)

slicing = cars[0:2]
a = cars[1:]
print(slicing)
print(a)
print("*"*15)
print(cars)
cars.sort()

print(cars)
print("*"*15)