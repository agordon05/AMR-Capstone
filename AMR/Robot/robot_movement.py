from jetbot import Robot
import robot_startup

# global direction variables
__moving_forward = False
__moving_backward = False
__rotating_left = False
__rotating_right = False

# robot speed
__movement_speed = 0.1
__rotation_speed = 0.01

# a dictionary to map directions to boolean flags
__direction_flags = {
    "forward": __moving_forward,
    "backward": __moving_backward,
    "rotating left": __rotating_left,
    "rotating right": __rotating_right
}


def get_direction_flags():
    global __direction_flags
    flags = {
        "forward": __direction_flags['forward'],
        "backward": __direction_flags['backward'],
        "rotating left": __direction_flags['rotating left'],
        "rotating right": __direction_flags['rotating right']
    }
    return flags


# Change the global direction variables based on the provided direction string
def _change_direction(direction: str):
    global __direction_flags
    # Reset all direction flags to False
    for flag in __direction_flags:
        __direction_flags[flag] = False

    # for key_value in direction_flags:
    #     print(key_value)
    #     print(direction_flags[key_value])
    #
    # print()
    if direction == "stop":
        # print("direction is stop")
        # print(direction_flags['forward'])
        # print(direction_flags['backward'])
        # print(direction_flags['rotating left'])
        # print(direction_flags['rotating right'])
        return

    # Set the corresponding direction flag to True
    if direction in __direction_flags:
        __direction_flags[direction] = True


# Define functions for each direction
def forward():
    global __movement_speed
    _change_direction("forward")
    robot_startup.robot.forward(__movement_speed)


def backward():
    global __movement_speed
    _change_direction("backward")
    robot_startup.robot.backward(__movement_speed)


def rotate_left():
    global __rotation_speed
    _change_direction("rotating left")
    robot_startup.robot.left(__rotation_speed)


def rotate_right():
    global __rotation_speed
    _change_direction("rotating right")
    robot_startup.robot.right(__rotation_speed)


def stop():
    _change_direction("stop")
    robot_startup.robot.stop()


