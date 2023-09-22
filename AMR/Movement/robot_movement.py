

# global direction variables
_moving_forward = False
_moving_backward = False
_rotating_left = False
_rotating_right = False

# a dictionary to map directions to boolean flags
direction_flags = {
    "forward": _moving_forward,
    "backward": _moving_backward,
    "rotating left": _rotating_left,
    "rotating right": _rotating_right
}


# Change the global direction variables based on the provided direction string
def _change_direction(direction: str):
    # Reset all direction flags to False
    for flag in direction_flags:
        direction_flags[flag] = False

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
    if direction in direction_flags:
        direction_flags[direction] = True


# Define functions for each direction
def forward():
    _change_direction("forward")


def backward():
    _change_direction("backward")


def rotate_left():
    _change_direction("rotating left")


def rotate_right():
    _change_direction("rotating right")


def stop():
    _change_direction("stop")

