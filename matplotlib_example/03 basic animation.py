'''
Ref: http://www.riptutorial.com/matplotlib/example/23558/basic-animation-with-funcanimation

Ref:
http://devosoft.org/making-efficient-animations-in-matplotlib-with-blitting/

'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

TWOPI = 2*np.pi

fig, ax = plt.subplots()

t = np.arange(0.0, TWOPI, 0.001)
s = np.sin(t)
l = plt.plot(t, s)

ax = plt.axis([0,TWOPI,-1,1])    # [x_min, x_max, y_min, y_max]

redDot, = plt.plot([0], [np.sin(0)], 'ro')

def animate(i):
    redDot.set_data(i, np.sin(i))
    return redDot,

# FuncAnimation creates animation by keep calling the animate() function
# update interval is in millisec
# every step 0.1
# set 'blit' to optimize drawing
#    If you aren’t using blitting, this function generates each one of your 
#    frames from scratch. In most cases, frames aren’t 100% different from 
#    each otherBlitting takes advantage of this by just changing the plot 
#    elements that need to be changed.
myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(0.0, TWOPI,\
                        0.1), interval=500, blit=True, repeat=True)    

plt.show()