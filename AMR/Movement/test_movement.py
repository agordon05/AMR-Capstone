import unittest
import os
import sys

# Add the parent directory (AMR) to the Python path -- ChatGPT -- used for "python Movement/test_movement.py >
# movement-test.log" in the terminal, for some reason it wasn't using AMR as base directory
amr_directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(amr_directory)
import movement
import coordinates
from Robot_command import robot_movement
from Model import robot as bot

# --- NOTE ---
# comment out import jetbot in robot_movement.py
# comment out portions of the methods in robot_movement.py -- marked with "--- NOTE ---"
# some will have "# --- END OF COMMENTING OUT ---" after a few lines of code to signify multiple lines to be commented out


class Test_Movement(unittest.TestCase):

    # def test_signal(self):
    #     # movement.signal = 'forward'
    #     robot.set_signal('forward')
    #     self.assertEqual(movement.get_signal(), "forward")
    #
    #     movement.set_user_signal('backward')
    #     # movement.signal = 'backward'
    #     self.assertEqual(movement.get_signal(), "backward")
    #
    #     movement.set_signal('rotating left')
    #     # movement.signal = 'rotating left'
    #     self.assertEqual(movement.get_signal(), "rotating left")
    #
    #     movement.set_signal('rotating right')
    #     # movement.signal = 'rotating right'
    #     self.assertEqual(movement.get_signal(), "rotating right")
    #
    #     movement.set_signal('stop')
    #     # movement.signal = 'stop'
    #     self.assertEqual(movement.get_signal(), "stop")
    #
    #     movement.set_signal('continue')
    #     # movement.signal = 'continue'
    #     self.assertEqual(movement.get_signal(), None)
    #     movement.signal = None
    #     self.assertEqual(movement.get_signal(), None)

    def test_at_destination(self):
        # destination = {
        #     'x': 0.0,
        #     'y': 0.0
        # }
        x_destination: float = 0
        y_destination: float = 0
        # tests that method returns true when movement and coordinates are the same
        # movement.set_destination(destination)
        bot.set_x_destination(x_destination)
        bot.set_y_destination(y_destination)

        bot.set_x_pos(0)
        bot.set_y_pos(0)

        result = movement.at_destination()
        self.assertEqual(True, result)

        # tests that method returns true when movement and coordinates are within percentage error

        # movement._destination['x'] = 0.025
        # movement._destination['y'] = 0.025
        # destination['x'] = 0.025
        # destination['y'] = 0.025
        # movement.set_destination(destination)
        bot.set_x_destination(0.025)
        bot.set_y_destination(0.025)
        bot.set_x_pos(0)
        bot.set_y_pos(0)
        movement._set_position_error(0.05)
        result = movement.at_destination()
        self.assertEqual(True, result)

        # tests that method returns true when movement and coordinates are within percentage error

        # movement._destination['x'] = 5
        # movement._destination['y'] = 6
        # destination['x'] = 5.0
        # destination['y'] = 6.0
        # movement.set_destination(destination)
        bot.set_x_destination(5)
        bot.set_y_destination(6)

        bot.set_x_pos(5.01)
        bot.set_y_pos(5.96)
        # coordinates.x_pos = 5.01
        # coordinates.y_pos = 5.96
        # movement.position_percentage_error = 0.05
        # movement._set_position_error(0.05)
        result = movement.at_destination()
        self.assertEqual(True, result)
        bot.set_x_pos(5.05)
        bot.set_y_pos(5.95)
        # coordinates.x_pos = 5.05
        # coordinates.y_pos = 5.95
        # movement.position_percentage_error = 0.05
        # movement._set_position_error(0.05)
        result = movement.at_destination()
        self.assertEqual(False, result)

        pass

    def test_is_rotation_there(self):
        rotation = 94
        rotation_needed = 100
        # movement.rotation_percentage_error = 5
        movement._set_rotation_error(5)
        result = movement.is_rotation_there(rotation, rotation_needed)
        self.assertEqual(False, result)

        rotation = 95
        rotation_needed = 100
        # movement.rotation_percentage_error = 5
        # movement._set_rotation_error(5)
        result = movement.is_rotation_there(rotation, rotation_needed)
        self.assertEqual(True, result)

        rotation = 100.05
        rotation_needed = 100
        # movement.rotation_percentage_error = 0.05
        movement._set_rotation_error(0.05)
        result = movement.is_rotation_there(rotation, rotation_needed)
        self.assertEqual(True, result)

        rotation = 99.95
        rotation_needed = 100
        # movement.rotation_percentage_error = 0.05
        # movement._set_rotation_error(0.05)
        result = movement.is_rotation_there(rotation, rotation_needed)
        self.assertEqual(True, result)

    def test_get_rotation_needed(self):

        # tests that method works
        # movement._destination = {
        #     'x': 5,
        #     'y': 5
        # }
        # destination = {
        #     'x': 5,
        #     'y': 5
        # }
        # movement.set_destination(destination)
        bot.set_x_destination(5)
        bot.set_y_destination(5)

        bot.set_x_pos(0)
        bot.set_y_pos(0)

        result = movement.get_rotation_needed()
        self.assertEqual(45, result)

        # test for x positions being the same

        # destination['x'] = 0.0
        # destination['y'] = 5.0
        # movement.set_destination(destination)
        bot.set_x_destination(0)
        bot.set_y_destination(5)

        bot.set_x_pos(0)
        bot.set_y_pos(0)
        result = movement.get_rotation_needed()
        self.assertEqual(90, result)

        # test for x positions being the same
        # movement._destination = {
        #     'x': 0,
        #     'y': -5
        # }
        # destination['x'] = 0.0
        # destination['y'] = -5.0
        bot.set_x_destination(0)
        bot.set_y_destination(-5)
        # movement.set_destination(destination)
        bot.set_x_pos(0)
        bot.set_y_pos(0)
        result = movement.get_rotation_needed()
        self.assertEqual(270, result)

        # NO CHECK NEEDED
        # movement._destination = {
        #     'x': 0,
        #     'y': 0
        # }
        # coordinates.x_pos = 0
        # coordinates.y_pos = 0
        # result = movement.get_rotation_needed()
        # self.assertEqual(None, result)

        # test for y positions being the same
        # movement._destination = {
        #     'x': 5,
        #     'y': 0
        # }
        # destination['x'] = 5.0
        # destination['y'] = 0.0
        # movement.set_destination(destination)
        bot.set_x_destination(5)
        bot.set_y_destination(0)
        bot.set_x_pos(0)
        bot.set_y_pos(0)
        result = movement.get_rotation_needed()
        self.assertEqual(0, result)

        # test for y positions being the same
        # movement._destination = {
        #     'x': -5,
        #     'y': 0
        # }
        # destination['x'] = -5.0
        # destination['y'] = 0.0
        # movement.set_destination(destination)
        bot.set_x_destination(-5)
        bot.set_y_destination(0)
        bot.set_x_pos(0)
        bot.set_y_pos(0)
        result = movement.get_rotation_needed()
        self.assertEqual(180, result)

        # tests for correct result for dealing with arctan
        # movement._destination = {
        #     'x': -5,
        #     'y': 5
        # }
        # destination['x'] = -5.0
        # destination['y'] = 5.0
        # movement.set_destination(destination)
        bot.set_x_destination(-5)
        bot.set_y_destination(5)

        bot.set_x_pos(0)
        bot.set_y_pos(0)
        result = movement.get_rotation_needed()
        self.assertEqual(135, result)

        # tests for correct result for dealing with arctan
        # movement._destination = {
        #     'x': -5,
        #     'y': -5
        # }
        # destination['x'] = -5.0
        # destination['y'] = -5.0
        # movement.set_destination(destination)
        bot.set_x_destination(-5)
        bot.set_y_destination(-5)

        bot.set_x_pos(0)
        bot.set_y_pos(0)
        result = movement.get_rotation_needed()
        self.assertEqual(225, result)

        # tests for correct result for when coordinates are not 0
        # movement._destination = {
        #     'x': -5,
        #     'y': -5
        # }
        # destination['x'] = -5.0
        # destination['y'] = -5.0
        # movement.set_destination(destination)
        bot.set_x_pos(2)
        bot.set_y_pos(2)
        result = movement.get_rotation_needed()
        self.assertEqual(225, result)

        # tests for correct result for when coordinates are not 0
        # movement._destination = {
        #     'x': -5,
        #     'y': -5
        # }
        # destination['x'] = -5.0
        # destination['y'] = -5.0
        # movement.set_destination(destination)
        bot.set_x_pos(-7)
        bot.set_y_pos(-7)
        result = movement.get_rotation_needed()
        self.assertEqual(45, result)

    def test_is_rotation_left(self):

        # basic left or right tests
        result = movement.is_rotate_left(0, 45)
        self.assertEqual(True, result)

        result = movement.is_rotate_left(90, 135)
        self.assertEqual(True, result)

        result = movement.is_rotate_left(90, 45)
        self.assertEqual(False, result)

        # tests for change with 0 to 360
        result = movement.is_rotate_left(10, 350)
        self.assertEqual(False, result)

        result = movement.is_rotate_left(350, 10)
        self.assertEqual(True, result)

        # tests for shorter turn
        result = movement.is_rotate_left(0, 181)
        self.assertEqual(False, result)

        result = movement.is_rotate_left(181, 0)
        self.assertEqual(True, result)

        result = movement.is_rotate_left(0, 179)
        self.assertEqual(True, result)

        result = movement.is_rotate_left(179, 0)
        self.assertEqual(False, result)

        # # UNNECESSARY TEST -- turning 180 can be left or right
        # result = movement.is_rotate_left(180, 0)
        # self.assertEqual(False, result)
        #
        # result = movement.is_rotate_left(0, 180)
        # self.assertEqual(True, result)

    def test_is_move_change(self):

        robot_movement._change_direction("forward")
        result = movement.is_move_change("forward")
        self.assertEqual(False, result)
        result = movement.is_move_change("backward")
        self.assertEqual(True, result)
        result = movement.is_move_change("stop")
        self.assertEqual(True, result)

        robot_movement._change_direction("rotating left")
        result = movement.is_move_change("rotating left")
        self.assertEqual(False, result)
        result = movement.is_move_change("backward")
        self.assertEqual(True, result)
        result = movement.is_move_change("stop")
        self.assertEqual(True, result)

        robot_movement._change_direction("stop")
        result = movement.is_move_change("rotating left")
        self.assertEqual(True, result)
        result = movement.is_move_change("backward")
        self.assertEqual(True, result)
        result = movement.is_move_change("stop")
        self.assertEqual(False, result)

        robot_movement._change_direction("forward")
        result = movement.is_move_change("stop")
        self.assertEqual(True, result)

        pass

    def test_move_change(self):

        robot_movement.stop()
        movement.move_change("rotating right")
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], False)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], False)
        self.assertEqual(flags['rotating right'], True)

        robot_movement.rotate_right()
        movement.move_change("forward")
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], True)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], False)
        self.assertEqual(flags['rotating right'], False)

        robot_movement.rotate_right()
        movement.move_change("stop")
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], False)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], False)
        self.assertEqual(flags['rotating right'], False)

        robot_movement.backward()
        movement.move_change("continue")
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], False)
        self.assertEqual(flags['backward'], True)
        self.assertEqual(flags['rotating left'], False)
        self.assertEqual(flags['rotating right'], False)

        pass

    def test_move(self):
        # prerequisites to method call
        # movement.position_percentage_error = 0.5
        # movement.rotation_percentage_error = 0.5
        movement._set_position_error(0.5)
        movement._set_rotation_error(0.5)
        robot_movement.stop()
        # destination = {
        #     'x': 0,
        #     'y': 0
        # }
        # movement.set_destination(destination)
        bot.set_x_destination(0)
        bot.set_y_destination(-5)

        bot.set_x_pos(0)
        bot.set_y_pos(0)
        bot.set_rotation(0)
        bot.set_user_command("forward")
        # method call
        movement.move()

        # testing robot movement change
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], True)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], False)
        self.assertEqual(flags['rotating right'], False)

        # prerequisites to method call
        robot_movement.stop()
        # destination['x'] = 5.0
        # destination['y'] = 0.0
        # movement.set_destination(destination)
        bot.set_x_destination(5)
        bot.set_y_destination(0)

        bot.set_user_command("rotating left")

        # method call
        movement.move()

        # testing robot movement change
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], False)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], True)
        self.assertEqual(flags['rotating right'], False)

        # prerequisites to method call
        robot_movement.stop()
        bot.set_x_pos(0)
        bot.set_y_pos(0)
        bot.set_rotation(0)

        bot.set_user_command("")

        # method call
        movement.move()
        # for key in robot_movement.direction_flags.keys():
        #     print(robot_movement.direction_flags[key])
        # testing robot movement change
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], True)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], False)
        self.assertEqual(flags['rotating right'], False)

        # prerequisites to method call
        robot_movement.stop()
        # destination['x'] = -5.0
        # destination['y'] = 0.0
        # movement.set_destination(destination)
        bot.set_x_destination(-5)
        bot.set_y_destination(0)
        # method call
        movement.move()

        # testing robot movement change
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], False)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], True)
        self.assertEqual(flags['rotating right'], False)

        # prerequisites to method call
        robot_movement.stop()
        # destination['x'] = 5.0
        # destination['y'] = 5.0
        # movement.set_destination(destination)
        bot.set_x_destination(5)
        bot.set_y_destination(5)
        # method call
        movement.move()

        # testing robot movement change
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], False)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], True)
        self.assertEqual(flags['rotating right'], False)

        # prerequisites to method call
        robot_movement.stop()
        # destination['x'] = 5.0
        # destination['y'] = 0.0
        # movement.set_destination(destination)
        bot.set_x_destination(5)
        bot.set_y_destination(0)

        bot.set_rotation(45)
        # method call
        movement.move()

        # testing robot movement change
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], False)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], False)
        self.assertEqual(flags['rotating right'], True)

        # prerequisites to method call
        robot_movement.stop()

        bot.set_rotation(0)

        # method call
        movement.move()

        # testing robot movement change
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], True)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], False)
        self.assertEqual(flags['rotating right'], False)

        # prerequisites to method call
        robot_movement.stop()
        bot.set_rotation(0.5)

        # method call
        movement.move()

        # testing robot movement change
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], True)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], False)
        self.assertEqual(flags['rotating right'], False)

        # prerequisites to method call
        robot_movement.stop()
        bot.set_rotation(0.6)

        # method call
        movement.move()

        # testing robot movement change
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], False)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], False)
        self.assertEqual(flags['rotating right'], True)

        # prerequisites to method call
        robot_movement.stop()
        bot.set_rotation(355.5)

        # method call
        movement.move()

        # testing robot movement change
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], False)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], True)
        self.assertEqual(flags['rotating right'], False)

        # prerequisites to method call
        robot_movement.stop()

        bot.set_x_pos(5)
        bot.set_y_pos(0)

        bot.set_rotation(0.6)

        # method call
        movement.move()

        # testing robot movement change
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], False)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], False)
        self.assertEqual(flags['rotating right'], False)

        # prerequisites to method call
        robot_movement.stop()

        bot.set_x_pos(4.5)
        bot.set_y_pos(0.5)

        # coordinates.x_pos = 4.5
        # coordinates.y_pos = 0.5

        bot.set_rotation(0.6)

        # method call
        movement.move()

        # testing robot movement change
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], False)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], False)
        self.assertEqual(flags['rotating right'], True)

        # prerequisites to method call
        robot_movement.stop()

        bot.set_x_pos(4.5)
        bot.set_y_pos(0.5)

        bot.set_rotation(145)

        # method call
        movement.move()

        # testing robot movement change
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], False)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], True)
        self.assertEqual(flags['rotating right'], False)
