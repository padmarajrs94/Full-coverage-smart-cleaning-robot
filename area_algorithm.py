import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

start_time = time.time()
# color image
image = cv2.imread('Room.png')
obstacles = []
color = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (128, 128, 128), (128, 0, 255), (255, 0, 128), (0, 128, 255), (0, 255, 255), (255, 128, 0)]
H, V, HR, VR = [], [], [], []

# grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
height, width = gray_image.shape[:2]
# cv2.imshow('ROOM', image)
ret, binary = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)   # To convert image from Grayscale to Binary format
# cv2.imshow('ROOM THRESHOLD', thresh)
cv2.imwrite('Room_binary.png', binary)

binary = np.float32(binary)
corners = cv2.goodFeaturesToTrack(binary, 100, 0.01, 5)         # To find the corners of the image
corners = np.int0(corners)

'''
for i in corners:
    x,y = i.ravel()
    cv2.circle(gray_image, (x,y), 3, 0, -1)
print(corners)
plt.imshow(gray_image)
plt.show()
print(corners)
'''
cx, cy = corners.shape[0], corners.shape[1]


def create_grid():
    new_img = cv2.imread('Room_binary.png', 0)
    px = 50
    for i in range(0, width, px):
        cv2.line(new_img, (i, 0), (i, height), 0)
    for i in range(0, height, px):
        cv2.line(new_img, (0, i), (width, i), 0)
    cv2.imwrite('Room_binary.png', new_img)


# Area division
def area_div():
    # x, y = V[0], HR[0]     # 0, 899
    # while True:
    for x in V:                 # [0, 399, 499, 500, 599, 699, 799, 899]
        for y in HR:            # [899, 799, 699, 499, 399, 398, 199, 0]
            new_img = cv2.imread('Room_binary.png', 0)
            fixed_pos = new_img[x][y]
            flag = 0
            if fixed_pos == 255:
                for iy in H:        # [0, 199, 398, 399, 499, 699, 799, 899]
                    for ix in VR:   # [899, 799, 699, 599, 500, 499, 399, 0]
                        var_pos = new_img[ix][iy]
                        if var_pos == 255:
                            start_row, start_col = iy, x
                            end_row, end_col = y, ix
                            bool = False

                            for i in range(start_row, end_row+1):
                                for j in range(start_col, end_col+1):
                                    if new_img[i][j] == 0:
                                        bool = True
                            print('Loop: ', x, y, ix, iy, '\t', start_row, start_col, end_row, end_col)
                            if bool == False:
                                for i in range(start_row, end_row+1):
                                    for j in range(start_col, end_col+1):
                                        new_img[i][j] = 128
                                cv2.imwrite('Room_binary.png', new_img)
                                print('no:', x, y, ix, iy, '\t', start_row, start_col, end_row, end_col)
                                flag = 1
                                break
                    if flag == 1:
                        break


new_corner = []
for i in corners.reshape(cx, 2):
    new_corner.append(tuple((i[0], i[1])))
corners = new_corner
for (c1, c2) in corners:
    H.append(c2-1)
    V.append(c1-1)
H.append(0)
H.append(899)
V.append(0)
V.append(899)
H.sort()
V.sort()


def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


H = Remove(H)
V = Remove(V)
HR = H[::-1]
VR = V[::-1]
print(H)
print(V)
print(HR)
print(VR)

area_div()

# create_grid()

print(time.time() - start_time)