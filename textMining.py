from bs4 import BeautifulSoup
import requests

headers = {'User-Agent' : 'Mozilla/5.0'}
#url = 'https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=129406&target=after&page=1'
url = 'https://movie.naver.com/movie/bi/mi/point.nhn?code=181710'
data = requests.get(url, headers = headers).text
soup = BeautifulSoup(data, 'html.parser')
#table = soup.select("table", class_= "list_netizen")
table = soup.select("div", class_="input_netizen ")
#review = table.find_all("br")
print(table)
