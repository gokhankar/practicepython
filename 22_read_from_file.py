# Given a .txt file that has a list of a bunch of names, count how many of each name there
# are in the file, and print out the results to the screen. I have a .txt file for you, if you
# want to use it! Extra: Instead of using the .txt file from above (or instead of, if you want
# the challenge), take this .txt file, and count how many of each “category” of each image
# there are. This text file is actually a list of files corresponding to the SUN database scene
# recognition database, and lists the file directory hierarchy for the images. Once you take
# a look at the first line or two of the file, it will be clear which part represents the scene
# category. To do this, you’re going to have to remember a bit about string parsing in Python 3.


# file = open("nameslist.txt", "r")
with open('nameslist.txt', 'r') as file:
    my_list = file.readlines()
# my_set = set(my_list)                # Darth, Luke, Lea (3 Objects)
# print(my_set)
count_darth = 0
count_luke = 0
count_lea = 0
for i in my_list:
    if "Darth" in i:
        count_darth += 1
    if "Luke" in i:
        count_luke += 1
    if "Lea" in i:
        count_lea += 1
print(f"Darth {count_darth}")
print(f"Luke {count_luke}")
print(f"Lea {count_lea}")

file.close()
