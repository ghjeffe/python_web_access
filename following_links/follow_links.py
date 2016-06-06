import requests
from bs4 import BeautifulSoup as bs

start_point = 18
repeat = 7
url = 'http://python-data.dr-chuck.net/known_by_Parker.html'
page_text = requests.get(url).text
soup = bs(page_text)
anchors = soup('a')

for _ in range(repeat):
    anchor = anchors[start_point - 1]
    print(anchor.text)
    url = anchor.get('href')
    page_text = requests.get(url).text
    soup = bs(page_text)
    anchors = soup('a')
