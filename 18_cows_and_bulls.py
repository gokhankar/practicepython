# Create a program that will play the “cows and bulls” game with the user.

import random


def make_list():
    generated_list = [str(random.randint(1, 9))]
    while len(generated_list) < 4:
        elem = str(random.randint(0, 9))
        if elem not in generated_list:
            generated_list.append(elem)
    return generated_list


def get_num(help_text="Guess a 4-digit number: "):
    while True:
        try:
            num = int(input(help_text))
        except:
            print("Please type a 4-digit number")
            continue
        if 10000 > num > 999:
            return num
        else:
            print("Please type a 4-digit number")


def cows_and_bulls():
    global count
    cows, bulls = 0, 0
    for i in range(0, 4):
        if guess_list[i] == my_list[i]:
            bulls += 1
        elif guess_list[i] in my_list:
            cows += 1
    print(f"cows={cows} and bulls={bulls}")
    count += 1
    if cows == 4:
        print(f"Congratulations!!!\nYou succeeded in {count}. try")
        quit()


my_list = make_list()
print(my_list)
print("Lets play Cows and bulls!\nI generated a 4-digit number. ")
count = 0
while True:
    guess_list = list(str((get_num())))
    cows_and_bulls()
