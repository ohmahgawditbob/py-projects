import cv2
import numpy as np
import matplotlib.pyplot as plt

feed = cv2.VideoCapture(0)

while True:
    ret, frame = feed.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original', frame)
    cv2.imshow('Grayscale', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

feed.release()
cv2.destroyAllWindows()
