import numpy as np
import cv2
import matplotlib.pyplot as plt

image = np.array([[9, 7, 255, 0], 
                  [10, 10, 10, 0], 
                  [254, 0, 1, 1], 
                  [5, 6, 7, 8]], dtype=np.uint8)

# 0: 3
# 1: 2
# 2: 0
# 3: 0
...
# 255: 1

cv2.imwrite('output/result3.jpg', image)

histogram = [3, 2, 0, 0, 1]
plt.plot(histogram)
plt.show()