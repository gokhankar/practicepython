# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list
# that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
# Extras: Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_list = []
for elem in a :
    if elem in b:
        if elem in common_list:
            continue
        else:
            common_list.append(elem)
print(common_list)
"""

# Extras: Randomly generate two lists to test this
import random
list1 = random.sample(range(100), k=20)
list2 = random.sample(range(100), k=20)
common_list = []
for elem in list1:
    if elem in list2:
        if elem in common_list:
            continue
        else:
            common_list.append(elem)
print(common_list)

"""
common_list.sort()
print(common_list)
print(list1)
print(list2)
"""

# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
