import cv2 as cv
import numpy as np

# ================================ 데이터 불러오기 ========================================#

file = 'drive.mp4'
cap = cv.VideoCapture(file)
Nframe = 0  # frame 수

# =================================== 메인 루틴 ===========================================#

while cap.isOpened():
    ret, frame = cap.read()

    if ret:  # 비디오 프레임을 읽기 성공했으면 진행
        frame = cv.resize(frame, (1000, 562))
    else:
        break

    Nframe += 1
    origin = np.copy(frame) #동영상 파일 카피

    gray = cv.cvtColor(origin, cv.COLOR_BGR2GRAY) #회색으로 이미지 만들기

    blur = cv.GaussianBlur(gray, (11, 11), 2) #가우시안 필터 사용하여 블러링 처리

    canny = cv.Canny(blur, 30, 70) #canny엣지필터사용하여 엣지검출


    # cv.imshow('canny', canny)
    #   # 원본영상

    # 다각형으로 차선만을 검출 ROI 설정
    def region_of_interest(origin, verticles, color3=(255,255,255), color1=255):
        mask = np.zeros_like(origin)
        if len(origin.shape) > 2:
            color = color3
        else:
            color = color1

        cv.fillPoly(mask, verticles, color)

        ROI_cap = cv.bitwise_and(origin, mask)
        return ROI_cap

    point = np.array([[280,300],[900,300],[1000,500],[0,500]])
    roi = region_of_interest(canny, [point])

    cv.imshow('roi', roi)

    # cv2.HoughLines(image, rho, theta, threshold)
    # 허프변환 이용하기
    lines = cv.HoughLines(roi, 1, np.pi / 180, 150)

    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv.line(origin, (x1, y1), (x2, y2), (255, 0, 0), 2)

    cv.imshow('original', origin)

    if cv.waitKey(1) & 0xff == ord('q'):  # 'q'누르면 영상 종료
        break



print("Number of Frame: ", Nframe)  # 영상의 frame 수 출력

cap.release()
cv.destroyAllWindows()
