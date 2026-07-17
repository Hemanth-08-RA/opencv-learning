#Background Subtraction using OpenCV
import cv2
import numpy as np
# Built-in Background Subtractor
fgbg1 = cv2.createBackgroundSubtractorMOG2()
fgbg2 = cv2.createBackgroundSubtractorKNN()

cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    if not ret:
        break
    
    fgmask1 = fgbg1.apply(img)
    fgmask2 = fgbg2.apply(img)

    cv2.imshow('Original', img)
    cv2.imshow('MOG2', fgmask1)
    cv2.imshow('KMN', fgmask2)
 
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
            break
    
cap.release()
cv2.destroyAllWindows()