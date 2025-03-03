# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 17:30:39 2025

@author: mohamed
"""

import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('balloons_noisy.png')

averaging = cv2.blur(img,(5,5))

gblur = cv2.GaussianBlur(img, (5, 5), 0)

median = cv2.medianBlur(img, 5)


cv2.imshow("img", img)
cv2.imshow("averaging", averaging)
cv2.imshow("gblur", gblur)
cv2.imshow("median", median)

cv2.imwrite('output/gblur.png', gblur) 
cv2.imwrite('output/averaging2.png', averaging)
cv2.imwrite('output/median.png', median) 

cv2.waitKey(0)

cv2.destroyAllWindows()