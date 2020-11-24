import urllib.request
import csv
from bs4 import BeautifulSoup as bs

hdr = { 'User-Agent' : 'Mozilla/5.0' }
url = 'https://www.melon.com/chart/'

req = urllib.request.Request(url, headers = hdr)
html = urllib.request.urlopen(req).read()
soup = bs(html, 'html.parser')

lst50 = soup.select(".lst50, .lst100")
melonList = []

for i in lst50:
    temp = []
    temp.append(i.select_one('.rank').text + '위')
    temp.append(i.select_one('.ellipsis.rank01').a.text) 
    temp.append(i.select_one('.ellipsis.rank02').a.text)
    temp.append(i.select_one('.ellipsis.rank03').a.text)
    melonList.append(temp)

print(melonList)

with open('melon_chart.txt', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['순위', '곡명', '아티스트', '앨범'])
    writer.writerows(melonList)