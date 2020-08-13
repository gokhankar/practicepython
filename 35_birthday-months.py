#  In this exercise, load that JSON file from disk, extract the months of all the birthdays,
#  and count how many scientists have a birthday in each month.

import json
from collections import Counter

with open("info.json", "r") as f:
    birthday_dictionary = json.load(f)

dates = birthday_dictionary.values()
months = []
for date in dates:
    month = str(list(date)[3] + list(date)[4])
    months.append(month)
c = Counter(months)
print(c)
