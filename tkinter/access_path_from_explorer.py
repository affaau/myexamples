from tkinter.filedialog import askopenfilename, askdirectory
import tkinter

root = tkinter.Tk()

# Hide the root 'empty' window
root.withdraw()

# Make use of this function to get full path name of file
f_name = askopenfilename()
print(f_name)

# Make use of this function to get full directory path name
d_path = askdirectory()
print(d_path)


# root.quit() causes mainloop to exit. The interpreter is still intact,
# as are all the widgets. If you call this function, you can have code
# that executes after the call to root.mainloop(), and that code can interact
# with the widgets (for example, get a value from an entry widget).

# root.quit()

# Calling root.destroy() will destroy all the widgets and exit mainloop.
# Any code after the call to root.mainloop() will run, but any attempt to
# access any widgets (for example, get a value from an entry widget) will
# fail because the widget no longer exists.
root.destroy()
print('root is: {}, {}'.format(root, type(root)))
