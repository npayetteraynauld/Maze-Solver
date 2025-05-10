from tkinter import Tk, BOTH, Canvas
from window import *
from point import *
from cell import *
from maze import * 

win = Window(800, 600)

maze = Maze(5, 5, 25, 35, 20, 20, win)
maze._break_entrance_and_exit()
maze._break_walls_r(0, 0)
maze._reset_cells_visited()
win.wait_for_close()
