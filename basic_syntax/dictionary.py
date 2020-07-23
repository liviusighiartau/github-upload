"""
Data type to store more than one value in a variable name, in terms of key values pairs
Dictionary items are in brackets {} in key:value pairs, separated with ","
Example: {'k1':v1', 'k2':'v2'}
Dictionary is not sequenced, no indexing, it is Mapping
"""

car = {'make': 'bmw', 'model': '325i', 'year': 2020}
print(car)

d = {}

model = car['model']

print(car['make'])
print(model)

d['one'] = 1
d['two'] = 2

print(d)

sum_1 = d['two'] + 5
print(sum_1)
d['two'] = d['two'] + 8
print(d)
