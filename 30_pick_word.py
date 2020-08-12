# In this exercise, the task is to write a function that picks a random word from a list of words
# from the SOWPODS dictionary.
import random


def pick_a_word():
    file = open("sowpods.txt", "r")
    my_list = file.readlines()
    random_index = random.randint(1, (len(my_list)-1))
    return my_list[random_index].replace("\n", "")


picked_word = pick_a_word()
print(picked_word)
