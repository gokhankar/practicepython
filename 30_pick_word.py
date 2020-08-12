# In this exercise, the task is to write a function that picks a random word from a list of words
# from the SOWPODS dictionary.
import random


def pick_a_word():
    with open('sowpods.txt', 'r') as f:
        my_list = f.readlines()
    return random.choice(my_list).strip()


picked_word = pick_a_word()
print(picked_word)
