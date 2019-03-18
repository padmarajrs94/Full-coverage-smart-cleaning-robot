import cv2
import numpy as np


gray_image = cv2.imread('Room.png', 0)
row, height = gray_image.shape
#cv2.imshow('ROOM', image)
ret, binary = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)   # To convert image from Grayscale to Binary format
#cv2.imshow('ROOM THRESHOLD', thresh)
cv2.imwrite('Room_binary.jpg', binary)


binary = np.float32(binary)
corners = cv2.goodFeaturesToTrack(binary, 100, 0.01, 5)         #To find the corners of the image
corners = np.int0(corners)
