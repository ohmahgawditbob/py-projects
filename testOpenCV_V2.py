import numpy as np
import cv2
from time import sleep

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
tempret, initframe = cap.read()
#sleep(1)
calib = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)
prev_frame = cv2.cvtColor(initframe, cv2.COLOR_BGR2GRAY)
while(True):
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    res = cv2.subtract(calib, gray)

    _, blurskinthresh = cv2.threshold(cv2.medianBlur(res,5), 50, 255, cv2.THRESH_BINARY)
    
    ##graythresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    _, graythresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)
    change = cv2.subtract(gray, prev_frame)
    fgmask = fgbg.apply(frame)
    _, fg = cv2.threshold(fgmask, 250, 255, cv2.THRESH_BINARY)
    ##_, changethresh = cv2.threshold(change, 115, 255, cv2.THRESH_BINARY)
    ##changethresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    _, contours,_ = cv2.findContours(blurskinthresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    if len(contours) > 0:
        hull = cv2.convexHull(contours[0],returnPoints = False)
    ##defects = cv2.convexityDefects(contours[0],hull)
    cv2.drawContours(frame, contours, -1,(0,0,255), 2)
    ##for i in range(defects.shape[0]):
    ##    s,e,f,d = defects[i,0]
    ##    start = tuple(contours[0][s][0])
    ##    end = tuple(contours[0][e][0])
    ##    far = tuple(contours[0][f][0])
    ##    cv2.line(frame,start,end,[0,255,0],2)
    ##    cv2.circle(frame,far,5,[0,0,255],-1)
    cv2.imshow('Original',frame)
    cv2.imshow('Movement', change)
    cv2.imshow('Matte', graythresh)
    cv2.imshow('Arms', blurskinthresh)
    cv2.imshow('Foreground', res)
    ##cv2.imshow('Foreground', fg)
    ##cv2.imshow('Movement Threshold', changethresh)
    
    prev_frame = gray
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()
