import pyautogui as pag
from selenium import webdriver
import os

def position():
    c = pag.position()
    print(c)


print('1. 좌표 구하기 2. 종료')
while True:
    num = input('입력 : ')
    num = int(num)
    if num == 1:
        position()
    elif num == 2:
        print('프로그램을 종료합니다.')
        break
    else:
        print('잘못 입력하셨습니다.')

os.system("pause")