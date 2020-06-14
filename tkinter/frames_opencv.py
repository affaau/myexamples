import tkinter as tk
from PIL import Image, ImageTk
import cv2

root = tk.Tk()
root.title("Framework")
root.iconbitmap('moveon-logo-512.ico')
root.resizable(0,0)

#################
#### frame 1 ####
#################
# slide bars
# parameters setting
# message display
frame1 = tk.Frame(root)
frame1.pack(side='left', fill="both", expand=1)
frame1.config(highlightbackground="gray", highlightthickness=2)
label1_1 = tk.Label(frame1, text="Commands")
label1_1.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
tk.Entry(frame1).grid(row=0, column=1, padx=5)
tk.Label(frame1, text="Contrast").grid(row=1,column=0, sticky=tk.W, padx=5,
         pady=5)
# Example slide bar
scale_1_start = 0
scale_1_end = 100
scale_1 = tk.Scale(frame1, from_=scale_1_start, to=scale_1_end, 
                   orient=tk. HORIZONTAL, length=120, 
                   tickinterval=(scale_1_end-scale_1_start), cursor='hand2')
scale_1.grid(row=1, column=1, padx=5, sticky=tk.W)

#################
#### frame 2 ####
#################
# canvas
# zoom in/out
# scale display
# movement
# curson location display
c_width, c_height = 640, 480
# Scaling factor per roll of mouse wheel
FACTOR = 1.1
# Store the actual scale of image
scale = 0.5
# Flag to indicate if image should be moved
ready_to_move = False
# Relative positions between cursor coord wrt 
# top-left corner coord of image
rel_x, rel_y = 0, 0


def _inside_image(xm, ym):
    '''Check if cursor is clicked within the image area
    '''
    global x0, y0, x1, y1
    
    if xm > x0 and xm < x1 and ym > y0 and ym < y1:
        return True
    
    return False


def _left_click(xm, ym):
    '''Show coordinates of cursor when left click
    '''
    global cursor_coord, canvas

    text = "(x = {}, y = {})".format(xm, ym)
    canvas.delete(cursor_coord)
    cursor_coord = canvas.create_text(5, 470, anchor=tk.W, font=("Purisa", 8),
                                      text=text, fill="yellow")


def prepare_move(event):
    '''When left button is pressed, prepare if moving image is allowed
    '''
    global ready_to_move, rel_x, rel_y, x0, y0
    
    if _inside_image(event.x, event.y):
        ready_to_move = True
        rel_x = event.x - x0
        rel_y = event.y - y0
    else:
        ready_to_move = False
    
    _left_click(event.x, event.y)


def moving(event):
    '''Move image with the cursor if cursor is within the image area
    '''
    global canvas, render, img, x0, y0, rel_x, rel_y
    global ready_to_move
    
    if ready_to_move:
        x0 = event.x - rel_x
        y0 = event.y - rel_y
        canvas.delete(img)
        img = canvas.create_image(x0, y0, anchor=tk.NW, image=render)

    _left_click(event.x, event.y)


def release(event):
    '''Take down the latest image location
    '''
    global x0, y0, x1, y1, render, ready_to_move
    
    if ready_to_move:
        x1 = x0 + render.width()
        y1 = y0 + render.height()


def zoom(event):
    '''Dynamically change the size of image
    Roll forward to zoom in, roll backward to zoom out
    Update the image location after scaling
    '''
    global canvas, cvtRGB, render, img, scale, x0, y0, x1, y1
    global scale_display
    
    if _inside_image(event.x, event.y):
        canvas.delete(img)
        # Zoom in or out 
        # Update ultimate scale and delta x&y
        if event.delta > 0:
            scale *= FACTOR
            delta_x = (event.x - x0)*FACTOR
            delta_y = (event.y - y0)*FACTOR
        else:
            scale /= FACTOR
            delta_x = (event.x - x0)/FACTOR
            delta_y = (event.y - y0)/FACTOR
    
        # Update x0, y0
        x0 = event.x - delta_x
        y0 = event.y - delta_y
        # Resize & redraw
        scaled = cv2.resize(cvtRGB, (int(WIDTH*scale),int(HEIGHT*scale)))
        render = ImageTk.PhotoImage(Image.fromarray(scaled))
        img = canvas.create_image(x0, y0, anchor=tk.NW, image=render)
        # Update x1, y1
        x1 = x0 + scaled.shape[1]
        y1 = y0 + scaled.shape[0]
        
        text = "(scale: {:.2f} %)".format(scale*100)
        canvas.delete(scale_display)
        scale_display = canvas.create_text(550, 470, anchor=tk.W, 
                                           font=("Purisa", 8),
                                           text=text, fill="green")

frame2 = tk.Frame(root)
frame2.pack(side="top", anchor=tk.NE)
canvas = tk.Canvas(frame2, width=c_width, height=c_height, bg="black")
canvas.pack()

#### load and display image ####
load = cv2.imread('lena.jpg')
cvtRGB = cv2.cvtColor(load, cv2.COLOR_BGR2RGB)
HEIGHT, WIDTH = cvtRGB.shape[0:2]
# Half the size
scaled = cv2.resize(cvtRGB, (int(WIDTH*scale),int(HEIGHT*scale)))
render = ImageTk.PhotoImage(Image.fromarray(scaled))
# Place image center at the given (loc_x, loc_y)
loc_x, loc_y = c_width//2, c_height//2
img = canvas.create_image(loc_x, loc_y, image=render)
# Top-left corner of image
x0 = loc_x - int(scaled.shape[1]//2)
y0 = loc_y - int(scaled.shape[0]//2)
# bottom-right corner of image
x1 = x0 + scaled.shape[1]
y1 = y0 + scaled.shape[0]

canvas.bind('<MouseWheel>', zoom)  
canvas.bind('<ButtonPress-1>', prepare_move)
canvas.bind('<B1-Motion>', moving)
canvas.bind('<ButtonRelease-1>', release)
cursor_coord = canvas.create_text(5, 470, anchor=tk.W, font=("Purisa", 8),
                                  fill="yellow")
scale_display = canvas.create_text(550, 470, anchor=tk.W, font=("Purisa", 8),
                                   fill="green")

#################
#### frame 3 ####
#################
# function commands
# save image
# exit
frame3 = tk.Frame(root, bg="green")
frame3.pack(fill="both", expand=1)
# Examples buttons
tk.Button(frame3, text="Click", command=None).grid(row=0, column=0, columnspan=2, 
          padx=2, pady=2)
tk.Button(frame3, text="Reset", command=None).grid(row=1, column=0, padx=2, pady=2)
tk.Button(frame3, text="Save", command=None).grid(row=1, column=1, padx=2, pady=2)

##################
#### Menu bar ####
##################
menubar = tk.Menu(root)
root.configure(menu=menubar)

fileMenu = tk.Menu(menubar)
fileMenu.add_command(label="Control", command=None)
fileMenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=fileMenu)

helpMenu = tk.Menu(menubar)
helpMenu.add_command(label="About", command=None)
menubar.add_cascade(label="Help", menu=helpMenu)


root.mainloop()
