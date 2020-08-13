# In the previous exercise we created a dictionary of famous scientists’ birthdays.
# In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk,
# rather than having the dictionary defined in the program.#
# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you
# have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON
# file should keep getting bigger and bigger.

import json

def add_birthday():
    name = input("Please write the name and surname of person you want to add to our dictionary: ")
    birthday = input("Please now write the birthday of the person: ")
    birthday_dictionary[name] = birthday
    print("Data saved to our dictionary")

print("Welcome to birthday dictionary!\nThis is a database that saves birthdays of people.")
with open("info.json", "r") as f:
    birthday_dictionary = json.load(f)
print("We have the data of these people:")
print(birthday_dictionary.keys())
# print(birthday_dictionary)
while True:
    ans = input("Do you want to add a person to our birthday dictionary? 'Y' for yes, 'N' for no: ").upper()
    if ans == "Y":
        add_birthday()
    elif ans == "N":
        print(birthday_dictionary)
        with open("info.json", "w") as f:
            json.dump(birthday_dictionary, f)
        quit()
    else:
        continue
