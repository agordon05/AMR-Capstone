import time
import numpy
import coordinates
from Robot import robot_movement

__destination = {
    'x': 0,
    'y': 0,
}
# _source = {
#     'x': 0,
#     'y': 0,
# }
__signal = None  # Allows outside component to control the movement

__position_percentage_error = 0.05  # percentage error allowed for how close robot can be to destination or source to not
# move
# how far away robot can be from destination -- A value of 0.05 means the robot has to be within 0.05 "meters" assuming
# that a distance of 1 is 1 "meter"

__rotation_percentage_error = 0.05  # percentage error allowed for how close the robot direction towards it's destination
# can be
# 0.05 corresponds to an accuracy of give or take 5 degrees.  if the degree needed is 100, rotation can be between 95
# and 105
__movement_change_time_delay = 0.3  # delay is in seconds


def set_destination(dest: dict):
    global __destination
    __destination['x'] = dest['x']
    __destination['y'] = dest['y']


def get_destination():
    global __destination
    destination = {
        'x': __destination['x'],
        'y': __destination['y']
    }
    return destination

# def set_source(source: dict):
#     global _source
#     _source = source


def set_signal(signal):
    global __signal
    __signal = signal


# def get_signal():
#     global __signal
#     return __signal
# same method below


def _set_position_error(num):
    global __position_percentage_error
    __position_percentage_error = num


def _set_rotation_error(num):
    global __rotation_percentage_error
    __rotation_percentage_error = num


def move():
    global __signal

    # another component is telling the robot where to go
    control = get_signal()

    # if at destination, do nothing
    if control is None:
        if at_destination() is True:
            control = "stop"

    if control is None:
        # calculate rotation needed
        angle_needed = get_rotation_needed()
        # if direction is not close, rotate
        if is_rotation_there(coordinates.get_rotation(), angle_needed) is False:
            # figure out how whether to rotate left or right
            if is_rotate_left(coordinates.get_rotation(), angle_needed) is True:
                control = "rotating left"
            else:
                control = "rotating right"

    if control is None:
        control = "forward"

    # change movement
    if is_move_change(control) is True:
        move_change(control)


def get_signal():
    global __signal
    # another component is telling the robot where to go
    if __signal is not None:
        if __signal == "forward" or __signal == "backward" or __signal == "rotating left" or __signal == "rotating right" or __signal == "stop":
            return __signal
        else:
            __signal = None

    return None


# finds out if robot is at or close enough to destination
def at_destination() -> bool:
    global __destination, __position_percentage_error
    dest_x = __destination['x']
    dest_y = __destination['y']
    x_pos = coordinates.get_x_pos()
    y_pos = coordinates.get_y_pos()
    per_error = __position_percentage_error

    # pos_x_diff = numpy.absolute(x_pos - dest_x)  # distance from destination on x axis
    # pos_y_diff = numpy.absolute(y_pos - dest_y)  # distance from destination on y axis

    diff = numpy.sqrt(numpy.square(x_pos - dest_x) + numpy.square(y_pos - dest_y))  # sqrt((x1 - x2)^2 + (y1 - y2)^2)

    if diff > per_error:  # is the difference is greater than percent error
        return False

    return True


# is rotation given close enough to the rotation needed
def is_rotation_there(angle: float, angle_needed: float) -> bool:
    global __rotation_percentage_error
    angle_closeness = numpy.absolute(angle - angle_needed)
    if angle_closeness <= __rotation_percentage_error:
        return True
    return False


# returns the rotation needed in degrees
def get_rotation_needed() -> float:
    global __destination
    x_pos = coordinates.get_x_pos()  # current x position
    y_pos = coordinates.get_y_pos()  # current y position

    # NOT NEEDED -- there is a check method, at_destination that checks this beforehand
    # if x_pos == _destination['x'] and y_pos == _destination['y']:
    #     return None

    if x_pos == __destination['x']:
        if y_pos < __destination['y']:
            angle_needed = 90
        else:
            angle_needed = 270

    elif y_pos == __destination['y']:
        if x_pos > __destination['x']:
            angle_needed = 180
        else:
            angle_needed = 0

    else:
        slope = (y_pos - __destination['y']) / (x_pos - __destination['x'])  # finds slope
        # print(f'slope: {slope}')
        angle_needed = numpy.arctan(slope)  # converts slope to angle
        angle_needed = numpy.rad2deg(angle_needed)  # converts radians to degrees

        # if slope > 0:
        # arctan only operates from 90 to -90, missing 2nd and 3rd quadrant of the circle i.e. 90 to 270 degrees
        if __destination['x'] < x_pos:  # finds if destination is in 2nd or 3rd quadrant of a circle
            angle_needed += 180  # adds 180 to angle if it is
        #     else:
        #         pass
        # else:
        #     if _destination['x'] < x_pos:
        #         angle_needed += 180
        #     else:
        #         pass
        #     pass

        #ensures angle is within 0 and 360
        while angle_needed < 0:
            angle_needed += 360
        while angle_needed >= 360:
            angle_needed -= 360

        # print(angle_needed)

    return angle_needed


# if robot needs to move left or right
def is_rotate_left(angle: float, angle_needed: float) -> bool:

    left_angles = angle_needed - angle  # gets the difference between the two angles

    while left_angles < -180:
        left_angles += 360
    while left_angles > 180:
        left_angles -= 360

    if left_angles >= 0:  # rotating left is better/shorter
        return True
    if left_angles < 0:  # rotating right is better/shorter
        return False


def is_move_change(control: str) -> bool:

    # NOT NEEDED -- control will always be a string
    if control is None:
        return True
    flags = robot_movement.get_direction_flags()
    if control == "rotating left":
        if flags['rotating left'] is False:  # if robot is not already rotating left, there is a move change
            return True
    elif control == "rotating right":
        if flags['rotating right'] is False:  # if robot is not already rotating right, there is a move change
            return True
    elif control == "forward":
        if flags['forward'] is False:  # if robot is not already moving forward, there is a move change
            return True
    elif control == "backward":
        if flags['backward'] is False:  # if robot is not already moving backward, there is a move change
            return True
    elif control == "stop":
        for key in flags.keys():
            if flags[key] is True:
                return True
    return False


def move_change(control: str):
    global __movement_change_time_delay
    if control != "stop" and control != "forward" and control != "backward" and control != "rotating left" and control != "rotating right":
        return

    coordinates.update()
    flags = robot_movement.get_direction_flags()
    for key in flags.keys():
        if flags[key] is True:
            robot_movement.stop()
            time.sleep(__movement_change_time_delay)
    # if robot_movement.direction_flags['forward'] is True or robot_movement.direction_flags['backward'] is True or
    # robot_movement.direction_flags['rotating left'] is True or robot_movement.direction_flags['rotating right'] is
    # True:
    #     robot_movement.stop()
    #     delay(movement_change_time_delay)
    if control == "stop":
        return
    if control == "rotating left":
        robot_movement.rotate_left()
    elif control == "rotating right":
        robot_movement.rotate_right()
    elif control == "forward":
        robot_movement.forward()
    elif control == "backward":
        robot_movement.backward()
