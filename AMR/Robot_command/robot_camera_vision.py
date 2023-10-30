import os
import sys
import numpy
import cv2
import traitlets
import ipywidgets.widgets as widgets

# directory = '~/jetbot'
# directory = os.path.expanduser(directory)
# sys.path.append(directory)
# #from jetbot import Camera

capture = cv2.VideoCapture(0)

# while True:
ret, frame = capture.read()

capture.release()
im = numpy.asarray(frame)
print(type(im))

#print data array
#cv2.imwrite(image, mode = 'RGB')