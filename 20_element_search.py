# Write a function that takes an ordered list of numbers (a list where the elements are in order
# from smallest to largest) and another number. The function decides whether or not the given
# number is inside the list and returns (then prints) an appropriate boolean.
# Extras: Use binary search.

import random


def my_function():
    random_list = random.sample(range(100), k=20)
    my_list = sorted(random_list)
    print(my_list)
    num = random.randint(1,100)
    print(num)
    return num in my_list


if my_function() is True:
    print(True)
else:
    print(False)