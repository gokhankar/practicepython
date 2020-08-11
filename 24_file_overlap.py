# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of
# happy numbers up to 1000.

file1 = open("happynumbers.txt", "r")
file2 = open("primenumbers.txt", "r")

my_list1 = file1.readlines()
my_list2 = file2.readlines()
overlapping_list = []

for i in my_list1:
    if i in my_list2:
        overlapping_list.append(i.replace("\n", ""))

for elem in overlapping_list:
    print(elem)
