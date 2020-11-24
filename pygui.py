import pyautogui as pag
import pyperclip
import time
# 조회 버튼
#pag.click(1183,138)

def click(x, y):
    return pag.click(x, y)

def input_lecture():
    global num
    num = input('강의 수 입력 : ')
    num = int(num)
    lecture = []
    for i in range(num):
        name = input(str(i+1) + '번째 강의명 : ')
        lecture.append(name)


def login(id, pw):
    click(1334, 430)
    pag.typewrite(id)
    click(1299, 488)
    pag.typewrite(pw)
    pag.click(1532, 486)
    time.sleep(0.8)

def basket():
    click(1227, 133)
    time.sleep(2)

def input_id():
    id = input('아이디 : ')
    return id
id = input_id()

def input_pw():
    pw = input('비밀번호 : ')
    return pw
pw = input_pw()

input_lecture()
login(id, pw)
basket()

def first_lecture_search():
    click(1718, 266)

def left_lecture_search():
    click(1543, 266)

def apply():
    for i in range(num):
        if i == 0:
            first_lecture_search()
        else:
            left_lecture_search()
    pyperclip.copy(lecture[i])
    pag.hotkey('ctrl', 'v')
    pag.press('enter')

    



def apply_first_lecure(lecture):
    pyperclip.copy(lecture)
    pag.hotkey('ctrl', 'v')
    pag.press('enter')

    #click lecture
    click(1161, 403)
    time.sleep(0.2)

    #apply lecture
    pag.click(1337, 428)
    pag.press('enter')
    time.sleep(0.3)
    pag.press('enter')
    time.sleep(0.3)

# 과목 검색
pag.click(1718, 266)
pyperclip.copy('응용')
pag.hotkey('ctrl', 'v')
pag.press('enter')

# 과목 클릭
pag.click(1161, 403)
time.sleep(0.2)

# 과목 신청
pag.click(1337, 428)
pag.press('enter')
time.sleep(0.3)
pag.press('enter')
time.sleep(0.3)

#-------------

# 과목 검색
pag.click(1543, 266)
pag.hotkey('ctrl', 'a')
pyperclip.copy('데이터과학을위한')
pag.hotkey('ctrl', 'v')
pag.press('enter')

# 과목 클릭
pag.click(1161, 403)
time.sleep(0.2)

# 과목 신청
pag.click(1337, 428)
pag.press('enter')
time.sleep(0.3)
pag.press('enter')
time.sleep(0.3)

#------------

# 과목 검색
pag.click(1543, 266)
pag.hotkey('ctrl', 'a')
pyperclip.copy('불어')
pag.hotkey('ctrl', 'v')
pag.press('enter')

# 과목 클릭
pag.click(1161, 403)
time.sleep(0.2)

# 과목 신청
pag.click(1337, 428)
pag.press('enter')
time.sleep(0.3)
pag.press('enter')
time.sleep(0.3)

#--------
# 과목 검색
pag.click(1543, 266)
pag.hotkey('ctrl', 'a')
pyperclip.copy('어드벤쳐')
pag.hotkey('ctrl', 'v')
pag.press('enter')

# 과목 클릭
pag.click(1161, 403)
time.sleep(0.2)

# 과목 신청
pag.click(1337, 428)
pag.press('enter')
time.sleep(0.3)
pag.press('enter')
time.sleep(0.3)

#-----------

# 과목 검색
pag.click(1543, 266)
pag.hotkey('ctrl', 'a')
pyperclip.copy('텍스트마이닝')
pag.hotkey('ctrl', 'v')
pag.press('enter')


# 과목 클릭
pag.click(1161, 403)
time.sleep(0.2)

# 과목 신청
pag.click(1337, 428)
pag.press('enter')
time.sleep(0.3)
pag.press('enter')
time.sleep(0.3)

#--------
# 과목 검색
pag.click(1543, 266)
pag.hotkey('ctrl', 'a')
pyperclip.copy('선형대수')
pag.hotkey('ctrl', 'v')
pag.press('enter')

# 과목 클릭
pag.click(1134, 508)
time.sleep(0.2)

# 과목 신청
pag.click(1337, 428)
pag.press('enter')
time.sleep(0.3)
pag.press('enter')
time.sleep(0.3)

#-----

# 과목 검색
pag.click(1543, 266)
pag.hotkey('ctrl', 'a')
pyperclip.copy('자바')
pag.hotkey('ctrl', 'v')
pag.press('enter')

# 과목 클릭
pag.click(1161, 403)
time.sleep(0.2)

# 과목 신청
pag.click(1337, 428)
pag.press('enter')
time.sleep(0.3)
pag.press('enter')
time.sleep(0.3)