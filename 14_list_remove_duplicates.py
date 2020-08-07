# Write a program (function!) that takes a list and returns a new list
# that contains all the elements of the first list minus all the duplicates.
# Extras:Write two different functions to do this - one using a loop and constructing a list,
# and another using sets.

def loop_list():
    new_loop_list = []
    for i in my_list:
        if i not in new_loop_list:
            new_loop_list.append(i)
    print(new_loop_list)


def set_list():
    new_set_list = list(set(my_list))
    print(new_set_list)


my_list = [1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 8, 8, 8, 9, 9, 0, 12, 5, 7, 21, 33, 12, 23]
loop_list()
set_list()
