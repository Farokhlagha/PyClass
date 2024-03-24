# image1: 255, 100, 1, 127, 250
# image2: 255, 100, 1, 127, 250

# result: 1, 1, 1, 1, 1

import cv2
image1 = cv2.imread('input/a.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('input/b.jpg', cv2.IMREAD_GRAYSCALE)

result = image1 / image2

cv2.imshow('result', result)
cv2.waitKey()
