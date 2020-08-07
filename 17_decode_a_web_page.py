#  Use the BeautifulSoup and requests Python packages to print out a list
#  of all the article titles on the New York Times homepage.


import requests
from bs4 import BeautifulSoup


r = requests.get("https://www.nytimes.com")
source = BeautifulSoup(r.content, "lxml")
titles = source.find_all("h2")
end_titles = titles.pop(len(titles)-1)
end_titles = titles.pop(len(titles)-1)
titles_list = []
for i in titles:
    titles_list.append(i.text)
print(titles_list)
