import os
import sys
# import numpy
# import cv2
# import traitlets
# import ipywidgets.widgets as widgets
directory = '~/jetbot'
directory = os.path.expanduser(directory)
sys.path.append(directory)
# from jetbot import Camera #this is part that gives numpy error
import traitlets
import ipywidgets.widgets as widgets
from IPython.display import display
from jetbot import Camera, bgr8_to_jpeg


# should only display a live image feed
def method():
    camera = Camera.instance(width=224, height=224)
    image = widgets.Image(format='jpeg', width=224,
                          height=224)  # this width and height doesn't necessarily have to match the camera
    camera_link = traitlets.dlink((camera, 'value'), (image, 'value'), transform=bgr8_to_jpeg)
    display(image)

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