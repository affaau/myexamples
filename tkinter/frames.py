import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Frames")
root.resizable(0,0)

frame1 = tk.Frame(root)
frame1.pack(side='left', fill="both", expand=1)
frame1.config(highlightbackground="gray", highlightthickness=2)
label1_1 = tk.Label(frame1, text="Commands")
label1_1.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
tk.Entry(frame1).grid(row=0, column=1, padx=5)
tk.Label(frame1, text="Contrast").grid(row=1,column=0, sticky=tk.W, padx=5,
         pady=5)
scale_1_start = 0
scale_1_end = 100
scale_1 = tk.Scale(frame1, from_=scale_1_start, to=scale_1_end, 
                   orient=tk. HORIZONTAL, length=120, 
                   tickinterval=(scale_1_end-scale_1_start), cursor='hand2')
scale_1.grid(row=1, column=1, padx=5, sticky=tk.W)

c_width, c_height = 640, 480

def left_click(event):
    global c_txt, canvas
    global img, render, x0, y0, x1, y1

    text = "(x = {}, y = {})".format(event.x, event.y)
    canvas.delete(c_txt)
    c_txt = canvas.create_text(5, 470, anchor=tk.W, font=("Purisa", 8), text=text,
                               fill="yellow")
    canvas.delete(img)
    # Plot image with cursor as the center of image
    img = canvas.create_image(event.x, event.y, image=render)
    x0 = event.x - render.width()//2
    y0 = event.y - render.height()//2
    x1 = x0 + render.width()
    y1 = y0 + render.height()

frame2 = tk.Frame(root)
frame2.pack(side="top", anchor=tk.NE)
canvas = tk.Canvas(frame2, width=c_width, height=c_height, bg="black")
canvas.pack()
canvas.bind('<Button-1>', left_click)

c_txt = canvas.create_text(5, 470, anchor=tk.W, font="Purisa", fill="yellow") 

########
FACTOR = 1.1
scale = 0.5
load = Image.open('lena.jpg')
scaled = load.resize((int(load.size[0]*scale), int(load.size[1]*scale)),
                     Image.ANTIALIAS)
render = ImageTk.PhotoImage(scaled)

# Place image center at the given (loc_x, loc_y)
loc_x, loc_y = c_width//2, c_height//2
img = canvas.create_image(loc_x, loc_y, image=render)

# Top-left corner of image
x0 = loc_x - int(render.width()*scale)
y0 = loc_y - int(render.height()*scale)
# bottom-right corner of image
x1 = x0 + render.width()
y1 = y0 + render.height()


def inside_image(xm, ym):
    global x0, y0, x1, y1
    
    if xm > x0 and xm < x1 and ym > y0 and ym < y1:
        return True
    
    return False
    
    
def zoom(event):
    global canvas, load, render, img, scale, x0, y0, x1, y1
    
    if inside_image(event.x, event.y):
        canvas.delete(img)
        # Zoom in or out 
        # Update ultimate scale and delta x&y
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
     
        # Update x0, y0
        x0 = event.x - delta_x
        y0 = event.y - delta_y
        # Resize & redraw
        scaled_img = load.resize((int(load.size[0]*scale), int(load.size[1]*scale)), 
                                 Image.ANTIALIAS)
        render = ImageTk.PhotoImage(scaled_img)
        img = canvas.create_image(x0, y0, anchor=tk.NW, image=render)
        # Update x1, y1
        x1 = x0 + render.width()
        y1 = y0 + render.height()

canvas.bind('<MouseWheel>', zoom)    

########

frame3 = tk.Frame(root, bg="green")
frame3.pack(fill="both", expand=1)

tk.Button(frame3, text="Click", command=None).grid(row=0, column=0, columnspan=2, 
          padx=2, pady=2)
tk.Button(frame3, text="Reset", command=None).grid(row=1, column=0, padx=2, pady=2)
tk.Button(frame3, text="Save", command=None).grid(row=1, column=1, padx=2, pady=2)

root.mainloop()
