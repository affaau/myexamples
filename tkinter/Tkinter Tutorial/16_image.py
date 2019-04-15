import tkinter

window = tkinter.Tk()
window.title("GUI")
window.geometry('600x200') 

# taking image from the directory and storing the source in a variable
icon = tkinter.PhotoImage(file = "edureka.png")
# displaying the picture using a 'Label' by passing the 'picture' variable to 'image' parameter
label = tkinter.Label(window, image = icon)
label.pack()

window.mainloop()
