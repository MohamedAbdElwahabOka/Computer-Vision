# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:55:40 2025

@author: mohamed
"""

import cv2

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)

    # Pick pixel value
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

    color = "Undefined"

    if hue_value < 5:
        color = "DEEP RED"
    elif hue_value < 10:
        color = "RED"
    elif hue_value < 15:
        color = "BRICK RED"
    elif hue_value < 20:
        color = "BROWNISH RED"
    elif hue_value < 25:
        color = "RED-ORANGE"
    elif hue_value < 30:
        color = "ORANGE"
    elif hue_value < 35:
        color = "DARK ORANGE"
    elif hue_value < 40:
        color = "GOLDEN ORANGE"
    elif hue_value < 45:
        color = "GOLD"
    elif hue_value < 50:
        color = "YELLOW"
    elif hue_value < 55:
        color = "PALE YELLOW"
    elif hue_value < 60:
        color = "LEMON YELLOW"
    elif hue_value < 65:
        color = "YELLOW-GREEN"
    elif hue_value < 70:
        color = "LIME"
    elif hue_value < 75:
        color = "LIME GREEN"
    elif hue_value < 80:
        color = "LIGHT GREEN"
    elif hue_value < 90:
        color = "EMERALD GREEN"
    elif hue_value < 100:
        color = "DARK GREEN"
    elif hue_value < 110:
        color = "TEAL"
    elif hue_value < 120:
        color = "CYAN-GREEN"
    elif hue_value < 130:
        color = "CYAN"
    elif hue_value < 140:
        color = "AQUA"
    elif hue_value < 150:
        color = "LIGHT BLUE"
    elif hue_value < 160:
        color = "SKY BLUE"
    elif hue_value < 170:
        color = "PERIWINKLE"
    elif hue_value < 180:
        color = "BLUE"
    elif hue_value < 190:
        color = "INDIGO"
    elif hue_value < 200:
        color = "DARK BLUE"
    elif hue_value < 210:
        color = "PURPLE-BLUE"
    elif hue_value < 220:
        color = "VIOLET"
    elif hue_value < 230:
        color = "DARK VIOLET"
    elif hue_value < 240:
        color = "PURPLE"
    elif hue_value < 250:
        color = "MAGENTA"
    elif hue_value < 260:
        color = "HOT PINK"
    elif hue_value < 270:
        color = "BRIGHT PINK"
    elif hue_value < 280:
        color = "LIGHT PINK"
    elif hue_value < 290:
        color = "PASTEL PINK"
    elif hue_value < 300:
        color = "ROSE PINK"
    elif hue_value < 310:
        color = "PINKISH RED"
    elif hue_value < 320:
        color = "DARK PINK"
    elif hue_value < 330:
        color = "DEEP RED-PINK"
    elif hue_value < 340:
        color = "BURGUNDY"
    elif hue_value < 350:
        color = "DARK RED"
    else:
        color = "RED"

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
    cv2.imshow("Frame", frame)
    #out.write(frame) #save your video
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()

cv2.destroyAllWindows()