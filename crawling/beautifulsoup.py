from bs4 import BeautifulSoup
import  urllib.request as req

res = req.urlopen('http://127.0.0.1:5500/test.html')
soup = BeautifulSoup(res, 'html.parser')
text = soup.p.text
div = soup.find_all('div')
print(div)