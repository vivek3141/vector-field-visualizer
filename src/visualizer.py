from math import *
import numpy as np
import math
import matplotlib.pyplot as plt


class Visualizer:
    def __init__(self, f_x, f_y):
        self.color_list = ['#e22b2b', '#e88e10', '#eae600', '#88ea00',
                           '#00eae2', '#0094ea', "#2700ea", '#bf00ea', '#ea0078']
        self.fx = eval("lambda x,y: " + str(f_x))
        self.fy = eval("lambda x,y: " + str(f_y))

    def div(self, x, y, d=0.0001):
        return round(((self.fx(x + d, y) - self.fx(x, y)) / d) + ((self.fy(x, y + d) - self.fy(x, y)) / d), 3)

    def curl(self, x, y, d=0.0001):
        return round(((self.fy(x + d, y) - self.fy(x, y)) / d) - ((self.fx(x, y + d) - self.fx(x, y)) / d), 3)

    def plot(self, bound=(-10, 10), skip=1):
        c = "#0F0F0F"
        space = np.append(np.arange(bound[0], bound[1], skip), [bound[1]])
        head_size = (math.fabs(bound[0]) + math.fabs(bound[1]))/40
        for y in space:
            for x in space:
                plt.scatter([x], [y], c=c, s=[5/head_size])
                plt.arrow(x, y, self.fx(x, y), self.fy(x, y),
                          head_width=head_size, head_length=head_size, color=c)
        return plt

    def plot_color(self, bound=(-10, 10), skip=1, prop=0):
        head_size = (math.fabs(bound[0]) + math.fabs(bound[1])) / 40
        space = np.append(np.arange(bound[0], bound[1], skip), [bound[1]])
        for y in space:
            for x in space:
                v = int(math.sqrt(x ** 2 + y ** 2) / 10 ** prop)
                index = len(self.color_list) - 1 if v > len(self.color_list) - 1 else v
                c = self.color_list[index]
                plt.scatter([x], [y], c=c, s=[5/head_size])
                x_val = float(self.fx(float(x), float(y)))
                y_val = float(self.fy(float(x), float(y)))
                try:
                    angle = math.atan(y_val / x_val) if x_val > 0 else (math.atan(y_val / x_val) + math.pi)
                    plt.arrow(x, y, math.cos(angle), math.sin(angle),
                              head_width=head_size, head_length=head_size, color=c)
                except ZeroDivisionError:
                    try:
                        plt.arrow(x, y, 0, y_val/math.fabs(y_val), head_width=head_size, head_length=head_size,
                                  color=c)
                    except ZeroDivisionError:
                        plt.scatter([x], [y], color=c, s=[10])
        return plt
