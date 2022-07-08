import cv2
cap = cv2.VideoCapture("rtsp://admin:Computervision20@63.42.242.124:8005")

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()