# For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information
# based on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should
# ask the user to enter a name, and return the birthday of that person back to them.

def gimme_birthday():
    print("I have data about:")
    for i in birthday_dictionary.keys():
        print(i)
    return print(birthday_dictionary[input("Who's birthday do you want to learn? ")])


birthday_dictionary = {
    "Gökhan Karaçay": "28.03.1983",
    "Umut Rıza Ertürk": "02.02.1983",
    "Şahin K.": "01.01.1963",
    "Murat Karadut": "31.01.1960",
    "Coşkun Soysal": "04.04.1983"
}

# print(birthday_dictionary)
gimme_birthday()
