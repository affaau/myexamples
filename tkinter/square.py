#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This program draws three
rectangles filled with different
colours.

Author: Jan Bodnar
Last modified: July 2017
Website: www.zetcode.com
"""

from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()
        
        
    def initUI(self):
      
        self.master.title("Colours")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_rectangle(30, 10, 120, 80, 
            outline="#fb0", fill="#fb0")
        canvas.create_rectangle(150, 10, 240, 80, 
            outline="#f50", fill="#f50")
        canvas.create_rectangle(270, 10, 370, 80, 
            outline="#05f", fill="#05f")            
        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Example()
    root.geometry("400x100+100+300")  # "widthxheight+leftTopX+leftTopY"
    root.mainloop()  


if __name__ == '__main__':
    main()
