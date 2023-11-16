import os
import sys
import time
from Robot_command import robot_startup
directory = robot_startup.directory
sys.path.append(directory)
from jetbot import robot
from Movement import coordinates
from Model import robot as bot


# robot speed
__movement_speed = 0.25
__rotation_speed = 0.22

__left_rotation_sleep_time = 0.62
__right_rotation_sleep_time = 0.55
__movement_sleep_time = 2

# a dictionary to map directions to boolean flags
__direction_flags = {
    "forward": False,
    "backward": False,
    "rotating left": False,
    "rotating right": False
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

    if direction == "stop":
        return

    # Set the corresponding direction flag to True
    if direction in __direction_flags:
        __direction_flags[direction] = True


# Define functions for each direction
def forward():
    global __movement_speed, __movement_sleep_time, __rotation_speed
    _change_direction("forward")
    robot_startup.robot.forward(__movement_speed)
    time.sleep(__movement_sleep_time)
    
    stop()
    
    direction = bot.get_direction()
    x_pos = bot.get_x_pos()
    y_pos = bot.get_y_pos()
    
    if direction is 'Up':
        y_pos += 1
    if direction is 'Down':
        y_pos -= 1
    if direction is 'Left':
        x_pos -= 1
    if direction is 'Right':
        x_pos += 1
    
    bot.set_x_pos(x_pos)
    bot.set_y_pos(y_pos)
   
    print(f'x pos: {bot.get_x_pos()} -- y pos: {bot.get_y_pos()} -- degrees: {bot.get_rotation()}')
    print("Direction: " + bot.get_direction())
    


def backward():
    global __movement_speed, __movement_sleep_time
    _change_direction("backward")
    robot_startup.robot.backward(__movement_speed)
    time.sleep(__movement_sleep_time)
    stop()


def rotate_left():
    global __rotation_speed, __left_rotation_sleep_time
    # coordinates.update()
    _change_direction("rotating left")
    robot_startup.robot.left(__rotation_speed)
    time.sleep(__left_rotation_sleep_time)
    # coordinates.update()
    stop()
    bot.turn_left()
    rotation = (bot.get_rotation() + 90) % 360
    bot.set_rotation(rotation)
    print(f'x pos: {bot.get_x_pos()} -- y pos: {bot.get_y_pos()} -- degrees: {bot.get_rotation()}')
    print("Direction: " + bot.get_direction())


def rotate_right():
    global __rotation_speed, __right_rotation_sleep_time
    _change_direction("rotating right")
    robot_startup.robot.right(__rotation_speed)
    time.sleep(__right_rotation_sleep_time)
    # coordinates.update()
    stop()
    bot.turn_right()
    rotation = bot.get_rotation() - 90
    if rotation < 0:
        rotation += 360
    bot.set_rotation(rotation)
    print(f'x pos: {bot.get_x_pos()} -- y pos: {bot.get_y_pos()} -- degrees: {bot.get_rotation()}')
    print("Direction: " + bot.get_direction())
    

def stop():
    robot_startup.robot.stop()
    _change_direction("stop")  

    
# --- FOR FUTURE IMPLEMENTATION ---
def control_start():
    _change_direction("stop")
    coordinates.update()
    
def control_forward():
    global __movement_speed 
    coordinates.update()
    robot_startup.robot.forward(__movement_speed)
    _change_direction("forward")

    
def control_backward():
    global __movement_speed 
    coordinates.update()
    robot_startup.robot.backward(__movement_speed)
        _change_direction("backward")

    
def control_left():
    global __rotation_speed 
    coordinates.update()
    robot_startup.robot.left(__rotation_speed)
        _change_direction("rotating left")

    
def control_right():
    global __rotation_speed 
    coordinates.update()
    robot_startup.robot.right(__rotation_speed)
        _change_direction("rotating right")

    
def control_stop():
    coordinates.update()
    robot_startup.robot.stop()
    _change_direction("stop")








