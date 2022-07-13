import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

#quote_plus() : 문자를 아스키코드로 바꿈
headers = {'User-Agent': 'Mozilla/5.0'}

base_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plus_url = input('검색어를 입력하세요 : ')

url = base_url + quote_plus(plus_url)
html = requests.get(url, headers = headers).text
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all('img', '_img')

for i in img:
    print(i['data-source'])
    print()