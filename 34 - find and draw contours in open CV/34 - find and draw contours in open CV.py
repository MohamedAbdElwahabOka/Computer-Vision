# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 22:17:21 2025

@author: mohamed
"""

import numpy as np
import cv2


img = cv2.imread('images.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgray, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print("Number of contours = " + str(len(contours)))

print(contours[0])


cv2.drawContours(img, contours, 2, (0, 255, 0), 3)

cv2.imshow('Image', img)

cv2.imshow('Image GRAY', imgray)

cv2.waitKey(0)

cv2.destroyAllWindows()#close window