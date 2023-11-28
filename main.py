# import cv2
# cap = cv2.VideoCapture(0)


# rep, frame = cap.read()

# print(rep)

# while rep == True:
#     _, frame = cap.read()

#     cv2.imshow("gui", frame)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()
# print("bskdfhs")

import requests
import numpy as np
import cv2

url = 'http://192.168.2.140/cam-hi.jpg'


while True:

    response = requests.get(url)
    image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # low_b = np.uint8([5,5,5])
    # high_b = np.uint8([0,0,0])
    # mask = cv2.inRange(image, high_b, low_b)
    # contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)
    # cv2.imshow('mask', mask)gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Chuyển ảnh sang ảnh xám
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Áp dụng Gaussian Blur để làm mờ ảnh
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Phát hiện cạnh trong ảnh
    edges = cv2.Canny(blur, 50, 150)

    # Dò line bằng phương pháp Hough Line Transform
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)

    # Vẽ các line lên ảnh gốc
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow('Image', image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()