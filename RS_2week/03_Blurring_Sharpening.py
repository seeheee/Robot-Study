import cv2 as cv
import numpy as np

Path = 'Data/'
Name1 = 'lenna.tif'
Name2 = 'salt_pepper.jpg'

src1 = Path + Name1
src2 = Path + Name2

img = cv.imread(src1, cv.IMREAD_GRAYSCALE)
img2 = cv.imread(src2, cv.IMREAD_GRAYSCALE)

cv.imshow('Original', img)

# ==================================================
# cv2.filter2D(src, ddepth, kernel)
#   src : 입력 영상
#   ddepth : 출력 영상의 데이터 타입, -1로 지정하면 입력 영상과 같은 데이터 타입으로 생성
#     cv2.CV_8U / cv2.CV_32F / cv2.CV_64F
#   kernel : 필터 행렬
# ==================================================


# ==================== 평균값 필터 ====================
# **** 실습 3) 직접 평균값 필터를 만들어 제공된 영상에 컨볼루션 연산 적용하기 ****
# blurfilter = np.array([[1/9,1/9,1/9]*3])
#
# blurimg = cv.filter2D(img, -1, blurfilter)
# cv.imshow('blurimg', blurimg)
# cv.waitKey()
# exit()
# ==================================================


# ==================== 미디언 필터 ====================
# cv2.medianBlur(src, ksize)
#   src : 원본 이미지
#   ksize: 필터 크기
# ==================================================
# median_img = cv.medianBlur(img2, 5)
#
# cv.imshow('Salt & Pepper Image', img2)
# cv.imshow('median_img', median_img)
# cv.waitKey()
# exit()
# ==================================================


# ==================== 가우시안 필터 ====================
# **** 실습 4) 직접 가우시안 필터를 만들어 제공된 영상에 컨볼루션 연산 적용하기 ****
# 3*3
# gauss_filter = np.array([[1/16, 1/8, 1/16],[1/8, 1/4, 1/8], [1/16, 1/8, 1/16]])

# 5*5
# gauss_filter = np.array([[1/256, 1/64, 1/46, 1/64, 1/256],[1/64, 1/16, 24/256, 16/256, 4/256], [6/256, 24/256, 36/256, 24/256, 6/256], ])
# gauss_img = cv.filter2D(img, -1, gauss_filter)
#
# cv.imshow('gauss_img', gauss_img)
#
# cv.waitKey()
# exit()
# ==================================================


# =============== 가우시안 필터 (함수 사용) ===============
# cv2.getGaussianKernel(ksize, sigma, ktype)
#   ksize : 필터 크기
#   sigma : 가우시안 함수 식 중 시그마 값
#   ktype : 필터 자료형 (default : float64)
# ==================================================
# gauss_filter = cv.getGaussianKernel(5, 3)
# gauss_img = cv.filter2D(img, -1, gauss_filter)
#
# cv.imshow('gauss_img', gauss_img)
#
# cv.waitKey()
# exit()
# ==================================================


# =============== 가우시안 필터 (함수 사용 2) ===============
# cv2.GaussianBlur(src, ksize, sigmaX)
#   src : 원본 이미지
#   ksize : 필터 크기, (0, 0)을 할당할 경우 sigmaX 값에 따라 자동으로 설정
#   sigmaX : 가우시안 함수 식 중 시그마값
# ==================================================
# for sigma in range(1, 5):
#     gauss_img = cv.GaussianBlur(img, (0, 0), sigma)
#     cv.imshow(f'gauss_img{sigma}', gauss_img)
#
# cv.waitKey()
# exit()
# ==================================================


# ==================== 샤프닝 ====================
# **** 실습 5) 직접 샤프닝 필터를 만들어 제공된 영상에 컨볼루션 연산 적용하기 ****
sharpfilter = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
sharpfilter2 = np.array([[0,-2,0],[-2,9,-2],[0,-2,0]])
sharpfilter3 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])

sharp_img = cv.filter2D(img, -1, sharpfilter)
sharp_img2 = cv.filter2D(img, -1, sharpfilter2)
sharp_img3 = cv.filter2D(img, -1, sharpfilter3)

cv.imshow('sharpimg', sharp_img)
cv.imshow('sharpimg2', sharp_img2)
cv.imshow('sharpimg3', sharp_img3)

cv.waitKey()
exit()
# ==================================================
