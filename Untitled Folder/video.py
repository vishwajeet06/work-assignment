import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while cap.isOpened():

    ret, image = cap.read()
    if ret:
        # convert to gray
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # zeros = np.zeros((gray.shape[0], gray.shape[1]), np.uint8)
        # b, g, r = cv2.split(image)

        # red = cv2.merge((zeros, zeros, r))
        # blue = cv2.merge((b, zeros, zeros))
        # green = cv2.merge((zeros, g, zeros))
        # cv2.imshow('red', red)
        # cv2.imshow('blue', blue)
        # cv2.imshow('green', green)
        cv2.imshow('image', image)
        cv2.imshow('gray', gray)
        k = cv2.waitKey(50)
        if k & 0xFF == ord('q'):
            break
