import unittest
import movement
import coordinates
from Robot import robot_movement


class Test_Movement(unittest.TestCase):

    def test_signal(self):
        # movement.signal = 'forward'
        movement.set_signal('forward')
        self.assertEqual(movement.get_signal(), "forward")

        movement.set_signal('backward')
        # movement.signal = 'backward'
        self.assertEqual(movement.get_signal(), "backward")

        movement.set_signal('rotating left')
        # movement.signal = 'rotating left'
        self.assertEqual(movement.get_signal(), "rotating left")

        movement.set_signal('rotating right')
        # movement.signal = 'rotating right'
        self.assertEqual(movement.get_signal(), "rotating right")

        movement.set_signal('stop')
        # movement.signal = 'stop'
        self.assertEqual(movement.get_signal(), "stop")

        movement.set_signal('continue')
        # movement.signal = 'continue'
        self.assertEqual(movement.get_signal(), None)
        movement.signal = None
        self.assertEqual(movement.get_signal(), None)

    def test_at_destination(self):
        destination = {
            'x': 0.0,
            'y': 0.0
        }
        # tests that method returns true when movement and coordinates are the same
        movement.set_destination(destination)
        coordinates._set_x_pos(0)
        coordinates._set_y_pos(0)
        result = movement.at_destination()
        self.assertEqual(True, result)

        # tests that method returns true when movement and coordinates are within percentage error

        # movement._destination['x'] = 0.025
        # movement._destination['y'] = 0.025
        destination['x'] = 0.025
        destination['y'] = 0.025
        movement.set_destination(destination)
        coordinates._set_x_pos(0)
        coordinates._set_y_pos(0)
        movement._set_position_error(0.05)
        result = movement.at_destination()
        self.assertEqual(True, result)

        # tests that method returns true when movement and coordinates are within percentage error

        # movement._destination['x'] = 5
        # movement._destination['y'] = 6
        destination['x'] = 5.0
        destination['y'] = 6.0
        movement.set_destination(destination)
        coordinates._set_x_pos(5.01)
        coordinates._set_y_pos(5.96)
        # coordinates.x_pos = 5.01
        # coordinates.y_pos = 5.96
        # movement.position_percentage_error = 0.05
        # movement._set_position_error(0.05)
        result = movement.at_destination()
        self.assertEqual(True, result)
        coordinates._set_x_pos(5.05)
        coordinates._set_y_pos(5.95)
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
        destination = {
            'x': 5,
            'y': 5
        }
        movement.set_destination(destination)
        coordinates._set_x_pos(0)
        coordinates._set_y_pos(0)
        result = movement.get_rotation_needed()
        self.assertEqual(45, result)

        # test for x positions being the same

        destination['x'] = 0.0
        destination['y'] = 5.0
        movement.set_destination(destination)
        coordinates._set_x_pos(0)
        coordinates._set_y_pos(0)
        result = movement.get_rotation_needed()
        self.assertEqual(90, result)

        # test for x positions being the same
        # movement._destination = {
        #     'x': 0,
        #     'y': -5
        # }
        destination['x'] = 0.0
        destination['y'] = -5.0
        movement.set_destination(destination)
        coordinates._set_x_pos(0)
        coordinates._set_y_pos(0)
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
        destination['x'] = 5.0
        destination['y'] = 0.0
        movement.set_destination(destination)
        coordinates._set_x_pos(0)
        coordinates._set_y_pos(0)
        result = movement.get_rotation_needed()
        self.assertEqual(0, result)

        # test for y positions being the same
        # movement._destination = {
        #     'x': -5,
        #     'y': 0
        # }
        destination['x'] = -5.0
        destination['y'] = 0.0
        movement.set_destination(destination)
        coordinates._set_x_pos(0)
        coordinates._set_y_pos(0)
        result = movement.get_rotation_needed()
        self.assertEqual(180, result)

        # tests for correct result for dealing with arctan
        # movement._destination = {
        #     'x': -5,
        #     'y': 5
        # }
        destination['x'] = -5.0
        destination['y'] = 5.0
        movement.set_destination(destination)
        coordinates._set_x_pos(0)
        coordinates._set_y_pos(0)
        result = movement.get_rotation_needed()
        self.assertEqual(135, result)

        # tests for correct result for dealing with arctan
        # movement._destination = {
        #     'x': -5,
        #     'y': -5
        # }
        destination['x'] = -5.0
        destination['y'] = -5.0
        movement.set_destination(destination)
        coordinates._set_x_pos(0)
        coordinates._set_y_pos(0)
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
        coordinates._set_x_pos(2)
        coordinates._set_y_pos(2)
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
        coordinates._set_x_pos(-7)
        coordinates._set_y_pos(-7)
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
        destination = {
            'x': 0,
            'y': 0
        }
        movement.set_destination(destination)
        coordinates._set_x_pos(0)
        coordinates._set_y_pos(0)
        coordinates.set_rotation(0)
        movement.set_signal("forward")
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
        destination['x'] = 5.0
        destination['y'] = 0.0
        movement.set_destination(destination)
        movement.set_signal("rotating left")

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
        coordinates._set_x_pos(0)
        coordinates._set_y_pos(0)
        coordinates.set_rotation(0)

        movement.set_signal(None)

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
        destination['x'] = -5.0
        destination['y'] = 0.0
        movement.set_destination(destination)
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
        destination['x'] = 5.0
        destination['y'] = 5.0
        movement.set_destination(destination)
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
        destination['x'] = 5.0
        destination['y'] = 0.0
        movement.set_destination(destination)
        coordinates.set_rotation(45)
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

        coordinates.set_rotation(0)

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
        coordinates.set_rotation(0.5)

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
        coordinates.set_rotation(0.6)

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
        coordinates.set_rotation(355.5)

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

        coordinates._set_x_pos(5)
        coordinates._set_y_pos(0)

        coordinates.set_rotation(0.6)

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

        coordinates._set_x_pos(4.5)
        coordinates._set_y_pos(0.5)

        # coordinates.x_pos = 4.5
        # coordinates.y_pos = 0.5

        coordinates.set_rotation(0.6)

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

        coordinates._set_x_pos(4.5)
        coordinates._set_y_pos(0.5)

        coordinates.set_rotation(145)

        # method call
        movement.move()

        # testing robot movement change
        flags = robot_movement.get_direction_flags()
        self.assertEqual(flags['forward'], False)
        self.assertEqual(flags['backward'], False)
        self.assertEqual(flags['rotating left'], True)
        self.assertEqual(flags['rotating right'], False)
