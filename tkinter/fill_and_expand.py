'''
The fill option tells the manager that the widget wants fill the entire space
assigned to it. The value controls how to fill the space; BOTH means that the
widget should expand both horisontally and vertically, X means that it should
expand only horisontally, and Y means that it should expand only vertically.

The expand option tells the manager to assign additional space to the widget
box. If the parent widget is made larger than necessary to hold all packed
widgets, any exceeding space will be distributed among all widgets that have
the expand option set to a non-zero value.

So fill tells the widget to grow to as much space is available for it in the
direction specified, expand tells the master to take any space that is not
assigned to any widget and distribute it to all widgets that have a non-zero
expand value.
'''
import tkinter as tk

root = tk.Tk()
root.geometry('200x200+200+200')

# The label with expand=1 gets assigned as much space as
# available for it, but only occupies it in the direction specified, Y. The
# label with fill=tk.BOTH expands in both directions, but has less space 
# available.
tk.Label(root, text='Label', bg='green').pack(expand=1, fill=tk.Y)
tk.Label(root, text='Label2', bg='red').pack(fill=tk.BOTH)  
# what happen if expand=1 for Label2?

root.mainloop()