import cv2
import numpy as np

image_tooth = cv2.imread('input/tooth.png')
image_mask = cv2.imread('input/mask.png')

image_tooth = cv2.cvtColor(image_tooth, cv2.COLOR_BGR2GRAY)
image_mask = cv2.cvtColor(image_mask, cv2.COLOR_BGR2GRAY)

# for chang blac to 255, white to 0
image_mask = image_mask / 255.0

# result = image_tooth * image_mask
result = cv2.multiply(image_tooth, image_mask)

cv2.imwrite('output/new-tooth.png', result)