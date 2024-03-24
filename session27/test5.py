import cv2  

cap = cv2.VideoCapture('Qt 6 - The Ultimate UX Development Platform.mp4')  

while True:
    _, farme = cap.read()
    frame = cv2.cvtColor(farme, cv2.COLOR_BGR2GRAY)

    _, frame = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY)

    cv2.imshow('result', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

