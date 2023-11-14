import time
import numpy
from Movement import coordinates
from Robot_command import robot_movement
from Model import robot as bot


__position_percentage_error = 0.1  # percentage error allowed for how close robot can be to destination or source to not
# move
# how far away robot can be from destination -- A value of 0.05 means the robot has to be within 0.05 "meters" assuming
# that a distance of 1 is 1 "meter"

__rotation_percentage_error = 10  # percentage error allowed for how close the robot direction towards it's destination
# can be
# 0.05 corresponds to an accuracy of give or take 5 degrees.  if the degree needed is 100, rotation can be between 95
# and 105
__movement_change_time_delay = 0.3  # delay is in seconds


def _set_position_error(num):
    global __position_percentage_error
    __position_percentage_error = num


def _set_rotation_error(num):
    global __rotation_percentage_error
    __rotation_percentage_error = num


def move():
    # global __signal

    # another component is telling the robot where to go
    # print("getting signal")
    control = get_signal()

    # if at destination, do nothing
    if control is None:
        # print("is at destination")
        if at_destination() is True:
            control = "stop"
            # print("control is stop")

    if control is None:
        # print("where to turn?")
        # calculate rotation needed
        angle_needed = get_rotation_needed()
        # if direction is not close, rotate
        if is_rotation_there(bot.get_rotation(), angle_needed) is False:
            # figure out how whether to rotate left or right
            if is_rotate_left(bot.get_rotation(), angle_needed) is True:
                control = "rotating left"
                # print("rotating left")
            else:
                control = "rotating right"
                # print("rotating right")

    if control is None:
        control = "forward"
        # print("moving forward")

    # update coordinates
    coordinates.update()

    # change movement
    if is_move_change(control) is True:
        # print("changing movement")
        move_change(control)
    else:
        # print("movement did not change")


def get_signal():

    signal = bot.get_user_command()

    # user is telling the robot where to go
    if signal is not None:
        if signal == "forward" or signal == "backward" or signal == "rotating left" or signal == "rotating right" or signal == "stop":
            return signal
        else:
            bot.set_user_command("")

    signal = bot.get_robot_command()

    # another robot component is telling the robot where to go
    if signal is not None:
        if signal == "forward" or signal == "backward" or signal == "rotating left" or signal == "rotating right" or signal == "stop":
            return signal
        else:
            bot.set_robot_command("")

    return None


# finds out if robot is at or close enough to destination
def at_destination() -> bool:
    global __position_percentage_error

    dest_x: float = bot.get_x_destination()
    dest_y: float = bot.get_y_destination()
    x_pos: float = bot.get_x_pos()
    y_pos: float = bot.get_y_pos()
    per_error = __position_percentage_error

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

    x_pos: float = bot.get_x_pos()  # current x position
    y_pos: float = bot.get_y_pos()  # current y position
    x_destination: float = bot.get_x_destination()
    y_destination: float = bot.get_y_destination()

    if x_pos == x_destination:
        if y_pos < y_destination:
            angle_needed = 90
        else:
            angle_needed = 270

    elif y_pos == y_destination:
        if x_pos > x_destination:
            angle_needed = 180
        else:
            angle_needed = 0

    else:
        slope = (y_pos - y_destination) / (x_pos - x_destination)  # finds slope

        angle_needed = numpy.arctan(slope)  # converts slope to angle
        angle_needed = numpy.rad2deg(angle_needed)  # converts radians to degrees

        # arctan only operates from 90 to -90, missing 2nd and 3rd quadrant of the circle i.e. 90 to 270 degrees
        if x_destination < x_pos:  # finds if destination is in 2nd or 3rd quadrant of a circle
            angle_needed += 180  # adds 180 to angle if it is

        # ensures angle is within 0 and 360
        while angle_needed < 0:
            angle_needed += 360
        while angle_needed >= 360:
            angle_needed -= 360

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


def run():
    while True:
        move()
