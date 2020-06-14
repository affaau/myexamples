# Tested in Python 3.7.3
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title("Python GUI")
#win.resizable(0, 0)

monty = ttk.LabelFrame(win, text=" Monty Python ")
monty.grid(column=0, row=0)

# Button click event (callback) function
def clickMe():
    action.configure(text="Hello " + name.get() + " " + number.get())

ttk.Label(monty, text="Enter a name:").grid(column=0, row=0, sticky="W")
name = tk.StringVar()
# Text enrty Widget, hard coded to a width of 12
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky=tk.W)
# Other options like sticky=(tk.W, tk.S, ..)

# Adding a button
action = ttk.Button(monty, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)

ttk.Label(monty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
# Set up a combobox, selection choices and default visible value
numberChosen = ttk.Combobox(monty, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1,2,4,42,100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)  # index number

# Create 3 checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(monty, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check1 = tk.Checkbutton(monty, text="Unchecked", variable=chVarUn)
check1.deselect()
check1.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check1 = tk.Checkbutton(monty, text="Toggle", variable=chVarEn)
check1.deselect()
check1.grid(column=2, row=4, sticky=tk.W)

# Using scrolled text control
scrolW = 30
scrolH =  3
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, sticky='WE', columnspan=3)

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
    curRad = tk.Radiobutton(monty, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)

# Create a container to hold Labels
labelsFrame = ttk.LabelFrame(monty, text=" Labels in a Frame ")
# Add padding to the Frame
labelsFrame.grid(column=0, row=7, padx=20, pady=40)

# Place Labels into the container element
ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
ttk.Label(labelsFrame, text="Label3").grid(column=0, row=2)

# A way to add pad to every child under a Frame
for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)

nameEntered.focus()

win.mainloop()
