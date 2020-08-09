# Using the requests and BeautifulSoup Python libraries, print to the screen the full text
# of the article on this website:
# http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture
# The article is long, so it is split up between 4 pages.
# Your task is to print out the text to the screen so that you can read the full
# article without having to click any buttons.


import requests
from bs4 import BeautifulSoup


r = requests.get('http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture')
soup = BeautifulSoup(r.content, 'html.parser')
my_text = soup.find_all('p')
# for item in enumerate(my_text):
#    print(item)
edit_text = my_text[6:86]
text = ""
for item in edit_text:
    item = str(item)
    item = item.replace("<p>", "").replace("</p>", "").replace('<p class="has-dropcap">', "")
    item = item.replace("<em>", "").replace("</em>", "").replace("<strong>", "").replace("</strong>", "")
    text = text + item + "\n"

print(text)
