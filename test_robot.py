import unittest
from robot import Robot

class Test_Robot(unittest.TestCase):

    def test_correct_place(self):
        robot = Robot()
        robot.place(1, 1, 'WEST')
        self.assertEqual(robot.position, (1, 1))
        self.assertEqual(robot.direction[2], 'WEST')
    
    def test_out_of_bounds_place(self):
        robot = Robot()
        robot.place(-1, 6, 'WEST')
        self.assertEqual(robot.position, (None, None))
        self.assertEqual(robot.direction, (0, 0, "NONE"))

    def test_correct_move(self):
        robot = Robot()
        robot.place(0, 0, 'NORTH')
        robot.move()
        self.assertEqual(robot.position, (0, 1))
        self.assertEqual(robot.direction[2], 'NORTH')

    def test_out_of_bounds_move(self):
        robot = Robot()
        robot.place(0, 0, 'WEST')
        robot.move()
        self.assertEqual(robot.position, (0, 0))
        self.assertEqual(robot.direction[2], 'WEST')

    def test_move_without_place(self):
        robot = Robot()
        before_move_pos = robot.position
        before_move_dir = robot.direction
        robot.move()
        self.assertEqual(robot.position, before_move_pos)
        self.assertEqual(robot.direction, before_move_dir)

    def test_turn_without_place(self):
        robot = Robot()
        before_turn_pos = robot.position        
        before_turn_dir = robot.direction
        robot.turn('RIGHT')
        self.assertEqual(robot.position, before_turn_pos)
        self.assertEqual(robot.direction, before_turn_dir)

    def test_rotation_right_from_west(self):
        robot = Robot()
        robot.place(0, 0, 'WEST')
        robot.turn('RIGHT')
        self.assertEqual(robot.position, (0, 0))
        self.assertEqual(robot.direction[2], 'NORTH')

    def test_rotation_left_from_north(self):
        robot = Robot()
        robot.place(0, 0, 'NORTH')
        robot.turn('LEFT')
        self.assertEqual(robot.position, (0, 0))
        self.assertEqual(robot.direction[2], 'WEST')

    def test_multiple_actions(self):
        robot = Robot()
        robot.place(1, 2, 'EAST')
        robot.move()
        robot.move()
        robot.turn('LEFT')
        robot.move()
        self.assertEqual(robot.position, (3, 3))
        self.assertEqual(robot.direction[2], 'NORTH')

if __name__ == '__main__':
    unittest.main()
