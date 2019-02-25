import tkinter

window = tkinter.Tk()
window.title("GUI")
window.geometry('350x200')  

# organizing layouts and widgets
# creating 2 frames TOP and BOTTOM
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")

# now, create some widgets in the top_frame and bottom_frame
# 'fg - foreground' is used to color the contents
# 'text' is used to write the text on the Button
btn1 = tkinter.Button(top_frame, text = "Button1", fg = "red").pack()
btn2 = tkinter.Button(top_frame, text = "Button2", fg = "green").pack()
# 'side' is used to align the widgets
btn4 = tkinter.Button(bottom_frame, text = "Button4", fg = "orange").pack(side = "left")
btn3 = tkinter.Button(bottom_frame, text = "Button3", fg = "purple").pack(side = "left")

window.mainloop()
