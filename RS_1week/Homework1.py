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

# 이미지 복사(원본이미지도 띄우고 싶어서..)
img_copy = img.copy()

# 가로축 그리기
cv.line(img_copy, (0, 256), (512, 256), (255, 0, 0), 3)
# 세로축 그리기
cv.line(img_copy, (256, 0), (256, 512), (255, 0, 0), 3)

# x좌표의 합과 y좌표의 합을 담을 변수 초기화
sum_x = 0
sum_y = 0
cnt = 0

for y in range(512):
    for x in range(512):
        if img_copy[y][x][2] > 175:
            img_copy[y][x][0] = 0
            img_copy[y][x][1] = 0
            img_copy[y][x][2] = 255
            sum_x += x
            sum_y += y
            cnt += 1
# print("x의 총합", "y의 총합", "count", sum_x,sum_y,cnt)

# 어차피 사분면에 모여있을테니까는 x와 y좌표의 평균값을 구하면 한라봉이 몇 사분면에 존재하는지 알 수 있음
avg_X = sum_x / cnt
avg_y = sum_y / cnt

if 256 <= avg_X < 512 and 0 <= avg_y < 256:
    print("위치: 제1사분면")
elif 0 <= avg_X < 256 and 0 <= avg_y < 256:
    print("위치: 제2사분면")
elif 0 <= avg_X < 256 and 256 <= avg_y < 512:
    print("위치: 제3사분면")
elif 256 <= avg_X < 512 and 256 <= avg_y < 512:
    print("위치: 제4사분면")

# 원본 이미지 출력
cv.imshow('Original', img)
# 결과 이미지 출력
cv.imshow('result', img_copy)

# 가로, 세로 픽셀 수, 채널 수 출력
print("크기:", img.shape)

while cv.waitKey(33) <= 0:
    cv.setMouseCallback('result', mouse_callback, img)  #imshow에 쓴 winName이랑 같은 창에 마우스이벤트 적용

cv.waitKey(0)


