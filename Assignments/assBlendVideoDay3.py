import cv2
import os
import numpy as np

listImg = os.listdir("images")
# print(listImg) for checking correct directory

imgList = []

for img in listImg:
    img = cv2.imread(f'images/{img}')
    imgList.append(img)

count = 0

video = cv2.VideoCapture(0)
print("video loaded")

while(video.isOpened()):
    ret, frame = video.read()
    if ret == True:
        # blend image and video
        frame = cv2.addWeighted(imgList[count], 0.5, frame, 0.4, 0.5)
        cv2.imshow('frame', frame)

        key = cv2.waitKey(1)
        if key == ord('a'):
            count = 1
        elif key == ord('b'):
            count = 2
        elif key == ord('c'):
            count = 3
        elif key == ord('d'):
            count = 4
        elif key == ord('e'):
            count = 5
        elif key == ord('f'):
            count = 6
        elif key == ord('g'):
            count = 7
        elif key == ord('h'):
            count = 8
        if key == ord('q'):
            break
        elif key == ord('i'):
            count = 9
video.release()
cv2.destroyAllWindows()
