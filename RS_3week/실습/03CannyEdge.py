import cv2 as cv

Path = ''
Name = 'img.jpg'
FullName = Path+Name

img = cv.imread(FullName, cv.IMREAD_GRAYSCALE)

# cv2.Canny() 함수
# cv2.Canny(img, minimum thresholding value, maximum thresholding value)
canny = cv.Canny(img, 30, 100)

cv.imshow('original', img)
cv.imshow('CannyEdge', canny)
cv.waitKey(0)
cv.destroyAllWindows()