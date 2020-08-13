# In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in!


import json
from collections import Counter

with open("info.json", "r") as f:
    birthdays = json.load(f)

num_to_string = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

months = []
for name, birthday_string in birthdays.items():
    month = str(birthday_string.split(".")[1])
    months.append(num_to_string[month])

print(Counter(months))
