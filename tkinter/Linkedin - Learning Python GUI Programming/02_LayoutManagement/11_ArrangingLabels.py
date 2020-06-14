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
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
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

# Using scrolled text control
scrolW = 30
scrolH =  3
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

# Radiobutton Globals
colors = ["Blue", "Gold", "Red"]

# Radiobutton callback
def radCall():
    radSel = radVar.get()
    if   radSel == 0:
        win.configure(background=colors[0])
    elif radSel == 1:
        win.configure(background=colors[1])
    elif radSel == 2:
        win.configure(background=colors[2])

radVar = tk.IntVar()
radVar.set(99)
# Creating 3 radio buttons in a loop
for col in range(3):
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)

# Create a container to hold Labels
labelsFrame = ttk.LabelFrame(win, text=" Labels in a Frame ")
labelsFrame.grid(column=0, row=7)

# Place Labels into the container element
ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(labelsFrame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(labelsFrame, text="Label3").grid(column=2, row=0, sticky=tk.W)

nameEntered.focus()

win.mainloop()
