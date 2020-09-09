from bs4 import BeautifulSoup
import requests
import os

login_url = "https://smartlead.hallym.ac.kr/login/index.php"
craw_url = 'https://smartlead.hallym.ac.kr/'
task_url = 'https://smartlead.hallym.ac.kr/mod/assign/index.php?id='
home_url = "https://smartlead.hallym.ac.kr/course/view.php?id="
session = requests.session()

while True:
    id = input('학번 : ')
    id = str(id)
    pw = input('PW : ')
    pw = str(pw)
    params = dict()
    params['username'] = id
    params['password'] = pw

    try:
        res = session.post(login_url, data = params)
        res.raise_for_status()
        res = session.get(craw_url)
        soup = BeautifulSoup(res.content, "html.parser")
        title = soup.find_all('h3')
        prof = soup.find_all('p', 'prof')
        link = soup.find_all('a', 'course_link')

        subjectNum_list = []
        for i in link:
            temp = []
            temp.append(i["href"][50:])
            subjectNum_list.append(temp)

        title_list_temp = []
        for i in title:
            temp_1 = []
            temp_1.append(i.get_text())
            title_list_temp.append("'".join(temp_1))
        
        title_list= []
        for i in range(0, len(title_list_temp)):
            if (title_list_temp[i])[-3:] == "NEW":
                title_list.append((title_list_temp[i])[:-3])
            else :
                title_list.append(title_list_temp[i])

        prof_list = []
        for i in prof:
            temp_2 = []
            temp_2.append(i.get_text())
            prof_list.append(temp_2)

        task_list = []
        for i in range(0, len(subjectNum_list)):
            temp_3 = []
            res = session.get(task_url + "'".join(subjectNum_list[i]))
            soup = BeautifulSoup(res.content, "html.parser")
            try:
                atd = soup.find_all("td", 'cell c3')[-1].text
                temp_3.append(atd)
                task_list.append(temp_3)
            except IndexError as e:
                temp_3.append("과제 없음")
                task_list.append(temp_3)

        attend_y_list = []
        attend_n_list = []
        attend_l_list = []

        for i in range(0, len(title_list)):
            temp_4 = []
            temp_5 = []
            temp_6 = []

            res = session.get(home_url + "'".join(subjectNum_list[i]))
            soup = BeautifulSoup(res.content, "html.parser")
            
            try:
                attend_y = soup.find("p", "count01").text
                temp_4.append(attend_y)
                attend_y_list.append(temp_4)

                attend_n = soup.find("p", "count02").text
                temp_5.append(attend_n)
                attend_n_list.append(temp_5)

                attend_l = soup.find("p", "count03").text
                temp_6.append(attend_l)
                attend_l_list.append(temp_6)
            except AttributeError:
                temp_4.append("0")
                attend_y_list.append(temp_4)
                temp_5.append("0")
                attend_l_list.append(temp_5)
                temp_6.append("0")
                attend_n_list.append(temp_6)
        break
    except IndexError:
        print("학번 또는 비밀번호 오류\n")

cnt_a = 0
cnt_t = 0

attend_index_list = []
for i in range(0, len(attend_y_list)):
    temp_7 = []
    if int("'".join(attend_l_list[i])[-1]) >= 1 or int("'".join(attend_n_list[i])[-1]) >= 1:
        cnt_a += 1
        temp_7.append(i)
        attend_index_list.append(" ".join(map(str, temp_7)))

task_index_list = []
for i in range(0, len(task_list)):
    temp_8 = []
    if "'".join(task_list[i]) == "미제출":
        cnt_t += 1
        temp_8.append(i)
        task_index_list.append(" ".join(map(str, temp_8)))

print("")
for i in range(0, len(title_list)):
        print("강의 " + str(i+1))
        print("===========================================")
        print(title_list[i] + " - " + "'".join(prof_list[i]))
        if int("'".join(attend_y_list[i])[-1]) == 0 and int("'".join(attend_n_list[i])[-1]) == 0 and int("'".join(attend_l_list[i])[-1]) == 0:
            print("\n-출결 : X")
        else :
            print("\n-출결 : " + "'".join(attend_y_list[i]) + " " + "'".join(attend_n_list[i]) + " " + "'".join(attend_l_list[i]))
        print("\n-과제 : " + "'".join(task_list[i]))
        print("===========================================\n\n")

unsubmit_subject_list = []
print("제출해야 할 과제 : " + str(cnt_t) + "개")
for i in range(0, len(title_list)):
    for t in range(0, len(task_index_list)):
        temp_9 = []
        if str(i) == str(task_index_list[t]):
            temp_9.append(title_list[i])
            unsubmit_subject_list.append("'".join(temp_9))
print(unsubmit_subject_list)

absent_subject_list = []
print("\n출석 미완료 강의 : " + str(cnt_a) + "개")
for i in range(0, len(title_list)):
    for t in range(0, len(attend_index_list)):
        temp_10 = []
        if str(i) == str(attend_index_list[t]):
            temp_10.append(title_list[i])
            absent_subject_list.append("'".join(temp_10))
print(absent_subject_list)

os.system("pause")