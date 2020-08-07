# Create a program that will play the “cows and bulls” game with the user.

import random


def generate_number():
    return random.randint(1000, 10000)


def make_list():
    return list(str(random_number))


def get_num(help_text="Guess a 4-digit number: "):
    return input(help_text)


def cows_and_bulls():
    cows = 0
    bulls = 0
    for i in range(0, 4):
        if guess_list[i] == my_list[i]:
            cows += 1
        elif guess_list[i] in my_list:
            bulls += 1
    print(f"cows={cows} and bulls={bulls}")


random_number = generate_number()
my_list = make_list()
print(my_list)
print("Lets play Cows and bulls!\nI generated a 4-digit number. ")
while True:
    guess_list = list(str((get_num())))
    print(guess_list)
    cows_and_bulls()
