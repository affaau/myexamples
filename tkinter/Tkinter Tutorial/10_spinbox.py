import tkinter as tk

window = tk.Tk()
window.title("Welcome to edureka!")
# default size of table 'width x height'
window.geometry('350x200')   

# spinbox
spin = tk.Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=0, row=0)

window.mainloop()
