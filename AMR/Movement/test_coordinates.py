import time
import unittest
import os
import sys

# Add the parent directory (AMR) to the Python path -- ChatGPT used for line below-- used for " python3 -m unittest
# discover -v Movement/ > Movement-test.log 2>&1" in the terminal, "python test_out.py > pytest.log" wasn't working and
# doing unit tests in the terminal resulted in AMR not being the base directory
amr_directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(amr_directory)
import coordinates
from Model import robot as bot

# --- NOTE ---
# comment out import jetbot in robot_movement.py
# comment out portions of the methods in robot_movement.py -- marked with "--- NOTE ---"
# some will have "# --- END OF COMMENTING OUT ---" after a few lines of code to signify multiple lines to be commented out
# expected should be changed if scale is adjusted -- currently movement_scale = 0.16  and rotation_scale = 0.35


class Test_Coordinates(unittest.TestCase):

    def test_time(self):

        # resets time recorder for test
        coordinates._set_time_of_last_update(0)

        result = coordinates.time_since_lest_update()
        # print(result)
        self.assertEqual(result, 0)

        time.sleep(0.03)
        result = coordinates.time_since_lest_update()
        # print(result)
        self.assertGreater(result, 0.029 * 1000)

        time.sleep(.5)
        result = coordinates.time_since_lest_update()
        # print(result)
        self.assertGreater(result, 0.49 * 1000)

    def test_move_forward(self):
        # resets position and rotation for test
        bot.set_x_pos(0)
        bot.set_y_pos(0)
        bot.set_rotation(90)

        # x_pos: float = coordinates.x_pos
        # y_pos: float = coordinates.y_pos
        # rotation = coordinates.direction_in_degrees
        # # print(f'x position: {x_pos} -- y position: {y_pos} -- rotation: {rotation}')
        # self.assertEqual(x_pos, 0)
        # self.assertEqual(y_pos, 0)
        # self.assertEqual(rotation, 90)

        time_since = coordinates.time_since_lest_update()
        # print(f'time: {time_since}')
        if time_since == 0:
            time.sleep(0.1)
            time_since = coordinates.time_since_lest_update()
            print(f'time: {time_since}')

        # tests sin and cos functions work correctly
        coordinates.move_forward(time_since)
        # x_pos = coordinates.get_x_pos()
        # y_pos = coordinates.get_y_pos()
        self.assertAlmostEqual(bot.get_x_pos(), 0, 5)
        self.assertGreater(bot.get_y_pos(), 0)

        # tests scaling of movement, a movement scaling of 1 should move the robot 1 coordinate in 1 second
        bot.set_x_pos(0)
        bot.set_y_pos(0)
        coordinates.move_forward(1000)

        # expected should be changed if scale is adjusted
        self.assertAlmostEqual(bot.get_x_pos(), 0, 5,
                               "x position was not close enough to 0")  # x is 0 with a margin of error of 0.00001

        # expected should be changed if scale is adjusted
        self.assertAlmostEqual(bot.get_y_pos(), 0.16, 5,
                               "y position was not close enough to 1")  # y is 1 with a margin of error of 0.00001

        ### RETEST ###
        # tests that movement is rounded so that insignificant change is not recorded
        # tests scaling of movement, a movement scaling of 1 should move the robot 1 coordinate in 1 second
        bot.set_x_pos(0)
        bot.set_y_pos(0)
        coordinates.move_forward(1000)

        # expected should be changed if scale is adjusted
        self.assertEqual(bot.get_x_pos(), 0, 0)  # x is 0 with a margin of error of 0.00001
        self.assertEqual(bot.get_y_pos(), 0.16, 0)  # y is 1 with a margin of error of 0.00001

        # tests scaling
        bot.set_x_pos(0)
        bot.set_y_pos(0)
        coordinates.move_forward(2000)  # 2 seconds of moving

        # expected should be changed if scale is adjusted
        self.assertEqual(bot.get_x_pos(), 0, 0)  # x is 0 with a margin of error of 0.00001
        self.assertEqual(bot.get_y_pos(), 0.32, 0)  # y is 1 with a margin of error of 0.00001

        bot.set_x_pos(0)
        bot.set_y_pos(0)
        coordinates.move_forward(500)  # 0.5 seconds of moving

        # expected should be changed if scale is adjusted
        self.assertEqual(bot.get_x_pos(), 0, 0)  # x is 0 with a margin of error of 0.00001
        self.assertEqual(bot.get_y_pos(), 0.08, 0)  # y is 1 with a margin of error of 0.00001

        # tests rotation is working correctly
        bot.set_rotation(0)
        bot.set_x_pos(0)
        bot.set_y_pos(0)
        coordinates.move_forward(500)  # 0.5 seconds of moving

        # expected should be changed if scale is adjusted
        self.assertEqual(bot.get_x_pos(), 0.08, 0)  # x is 0 with a margin of error of 0.00001
        self.assertEqual(bot.get_y_pos(), 0, 0)  # y is 1 with a margin of error of 0.00001

    # should be the same as move forward but subtracting instead of adding
    def test_move_backward(self):
        # tests that movement is rounded so that insignificant change is not recorded
        # tests scaling of movement, a movement scaling of 1 should move the robot 1 coordinate in 1 second
        bot.set_x_pos(0)
        bot.set_y_pos(0)
        coordinates.move_backward(1000)

        # expected should be changed if scale is adjusted
        self.assertEqual(bot.get_x_pos(), -0.16)
        self.assertEqual(bot.get_y_pos(), 0)

        # tests scaling
        bot.set_x_pos(0)
        bot.set_y_pos(0)
        coordinates.move_backward(2000)  # 2 seconds of moving

        # expected should be changed if scale is adjusted
        self.assertEqual(bot.get_x_pos(), -0.32)  # x is 0 with a margin of error of 0.00001
        self.assertEqual(bot.get_y_pos(), 0)  # y is 1 with a margin of error of 0.00001

        bot.set_x_pos(0)
        bot.set_y_pos(0)
        coordinates.move_backward(500)  # 0.5 seconds of moving

        # expected should be changed if scale is adjusted
        self.assertEqual(bot.get_x_pos(), -0.08)  # x is 0 with a margin of error of 0.00001
        self.assertEqual(bot.get_y_pos(), 0)  # y is 1 with a margin of error of 0.00001

    def test_rotate_left(self):

        coordinates.rotation_scale = 1
        # tests scaling of rotation, a rotation scaling of 1 should rotate the robot a full 360 degrees in 1 second
        bot.set_rotation(0)
        coordinates.rotate_left(1000)

        # expected should be changed if scale is adjusted
        self.assertAlmostEqual(bot.get_rotation(), 126)

        # tests scaling of rotation, a rotation scaling of 1 should rotate the robot a full 360 degrees in 1 second
        bot.set_rotation(90)
        coordinates.rotate_left(1000)

        # expected should be changed if scale is adjusted
        self.assertAlmostEqual(bot.get_rotation(), 216)

        # tests scaling of rotation, rotation for half a second is 180 degrees
        bot.set_rotation(0)
        coordinates.rotate_left(500)

        # expected should be changed if scale is adjusted
        self.assertAlmostEqual(bot.get_rotation(), 63)

        # tests direction of rotation, ensures coordinate tracking is rotating in the right way
        bot.set_rotation(90)
        coordinates.rotate_left(250)

        # expected should be changed if scale is adjusted
        self.assertAlmostEqual(bot.get_rotation(), 121.5)  # degrees is 90 with no margin of error

    def test_rotate_right(self):
        coordinates.rotation_scale = 1
        # tests scaling of rotation, a rotation scaling of 1 should rotate the robot a full 360 degrees in 1 second
        bot.set_rotation(0)
        coordinates.rotate_right(1000)

        # expected should be changed if scale is adjusted
        self.assertAlmostEqual(bot.get_rotation(), 234, 0)  # degrees is 0 with no margin of error

        # tests scaling of rotation, a rotation scaling of 1 should rotate the robot a full 360 degrees in 1 second
        bot.set_rotation(90)
        coordinates.rotate_right(1000)

        # expected should be changed if scale is adjusted
        self.assertAlmostEqual(bot.get_rotation(), 324, 0)  # degrees is 90 with no margin of error

        # tests scaling of rotation, rotation for half a second is 180 degrees
        bot.set_rotation(0)
        coordinates.rotate_right(500)

        # expected should be changed if scale is adjusted
        self.assertAlmostEqual(bot.get_rotation(), 297, 0)  # degrees is 90 with no margin of error

        # tests direction of rotation, ensures coordinate tracking is rotating in the right way
        bot.set_rotation(90)
        coordinates.rotate_right(250)

        # expected should be changed if scale is adjusted
        self.assertAlmostEqual(bot.get_rotation(), 58.5, 0)  # degrees is 90 with no margin of error
