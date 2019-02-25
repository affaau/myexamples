from collections import deque
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import FuncFormatter

'''
real time graph reference:
https://stackoverflow.com/questions/49405499/real-time-matplotlib-plotting

Additional:
https://docs.python.org/3.6/library/collections.html#collections.deque

deque() example
>>> import collections
>>> data = collections.deque(np.array([1,2,3,4]), 5)
>>> data
deque([1, 2, 3, 4], maxlen=5)
>>> data.append(6)
>>> data
deque([1, 2, 3, 4, 6], maxlen=5)
>>> data.append(7)
>>> data
deque([2, 3, 4, 6, 7], maxlen=5)
'''

def init():
    line.set_ydata([np.nan] * len(x))
    return line,

def animate(i):
    # Add next value
    data.append(np.random.randint(0, max_rand))
    line.set_ydata(data)  
    #plt.savefig('C:\\Users\\baba\\fig_{:02}'.format(i))
    print(i)   # debug use
    return line,

max_x = 10
max_rand = 5

data = deque(np.zeros(max_x), maxlen=max_x)  # hold the last 10 values

#  The x axis is just a range here, it can be anything you want.
#x = np.arange(max_x-1, -1, -1)  # reverse direction of moving
x = np.arange(0, max_x)

fig, ax = plt.subplots()

ax.set_ylim(0, max_rand)
ax.set_xlim(0, max_x-1)
line, = ax.plot(x, np.random.randint(0, max_rand, max_x))
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: '{:.0f}s'.format(max_x - x - 1)))
plt.xlabel('Seconds ago')

ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=500, blit=True, save_count=10)

plt.show()
