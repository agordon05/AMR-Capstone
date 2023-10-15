import os
import sys
import numpy
import cv2
import pylibdmtx #https://libdmtx.sourceforge.net/
from pylibdmtx.pylibdmtx import decode #as dmtxdecode

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
capture.release()
