import os
import sys
import robot_startup
from robot_startup import robot
import numpy
import cv2
import traitlets
import ipywidgets.widgets as widgets

directory = '~/jetbot'
directory = os.path.expanduser(directory)
sys.path.append(directory)
from jetbot import Camera

#print data array
#cv2.imwrite(image, mode = 'RGB')