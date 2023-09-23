import unittest
from Robot import robot_movement


class Test_Robot_Movement(unittest.TestCase):

    # tests that the direction flags change appropriately to the direction the robot is moving
    def test_change_direction(self):

        # tests that the direction flag will change
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], False)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], False)
        self.assertEqual(flags['rotating right'], False)

        robot_movement.forward()
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], True)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], False)
        self.assertEqual(flags['rotating right'], False)


        # tests that the stop condition turns all flags false
        robot_movement.stop()
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], False, "Forward flag did not turn false")
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], False)
        self.assertEqual(flags['rotating right'], False)

        # tests that changing direction will change the the flags correctly
        robot_movement.forward()
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], True)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], False)
        self.assertEqual(flags['rotating right'], False)

        robot_movement.rotate_left()
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], False)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], True)
        self.assertEqual(flags['rotating right'], False)