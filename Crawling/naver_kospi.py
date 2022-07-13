import urllib.request as req
from bs4 import BeautifulSoup
import requests
import os

headers = {'User-Agent': 'Mozilla/5.0'}

url = 'https://finance.naver.com/'
data = requests.get(url, headers = headers).text
soup = BeautifulSoup(data, 'html.parser')
kospi = soup.find_all('span', 'num')[0].get_text()
print('현재 코스피 지수는 ' + kospi + ' 입니다.\n')

num = soup.find_all('span', 'num_quot up')
print('')

for i in num:
    blind = i.find('span', 'blind')
    print(blind)

print(num)

fluc_num = soup.find_all('span', 'num2')[0].get_text()
print('전일 대비 ' + fluc_num + ' 하락했습니다.')

persent = soup.find_all('span', 'num3')
div = soup.find_all('div', 'heading_area')[0]

os.system('Pause')