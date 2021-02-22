import cv2 as cv
import numpy as np

img = cv.imread('homework.jpg')     # image size : (429, 697)

# 1. 주어진 이미지를 Gray Scale로 변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 2. 이미지 Blurring 처리
blur = cv.GaussianBlur(gray, (7, 7), 2)

# 3. Canny Edge로 Edge만 검출
canny = cv.Canny(blur, 30, 70)

# 4. ROI로 차선 부분만 추출
## 직사각형이 아닌 사다리꼴 등의 모양으로 ROI 할 때 사용 ##
def region_of_interest(img, vertices, color3=(255, 255, 255), color1=255):  # ROI 셋팅
    mask = np.zeros_like(img)  # mask = img와 같은 크기의 빈 이미지
    if len(img.shape) > 2:  # Color 이미지(3채널)라면 :
        color = color3
    else:  # 흑백 이미지(1채널)라면 :
        color = color1
    # vertices에 정한 점들로 이뤄진 다각형부분(ROI 설정부분)을 color로 채움
    cv.fillPoly(mask, vertices, color)
    # 이미지와 color로 채워진 ROI를 합침
    ROI_image = cv.bitwise_and(img, mask)
    return ROI_image

# vertices point 설정 - np.array([[왼쪽 위], [오른쪽 위], [오른쪽 아래], [왼쪽 아래]])
point = np.array([[10,315], [790,240], [790,680], [0,680]])
roi = region_of_interest(canny, [point])

cv.imshow("original", img)
cv.imshow("gray", gray)
cv.imshow("blur", blur)
cv.imshow("canny", canny)
cv.imshow("final", roi)
cv.waitKey(0)