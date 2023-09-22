import time
import numpy
import coordinates
import robot_movement

_destination = {
    'x': 0,
    'y': 0,
}
_source = {
    'x': 0,
    'y': 0,
}
signal = None  # Allows outside component to control the movement

position_percentage_error = 0.05  # percentage error allowed for how close robot can be to destination or source to not
# move
# how far away robot can be from destination -- A value of 0.05 means the robot has to be within 0.05 "meters" assuming
# that a distance of 1 is 1 "meter"

rotation_percentage_error = 0.05  # percentage error allowed for how close the robot direction towards it's destination
# can be
# 0.05 corresponds to an accuracy of give or take 5 degrees.  if the degree needed is 100, rotation can be between 95
# and 105
movement_change_time_delay = 0.3  # delay is in seconds


def set_destination(dest: dict):
    global _destination
    _destination = dest
    pass


def set_source(source: dict):
    global _source
    _source = source


def move():
    global signal

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
        if is_rotation_there(coordinates.direction_in_degrees, angle_needed) is False:
            # figure out how whether to rotate left or right
            if is_rotate_left(coordinates.direction_in_degrees, angle_needed) is True:
                control = "rotating left"
            else:
                control = "rotating right"

    if control is None:
        control = "forward"

    # change movement
    if is_move_change(control) is True:
        move_change(control)


def get_signal() -> str:
    global signal
    # another component is telling the robot where to go
    if signal is not None:
        if signal == "forward" or signal == "backward" or signal == "rotating left" or signal == "rotating right" or signal == "stop":
            return signal
        else:
            signal = None

    return None


# finds out if robot is at or close enough to destination
def at_destination() -> bool:

    dest_x = _destination['x']
    dest_y = _destination['y']
    x_pos = coordinates.x_pos
    y_pos = coordinates.y_pos
    per_error = position_percentage_error

    # pos_x_diff = numpy.absolute(x_pos - dest_x)  # distance from destination on x axis
    # pos_y_diff = numpy.absolute(y_pos - dest_y)  # distance from destination on y axis

    diff = numpy.sqrt(numpy.square(x_pos - dest_x) + numpy.square(y_pos - dest_y))  # sqrt((x1 - x2)^2 + (y1 - y2)^2)

    if diff > per_error:  # is the difference is greater than percent error
        return False

    return True


# is rotation given close enough to the rotation needed
def is_rotation_there(angle: float, angle_needed: float) -> bool:

    angle_closeness = numpy.absolute(angle - angle_needed)
    if angle_closeness <= rotation_percentage_error:
        return True
    return False


# returns the rotation needed in degrees
def get_rotation_needed() -> float:

    x_pos = coordinates.x_pos  # current x position
    y_pos = coordinates.y_pos  # current y position

    # NOT NEEDED -- there is a check method, at_destination that checks this beforehand
    # if x_pos == _destination['x'] and y_pos == _destination['y']:
    #     return None

    if x_pos == _destination['x']:
        if y_pos < _destination['y']:
            angle_needed = 90
        else:
            angle_needed = 270

    elif y_pos == _destination['y']:
        if x_pos > _destination['x']:
            angle_needed = 180
        else:
            angle_needed = 0

    else:
        slope = (y_pos - _destination['y']) / (x_pos - _destination['x'])  # finds slope
        # print(f'slope: {slope}')
        angle_needed = numpy.arctan(slope)  # converts slope to angle
        angle_needed = numpy.rad2deg(angle_needed)  # converts radians to degrees

        # if slope > 0:
        # arctan only operates from 90 to -90, missing 2nd and 3rd quadrant of the circle i.e. 90 to 270 degrees
        if _destination['x'] < x_pos:  # finds if destination is in 2nd or 3rd quadrant of a circle
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

    if control == "rotating left":
        if robot_movement.direction_flags['rotating left'] is False:  # if robot is not already rotating left, there is a move change
            return True
    elif control == "rotating right":
        if robot_movement.direction_flags['rotating right'] is False:  # if robot is not already rotating right, there is a move change
            return True
    elif control == "forward":
        if robot_movement.direction_flags['forward'] is False:  # if robot is not already moving forward, there is a move change
            return True
    elif control == "backward":
        if robot_movement.direction_flags['backward'] is False:  # if robot is not already moving backward, there is a move change
            return True
    elif control == "stop":
        for key in robot_movement.direction_flags.keys():
            if robot_movement.direction_flags[key] is True:
                return True
    return False


def move_change(control: str):

    if control != "stop" and control != "forward" and control != "backward" and control != "rotating left" and control != "rotating right":
        return

    coordinates.update()
    for key in robot_movement.direction_flags.keys():
        if robot_movement.direction_flags[key] is True:
            robot_movement.stop()
            time.sleep(movement_change_time_delay)
    # if robot_movement.direction_flags['forward'] is True or robot_movement.direction_flags['backward'] is True or robot_movement.direction_flags['rotating left'] is True or robot_movement.direction_flags['rotating right'] is True:
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
