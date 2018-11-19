import matplotlib.pyplot as plt
import math

color_list = ['#e22b2b', '#e88e10', '#eae600', '#88ea00',
              '#00eae2', '#0094ea', "#2700ea", '#bf00ea', '#ea0078']


def plot(fx, fy, bound_x=(-10, 10), bound_y=(-10, 10), skip=1, head_size=0.5):
    c = "#0F0F0F"
    for y in range(bound_y[0] - 1, bound_y[1] + 1, skip):
        for x in range(bound_x[0] - 1, bound_y[1] + 1, skip):
            plt.scatter([x], [y], c=c, s=[10])
            plt.arrow(x, y, fx(x, y), fy(x, y),
                      head_width=head_size, head_length=head_size, color=c)
    plt.savefig("vector_field.jpg")
    plt.show()


def plot_color(fx, fy, bound_x=(-10, 10), bound_y=(-10, 10), skip=1, prop=0, head_size=0.5):
    for y in range(bound_y[0] - 1, bound_y[1] + 1, skip):
        for x in range(bound_x[0] - 1, bound_y[1] + 1, skip):
            v = int(math.sqrt(x ** 2 + y ** 2) / 10 ** prop)
            index = len(color_list) - 1 if v > len(color_list) - 1 else v
            c = color_list[index]
            plt.scatter([x], [y], c=c, s=[10])
            x_val = fx(x, y)
            y_val = fy(x, y)
            try:
                angle = math.atan(y_val / x_val) if x_val > 0 else (math.atan(y_val / x_val) + math.pi)
            except ZeroDivisionError:
                angle = 0

            plt.arrow(x, y, math.cos(angle), math.sin(angle),
                      head_width=head_size, head_length=head_size, color=c)
    plt.savefig("vector_field.png")
    plt.show()
