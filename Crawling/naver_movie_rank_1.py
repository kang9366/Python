from bs4 import BeautifulSoup
import requests
import os

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date='

while True:
    num = input('1. 순위 검색 2. 종료 : ')
    num = int(num)
    if num == 1:
        year = input('input year for 4 digits : ')
        month = input('input month for 2 digits : ')
        date = input('input date for 2 digits : ')
        d_url = url + year + month + date

        data = requests.get(d_url, headers = headers).text
        soup = BeautifulSoup(data, 'html.parser')
        td = soup.find_all('div', 'tit3')

        title = []
        for i in td:
            temp = []
            temp.append(i.find('a').text)
            title.append(temp)
        print('\n' + str(year) + '년 ' + str(month) + '월 ' + str(date) + '일 영화 순위' + '\n')
        for i in range(len(title)):
            if i < 9:
                print(' ' + str(i + 1) + '위 : ', end = "")
                print(", ".join(title[i]))
            else : 
                print(str(i + 1) + '위 : ', end = "")
                print(", ".join(title[i]))
    elif num == 2:
        break
    else:
        print('잘못 입력하셨습니다.')
    



os.system('Pause')
