import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.title("Welcome to edureka!")
# default size of table 'width x height'
window.geometry('350x200')   

# Combobox object to create a list of options
combo = ttk.Combobox(window)
combo['values'] = (1,2,3,4,5,"Text")
combo.current(3)  # set default
combo.grid(column=0, row=0)

window.mainloop()
