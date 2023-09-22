import unittest
import robot_movement


class Test_Robot_Movement(unittest.TestCase):

    # tests that the direction flags change appropriately to the direction the robot is moving
    def test_change_direction(self):

        # tests that the direction flag will change
        self.assertEqual(robot_movement.direction_flags['forward'], False)
        self.assertEqual(robot_movement.direction_flags['backward'], False)
        self.assertEqual(robot_movement.direction_flags['rotating left'], False)
        self.assertEqual(robot_movement.direction_flags['rotating right'], False)

        robot_movement.forward()

        self.assertEqual(robot_movement.direction_flags['forward'], True)
        self.assertEqual(robot_movement.direction_flags['backward'], False)
        self.assertEqual(robot_movement.direction_flags['rotating left'], False)
        self.assertEqual(robot_movement.direction_flags['rotating right'], False)


        # tests that the stop condition turns all flags false
        robot_movement.stop()
        self.assertEqual(robot_movement.direction_flags['forward'], False, "Forward flag did not turn false")
        self.assertEqual(robot_movement.direction_flags['backward'], False)
        self.assertEqual(robot_movement.direction_flags['rotating left'], False)
        self.assertEqual(robot_movement.direction_flags['rotating right'], False)

        # tests that changing direction will change the the flags correctly
        robot_movement.forward()
        self.assertEqual(robot_movement.direction_flags['forward'], True)
        self.assertEqual(robot_movement.direction_flags['backward'], False)
        self.assertEqual(robot_movement.direction_flags['rotating left'], False)
        self.assertEqual(robot_movement.direction_flags['rotating right'], False)

        robot_movement.rotate_left()
        self.assertEqual(robot_movement.direction_flags['forward'], False)
        self.assertEqual(robot_movement.direction_flags['backward'], False)
        self.assertEqual(robot_movement.direction_flags['rotating left'], True)
        self.assertEqual(robot_movement.direction_flags['rotating right'], False)