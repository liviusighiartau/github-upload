"""
Iterating multiple lists at same time
"""

l1 = [1, 2, 3]
l2 = [4, 5, 6]

for a, b in zip(l1, l2):
    if a > b:
        print(a)
    else:
        print(b)
