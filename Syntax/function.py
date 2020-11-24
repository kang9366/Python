#type of function
# 1. method : 클래스 내에 선언된 함수
# 2. function : 사용자 정의 함수
# 3. lambda : lambda함수

import pyperclip
import pyautogui as pag

def input_lecture():
    global num
    num = input('강의 수 입력 : ')
    num = int(num)
    lecture = []
    for i in range(num):
        name = input(str(i+1) + '번째 강의명 : ')
        lecture.append(name)
    return lecture
lecture = input_lecture()

pyperclip.copy(lecture[0])
pyperclip.copy(lecture[1])
pyperclip.copy(lecture[2])
pag.hotkey('ctrl', 'v')