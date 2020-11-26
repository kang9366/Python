from bs4 import BeautifulSoup as bs
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
url = 'http://www.naver.com'
data = requests.get(url, headers = headers).text
soup = bs(data, 'html.parser')
realtime = soup.find_all('div', 'NM_RTK_VIEW_list_wrap')
print(realtime)