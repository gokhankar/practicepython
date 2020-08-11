# the user, will have in your head a number between 0 and 100. The program will guess a number,
# and you, the user, will say whether it is too high, too low, or your number. At the end of this
# exchange, your program should print out how many guesses it took to get your number. As the
# writer of this program, you will have to choose how your program will strategically guess.
# A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.)
# until you hit the number. But that’s not an optimal guessing strategy. An alternate strategy
# might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as
# needed. After you’ve written the program, try to find the optimal strategy!
# (We’ll talk about what is the optimal one next week with the solution.)


def binary():
    return my_list[(int((len(my_list)/2)))]


my_list = []
for i in range(1, 101):
    my_list.append(i)

print("Pick a number between 0 and 100 in your mind\nI will try to guess it")
start = input("Are you ready? Type 'Y' and press enter when ready: ").upper()
while True:
    if start == "Y":
        while int(len(my_list)) > 1:
            num = binary()
            print(f"Is your number: {num}?")
            y_n_answer = input("Type 'Y' for yes, type 'N'for no: ").upper()
            if y_n_answer == "Y":
                print(f"Bingo! \nThanks for the game!")
                quit()
            elif y_n_answer == "N":
                if int(len(my_list)) == 2:
                    print(f"Your number is {my_list[0]}.\nBingo!")
                    quit()
                l_h_answer = input(f"If {num} is higher than your number type 'H', or if {num} is lower type 'L' please: ").upper()
                if l_h_answer == "H":
                    del my_list[(int(len(my_list)/2)):]
                elif l_h_answer == "L":
                    del my_list[:((int(len(my_list) / 2))+1)]
            else:
                y_n_answer = input("Type 'Y' for yes, type 'N'for no: ").upper()
            print(my_list)
        if int(len(my_list)) < 2:
            print(f"Your number is {my_list[0]} \nBingo!")
            quit()

    else:
        start = input("Are you ready? Type 'Y' and press enter when ready: ").upper()
