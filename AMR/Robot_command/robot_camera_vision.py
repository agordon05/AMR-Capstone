import os
import sys
import numpy
import cv2
import traitlets
import ipywidgets.widgets as widgets

def method():
    directory = '~/jetbot'
    directory = os.path.expanduser(directory)
    sys.path.append(directory)
    from jetbot import Camera #this is part that gives numpy error

# capture = cv2.VideoCapture(0)
#
# # while True:
# ret, frame = capture.read()
#
# capture.release()
# im = numpy.asarray(frame)
# print(type(im)) #needs GStreamer pipeline implementation
#
# #print data array
# #cv2.imwrite(image, mode = 'RGB')