import cv2
import numpy as np


def converter():        # To convert image from BGR to Binary format
    image = cv2.imread('Room.png', 0)
    #cv2.imshow('ROOM', image)
    ret, thresh = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)
    #cv2.imshow('ROOM THRESHOLD', thresh)
    cv2.imwrite('Room_binary.jpg', thresh)
