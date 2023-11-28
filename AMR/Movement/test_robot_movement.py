import unittest
import os
import sys

# Add the parent directory (AMR) to the Python path -- ChatGPT used for line below-- used for " python3 -m unittest
# discover -v Movement/ > Movement-test.log 2>&1" in the terminal, "python test_out.py > pytest.log" wasn't working and
# doing unit tests in the terminal resulted in AMR not being the base directory
amr_directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(amr_directory)
from Robot_command import robot_movement

# --- NOTE ---
# comment out import jetbot in robot_movement.py
# comment out portions of the methods in robot_movement.py -- marked with "--- NOTE ---"
# some will have "# --- END OF COMMENTING OUT ---" after a few lines of code to signify multiple lines to be commented out


class Test_Robot_Movement(unittest.TestCase):

    # tests that the direction flags change appropriately to the direction the robot is moving
    def test_change_direction(self):
        robot_movement.stop()
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