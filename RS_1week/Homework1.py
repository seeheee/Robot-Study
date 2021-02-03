import cv2 as cv
import numpy as np

def mouse_callback(event, x, y, flags, param):
    if event == 1:
        print('B: ', param[y][x][0], '\nG: ', param[y][x][1], '\nR: ', param[y][x][2])
        print('=================================')


Path = 'Data/'
Name = 'rabong.jpg'
FullName = Path + Name

# 이미지 읽기
img = cv.imread(FullName)







# 이미지 출력
cv.imshow('result', img)

while cv.waitKey(33) <= 0:
    cv.setMouseCallback('result', mouse_callback, img)  #imshow에 쓴 winName이랑 같은 창에 마우스이벤트 적용

cv.waitKey(0)


