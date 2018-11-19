from math import *


def div(fx, fy, x, y, d=0.0001):
    f_x = eval("lambda x,y: " + str(fx))
    f_y = eval("lambda x,y: " + str(fy))
    return round(((f_x(x + d, y) - f_x(x, y)) / d) + ((f_y(x, y + d) - f_y(x, y)) / d), 3)


def curl(fx, fy, x, y, d=0.0001):
    f_x = eval("lambda x,y: " + str(fx))
    f_y = eval("lambda x,y: " + str(fy))
    return round(((f_y(x + d, y) - f_y(x, y)) / d) - ((f_x(x, y + d) - f_x(x, y)) / d), 3)
