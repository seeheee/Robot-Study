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

# ==================== Roberts filter(로버츠 필터) 이용 ====================
# RobertsFilter_x = np.array([[0, 0, 0],[0, 1, 0],[-1, 0, 0]])
# RobertsFilter_y = np.array([[-1, 0, 0],[0, 1, 0],[0, 0, 0]])
#
# Roberts_img_x = cv.filter2D(img, -1, RobertsFilter_x)
# Roberts_img_y = cv.filter2D(img, -1, RobertsFilter_y)
#
# cv.imshow('RobertsimgX', Roberts_img_x)
# cv.imshow('RobertsimgY', Roberts_img_y)
#
#
# cv.waitKey()
# exit()
# ==================================================

# # ==================== Prewitt filter(프리윗 필터) 이용 ====================
# PrewittFilter_x = np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]])
# PrewittFilter_y = np.array([[-1, -1, -1],[0, 0, 0],[1, 1, 1]])
#
# Prewitt_img_x = cv.filter2D(img, -1, PrewittFilter_x)
# Prewitt_img_y = cv.filter2D(img, -1, PrewittFilter_y)
#
# cv.imshow('PrewittimgX', Prewitt_img_x)
# cv.imshow('PrewittimgY', Prewitt_img_y)
#
#
# cv.waitKey()
# exit()
# # # ==================================================

# # ==================== Sobel filter(소벨 필터) 이용 ====================
# SobelFilter_x = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
# SobelFilter_y = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]])
#
# Sobel_img_x = cv.filter2D(img, -1, SobelFilter_x)
# Sobel_img_y = cv.filter2D(img, -1, SobelFilter_y)
#
# cv.imshow('SobelimgX', Sobel_img_x)
# cv.imshow('SobelimgY', Sobel_img_y)
#
#
# cv.waitKey()
# exit()
# # ==================================================