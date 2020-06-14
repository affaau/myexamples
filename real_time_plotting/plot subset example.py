import matplotlib.pyplot as plt


def get_start_end_from_cmd_line():   # substitute for your own function
    return 5, 9

def load_data():                     # substitute for your own function
    x, y = (list(range(3, 13)), list(range(10)))
    return x, y

xdata, ydata = load_data()
start, end = get_start_end_from_cmd_line()
subsetx, subsety = xdata[start: end], ydata[start: end]   # slice both the x and the corresponding y
plt.plot(subsetx, subsety, label="P1")
plt.show()