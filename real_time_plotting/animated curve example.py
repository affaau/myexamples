import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import collections

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

numpoints = 20
n = list(range(numpoints))
y = [np.sin(2*np.pi*i/numpoints) for i in n]
data = collections.deque(y, maxlen=20)
start = time.time()

def animate(i):
    global start
    current = time.time()
    print(current - start)
    start = current
    leftmost = data.popleft()
    data.append(leftmost)
    line.set_ydata(data)
    return line,

line, = ax.plot(n, y)
ani = animation.FuncAnimation(fig, animate, interval = 50)
plt.show()