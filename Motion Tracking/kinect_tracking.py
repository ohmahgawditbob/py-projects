## Note ##
# Be sure all parts of you have contrast with the background. An optimal setup would be a
# pure white background so that any article of clothing has contrast. A well lit scene is
# also recommended. Irregularities in the backdrop have strange effects on tracking...

## Code by Collin Harrell, licensed under the Unlicense.

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
_, initframe = cap.read()
calibrate_bool = True  # Set to false if you would like to use regular adaptive background subtraction algorithms. WARNING: This is less reliable
print("Starting...\n")

if calibrate_bool:
    #calib = cv2.cvtColor(initframe, cv2.COLOR_BGR2GRAY)  # Sets the calibration frame up to be used by the algorithm
    calib = cv2.medianBlur(cv2.imread(r'Path to Calibration Image', cv2.IMREAD_GRAYSCALE),3)  # Sets the calibration frame up to be used by the algorithm as a set background image
    while True:  # MAIN LOOP
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fg = abs(cv2.medianBlur(gray, 3) - calib)  # Blurs calibration and frame image to smooth out most of the noise (We only need a rough outline).
        _,mask = cv2.threshold(cv2.medianBlur(fg,5), 100, 255, cv2.THRESH_BINARY)
        _, contours,_ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

        cv2.drawContours(frame, contours, -1,(0,0,255), 2)

        cv2.imshow('Original', frame)
        cv2.imshow('Foreground', mask)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
else:
    fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=False, dist2Threshold=150)
    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fg = fgbg.apply(gray)
        _,mask = cv2.threshold(cv2.medianBlur(fg,5), 25, 255, cv2.THRESH_BINARY)

        _, contours,_ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            hull = cv2.convexHull(contours[0],returnPoints = False)
        #cv2.drawContours(frame, contours, -1,(0,0,255), 2)
        defects = cv2.convexityDefects(contours[0],hull)
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(contours[0][s][0])
            end = tuple(contours[0][e][0])
            far = tuple(contours[0][f][0])
            cv2.line(frame,start,end,[0,255,0],2)
            cv2.circle(frame,far,5,[0,0,255],-1)
        cv2.imshow('Original', frame)
        cv2.imshow('Mask', mask)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        elif k == 96:
            print("Calibration Image Saved")
            cv2.imwrite('calibration.png', frame)
            break

cap.release()
cv2.destroyAllWindows()