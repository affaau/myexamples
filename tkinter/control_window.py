import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np

# Main window setup
root = tk.Tk()
root.iconbitmap('moveon-logo-512.ico')
root.title('Main Window')
root.bind('<Escape>', lambda e:root.destroy())
root.geometry('640x480+200+100')

# OpenCV setup
width, height = 640, 480
version = cv2.__version__.split('.')
if int(version[0]) < 4:
    cap = cv2.VideoCapture(0)
else:
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

ctl = None
## Control Panel setup
# Callback functions
def brt_action(value):
    global cap
    #print("brightness is ", value)
    cap.set(cv2.CAP_PROP_BRIGHTNESS, int(value))

def control_panel():
    global ctl, cap
    ctl = tk.Toplevel()
    ctl.title('Control Window')
    ctl.iconbitmap('gear_icon.ico')
    ctl.geometry('+50+50')
    # Commands setup
    brt_label = tk.Label(ctl, text='Brightness: ')
    brt_label.grid(row=0, column=0)
    brt_scale = tk.Scale(ctl, from_=0, to=255, length=200, orient=tk.HORIZONTAL, command=brt_action)
    brt_scale.set(cap.get(cv2.CAP_PROP_BRIGHTNESS))
    brt_scale.grid(row=0, column=1)
    #

def ctl_func():
    # Check focus if window is not closed
    if ctl.winfo_exists():
        #print(ctl.state())
        ctl.focus_set()
    else:
        # Recreate if not exists
        control_panel()
        ctl.focus_set()

snap = False

def save_func():
    global snap
    snap = True
    print("[INFO] save image...")


# Create label to show image
img_label = tk.Label(root, text='image here')
img_label.pack(padx=5, pady=5)

def show_frame():
    global snap
    _, frame = cap.read()
    #frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    
    if snap:
        cv2.imwrite('saved_image.jpg', frame)
        snap = False
        
    img = Image.fromarray(cv2image)        
    imgtk = ImageTk.PhotoImage(image=img)  
    img_label.imgtk = imgtk                    
    img_label.configure(image=imgtk)           
    img_label.after(5, show_frame)      # Refresh at _ msec interval   

# Menu bar
menubar = tk.Menu(root)
root.configure(menu=menubar)
fileMenu = tk.Menu(menubar)
fileMenu.add_command(label="Control", command=ctl_func)
fileMenu.add_command(label="Save", command=save_func)
fileMenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=fileMenu)


show_frame()
control_panel()   # Turn ON control panel

root.mainloop()