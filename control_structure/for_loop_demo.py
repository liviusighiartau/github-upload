"""
Execute statement repeatedly
Conditions are used to stop the execution of loops
Iterable items are String, List, Tuple, Dictionary
"""

my_string = 'liviu'

for i in my_string:
    if i == 'l':
        print('L', end='')
    else:
        print(i, end='')
print()

cars = ['vw', 'alfa', 'opel', 'Tesla']
for car in cars:
    print(car)

nums = [1, 2, 3]
for n in nums:
    print(n + 1)

d = {'one': 1, 'two': 2, 'three': 3}

print("%" * 20)
for k in d:
    print(k + " " + str(d[k]))
print("%" * 20)

for k, v in d.items():
    print(k)
    print(v)
