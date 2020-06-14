# Tested in Python 3.7.3
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")
#win.resizable(0, 0)

# A label within the body
ttk.Label(win, text="A Label").grid(column=0, row=0)

# Window will optimize and adjust the size accordingly
win.mainloop()
