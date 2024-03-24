# for _ in range(10):     # when you have to use one varoable but you dont use after that, you can place _
#     print('Hello World')

import cv2 
import numpy as np

my_image = np.ones((500, 800), dtype=np.uint8) *255

# my_image = np.random.random((250, 350))*255
# my_image = np.array(my_image, dtype=np.uint8)

cv2.rectangle(my_image, (30, 35), (350, 410), 128, 4) # row is colom in here
cv2.circle(my_image, (600, 200), 100, 120, 10)
cv2.line(my_image, (100,100), (700, 150), 180, 15)
cv2.putText(my_image, 'Python is the best programming language', (40, 200), cv2.FONT_HERSHEY_SIMPLEX, 1,100 )

print(my_image)

cv2.imshow('result', my_image)
cv2.waitKey()