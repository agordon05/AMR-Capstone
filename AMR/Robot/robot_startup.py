import threading

# from jetbot import Robot

import Movement.movement

# robot object
# robot = Robot()

# move thread
movement_thread = threading.Thread(target=Movement.movement.run())


def run():

    # Start the thread
    movement_thread.start()

