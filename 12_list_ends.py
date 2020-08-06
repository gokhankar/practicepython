# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

def make_list():
    return [a[0], a[len(a) - 1]]


a = [5, 10, 15, 20, 25]
new_list = make_list()
print(new_list)
