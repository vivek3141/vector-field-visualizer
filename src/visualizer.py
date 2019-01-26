from math import *  # This import statement allows for all other functions like log(x), sin(x), etc.
import numpy as np
import math
import matplotlib.pyplot as plt


class Visualizer:
    def __init__(self, f_x, f_y):
        # List of all colors
        self.color_list = ['#e22b2b', '#e88e10', '#eae600', '#88ea00',
                           '#00eae2', '#0094ea', "#2700ea", '#bf00ea', '#ea0078']

        # Create the functions
        self.fx = eval("lambda x,y: " + f_x)
        self.fy = eval("lambda x,y: " + f_y)

    def div(self, x, y, d=0.0001):
        return round(((self.fx(x + d, y) - self.fx(x, y)) / d) + ((self.fy(x, y + d) - self.fy(x, y)) / d), 3)

    def curl(self, x, y, d=0.0001):
        return round(((self.fy(x + d, y) - self.fy(x, y)) / d) - ((self.fx(x, y + d) - self.fx(x, y)) / d), 3)

    def plot(self, bound=(-10, 10), skip=1):
        c = "#0F0F0F"
        space = np.append(np.arange(bound[0], bound[1], skip), [bound[1]])
        head_size = (math.fabs(bound[0]) + math.fabs(bound[1])) / 40
        for y in space:
            for x in space:
                plt.scatter([x], [y], c=c, s=[5 / head_size])
                plt.arrow(x, y, self.fx(x, y), self.fy(x, y),
                          head_width=head_size, head_length=head_size, color=c)
        return plt

    def plot_color(self, bound=(-10, 10), skip=1, prop=0):
        head_size = (math.fabs(bound[0]) + math.fabs(bound[1])) / 40  # calculate head size in proportion to bounds
        space = np.append(np.arange(bound[0], bound[1], skip), [bound[1]])  # All points to place vectors on

        # Loops
        for y in space:
            for x in space:
                v = int(math.sqrt(x ** 2 + y ** 2) / 10 ** prop)  # select color based on magnitude

                index = len(self.color_list) - 1 if v > len(self.color_list) - 1 else v  # prevent IndexError
                c = self.color_list[index]  # Choose color from list

                try:
                    # Use functions passed to calculate X and Y components
                    x_val = float(self.fx(float(x), float(y)))
                    y_val = float(self.fy(float(x), float(y)))

                # Make sure no Math Domain Error occurs, Eg. log(x)
                except ValueError:
                    plt.scatter([x], [y], c="WHITE",
                                s=[5 / head_size])  # Make sure that it's not stretched by missing points
                    continue

                # Place the beginning dot of the arrow
                plt.scatter([x], [y], c=c, s=[5 / head_size])

                try:
                    # Calculate angle; magnitude is always 1
                    angle = math.atan(y_val / x_val) if x_val > 0 else (math.atan(y_val / x_val) + math.pi)
                    plt.arrow(x, y, math.cos(angle), math.sin(angle),
                              head_width=head_size, head_length=head_size, color=c)  # place the arrow

                # If the angle is 0, use the X and Y components to make unit vector
                except ZeroDivisionError:
                    try:
                        plt.arrow(x, y, 0, y_val / math.fabs(y_val), head_width=head_size, head_length=head_size,
                                  color=c)

                    # If magnitude is 0, then it's a point
                    except ZeroDivisionError:
                        plt.scatter([x], [y], color=c, s=[10])
        return plt
