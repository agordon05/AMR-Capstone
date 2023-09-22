import time
import unittest
import coordinates


class Test_Coordinates(unittest.TestCase):

    def test_time(self):

        # resets time recorder for test
        coordinates.time_of_last_update_ms = 0

        result = coordinates.time_since_lest_update()
        # print(result)
        self.assertEqual(result, 0)

        time.sleep(0.03)
        result = coordinates.time_since_lest_update()
        # print(result)
        self.assertGreater(result, 0.03 * 1000)

        time.sleep(.5)
        result = coordinates.time_since_lest_update()
        # print(result)
        self.assertGreater(result, 0.5 * 1000)

    def test_move_forward(self):
        # resets position and rotation for test
        coordinates.x_pos = 0
        coordinates.y_pos = 0
        coordinates.direction_in_degrees = 90

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
        x_pos = coordinates.x_pos
        y_pos = coordinates.y_pos
        self.assertAlmostEqual(coordinates.x_pos, 0, 5)
        self.assertGreater(coordinates.y_pos, 0)

        # tests scaling of movement, a movement scaling of 1 should move the robot 1 coordinate in 1 second
        coordinates.x_pos = 0
        coordinates.y_pos = 0
        coordinates.move_forward(1000)
        self.assertAlmostEqual(coordinates.x_pos, 0, 5,
                               "x position was not close enough to 0")  # x is 0 with a margin of error of 0.00001
        self.assertAlmostEqual(coordinates.y_pos, 1, 5,
                               "y position was not close enough to 1")  # y is 1 with a margin of error of 0.00001

        ### RETEST ###
        # tests that movement is rounded so that insignificant change is not recorded
        # tests scaling of movement, a movement scaling of 1 should move the robot 1 coordinate in 1 second
        coordinates.x_pos = 0
        coordinates.y_pos = 0
        coordinates.move_forward(1000)
        self.assertEqual(coordinates.x_pos, 0, 0)  # x is 0 with a margin of error of 0.00001
        self.assertEqual(coordinates.y_pos, 1, 0)  # y is 1 with a margin of error of 0.00001

        # tests scaling
        coordinates.x_pos = 0
        coordinates.y_pos = 0
        coordinates.move_forward(2000)  # 2 seconds of moving
        self.assertEqual(coordinates.x_pos, 0, 0)  # x is 0 with a margin of error of 0.00001
        self.assertEqual(coordinates.y_pos, 2, 0)  # y is 1 with a margin of error of 0.00001

        coordinates.x_pos = 0
        coordinates.y_pos = 0
        coordinates.move_forward(500)  # 0.5 seconds of moving
        self.assertEqual(coordinates.x_pos, 0, 0)  # x is 0 with a margin of error of 0.00001
        self.assertEqual(coordinates.y_pos, 0.5, 0)  # y is 1 with a margin of error of 0.00001

        # tests rotation is working correctly
        coordinates.direction_in_degrees = 0
        coordinates.x_pos = 0
        coordinates.y_pos = 0
        coordinates.move_forward(500)  # 0.5 seconds of moving
        self.assertEqual(coordinates.x_pos, 0.5, 0)  # x is 0 with a margin of error of 0.00001
        self.assertEqual(coordinates.y_pos, 0, 0)  # y is 1 with a margin of error of 0.00001

    # should be the same as move forward but subtracting instead of adding
    def test_move_backward(self):
        # tests that movement is rounded so that insignificant change is not recorded
        # tests scaling of movement, a movement scaling of 1 should move the robot 1 coordinate in 1 second
        coordinates.x_pos = 0
        coordinates.y_pos = 0
        coordinates.move_backward(1000)
        self.assertEqual(coordinates.x_pos, 0, 0)  # x is 0 with a margin of error of 0.00001
        self.assertEqual(coordinates.y_pos, -1, 0)  # y is 1 with a margin of error of 0.00001

        # tests scaling
        coordinates.x_pos = 0
        coordinates.y_pos = 0
        coordinates.move_backward(2000)  # 2 seconds of moving
        self.assertEqual(coordinates.x_pos, 0, 0)  # x is 0 with a margin of error of 0.00001
        self.assertEqual(coordinates.y_pos, -2, 0)  # y is 1 with a margin of error of 0.00001

        coordinates.x_pos = 0
        coordinates.y_pos = 0
        coordinates.move_backward(500)  # 0.5 seconds of moving
        self.assertEqual(coordinates.x_pos, 0, 0)  # x is 0 with a margin of error of 0.00001
        self.assertEqual(coordinates.y_pos, -0.5, 0)  # y is 1 with a margin of error of 0.00001

    def test_rotate_left(self):

        coordinates.rotation_scale = 1
        # tests scaling of rotation, a rotation scaling of 1 should rotate the robot a full 360 degrees in 1 second
        coordinates.direction_in_degrees = 0
        coordinates.rotate_left(1000)
        self.assertAlmostEqual(coordinates.direction_in_degrees, 0, 0)  # degrees is 0 with no margin of error

        # tests scaling of rotation, a rotation scaling of 1 should rotate the robot a full 360 degrees in 1 second
        coordinates.direction_in_degrees = 90
        coordinates.rotate_left(1000)
        self.assertAlmostEqual(coordinates.direction_in_degrees, 90, 0)  # degrees is 90 with no margin of error

        # tests scaling of rotation, rotation for half a second is 180 degrees
        coordinates.direction_in_degrees = 0
        coordinates.rotate_left(500)
        self.assertAlmostEqual(coordinates.direction_in_degrees, 180, 0)  # degrees is 90 with no margin of error

        # tests direction of rotation, ensures coordinate tracking is rotating in the right way
        coordinates.direction_in_degrees = 90
        coordinates.rotate_left(250)
        self.assertAlmostEqual(coordinates.direction_in_degrees, 180, 0)  # degrees is 90 with no margin of error

    def test_rotate_right(self):
        coordinates.rotation_scale = 1
        # tests scaling of rotation, a rotation scaling of 1 should rotate the robot a full 360 degrees in 1 second
        coordinates.direction_in_degrees = 0
        coordinates.rotate_right(1000)
        self.assertAlmostEqual(coordinates.direction_in_degrees, 0, 0)  # degrees is 0 with no margin of error

        # tests scaling of rotation, a rotation scaling of 1 should rotate the robot a full 360 degrees in 1 second
        coordinates.direction_in_degrees = 90
        coordinates.rotate_right(1000)
        self.assertAlmostEqual(coordinates.direction_in_degrees, 90, 0)  # degrees is 90 with no margin of error

        # tests scaling of rotation, rotation for half a second is 180 degrees
        coordinates.direction_in_degrees = 0
        coordinates.rotate_right(500)
        self.assertAlmostEqual(coordinates.direction_in_degrees, 180, 0)  # degrees is 90 with no margin of error

        # tests direction of rotation, ensures coordinate tracking is rotating in the right way
        coordinates.direction_in_degrees = 90
        coordinates.rotate_right(250)
        self.assertAlmostEqual(coordinates.direction_in_degrees, 0, 0)  # degrees is 90 with no margin of error
