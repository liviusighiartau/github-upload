"""
Python contains a table in which it stores the counter of object references
In my example: Cluj is a string object
               1000, 9, are integer object
               a, b are references of the object
Every time i reference the same object the counter increases its value by 1
"""

a = "Cluj"
b = 1000
a = 9

print(a)
print(b)

c = 1
d = 1
# compares if the variables are referencing the same object
# !=, is, is not or any other expression can be used
print(c == d)
 