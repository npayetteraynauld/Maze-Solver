from point import *
from window import *

class Cell:
    def __init__(self, point1, point2, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__x1 = point1.x
        self.__y1 = point1.y

        self.__x2 = point2.x
        self.__y2 = point2.y

        self.__win = window

        self._visited = False

    def draw(self):
        top_left_point = Point(self.__x1, self.__y1)
        top_right_point = Point(self.__x2, self.__y1)
        bottom_left_point = Point(self.__x1, self.__y2)
        bottom_right_point = Point(self.__x2, self.__y2)

        if self.__win != None:

            if self.has_left_wall == True:
                left_wall = Line(top_left_point, bottom_left_point)
                self.__win.draw_line(left_wall)

            if self.has_right_wall == True:
                right_wall = Line(top_right_point, bottom_right_point)
                self.__win.draw_line(right_wall)

            if self.has_top_wall == True:
                top_wall = Line(top_left_point, top_right_point)
                self.__win.draw_line(top_wall)

            if self.has_bottom_wall == True:
                bottom_wall = Line(bottom_left_point, bottom_right_point)
                self.__win.draw_line(bottom_wall)

            if self.has_left_wall == False:
                left_wall = Line(top_left_point, bottom_left_point)
                self.__win.draw_line(left_wall, "#d9d9d9")

            if self.has_right_wall == False:
                right_wall = Line(top_right_point, bottom_right_point)
                self.__win.draw_line(right_wall, "#d9d9d9")

            if self.has_top_wall == False:
                top_wall = Line(top_left_point, top_right_point)
                self.__win.draw_line(top_wall, "#d9d9d9")

            if self.has_bottom_wall == False:
                bottom_wall = Line(bottom_left_point, bottom_right_point)
                self.__win.draw_line(bottom_wall, "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        x_center_self = ((self.__x2 - self.__x1) / 2) + self.__x1
        y_center_self = ((self.__y2 - self.__y1) / 2) + self.__y1

        x_center_cell = ((to_cell.__x2 - to_cell.__x1) / 2) + to_cell.__x1
        y_center_cell = ((to_cell.__y2 - to_cell.__y1) / 2) + to_cell.__y1

        center_self = Point(x_center_self, y_center_self)
        center_cell = Point(x_center_cell, y_center_cell)

        move_line = Line(center_self, center_cell)
        
        if self.__win != None:
            if undo == False:
                self.__win.draw_line(move_line, fill_color="red")

            else:
                self.__win.draw_line(move_line, fill_color="gray")
