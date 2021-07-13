import cv2

# 640 480
# resize image as videoCapture
bg = cv2.imread('bg.jpg')
bg1 = cv2.imread('bg1.jpg')
bg2 = cv2.imread('bg2.jpg')
bg3 = cv2.imread('bg3.jpg')
bg4 = cv2.imread('bg4.jpg')
bg5 = cv2.imread('bg5.png')
bg6 = cv2.imread('bg6.jpg')
bg7 = cv2.imread('bg7.jpg')
bg8 = cv2.imread('bg8.jpg')
bg9 = cv2.imread('bg9.jpg')

image = cv2.resize(bg4, (640, 480))
cv2.imwrite('b-g4.jpg', image)
image = cv2.resize(bg5, (640, 480))
cv2.imwrite('b-g5.jpg', image)
image = cv2.resize(bg6, (640, 480))
cv2.imwrite('b-g6.jpg', image)
image = cv2.resize(bg7, (640, 480))
cv2.imwrite('b-g7.jpg', image)
image = cv2.resize(bg8, (640, 480))
cv2.imwrite('b-g8.jpg', image)
image = cv2.resize(bg9, (640, 480))
cv2.imwrite('b-g9.jpg', image)
