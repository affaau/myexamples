import tkinter

window = tkinter.Tk()
window.title("GUI")
window.geometry('350x200') 

# binding function to events

# mouse buttons
#    <Button-1> for left click
#    <Button-2> for middle click
#    <Button-3> for right click

# creating 3 different functions for 3 events
def left_click(event):
    tkinter.Label(window, text = "Left Click!").pack()

def middle_click(event):
    tkinter.Label(window, text = "Middle Click!").pack()

def right_click(event):
    tkinter.Label(window, text = "Right Click!").pack()

btn = tkinter.Button(window, text = "Click Me!")
# 'bind' takes 2 parameters 1st is 'event' 2nd is 'function'
btn.bind("<Button-1>", left_click)
btn.bind("<Button-2>", middle_click)
btn.bind("<Button-3>", right_click)

btn.pack()

window.mainloop()
