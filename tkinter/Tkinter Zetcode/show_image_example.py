#!/usr/bin/env python
"""
ZetCode Tkinter tutorial
http://zetcode.com/gui/tkinter/introduction/

This script shows a simple window on the screen.

author: Jan Bodnar
last modified: January 2011
website: www.zetcode.com
"""
import sys
if sys.version_info[0] < 3:
	# 2.x version
    from Tkinter import Tk, Frame, BOTH, Label
else:
    # 3.x & above
    from tkinter import Tk, Frame, BOTH, Label


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="red")   
        self.parent = parent       
        self.initUI()
    
    def initUI(self): 
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)
        

def main():
    root = Tk()
    # sets a size for the window and positions it on the screen
	# "width x height + x offset + y offset" based on top left corner
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

# import Image and display by graphics package Tkinter
from PIL import Image, ImageTk

def main2():
    # open an image and convert to byte format
    im = Image.open('lena_color512.jpg')
    
    # A root window for displaying objects
    root = Tk()
    
    # Convert the Image object into a TkPhoto object
    tkimage = ImageTk.PhotoImage(im)
    
    # Put it in the display window
    Label(root, image=tkimage).pack()
    
    root.mainloop() # Start the GUI


if __name__ == '__main__':
    #main()
    main2()
