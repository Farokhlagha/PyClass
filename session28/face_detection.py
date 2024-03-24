# github.com/opencv/opencv/data/harrcascades/
import cv2

image = cv2.imread('Cillian Murphy.jpeg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_sticker = cv2.imread('sticker.jpeg')

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = face_detector.detectMultiScale(image_gray)
for face in faces:
    x, y, w, h = face
    # cv2.rectangle(image_gray, [x, y], [x+w, y+h], 0, 4)
    sticker = cv2.resize(image_sticker, [w, h])
    image[y:y+h, x:x+w] = sticker


cv2.imshow('result', image)
cv2.waitKey()