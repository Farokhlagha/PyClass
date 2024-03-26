import cv2
import numpy as np

image = cv2.imread('input/Polar-Bear.jpg') #, cv2.IMREAD_GRAYSCALE)

#kernel = np.array([[0, -1, 0],    # sharpening filter
#                  [-1, 5, -1],
#                  [0, -1, 0]])

#kernel = np.array([[-2, -1, 0],    # emboss filter
#                  [-1, 1, 1],
#                  [0, 1, 2]])

#kernel = np.array([[-1, 0, 1],    # edge detection filter
#                  [-2, 0, 2],
#                  [-1, 0, 1]])

kernel = np.ones((3, 3)) /9   # blur filter
result = cv2.filter2D(image, -1, kernel)
#result = cv2.blur(image, [3,3]) # blur filter

cv2.imwrite('output/result5.jpg', result)

