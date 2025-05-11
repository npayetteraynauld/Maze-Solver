from tkinter import Tk, BOTH, Canvas
from window import *
from point import *
from cell import *
from maze import * 




def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()
    print("maze created")
    is_solvable = maze.solve()
    if not is_solvable:
        print("maze can't be solved")
    else:
        print("maze solved!")

    win.wait_for_close()

main()
