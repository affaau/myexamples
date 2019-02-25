import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], ' o', lw=2)
g = 9.81
h = 2
tc = 200
xs = [1] # the vertical position is fixed on x-axis
ys = [h, h]


# animation function.  This is called sequentially
def animate(y):
    ys[-1] = y
    line.set_data(xs, ys)
    return line,

def get_y():
  for step in range(tc):
    t = step / 100.0
    y = -0.5*g*t**2 + h  # the equation of diver's displacement on y axis
    yield y

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, frames=get_y, interval=100)

plt.show()