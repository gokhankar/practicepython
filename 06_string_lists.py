# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

print("A palindrome is a string that reads the same forwards and backwards.")
while True:
    word = input("Type a palindrome: ")
    wordlist = list(word)
    reverse_word =[]
    for i in wordlist:
        reverse_word.insert(0,i)

    if wordlist == reverse_word:
        print(f"'{word}' is a Palindrome")
    else:
        print(f"'{word}' is not a Palindrome")
