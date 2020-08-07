# Write a program (using functions!) that asks the user for a long string containing multiple
# words. Print back to the user the same string, except with the words in backwards order.

def get_sentence(help_text="Give me a sentence"):
    return input(help_text)


def backwards():
    new = sentence.split()
    for i in new:
        my_list.insert(0, i)


def make_sentence():
    last_sentence = " ".join(my_list)
    print(last_sentence)


sentence = get_sentence("Please type a long string containing multiple words: ")
my_list = []
backwards()
make_sentence()
