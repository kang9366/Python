import pyautogui as pag
import datetime as dt
import time


def click(x, y):
    return pag.click(x, y)

apply_tab = pag.locateOnScreen('apply_tab.png')
center = 

endhope=False

while True:
    print("0 : 수강신청 탭으로 이동 1 ~ 7 : 강의 수강신청")
    num = input('입력 : ')
    num = int(num)

    if(num == 0):
        while not endhope:
            tim=dt.datetime.now()
            if tim.second>=59 and tim.microsecond>100000:
                time.sleep(0.9)
                click(726, 125)
                #pag.press('enter')
                break
            else:
                time.sleep(0.1)
                print(tim)

    elif(num == 1):
        click(345, 325)
        pag.press('enter')
        pag.press('enter')

    elif(num == 2):
        click(338, 361)
        pag.press('enter')
        pag.press('enter')

    elif(num == 3):
        click(341, 395)
        pag.press('enter')
        pag.press('enter')

    elif(num == 4):
        click(339, 413)
        pag.press('enter')
        pag.press('enter')

    elif(num == 5):
        click(341, 430)
        pag.press('enter')
        pag.press('enter')

    elif(num == 6):
        click(338, 456)
        pag.press('enter')
        pag.press('enter')

    elif(num == 7):
        click(345, 486)
        pag.press('enter')
        pag.press('enter')

    elif(num == 8):
        break