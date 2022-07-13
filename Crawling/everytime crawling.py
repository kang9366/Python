from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('lang=ko_KR')
chromedriver = "C:/Users/kangseounggu/Desktop/Python_workspace/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

#, chrome_options = chrome_options

driver.get('https://everytime.kr/login')
driver.find_element_by_name('userid').send_keys('alex9366')
driver.find_element_by_name('password').send_keys('alex0817')
driver.find_element_by_tag_name('input').send_keys(Keys.RETURN)
time.sleep(2)

driver.find_element_by_xpath('//*[@id="submenu"]/div/div[2]/ul/li[4]/a').click()
time.sleep(2)

#1페이지
res = driver.page_source
soup = BeautifulSoup(res, 'html.parser')
date = soup.select("a.article > time,medium")
print("1page")
for i in date:
    print(i.get_text())
driver.find_element_by_xpath('//*[@id="container"]/div[3]/div[2]/a').click()
time.sleep(1.5)

#2페이지
res = driver.page_source
soup = BeautifulSoup(res, 'html.parser')
date = soup.select("a.article > time,medium")
print("2page")
for i in date:
    print(i.get_text())
driver.find_element_by_xpath('//*[@id="container"]/div[3]/div[2]/a[2]').click()
time.sleep(3)

t = 3

while True:
    res = driver.page_source
    soup = BeautifulSoup(res, 'html.parser')
    date = soup.select("a.article > time,medium")
    print("\n" + str(t) + "page")
    for i in date:
        print(i.get_text())
    driver.find_element_by_xpath('//*[@id="container"]/div[3]/div[2]/a[3]').send_keys(Keys.ENTER)
    time.sleep(3)
    t = t + 1