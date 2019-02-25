import tkinter

window = tkinter.Tk()
window.title("Welcome to edureka!")
# default size of table 'width x height'
window.geometry('350x200')   

l1 = tkinter.Label(window, text="edureka!", font=("Arial Bold", 50))
l1.grid(column=0, row=0)

window.mainloop()
