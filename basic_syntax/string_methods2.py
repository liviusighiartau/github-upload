"""
Examples of string methods
"""

# Replace Method
a = "1abc2abc3abc4abc"
print(a.replace('abc', 'ABC', 2))

# Sub-Strings Method
# Starting index is inclusive
# Ending index is exclusive
sub = a[1:6]
step = a[1:6:3]

print("***********")

print(sub)
print(step)