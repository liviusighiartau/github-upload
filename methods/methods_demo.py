"""
Group of statements containing code which can be used somewhere
Reusable code
Definition of method: def method_name():
Body of the method, describes the procedures that method is carrying out
Can take arguments, can perform operation on the arguments
Can be empty when no arguments are needed
Whenever we create a method we have to use it
"""


def sum_nums():
    print(10 + 2)


sum_nums()


def sum_nums2(n1, n2):
    print(n1 + n2)


sum_nums2(6, 9)


my_list1 = [1, 2, 3]
my_list2 = [0, 9, 8, 7]

print(my_list1 + my_list2)
my_list1.extend(my_list2)
print(my_list1)
