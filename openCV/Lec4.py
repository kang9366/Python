#도형 그리기

from pickletools import uint8
import cv2
import numpy as np

#480x640 에 해당하는 빈 스케치북 만들기

img = np.zeros((480, 640, 3), dtype = np.uint8)
img[:] = (0, 0, 0) #색상설정(BGR순)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#일부영역 색칠
img1 = np.zeros((480, 640, 3), dtype = np.uint8)

img1[100:200, 200:300] = (255, 255, 255)
cv2.imshow('img', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#직선
img2 = np.zeros((480, 640, 3), dtype = np.uint8)
color = (0, 255, 255) #BGR, 선의 색
thinkness = 3 #선의 두께
cv2.line(img2, (50, 100), (400, 50), color, thinkness, cv2.LINE_8) #대각선을 포함한 8방향으로 연결된 선(기본값)
cv2.line(img2, (50, 200), (400, 150), color, thinkness, cv2.LINE_4) #상하좌우 4방향으로 연결된 선
cv2.line(img2, (50, 300), (400, 250), color, thinkness, cv2.LINE_AA) #부드러운 선

cv2.imshow('img', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#원
img3 = np.zeros((480, 640, 3), dtype = np.uint8)
color = (255, 255, 0)
radius = 50
cv2.circle(img3, (200, 100), radius, color, thinkness, cv2.LINE_AA) #객체, 원의 중심, 반지름, 색상, 굵기, 선의 종류 --> 속이 빈 원
cv2.circle(img3, (400, 100), radius, color, cv2.FILLED, cv2.LINE_AA) #객체, 원의 중심, 반지름, 색상, 굵기, 선의 종류 --> 속이 찬 원


cv2.imshow('img', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

#사각형
img4 = np.zeros((640, 480, 3), dtype = np.uint8)
color = (255, 255, 0)

cv2.rectangle(img4, (100, 100), (200, 200), color, thinkness) #속이 빈 사각형
cv2.rectangle(img4, (300, 100), (400, 300), color, cv2.FILLED) #속이 찬 사각형
cv2.imshow('img', img4)
cv2.waitKey(0)
cv2.destroyAllWindows()

#다각형
img5 = np.zeros((640, 480, 3), dtype = np.uint8)

color = (0, 0, 255)

pts1 = np.array([[100, 100], [200, 200], [100, 200]])
cv2.polylines(img5, [pts1], True, color, thinkness, cv2.LINE_AA)

cv2.imshow('img', img5)
cv2.waitKey(0)
cv2.destroyAllWindows()