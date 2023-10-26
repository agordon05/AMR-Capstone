import numpy
from datetime import datetime
from Robot_command import robot_movement
from Model import robot as bot

# __x_pos: float = 0
# __y_pos: float = 0
# __direction_in_degrees = 0  # direction is in degrees for easy understanding

__movement_scale = 0.24  # scale of movement assuming constant speed
__rotation_scale = 0.12  # scale of rotation assuming constant speed
__wheel_bias = 0.00001  # when moving straight, how far is the robot drifting, positive number means robot is drifting to the right, negaative to the left
# when starting up, time of last update will be start time of program in milliseconds
__time_of_last_update_ms = 0  # is in milliseconds for precision
__time_converter_ms_s = 1 / 1000  # to be multiplied to time to convert milliseconds to seconds


# def get_x_pos():
#     global __x_pos
#     return __x_pos
#
#
# def _set_x_pos(x):
#     global __x_pos
#     __x_pos = x
#
#
# def get_y_pos():
#     global __y_pos
#     return __y_pos
#
#
# def _set_y_pos(y):
#     global __y_pos
#     __y_pos = y


# def get_rotation():
#     global __direction_in_degrees
#     return __direction_in_degrees


# def set_rotation(rotation):
#     global  __direction_in_degrees
#     __direction_in_degrees = rotation


def _set_time_of_last_update(time):
    global __time_of_last_update_ms
    __time_of_last_update_ms = time


# time needed to see how much to update coordinates by
def update():

    # calculates time since last update method called
    time = time_since_lest_update()
    flags = robot_movement.get_direction_flags()
    if flags['forward'] is True:
        move_forward(time)
        __wheel_bias_update(time)  

    elif flags['backward'] is True:
        move_backward(time)

    elif flags['rotating left'] is True:
        rotate_left(time)

    elif flags['rotating right'] is True:
        rotate_right(time)
    print(f'x pos: {bot.get_x_pos()} -- y pos: {bot.get_y_pos()} -- degrees: {bot.get_rotation()}')


def __wheel_bias_update(time: float):
    global __wheel_bias
    direction_in_degrees: float = bot.get_rotation()
    direction_in_degrees -= time * __wheel_bias
    bot.set_rotation(direction_in_degrees)


# calculated in ms for more precision
def time_since_lest_update():
    global __time_of_last_update_ms

    # calculating current time
    date = datetime.utcnow() - datetime(1970, 1, 1)
    date_in_seconds = date.total_seconds()
    current_time_ms = int(date_in_seconds * 1000)

    # if first time or instant update, only update time_of_last_update_ms
    if __time_of_last_update_ms == 0:
        __time_of_last_update_ms = current_time_ms
        return 0

    # calculate time since last update
    time = current_time_ms - __time_of_last_update_ms

    # update time of last update
    __time_of_last_update_ms = current_time_ms

    return time


def move_forward(time):
    global __movement_scale, __time_converter_ms_s

    time *= __time_converter_ms_s  # converts millisecond to second

    angle_rotation = numpy.deg2rad(bot.get_rotation)  # rotation angle has to be in radians

    # gets the coordinates of the robot
    x_pos: float = bot.get_x_pos()
    y_pos: float = bot.get_y_pos()

    x_pos += __movement_scale * numpy.cos(angle_rotation) * time  # moving x coordinate according to
    # angle, scale and time
    y_pos += __movement_scale * numpy.sin(angle_rotation) * time  # moving y coordinate according to

    x_pos = float(numpy.round(x_pos, 5))
    y_pos = float(numpy.round(y_pos, 5))

    # sets the coordinates of the robots
    bot.set_x_pos(x_pos)
    bot.set_y_pos(y_pos)


def move_backward(time):
    global __movement_scale, __time_converter_ms_s

    time *= __time_converter_ms_s  # converts millisecond to second
    angle_rotation = numpy.deg2rad(bot.get_rotation)  # rotation angle has to be in radians

    # gets the coordinates of the robot
    x_pos: float = bot.get_x_pos()
    y_pos: float = bot.get_y_pos()

    x_pos -= __movement_scale * numpy.cos(angle_rotation) * time  # moving x coordinate according to
    # angle, scale and time
    y_pos -= __movement_scale * numpy.sin(angle_rotation) * time  # moving y coordinate according to

    x_pos = float(numpy.round(x_pos, 5))
    y_pos = float(numpy.round(y_pos, 5))

    # sets the coordinates of the robots
    bot.set_x_pos(x_pos)
    bot.set_y_pos(y_pos)


def rotate_left(time):
    global __rotation_scale, __time_converter_ms_s
    time *= __time_converter_ms_s
    # rotating counter clockwise

    # getting rotation of robot
    direction_in_degrees: float = bot.get_rotation()

    direction_in_degrees += __rotation_scale * time * 360
    direction_in_degrees %= 360
    direction_in_degrees = float(numpy.round(direction_in_degrees, 5))

    # setting the rotation of the robot
    bot.set_rotation(direction_in_degrees)


def rotate_right(time):
    global __rotation_scale, __time_converter_ms_s

    time *= __time_converter_ms_s

    # getting rotation of robot
    direction_in_degrees = bot.get_rotation()

    # rotating clockwise
    direction_in_degrees -= __rotation_scale * time * 360
    if direction_in_degrees < 0:
        direction_in_degrees += 360

    # setting the rotation of the robot
    bot.set_rotation(direction_in_degrees)
