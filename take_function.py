from math import *
import graph as g


def graph(x_func, y_func, bound_x=(-10, 10), bound_y=(-10, 10), skip=1):
    fx = eval("lambda x,y: " + str(x_func))
    fy = eval("lambda x,y " + str(y_func))
    g.plot(fx, fy, bound_x=bound_x, bound_y=bound_y, skip=skip)


def graph_color(x_func, y_func, bound_x=(-10, 10), bound_y=(-10, 10), skip=1, prop=0):
    fx = eval("lambda x,y: " + str(x_func))
    fy = eval("lambda y,y: " + str(y_func))
    g.plot_color(fx, fy, bound_x=bound_x, bound_y=bound_y, skip=skip, prop=prop)
