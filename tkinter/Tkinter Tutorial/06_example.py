import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.title("Welcome to edureka!")
# default size of table 'width x height'
window.geometry('350x200')   

# Checkbutton object
chk_state = tk.BooleanVar()
chk_state.set(True)   # default as checked
chk = tk.Checkbutton(window, text='Select', var=chk_state)
chk.grid(column=0, row=0)

window.mainloop()
