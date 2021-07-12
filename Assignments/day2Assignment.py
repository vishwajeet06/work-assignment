import cv2
import numpy as np
import matplotlib.pyplot as plt


# converting video in normal and gray

video = cv2.VideoCapture('testing.mp4')
grayVideo = cv2.VideoCapture('testing.mp4', 0)
# grayVid = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
print('video loaded')

while video.isOpened():
    ret, frame = video.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        zeros = np.zeros((gray.shape[0], gray.shape[1]), np.uint8)
        b, g, r = cv2.split(frame)

        red = cv2.merge((zeros, zeros, r))
        green = cv2.merge((zeros, g, zeros))
        blue = cv2.merge((b, zeros, zeros))

        final = cv2.merge((b, g, r))
        # cv2.imshow('frame', final)

        # amplifying video
        cusVideo = cv2.merge((b+100, g, r+100))
        # cv2.imshow('frame', cusVideo)

        #  canvas
        # draw line
        cv2.line(frame, (100, 100),
                 (gray.shape[1]-100, gray.shape[0]-100), (0, 0, 255), 2)

        # draw rectangle
        cv2.rectangle(frame, (100, 100),
                      (gray.shape[1]-100, gray.shape[0]-100), (255, 0, 255), 2)
        # put text
        cv2.putText(frame, 'I think its done', (140, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 3, 255)

        # cv2.imshow('red', red)
        # cv2.imshow('green', green)
        # cv2.imshow('blue', blue)
        cv2.imshow('real', frame)
        # cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
