# Take the code from the How To Decode A Website exercise (if you did not do it or just want
# to play with some different code, use the code from the solution), and instead of printing
# the results to a screen, write the results to a txt file. In your code, just make up a name
# for the file you are saving to. Extras:
# Ask the user to specify the name of the output file that will be saved.


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

file = open("txt_file.txt", "a", encoding='utf-8')
file.write(text)
