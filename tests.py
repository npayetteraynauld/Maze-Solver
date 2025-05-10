import unittest
from maze import *

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    
    def test_maze_create_cells1(self):
        num_cols = 48
        num_rows = 100
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_maze_create_cells2(self):
        num_cols = 32
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_check_entrance_and_exit(self):
        num_cols = 32
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._cells[num_cols-1][num_rows-1].has_bottom_wall,
            False
        )

    def test_check_false_after_maze(self):
        maze = Maze(5, 5, 25, 35, 20, 20)
        maze._break_entrance_and_exit()
        maze._break_walls_r(0, 0)
        maze._reset_cells_visited()
        self.assertEqual(
            maze._cells[0][0]._visited,
            False
        )
        self.assertEqual(
            maze._cells[10][10]._visited,
            False
        )
        
if __name__ == "__main__":
    unittest.main()
