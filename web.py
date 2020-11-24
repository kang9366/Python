from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('http://www.naver.com/')
soup = BeautifulSoup(response, 'html.parser')
for anchor in soup.select("span.keyword"):
    print(anchor)