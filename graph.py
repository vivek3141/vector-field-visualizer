import matplotlib.pyplot as plt


def plot(fx, fy, boundx=[-10, 10], boundy=[-10, 10]):
    plt.axes()
    plt.arrow(0, 0, 0.5, 0.5, head_width=0, head_length=0, fc='k', ec='k')
    plt.show()
