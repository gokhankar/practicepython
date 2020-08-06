# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)
# Remember the rules:Rock beats scissors, Scissors beats paper, Paper beats rock
import random


def random_choice():
    random_list = ["R", "P", "S"]
    return random.choice(random_list)


def you_lose():
    print(f"My choice was '{my_choice}', you lose!")
    print("Lets play one more time")


def you_win():
    print(f"My choice was '{my_choice}', you win!")
    print("Congratulations!!!")
    print("Lets play one more time")


def draw():
    print(f"My choice was '{my_choice}' too! No Winner! ")
    print("Lets play one more time")


print("Lets play Rock Paper Scissors!")
while True:
    your_choice = input("Chose one: Rock, Paper or Scissors? R/P/S: ").upper()
    my_choice = random_choice()
    if your_choice == my_choice:
        draw()
    elif your_choice == "R":
        if my_choice == "P":
            you_lose()
        elif my_choice == "S":
            you_win()
    elif your_choice == "P":
        if my_choice == "S":
            you_lose()
        elif my_choice == "R":
            you_win()
    elif your_choice == "S":
        if my_choice == "R":
            you_lose()
        elif my_choice == "P":
            you_win()
    else:
        print("Please type only 'R', 'P' or 'S'")
    print(50 * "*")
