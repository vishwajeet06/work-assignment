import cv2
import numpy


# convert image to gray

grayImg = cv2.imread('goku.jpg', 0)
image = cv2.imread('goku.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imshow('goku', image)
# cv2.imshow('goku_gray', gray)
# cv2.imshow('gray',grayImg)


# for different color
zeros = numpy.zeros((gray.shape[0], gray.shape[1]), numpy.uint8)
b, g, r = cv2.split(image)

red = cv2.merge((zeros, zeros, r))
blue = cv2.merge((b, zeros, zeros))
green = cv2.merge((zeros, g, zeros))

# cv2.imshow('red',red)
# cv2.imshow('blue',blue)
# cv2.imshow('green',green)

cusImg = cv2.merge((b, g, r))
# cv2.imshow('cusImg',cusImg)

# savimg the image

# cv2.imwrite('blueGoku.png', blue)
# cv2.imwrite('greenGoku.png', green)
# cv2.imwrite('redGoku.png', red)


# amplifying image for testing (truncation)
cusImg = cv2.merge((b, g+100, r))
# cv2.imshow('cusImg', cusImg)


# broadcasting the image





cv2.waitKey(0)
