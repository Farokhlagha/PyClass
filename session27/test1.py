import time
import cv2


image = cv2.imread('wolf.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rows, cols = image.shape

threshold = 100
start_time = time.time()
# option1
# for r in range(rows):
#     for c in range(cols):
#         if image[r, c] > threshold:
#            image[r, c] = 255
#        else:
#           image[r, c] = 0

# option2
# image[image > threshold] = 255
# image[image <= threshold] = 0

# option3
_, image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)  # _ when we dont need this variable
end_time = time.time()

print(end_time - start_time)

cv2.imshow('result', image)
cv2.waitKey()

cv2.imwrite('output.jpg', image)