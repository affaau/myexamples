import tkinter

window = tkinter.Tk()
window.title("Welcome to edureka!")
# default size of table 'width x height'
window.geometry('350x200')   
l1 = tkinter.Label(window, text="edureka!")
l1.grid(column=0, row=0)

# create Entry object
txt = tkinter.Entry(window, width=10)
txt.grid(column=1, row=0)

def clicked():
	res = "Welcome to " + txt.get()
	l1.configure(text=res)

# create button object & click event
bt = tkinter.Button(window, text='Enter', command=clicked)
bt.grid(column=2, row=0)

window.mainloop()
