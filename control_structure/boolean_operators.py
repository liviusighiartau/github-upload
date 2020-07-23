"""
and
**********************************
True and True   --> True
True and False  --> False
False and False --> False
**********************************

or
**********************************
True or True   --> True
True or False  --> True
False or False --> False
**********************************

not
**********************************
not True  --> False
not False --> True
**********************************
"""

and_output1 = (18 == 18) and (0 > -1)
and_output2 = (10 - 1 == 9) and (0 > 1)
and_output3 = (0 > 1) and (1 - 1 == 1)

or_output1 = (10 == 10) or (5 + 1 == 6)
or_output2 = (100 / 3 == 2) or (5 < 6)
or_output3 = (100 % 2 == 1) or (5 % 2 == 3)

not_true = not (10 == 10)
not_false = not (10 % 2 == 3)

print(not_false)