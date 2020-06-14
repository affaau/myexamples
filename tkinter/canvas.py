import tkinter as tk
from PIL import Image, ImageTk

# Set up main window
w_width, w_height = 900, 600
root = tk.Tk()
root.title("GUI")
root.iconbitmap('moveon-logo-512.ico')
# Position the major window
root.geometry('{}x{}+50+50'.format(w_width, w_height))
root.resizable(0, 0)   # not resizable

# Set up canvas 
c_width, c_height = 640, 480
# creating the 'Canvas' area of width and height 500px
canvas = tk.Canvas(root, width = c_width, height = c_height, bg="black")
canvas.pack(side="right", anchor=tk.NE)

FACTOR = 1.05
scale = 0.5
load = Image.open('lena.jpg')
scaled = load.resize((int(load.size[0]*scale), int(load.size[1]*scale)), Image.ANTIALIAS)
render = ImageTk.PhotoImage(scaled)

# Place image center at the given (loc_x, loc_y)
loc_x, loc_y = c_width//2, c_height//2
img = canvas.create_image(loc_x, loc_y, image=render)

# top-left corner of image
x0 = loc_x - int(render.width()*scale)
y0 = loc_y - int(render.height()*scale)
# bottom-right corner of image
x1 = x0 + render.width()
y1 = y0 + render.height()

label_1 = tk.Label(root, text="")
label_1.pack(side="left")

def reposition(event):
    global img, label_1, render, canvas, x0, y0, x1, y1
    label_1.configure(text="({}, {})".format(event.x, event.y))
    canvas.delete(img)
    # plot image with cursor as the center of image
    img = canvas.create_image(event.x, event.y, image=render)
    x0 = event.x - render.width()//2
    y0 = event.y - render.height()//2
    x1 = x0 + render.width()
    y1 = y0 + render.height()

canvas.bind('<Button-1>', reposition)

def inside_image(xm, ym):
    global x0, y0, x1, y1
    if xm>x0 and xm<x1 and ym>y0 and ym<y1:
        return True
    
    return False

def zoom(event):
    global canvas, load, render, img, scale, x0, y0, x1, y1
    if inside_image(event.x, event.y):
        canvas.delete(img)
        # zoom in or out 
        # update ultimate scale and delta x&y
        if event.delta > 0:
            scale *= FACTOR
            delta_x = (event.x - x0)*FACTOR
            delta_y = (event.y - y0)*FACTOR
            print("increase to {}".format(scale))
        else:
            scale /= FACTOR
            delta_x = (event.x - x0)/FACTOR
            delta_y = (event.y - y0)/FACTOR
            print("decrease to {}".format(scale))
     
        # update x0, y0
        x0 = event.x - delta_x
        y0 = event.y - delta_y
        # resize & redraw
        scaled_img = load.resize((int(load.size[0]*scale), int(load.size[1]*scale)), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(scaled_img)
        img = canvas.create_image(x0, y0, anchor=tk.NW, image=render)
        # update x1, y1
        x1 = x0 + render.width()
        y1 = y0 + render.height()

canvas.bind('<MouseWheel>', zoom)

def foo():
    pass 

btn_1 = tk.Button(root, text="Commands", command=foo)
btn_1.pack(side="bottom", padx=5)

root.mainloop()
