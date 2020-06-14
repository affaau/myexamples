from tkinter import *
from PIL import Image, ImageTk
import random
import math

root = Tk()
canvas = Canvas(root)
img = Image.open("../lena.jpg")
background_image=ImageTk.PhotoImage(img)
canvas.imgtk = background_image
canvas.pack(fill=BOTH, expand=1) # Stretch canvas to root window size.
image = canvas.create_image(0, 0, anchor=NW, image=background_image)
#root.wm_geometry("794x370")
root.title('Map')
root.bind('<Escape>', lambda e: root.quit())

def toplevel():
    top = Toplevel()
    top.title('Optimized Map')
    top.wm_geometry("794x370")
    optimized_canvas = Canvas(top)
    optimized_canvas.pack(fill=BOTH, expand=1)
    optimized_image = optimized_canvas.create_image(0, 0, anchor=NW, image=background_image)

toplevel()

root.mainloop()