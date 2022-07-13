#image output

import cv2
import os

os.chdir("/Users/kangseunggu/Desktop/Python/openCV")
img = cv2.imread('img.jpg') #해당 경로의 파일 읽어오기

#읽기 옵션

img1 = cv2.imread('img.jpg', cv2.IMREAD_COLOR) #컬러 이미지, 투명영역 미포함
img2 = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE) #흑백 이미지
img3 = cv2.imread('img.jpg', cv2.IMREAD_UNCHANGED) #투명영역까지 포함

cv2.imshow('img', img2) #img라는 이름의 창에 img표시
cv2.waitKey(5000) #지정된 시간(ms) 동안 사용자 키 입력 대기(0일 때는 무한정대기)
cv2.destroyAllWindows() #모든 창 닫기


