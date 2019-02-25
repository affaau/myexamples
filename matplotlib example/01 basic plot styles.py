import matplotlib.pyplot as plt
'''Basic plot using different styles

ref: http://www.riptutorial.com/matplotlib/topic/881/getting-started-with-matplotlib
'''

import numpy as np

t = np.arange(0, 2, 0.01)  # from 0, step +0.01, excluding 2
y = np.sin(4 * np.pi * t)  # 2 Hz

# Imperative syntax
plt.figure(1)
plt.clf()                  # clear current figure
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.title('Sine Wave')
plt.grid(True)

# Object oriented syntax
# Explicit is better than implicit, this is a preferred python way
fig = plt.figure(2)
fig.clf()
ax = fig.add_subplot(1,1,1)
ax.plot(t, y)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude (V)')
ax.set_title('Sine Wave')
ax.grid(True)

plt.show()