import cv2  

cap = cv2.VideoCapture(0)  # open my webcam monitor: 0   webcame labtop: 1

_, frame = cap.read()
rows = frame.shape[0]
cols = frame.shape[1]

writer = cv2.VideoWriter('farok.mp4', cv2.VideoWriter_fourcc(*'XVID'), 30, (cols, rows)) # rows <> cols

while True:
    _, farme = cap.read()
    
    frame = cv2.cvtColor(farme, cv2.COLOR_BGR2GRAY)
    _, frame = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY)

    writer.write(frame)
    cv2.imshow('result', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    writer.release() # close file