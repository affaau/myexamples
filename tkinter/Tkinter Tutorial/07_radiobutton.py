import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.title("Welcome to edureka!")
# default size of table 'width x height'
window.geometry('350x200')   

# Radio button object
# common variable to keep selected value
selection = tk.IntVar()

def selected():
	choices = ['Python', 'Java', 'Scala']
	label.configure(text='{} is selected.'.format(choices[selection.get()]))

rad1 = tk.Radiobutton(window, text='Python', value=0, var=selection, command=selected)
rad2 = tk.Radiobutton(window, text='Java', value=1, var=selection, command=selected)
rad3 = tk.Radiobutton(window, text='Scala', value=2, var=selection, command=selected)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
rad2.select()   # default selection

# label to display selection
label = tk.Label(window, text='')
label.grid(column=0, row=1)
selected()

window.mainloop()
