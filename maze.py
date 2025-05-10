from cell import Cell
from point import *
import time
import random
from maze import *



class Maze:
    def __init__(self, 
                 x1, 
                 y1, 
                 num_rows, 
                 num_cols,
                 cell_size_x, 
                 cell_size_y, 
                 win=None,
                 seed=None
                 ):

        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._seed = seed

        if self._seed != None:
            random.seed(self._seed)

        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.__num_cols):
            column = []
            for j in range(self.__num_rows):
                x1 = self.__x1 + (i * self.__cell_size_x)
                y1 = self.__y1 + (j * self.__cell_size_y)

                x2 = x1 + self.__cell_size_x
                y2 = y1 + self.__cell_size_y

                p1 = Point(x1, y1)
                p2 = Point(x2, y2)

                cell = Cell(p1, p2, self.__win)

                column.append(cell)
 

            self._cells.append(column)

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw()
        self._animate()

    def _animate(self):
        if self.__win != None:
            self.__win.redraw()
            time.sleep(0.005)


    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.__num_cols-1][self.__num_rows-1].has_bottom_wall = False
        self._draw_cell(self.__num_cols-1, self.__num_rows-1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        current_cell = self._cells[i][j]
        
        while True:
            to_visit = []

            if i < (len(self._cells) - 1):
                if self._cells[i+1][j]._visited == False:
                    to_visit.append((i+1, j))

            if i > 0:
                if self._cells[i-1][j]._visited == False:
                    to_visit.append((i-1, j))

            if j < (len(self._cells[0]) - 1):
                if self._cells[i][j+1]._visited == False:
                    to_visit.append((i, j+1))
            
            if j > 0:
                if self._cells[i][j-1]._visited == False:
                    to_visit.append((i, j-1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            direction = random.randrange(len(to_visit))
            to_coords = to_visit[direction]
            to_cell = self._cells[to_coords[0]][to_coords[1]]

            #right
            if i < to_coords[0]:
                current_cell.has_right_wall = False
                to_cell.has_left_wall = False

            #left
            if i > to_coords[0]:
                current_cell.has_left_wall = False
                to_cell.has_right_wall = False
            #up
            if j > to_coords[1]:
                current_cell.has_top_wall = False
                to_cell.has_bottom_wall = False

            #down
            if j < to_coords[1]:
                current_cell.has_bottom_wall = False
                to_cell.has_top_wall = False

            self._break_walls_r(to_coords[0], to_coords[1])

    def _reset_cells_visited(self):
        for columns in self._cells:
            for cell in columns:
                cell._visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        end_cell = self._cells[len(self._cells) - 1][len(self._cells[0]) - 1]
        self._animate()
        current_cell = self._cells[i][j]
        
        current_cell._visited = True

        if current_cell == end_cell:
            return True

            






