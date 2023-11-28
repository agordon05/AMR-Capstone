import os
import sys
import threading
import time
directory = '~/jetbot'
directory = os.path.expanduser(directory)
sys.path.append(directory)

from jetbot import robot
from Movement import movement
from Robot_command import robot_camera_vision
from Api import RobotClient

# robot object
robot = robot.Robot()

# move thread
movement_thread = threading.Thread(target=movement.run)
camera_thread = threading.Thread(target=robot_camera_vision.run)
api_thread = threading.Thread(target=RobotClient.run)


def run():
    time.sleep(5)
    # Start the thread
    api_thread.start()
    movement_thread.start()
    camera_thread.start()

