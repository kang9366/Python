#video output
#동영상 파일 출력

import cv2
cap = cv2.VideoCapture('/Users/kangseunggu/Desktop/Python/openCV/video.mp4')


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("더 이상 가져올 프레임x")
        break
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'):
        print("사용자 입력에 의해 종료")
        break

cap.release()
cv2.destroyAllWindows()