import os
import sys
# import sensor

# import image #used in [https://www.youtube.com/watch?v=PffDblwNshM], may be needed
import cv2
import time
import math
# import pylibdmtx #import error

directory = '~/jetbot'
directory = os.path.expanduser(directory)
sys.path.append(directory)
import traitlets
import ipywidgets.widgets as widgets
from IPython.display import display
from jetbot import Camera, bgr8_to_jpeg
from Model import robot as bot

# dir = 'dataset/imageFeed'
# file_name = 'image.jpg'
sleep_time = 2
__image = None

def get_image():
    return __image

#detector = cv2.QRCodeDetector

# converts image to byte[] and sends it to the robot object
def send_to_robot():
    if __image:
        image_value = __image.value
        image_byte_array = list(image_value)
        bot.set_image(image_byte_array)

# should only display a live image feed
def run():
    global __image
    camera = Camera.instance(width=224, height=224)
    __image = widgets.Image(format='jpeg', width=224,
                          height=224)  # this width and height doesn't necessarily have to match the camera
    camera_link = traitlets.dlink((camera, 'value'), (__image, 'value'), transform=bgr8_to_jpeg)
    display(image)

    # try:
    #     os.makedirs(dir)
    # except FileExistsError:
    #     print('Directory not created because it already exists')

    while True:
        time.sleep(sleep_time)  # currently only captures images every [sleep_time] seconds
        # save_image(dir, image)
        send_to_robot()


# def save_image(directory, image):
#     image_path = os.path.join(directory, file_name)
#     with open(image_path, 'wb') as f:
#         f.write(image.value)




