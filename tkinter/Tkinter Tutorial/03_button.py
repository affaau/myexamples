import tkinter

window = tkinter.Tk()
window.title("Welcome to edureka!")
# default size of table 'width x height'
window.geometry('350x200')   
l1 = tkinter.Label(window, text="edureka!")
l1.grid(column=0, row=0)

def clicked():
	l1.configure(text='Button was clicked!!')

# create Button object & click event
bt = tkinter.Button(window, text='Enter', bg='orange', fg='red',
					command=clicked)
bt.grid(column=1, row=0)

window.mainloop()
