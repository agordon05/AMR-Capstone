import numpy
from datetime import datetime
import robot_movement


x_pos: float = 0
y_pos: float = 0
direction_in_degrees = 90  # direction is in degrees for easy understanding
movement_scale = 1  # scale of movement assuming constant speed
rotation_scale = 1  # scale of rotation assuming constant speed

# when starting up, time of last update will be start time of program in milliseconds
time_of_last_update_ms = 0  # is in milliseconds for precision
time_converter_ms_s = 1 / 1000  # to be multiplied to time to convert milliseconds to seconds


# time needed to see how much to update coordinates by
def update():

    # calculates time since last update method called
    time = time_since_lest_update()

    if robot_movement.direction_flags['forward'] is True:
        move_forward(time)

    elif robot_movement.direction_flags['backward'] is True:
        move_backward(time)

    elif robot_movement.direction_flags['rotating left'] is True:
        rotate_left(time)

    elif robot_movement.direction_flags['rotating right'] is True:
        rotate_right(time)


# calculated in ms for more precision
def time_since_lest_update():
    global time_of_last_update_ms

    # calculating current time
    date = datetime.utcnow() - datetime(1970, 1, 1)
    date_in_seconds = date.total_seconds()
    current_time_ms = int(date_in_seconds * 1000)

    # if first time or instant update, only update time_of_last_update_ms
    if time_of_last_update_ms == 0:
        time_of_last_update_ms = current_time_ms
        return 0

    # calculate time since last update
    time = current_time_ms - time_of_last_update_ms

    # update time of last update
    time_of_last_update_ms = current_time_ms

    return time


def move_forward(time):
    global x_pos, y_pos, direction_in_degrees, movement_scale, time_converter_ms_s

    time *= time_converter_ms_s # converts millisecond to second

    angle_rotation = numpy.deg2rad(direction_in_degrees)  # rotation angle has to be in radians
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

    x_pos += movement_scale * numpy.cos(angle_rotation) * time  # moving x coordinate according to
    # angle, scale and time
    y_pos += movement_scale * numpy.sin(angle_rotation) * time  # moving y coordinate according to

    # print(f'x position: {x_pos}')
    # print(f'y position: {y_pos}')

    x_pos = numpy.round(x_pos, 5)
    y_pos = numpy.round(y_pos, 5)

    # print(f'x position after rounding: {x_pos}')
    # print(f'y position after rounding: {y_pos}')


def move_backward(time):
    global x_pos, y_pos, direction_in_degrees, movement_scale, time_converter_ms_s

    time *= time_converter_ms_s  # converts millisecond to second
    angle_rotation = numpy.deg2rad(direction_in_degrees)  # rotation angle has to be in radians

    x_pos -= movement_scale * numpy.cos(angle_rotation) * time  # moving x coordinate according to
    # angle, scale and time
    y_pos -= movement_scale * numpy.sin(angle_rotation) * time  # moving y coordinate according to

    x_pos = numpy.round(x_pos, 5)
    y_pos = numpy.round(y_pos, 5)


def rotate_left(time):
    global direction_in_degrees, rotation_scale, time_converter_ms_s
    time *= time_converter_ms_s
    # rotating counter clockwise
    # print(f'rotation -- {rotation_scale * time * 360}')
    direction_in_degrees += rotation_scale * time * 360
    direction_in_degrees %= 360
    direction_in_degrees = numpy.round(direction_in_degrees, 5)


def rotate_right(time):
    global direction_in_degrees, rotation_scale, time_converter_ms_s
    time *= time_converter_ms_s

    # rotating clockwise
    direction_in_degrees -= rotation_scale * time * 360
    if direction_in_degrees < 0:
        direction_in_degrees += 360

