# Tested in Python 3.7.3
import tkinter as tk

win = tk.Tk()
win.title("Python GUI")
#
# (width, height) - default is resizable
# - 1/True resizeable
# - 0/False non-resizable
#win.resizable(0, 0)  # non-resizeable
win.resizable(1, 0)  # width resizable only
#

win.mainloop()
