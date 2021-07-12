import cv2

# open camera and show

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print('can\"t access camera')
        break
    cv2.imshow('camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
