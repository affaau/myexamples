import numpy as np
import matplotlib.pyplot as plt

# Initialize
x_axis_start = 0
x_axis_end = 10

plt.axis([x_axis_start, x_axis_end, 0, 1])
plt.ion()

# Realtime plot
for i in range(100):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.50)

    if i%10 == 0 and i>1:
        x_axis_start += 10
        x_axis_end += 10
        plt.axis([x_axis_start, x_axis_end, 0, 1])