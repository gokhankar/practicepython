# Implement a function that takes as input three variables, and returns the largest of the
# three. Do this without using the Python max() function!


print("I want three variables from you")
variable1 = input("Type 1st variable: ")
variable2 = input("Type 2nd variable: ")
variable3 = input("Type 3rd variable: ")
my_list = [variable1, variable2, variable3]
my_list.sort()
print(f"The largest variable is {my_list[len(my_list)-1]}")
