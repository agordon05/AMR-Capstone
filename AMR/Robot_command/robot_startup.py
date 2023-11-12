import os
import sys
import threading
import time
directory = '~/jetbot'
directory = os.path.expanduser(directory)
sys.path.append(directory)

from jetbot import robot
from Movement import movement

# robot object
robot = robot.Robot()

# move thread
movement_thread = threading.Thread(target=movement.run)


def run():
    for path in sys.path:
        print(path)
        if path == '~/jetbot':
            path = os.path.expanduser('~/jetbot')
            direct = os.listdir(path)
            for item in direct:
                print(item)
    time.sleep(30)
    # Start the thread
    movement_thread.start()

