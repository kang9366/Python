# ------------------------------------------
# 변수값 설정 부분(수정금지)
from urllib.request import urlopen
title_list, author_list = eval(urlopen("http://swclass.yonsei.ac.kr:2020/dev/web/hw_02.txt").read().decode().splitlines()[5])

print(f"# title_list = {title_list}")
print(f"# author_list = {author_list}")

lines_per_page = int(input("Lines per page: "))
page_num = int(input("Page number: "))
print("___output___")
# ------------------------------------------

# (순번(order), 타이틀(title), 게시자(author))를 video_list로 생성한다
video_list = []
for i in range(0, int(len(title_list)/lines_per_page)):
    video_list[i] = 

start =         # 목록 시작 위치
end =           # 목록 종료 위치

# video_list에서 출력할 부분을 잘라서 보여준다.
for  in :
    print(f"{order}: {title} - {author}")