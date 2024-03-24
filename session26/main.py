# pip install opencv-python
import cv2

my_image = cv2.imread('nowruz.jpg')  # read pic
my_image_2 = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)  # convert color pic

# print(my_image_2)
print(my_image_2.shape)
print(my_image_2[10, 15]) # index numpy array

# for i in range(10, 12):
#    for j in range(15, 18):
#        my_image_2[i, j] = 0

# my_image_2[0:5, 0:198] = 0 # top side
# my_image_2[0:148, 193:198] = 0 # right side
# my_image_2[0:148, 0:5] = 0 # left side
# my_image_2[143:148, 0:198] = 0 # bottom side

apple = my_image_2[80:120, 25:75 ]
my_image_2[85:125, 140:190] = apple

# cv2.imshow('', my_image_2)  # disply pic
cv2.imshow('', my_image_2)
cv2.waitKey()
# cv2.imwrite('result.jpg', my_image_2) # save pic