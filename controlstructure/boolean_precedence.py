"""
Order of precedence for boolean operators:
1. not
2. and
3. or
"""

bool_output = True or not False and False
print(bool_output)

bool_output1 = (10 + 1 == 11 or not (10 / 3 == 2)) and (10 / 3 == 2)
print(bool_output1)