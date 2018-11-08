import matplotlib.pyplot as plt


def plot(fx, fy, boundx=[-10, 10], boundy=[-10, 10], skip=1):
    for y in range(boundy[0] - 1, boundy[1] + 1, skip):
        for x in range(boundx[0] - 1, boundy[1] + 1, skip):
            print(x, y)
            plt.scatter([x], [y], c='black', s=[10])
            plt.arrow(x, y, fx(x, y), fy(x, y),
                      head_width=0.5, head_length=0.5, fc='k', ec='k')
    plt.show()


def Fx(x, y):
    return 1


def Fy(x, y):
    return 1


plot(Fx, Fy, skip=2)
