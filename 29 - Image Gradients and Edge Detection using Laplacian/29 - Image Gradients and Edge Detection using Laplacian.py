# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 21:31:16 2025

@author: mohamed
"""

import cv2
import numpy as np 
from matplotlib import pyplot as plt
img = cv2.imread("data/messi.jpg", 0)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
#lap2 = np.uint8(np.absolute(lap))

cv2.imshow("img", img)
cv2.imshow("lap", lap)
#cv2.imshow("lap", lap2)
cv2.imwrite('output/lap.png', lap)
#cv2.imwrite('output/lap.png', lap2)  
cv2.waitKey(0)

cv2.destroyAllWindows()