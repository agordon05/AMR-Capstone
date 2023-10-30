import os
import sys
from Robot_command import robot_startup
import numpy
import cv2
import traitlets
import ipywidgets.widgets as widgets

directory = robot_startup.directory
sys.path.append(directory)

from jetbot import Camera, bgr8_to_jpeg

camera = Camera.instance(width=224, height=224)
image = widgets.Image(format='jpeg', width=224, height=224)  # this width and height doesn't necessarily have to match the camera

camera_link = traitlets.dlink((camera, 'value'), (image, 'value'), transform=bgr8_to_jpeg)
#print data array
#cv2.imwrite(image, mode = 'RGB')