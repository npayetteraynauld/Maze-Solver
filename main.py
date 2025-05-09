from tkinter import Tk, BOTH, Canvas
from window import *
from point import *
from cell import *

win = Window(800, 600)

cell1 = Cell(Point(400, 300), Point(500, 400), win)
cell1.has_bottom_wall = False
cell2 = Cell(Point(300, 200), Point(350, 150), win)
cell2.has_bottom_wall = False

cell1.draw()
cell2.draw()

cell1.draw_move(cell2, undo=True)

win.wait_for_close()
