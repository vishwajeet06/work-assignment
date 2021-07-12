import cv2
import matplotlib.pyplot as plt

#  getting gray image with flag 0 deafult is 1 for rgb color
image = cv2.imread('./external-content.duckduckgo.com.jpg', 0)

cv2.imshow('goku', image)

# wait for any key to be pressed

cv2.waitKey(0)
