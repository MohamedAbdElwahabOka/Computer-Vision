# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 17:28:13 2025
@author: mohamed
"""

import cv2                      # OpenCV library for computer vision operations
import numpy as np              # NumPy for matrix operations
from time import sleep          # sleep() used for delay if needed

# ====================== Configuration ======================

y1 = 550                        # Y-coordinate for the counting line
ww = 80                         # Minimum width of a detected object to be considered a vehicle
hh = 80                         # Minimum height of a detected object
offset = 6                      # Margin range above/below the counting line to trigger counting

delay = 60                      # (Not used currently) could be for frame rate control
detect = []                     # List to store center points of detected vehicles
carros = 0                      # Vehicle counter

# ====================== Function to calculate center of object ======================
def pega_center(x, y, w, h):
    cx = x + int(w / 2)         # Center X = x + half width
    cy = y + int(h / 2)         # Center Y = y + half height
    return cx, cy

# ====================== Read the video ======================
cap = cv2.VideoCapture("video.mp4")   # Load video from file

# Create background subtractor using MOG2 method
BGS = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=100)

# ====================== Process video frame by frame ======================
while True:
    ret, frame1 = cap.read()           # Read one frame from video
    if not ret:                        # Break if no frame is returned (end of video)
        break

    # Convert frame to grayscale
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to smooth the image and reduce noise
    blur = cv2.GaussianBlur(grey, (1, 1), 5)

    # Apply background subtraction to get moving objects
    img_sub = BGS.apply(blur)

    # Convert the image to binary (only 0 and 255 values)
    _, img_sub = cv2.threshold(img_sub, 244, 255, cv2.THRESH_BINARY)

    # Create a kernel (matrix) for morphological operations
    kernel = np.ones((5, 5), np.uint8)

    # Remove noise using opening (erosion followed by dilation)
    cleaned = cv2.morphologyEx(img_sub, cv2.MORPH_OPEN, kernel, iterations=2)

    # Fill gaps using closing (dilation followed by erosion)
    cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Further dilate the image to strengthen white regions
    dilat = cv2.dilate(img_sub, kernel)

    # Find contours (boundaries) of white objects
    contor, _ = cv2.findContours(dilat, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the counting line on the original frame
    cv2.line(frame1, (25, y1), (1200, y1), (176, 130, 39), 2)

    # Loop through each detected contour
    for c in contor:
        (x, y, w, h) = cv2.boundingRect(c)             # Get bounding box for each contour

        # Only continue if the contour is big enough to be a vehicle
        validar_contor = (w >= ww) and (h >= hh)
        if not validar_contor:
            continue

        # Draw bounding box on the frame
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Calculate the center point of the object
        center = pega_center(x, y, w, h)
        detect.append(center)

        # Draw center point
        cv2.circle(frame1, center, 4, (0, 0, 255), -1)

        # Check if object has crossed the counting line
        for (cx, cy) in detect:
            if (y1 - offset) < cy < (y1 + offset):
                carros += 1                               # Increase vehicle counter
                cv2.line(frame1, (25, y1), (1200, y1), (100, 255, 13), 3)  # Highlight the line
                detect.remove((cx, cy))                   # Remove counted object
                print("عدد السيارات المكتشفة:", carros)     # Print car count in Arabic

    # Show total car count on frame
    cv2.putText(frame1, "VEHICLE COUNT: " + str(carros), (320, 70),
                cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)

    # Show the processed mask and original video
    cv2.imshow("Detection Mask", dilat)
    cv2.imshow("Video Original", frame1)

    # Press ESC to exit
    if cv2.waitKey(30) == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
