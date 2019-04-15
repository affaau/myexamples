import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title("Welcome to edureka!")
# default size of table 'width x height'
window.geometry('350x200')   

# create message box & yes-no question box
def clicked():
	tkinter.messagebox.showinfo('Message title', 'Message content')
	# question box will pop up after exiting the message box above!
	answer = tkinter.messagebox.askquestion('Quiz', 'Do you like Python?')
	if answer == 'yes':
		print("That's the right choice!")
	else:
		print('You better think twice.')

btn = tk.Button(window, text='Click here', command=clicked)
btn.grid(column=0, row=0)

window.mainloop()
