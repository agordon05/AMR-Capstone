import numpy
from datetime import datetime
from Robot_command import robot_movement

__x_pos: float = 0
__y_pos: float = 0
__direction_in_degrees = 0  # direction is in degrees for easy understanding
__movement_scale = 0.24  # scale of movement assuming constant speed
__rotation_scale = 0.12  # scale of rotation assuming constant speed
__wheel_bias = 0.00001  # when moving straight, how far is the robot drifting, positive number means robot is drifting to the right, negaative to the left
# when starting up, time of last update will be start time of program in milliseconds
__time_of_last_update_ms = 0  # is in milliseconds for precision
__time_converter_ms_s = 1 / 1000  # to be multiplied to time to convert milliseconds to seconds


def get_x_pos():
    global __x_pos
    return __x_pos


def _set_x_pos(x):
    global __x_pos
    __x_pos = x


def get_y_pos():
    global __y_pos
    return __y_pos


def _set_y_pos(y):
    global __y_pos
    __y_pos = y


def get_rotation():
    global __direction_in_degrees
    return __direction_in_degrees


def set_rotation(rotation):
    global  __direction_in_degrees
    __direction_in_degrees = rotation


def _set_time_of_last_update(time):
    global __time_of_last_update_ms
    __time_of_last_update_ms = time


# time needed to see how much to update coordinates by
def update():
    global __x_pos, __y_pos, __direction_in_degrees
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
    print(f'x pos: {__x_pos} -- y pos: {__y_pos} -- degrees: {__direction_in_degrees}')

def __wheel_bias_update(time: float):
    global __direction_in_degrees, __wheel_bias
    
    __direction_in_degrees -= time * __wheel_bias




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
    global __x_pos, __y_pos, __direction_in_degrees, __movement_scale, __time_converter_ms_s

    time *= __time_converter_ms_s  # converts millisecond to second

    angle_rotation = numpy.deg2rad(__direction_in_degrees)  # rotation angle has to be in radians
    # x_result = movement_scale * numpy.cos(angle_rotation) * time
    # y_result = movement_scale * numpy.sin(angle_rotation) * time

    # print()
    # print(f'movement_scale: {movement_scale} time: {time}')
    # print(f'sin(rotation): {numpy.sin(angle_rotation)}')
    # print(f'cos(rotation): {numpy.cos(angle_rotation)}')
    #
    # print(f'x position: {x_pos}')
    # print(f'y position: {y_pos}')
    #
    # print(f'x move by: {x_result}')
    # print(f'y move by: {y_result}')

    __x_pos += __movement_scale * numpy.cos(angle_rotation) * time  # moving x coordinate according to
    # angle, scale and time
    __y_pos += __movement_scale * numpy.sin(angle_rotation) * time  # moving y coordinate according to

    # print(f'x position: {x_pos}')
    # print(f'y position: {y_pos}')

    __x_pos = numpy.round(__x_pos, 5)
    __y_pos = numpy.round(__y_pos, 5)

    # print(f'x position after rounding: {x_pos}')
    # print(f'y position after rounding: {y_pos}')


def move_backward(time):
    global __x_pos, __y_pos, __direction_in_degrees, __movement_scale, __time_converter_ms_s

    time *= __time_converter_ms_s  # converts millisecond to second
    angle_rotation = numpy.deg2rad(__direction_in_degrees)  # rotation angle has to be in radians

    __x_pos -= __movement_scale * numpy.cos(angle_rotation) * time  # moving x coordinate according to
    # angle, scale and time
    __y_pos -= __movement_scale * numpy.sin(angle_rotation) * time  # moving y coordinate according to

    __x_pos = numpy.round(__x_pos, 5)
    __y_pos = numpy.round(__y_pos, 5)


def rotate_left(time):
    global __direction_in_degrees, __rotation_scale, __time_converter_ms_s
    time *= __time_converter_ms_s
    # rotating counter clockwise
    # print(f'rotation -- {rotation_scale * time * 360}')
    __direction_in_degrees += __rotation_scale * time * 360
    __direction_in_degrees %= 360
    __direction_in_degrees = numpy.round(__direction_in_degrees, 5)


def rotate_right(time):
    global __direction_in_degrees, __rotation_scale, __time_converter_ms_s
    time *= __time_converter_ms_s

    # rotating clockwise
    __direction_in_degrees -= __rotation_scale * time * 360
    if __direction_in_degrees < 0:
        __direction_in_degrees += 360

