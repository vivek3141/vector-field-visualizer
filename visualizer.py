from math import *
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

    def plot(self, bound_x=(-10, 10), bound_y=(-10, 10), skip=1, head_size=0.5):
        c = "#0F0F0F"
        for y in range(bound_y[0] - 1, bound_y[1] + 1, skip):
            for x in range(bound_x[0] - 1, bound_y[1] + 1, skip):
                plt.scatter([x], [y], c=c, s=[10])
                plt.arrow(x, y, self.fx(x, y), self.fy(x, y),
                          head_width=head_size, head_length=head_size, color=c)
        plt.savefig("vector_field.jpg")
        plt.show()

    def plot_color(self, bound_x=(-10, 10), bound_y=(-10, 10), skip=1, prop=0, head_size=0.5):
        for y in range(bound_y[0] - 1, bound_y[1] + 1, skip):
            for x in range(bound_x[0] - 1, bound_y[1] + 1, skip):
                v = int(math.sqrt(x ** 2 + y ** 2) / 10 ** prop)
                index = len(self.color_list) - 1 if v > len(self.color_list) - 1 else v
                c = self.color_list[index]
                plt.scatter([x], [y], c=c, s=[10])
                x_val = self.fx(x, y)
                y_val = self.fy(x, y)
                try:
                    angle = math.atan(y_val / x_val) if x_val > 0 else (math.atan(y_val / x_val) + math.pi)
                except ZeroDivisionError:
                    angle = 0

                plt.arrow(x, y, math.cos(angle), math.sin(angle),
                          head_width=head_size, head_length=head_size, color=c)
        plt.savefig("vector_field.jpg")
        plt.show()
