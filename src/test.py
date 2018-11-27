from visualizer import Visualizer

v = Visualizer("x*y+1", "y+x")
plt = v.plot_color(skip=2)
plt.show()
