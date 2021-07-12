import cv2
import numpy as np

# canvas
canvas = np.zeros((512,512,3), dtype = "uint8")



# draw line
cv2.line(canvas, (0,0), (511,511), 255, 5)

# draw rectangle
cv2.rectangle(canvas, (10,10), (500,500), (0,255,0), 3)

#  put text
cv2.putText(canvas, "Vishwajeet", (50,200), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)

cv2.imshow('canvas',canvas)
cv2.waitKey(0)