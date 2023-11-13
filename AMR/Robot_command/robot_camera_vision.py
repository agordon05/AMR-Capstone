import os
import sys
# import sensor

# import image #used in [https://www.youtube.com/watch?v=PffDblwNshM], may be needed
import cv2
import time
import math
import pylibdmtx.pylibdmtx
from pylibdmtx.pylibdmtx import decode

directory = '~/jetbot'
directory = os.path.expanduser(directory)
sys.path.append(directory)
import traitlets
import ipywidgets.widgets as widgets
from IPython.display import display
from jetbot import Camera, bgr8_to_jpeg

dir = 'dataset/imageFeed'
file_name = 'image.jpg'
sleep_time = 5

#detector = cv2.QRCodeDetector

# should only display a live image feed
def method():
    camera = Camera.instance(width=224, height=224)
    image = widgets.Image(format='jpeg', width=224,
                          height=224)  # this width and height doesn't necessarily have to match the camera
    camera_link = traitlets.dlink((camera, 'value'), (image, 'value'), transform=bgr8_to_jpeg)
    display(image)

    try:
        os.makedirs(dir)
    except FileExistsError:
        print('Directory not created because it already exists')

    while True:
        time.sleep(sleep_time)  # currently only captures images every [sleep_time] seconds
        save_image(dir, image)

# ^ convert image to grayscale
#
#
#
#

def save_image(directory, image):
    image_path = os.path.join(directory, file_name)
    with open(image_path, 'wb') as f:
        f.write(image.value)



