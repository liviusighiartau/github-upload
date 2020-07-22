"""
Execute statements repeatedly
Conditions are used to stop execution of loops
Iterable items are String, List, Tuple, Dictionary
"""

x = 0
while x < 10:
    print("Value of x is: " + str(x))
    x = x + 1

l = []
num = 0
while num < 10:
    l.append(num)
    num += 1
    print("Value of num is: " + str(num))

print(l)