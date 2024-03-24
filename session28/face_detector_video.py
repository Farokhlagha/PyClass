import cv2

cap = cv2.VideoCapture('obama.mp4')
image_sticker = cv2.imread('sticker.jpeg')

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    _, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(frame_gray, 1.3)

    for face in faces:
        x, y, w, h = face
        # cv2.rectangle(image_gray, [x, y], [x+w, y+h], 0, 4)
        sticker = cv2.resize(image_sticker, [w, h])
        frame[y:y+h, x:x+w] = sticker



    cv2.imshow('result', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break