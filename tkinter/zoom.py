import tkinter as tk
from PIL import Image, ImageTk

WIDTH, HEIGHT = 640, 480
loc_x, loc_y = 200, 200
center_x, center_y = WIDTH//2, HEIGHT//2

zoom_factor = {'in':1.2, 'out':0.8}
zoom_index = 'in'    # default is zoom-in

root = tk.Tk()
profile = "{}x{}+{}+{}".format(WIDTH, HEIGHT, loc_x, loc_y)
root.geometry(profile)
root.config(bg="black")
root.resizable(0, 0)  # Don't allow resize

def fit_window(w, h):
    '''Return a scaled factor that fit image with window'''
    if w/WIDTH > h/HEIGHT:
        return WIDTH/w
    else:
        return HEIGHT/h

load = Image.open(r'lena.jpg')
# load.size => (width, height)

# Fit the loaded image to root window
ratio = fit_window(*load.size)
new_w, new_h = int(load.size[0]*ratio), int(load.size[1]*ratio)
scaled = load.resize((new_w, new_h), Image.ANTIALIAS)

render = ImageTk.PhotoImage(scaled)
imgLabel = tk.Label(root, image=render)
imgLabel.config(borderwidth=0)
imgLabel.image = render
imgLabel.place(x=center_x - new_w//2, y=center_y - new_h//2)

def next_draw():
    global load, new_w, new_h, imgLabel, center_x, center_y
    scaled = load.resize((new_w, new_h), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(scaled)
    imgLabel.config(image=render)
    imgLabel.image = render
    # If image is smaller than display frame,
    # always centralize it in the center
    imgLabel.place(x=center_x - new_w//2, y=center_y - new_h//2)

def left_click(event):
    '''Change ROI and redraw image'''
    global center_x, center_y
    center_x, center_y = event.x, event.y
    print("({} , {})".format(center_x, center_y))
    # ROI of image

    ###
    ##    TO BE CONTINUE
    ###


def right_click(event):
    '''Zoom in/out and redraw image'''
    global center_x, center_y, new_w, new_h
    center_x, center_y = event.x, event.y
    factor = zoom_factor[zoom_index]
    # New size of image
    new_w, new_h = int(new_w*factor), int(new_h*factor)
    # ROI of image

    ###
    ##    TO BE CONTINUE
    ###

root.bind('<Button-1>', left_click)
root.bind('<Button-3>', right_click)

root.after(1000, next_draw)    # in millisec
root.mainloop()
