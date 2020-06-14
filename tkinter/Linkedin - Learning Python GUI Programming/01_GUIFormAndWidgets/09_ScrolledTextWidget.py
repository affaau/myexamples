# Tested in Python 3.7.3
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title("Python GUI")
#win.resizable(0, 0)

# Button click event (callback) function
def clickMe():
    action.configure(text="Hello " + name.get() + " " + number.get())

ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

name = tk.StringVar()
# Text enrty Widget, hard coded to a width of 12
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

# Adding a button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)

ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
# Set up a combobox, selection choices and default visible value
# By default, the value in combobox can be changed!
# Option to make it READ ONLY
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
# Althought the values are numbers, # they are converted to string
# as 'number' is defined as string
numberChosen['values'] = (1,2,4,42,100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)  # index number

# Create 3 checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check1 = tk.Checkbutton(win, text="Unchecked", variable=chVarUn)
check1.deselect()
check1.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check1 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check1.select()
check1.grid(column=2, row=4, sticky=tk.W)

# Radiobutton Globals
COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

# Radiobutton callback
def radCall():
    radSel = radVar.get()
    if   radSel == 1:
        win.configure(background=COLOR1)
    elif radSel == 2:
        win.configure(background=COLOR2)
    elif radSel == 3:
        win.configure(background=COLOR3)

# Create 3 Radiobuttons
radVar = tk.IntVar()
rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=5, sticky=tk.W)

rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=5, sticky=tk.W)

rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=5, sticky=tk.W)

# Using scrolled text control
scrolW = 30
scrolH =  3
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

nameEntered.focus()

win.mainloop()
