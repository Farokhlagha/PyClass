import cv2
import numpy as np

image_1 = cv2.imread('input/d1.png')
image_2 = cv2.imread('input/d2.png')

# result = image_1 - image_2
result = cv2.subtract(image_1, image_2)

result = 255 - result   # change palce of dark pixl with light 

cv2.imwrite('output/d.png', result)