import threading

from jetbot import Robot

import Movement.movement

# robot object
robot = Robot()

# move thread
my_thread = threading.Thread(target=Movement.movement.move())


def run():

    # Start the thread
    my_thread.start()

