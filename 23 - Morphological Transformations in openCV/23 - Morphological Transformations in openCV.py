# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 00:55:27 2025

@author: mohamed
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('smarties.png', 0)

_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV) 


kernal= np.ones((2,2),np.uint8)


dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=3)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)



cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.imshow('dilation', dilation)
cv2.imshow('erosion', erosion)
cv2.imshow('opening', opening)
cv2.imshow('closing', closing)


cv2.waitKey(0)

cv2.destroyAllWindows()