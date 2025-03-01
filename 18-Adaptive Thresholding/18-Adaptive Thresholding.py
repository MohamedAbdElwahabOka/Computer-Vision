# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:19:27 2025

@author: mohamed
"""

import cv2 
import numpy as np 


img = cv2.imread("sudoku.png")

_,th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)


th2 = cv2.adaptiveThreshold( , maxValue, adaptiveMethod, thresholdType, blockSize, C)


cv2.imshow("imge",img)
cv2.imshow("th1",th1)

 
cv2.waitKey(0)

cv2.destroyAllWindows()