# Tested in Python 3.7.3
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")
#win.resizable(0, 0)

# Button click event (callback) function
def clickMe():
    action.configure(text="Hello " + name.get())

ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

name = tk.StringVar()
# Text enrty Widget, hard coded to a width of 12
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

# Adding a button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=1, row=1)
# Disable the button function
action.configure(state='disabled')

# Set the focus point at name entry
# Placing the cursor into it when program starts
nameEntered.focus()

win.mainloop()
