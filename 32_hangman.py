# This exercise is Part 3 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 2.
# In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses
# (head, body, 2 legs, and 2 arms) before they lose the game.
# In Part 1, we loaded a random word list and picked a word from it.
# In Part 2, we wrote the logic for guessing the letter and displaying that information to the user.
# In this exercise, we have to put it all together and add logic for handling guesses.
# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:
# Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them
# - let them guess again. Optional additions:
# When the player wins or loses, let them start a new game.
# Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman.
# This is challenging - do the other parts of the exercise first!
# Your solution will be a lot cleaner if you make use of functions to help you!

import random


def pick_a_word():
    with open('sowpods.txt', 'r') as f:
        my_list = f.readlines()
    return random.choice(my_list).strip()


def printing():
    p_word = ""
    for elem in print_screen:
        p_word = p_word + elem + " "
    return p_word


def get_letter():
    global failures
    letters = "QWERTYUOPASDFGHJKLIZXCVBNM"
    print(printing())
    while len(letter_list) < len(list_word):
        letter = input("Type a letter please: ").upper()
        if letter in letters and len(letter) == 1:
            if letter not in all_letters:
                all_letters.append(letter)
                if letter in list_word:
                    if letter not in str(letter_list):
                        letter_list.append(letter)
                        #                        print(letter_list)
                        return letter
                else:
                    print(f"{letter} is not a letter of my word")
                    failures += 1
                    print(f"You have only {6 - failures} guesses, be careful! \n{hangman_figure()}  \n")
                    if failures == 6:
                        print(f"My word is {word}")
                        quit()
                    break
            else:
                print(f"You typed {letter} previously")
                continue
        else:
            print("Letters are here: QWERTYUOPASDFGHJKLIZXCVBNM")
            continue


def letter_search():
    count = 0
    for item in list_word:
        if item == lt:
            print_screen[count] = lt
            count += 1
        else:
            count += 1
            continue


def same_letters():
    lw = set(list_word)
    re_count = 0
    for item in list_word:
        if item in lw:
            lw.remove(item)
        else:
            re_count += 1
    return re_count


def hangman_figure():
    if failures == 1:
        return " ____." + "\n" + " ¦   |" + "\n" + " o   |" + "\n" + "     |" + "\n" + "     |" + "\n" + "     |"
    elif failures == 2:
        return " ____." + "\n" + " ¦   |" + "\n" + " o   |" + "\n" + " |   |" + "\n" + "     |" + "\n" + "     |"
    elif failures == 3:
        return " ____." + "\n" + " ¦   |" + "\n" + " o   |" + "\n" + "/|   |" + "\n" + "     |" + "\n" + "     |"
    elif failures == 4:
        return " ____." + "\n" + " ¦   |" + "\n" + " o   |" + "\n" + "/|\  |" + "\n" + "     |" + "\n" + "     |"
    elif failures == 5:
        return " ____." + "\n" + " ¦   |" + "\n" + " o   |" + "\n" + "/|\  |" + "\n" + "/    | " + "\n" + "     |"
    elif failures == 6:
        return " ____." + "\n" + " ¦   |" + "\n" + " o   |" + "\n" + "/|\  |" + "\n" + "/ \  | " + "\n" + "     |" + "You died!!! "


print("Lets play Hangman!\nI have a word, try to find!\nDo not forget that you can make only 6 failures!")
word = pick_a_word()
# print(word)
letter_list = []
all_letters = []
failures = 0
list_word = list(word)
print_screen = []
for i in list_word:
    if i in letter_list:
        print_screen.append(i)
    else:
        print_screen.append("_")
# print(list_word)
last_count = 0
r = same_letters()
while (len(list_word) - r) > len(letter_list):
    last_count += 1
    lt = get_letter()
    letter_search()
if (len(list_word) - r) == len(letter_list):
    print(printing())
    print(f"Congratulations! Bingo at {last_count}. try")
